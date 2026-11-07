#!/usr/bin/env python3
"""Smoke-test a *real* production site (not the Lumen test fixture) in Chromium or WebKit."""
import argparse
import json
import os
import re
from pathlib import Path

from playwright.sync_api import expect, sync_playwright

HOST = os.environ.get("CLIENT_SITE_URL", "http://127.0.0.1:4176")


def must_equal(locator, expected, label):
    actual = (locator.first.text_content() or "").strip()
    assert actual == expected, f"{label}: {actual!r} instead of {expected!r}"


def check_master_navigation(page, desktop):
    trigger = page.locator(
        '#salonDesktopTeam [data-desktop-master]:not([hidden])' if desktop
        else '#tn13Team [data-mid]'
    ).first
    if not trigger.count():
        return
    profile = page.locator('#stdMasterOverlay' if desktop else '.tn22-master-page')
    booking = page.locator('#stdBookOverlay' if desktop else '#tn13BookSheet')
    book_button = profile.locator('#stdMasterPageBook' if desktop else '.tn22-master-book')
    close_button = profile.locator('#stdMasterPageClose' if desktop else '.tn22-back')
    open_class = re.compile(r'\bopen\b')
    trigger.click(timeout=9000)
    profile.locator('.tanem-master-head').wait_for(state='visible')
    if desktop:
        portrait = profile.locator('.tanem-master-photo')
        assert 196 <= portrait.bounding_box()['width'] <= 200, 'Opened desktop portrait must be only slightly enlarged'

    book_button.click()
    expect(booking).to_have_class(open_class)
    page.keyboard.press('Escape')
    expect(booking).not_to_have_class(open_class)
    expect(profile).to_have_class(open_class)

    photo = profile.locator('[data-master-work]').first
    if photo.count():
        viewer = page.locator('#stdGallery' if desktop else '.tn22-viewer')
        photo.click()
        expect(viewer).to_have_class(open_class)
        gallery_button = viewer.locator('.std-view-gallery' if desktop else '.tn22-view-gallery')
        expect(gallery_button).to_be_visible()
        gallery_button.click()
        gallery = page.locator('#stdGalleryBrowser' if desktop else '#tn13Gallery')
        expect(gallery).to_have_class(open_class)
        # This is the COMMON gallery, with its complete category and visible tabs.
        tiles = gallery.locator('.std-gallery-browser-tile' if desktop else '.tn22-gallery-tile')
        gallery_tabs = gallery.locator('#stdGalleryBrowserTabs' if desktop else '.tn22-gallery-tabs-wrap')
        expect(gallery_tabs).to_be_visible()
        active_tab = gallery_tabs.locator('.active').first
        active = active_tab.get_attribute('data-gallery-category' if desktop else 'data-gcat')
        expected = page.evaluate('(category) => window.TANEM_SITE_DATA.media.gallery[category]?.length', active)
        assert expected and tiles.count() == expected, (
            f'Master gallery category {active!r} should contain all {expected} photos, got {tiles.count()}'
        )
        assert "SALON NAME" not in gallery.inner_text(), "Lazy gallery must render the client brand"
        page.keyboard.press('Escape')
        expect(gallery).not_to_have_class(open_class)
        expect(viewer).not_to_have_class(open_class)
        expect(profile).to_have_class(open_class)
        direct_gallery = profile.locator('[data-master-gallery]')
        direct_gallery.click()
        expect(gallery).to_have_class(open_class)
        expect(gallery_tabs).to_be_visible()
        page.keyboard.press('Escape')
        expect(profile).to_have_class(open_class)
        if desktop:
            assert page.locator('body').evaluate('(node) => node.style.overflow') == 'hidden', (
                'Closing a master photo must keep background scrolling locked'
            )

    review_section = profile.locator('#tanem-master-reviews')
    expect(review_section).to_be_visible()
    review_empty = 'пока не добавлены' if page.evaluate('document.documentElement.lang') == 'ru' else 'not been added'
    assert review_empty in review_section.inner_text().lower(), 'Master reviews need a localized neutral empty state'
    assert 'Проверка прокрутки' not in profile.inner_text(), 'Test copy must never appear on a client site'
    assert profile.locator('.tanem-master-review').count() == 0, 'Temporary testimonials must be removed'

    page.go_back()
    expect(profile).not_to_have_class(open_class)
    page.go_forward()
    expect(profile).to_have_class(open_class)
    profile.locator('.tanem-master-head').wait_for(state='visible')
    # WebKit can briefly show the restored profile before a stale observer
    # triggers a second Back. Wait beyond the close animation to catch it.
    page.wait_for_timeout(700)
    expect(profile).to_have_class(open_class)
    assert page.evaluate('history.state?.tanemMasterProfile'), (
        'Restoring a master profile must retain its browser-history entry'
    )
    close_button.click()
    expect(profile).not_to_have_class(open_class)


    # Closing a different specialist must never restore the previous one.
    page.emulate_media(reduced_motion='no-preference')
    triggers = page.locator('#salonDesktopTeam [data-desktop-master]:not([hidden])' if desktop else '#tn13Team [data-mid]')
    for i in range(triggers.count()):
        button = triggers.nth(i)
        button.click(timeout=9000)
        expect(profile).to_have_class(open_class)
        team = page.locator('#salonDesktopTeam' if desktop else '#tn13Team')
        team_top = team.bounding_box()['y']
        close_button.click()
        if not desktop:
            positions = page.evaluate('''() => new Promise(resolve => {
                const positions = [], start = performance.now();
                function sample(now) {
                    positions.push(document.querySelector('#tn13Team').getBoundingClientRect().top);
                    if (now - start < 700) requestAnimationFrame(sample);
                    else resolve(positions);
                }
                requestAnimationFrame(sample);
            })''')
            assert max(abs(y - team_top) for y in positions) <= 2, 'Team must stay in place throughout profile closing'
        else:
            page.wait_for_timeout(700)
        expect(profile).not_to_have_class(open_class)
        assert not page.evaluate('history.state?.tanemMasterProfile'), 'Closed profile must not survive in history state'
        expect(button).to_be_visible()
    page.emulate_media(reduced_motion='reduce')


def check(browser, width, height, mobile, language):
    context = browser.new_context(
        viewport={"width": width, "height": height},
        is_mobile=mobile,
        has_touch=mobile,
        locale="ru-RU",
        reduced_motion="reduce",
    )
    page = context.new_page()
    errors = []
    failed_assets = []
    page.on("pageerror", lambda error: errors.append(str(error)))
    page.on("response", lambda response: failed_assets.append(response.url)
            if response.status >= 400 and response.url.startswith(HOST)
            and re.search(r"\.(?:js|css|webp|png|jpe?g|svg)(?:\?|$)", response.url)
            else None)
    page.goto(HOST, wait_until="domcontentloaded", timeout=30000)
    data = page.evaluate("window.TANEM_SITE_DATA")
    assert data and data["mode"] == "production", "Site did not load production data"
    desktop = (width >= 1024) or not mobile
    root = "#salon-desktop-v1" if desktop else "#salon-mobile"
    page.locator(root).wait_for(state="visible", timeout=18000)
    page.wait_for_function("!document.documentElement.classList.contains('br-booting')")
    switch = f'[data-desktop-lang="{language}"]' if desktop else f'[data-lang="{language}"]'
    page.locator(switch).first.click(timeout=9000)
    page.wait_for_timeout(250)
    brand = ".std-header-brand-main" if desktop else ".tn22-title"
    must_equal(page.locator(brand), data["salon"]["name"][language], "brand")
    if desktop:
        assert page.locator(".std-header-brand-main img").count() == 0, "Desktop header must always use one-line text branding"
        if data.get("media", {}).get("logo") == "logo.png":
            hero_logo = page.locator("#salonDesktopTop h1.std-logo-image img")
            assert hero_logo.count() == 1, "Eva hero should show exactly one logo image"
            assert hero_logo.get_attribute("src") == "logo.png"
            assert hero_logo.evaluate("(img) => img.complete && img.naturalWidth > 0"), (
                "Eva hero logo must load correctly"
            )
            nav = page.locator(".std-nav a")
            assert nav.count() == 6, "Desktop navigation must contain six links"
            assert nav.nth(3).get_attribute("href") == "#salonDesktopTeam", (
                "Team must appear between About and Reviews"
            )
            team_link = page.locator('.std-nav a[href="#salonDesktopTeam"]')
            assert team_link.count() == 1
            team_link.click()
            assert page.evaluate("location.hash") == "#salonDesktopTeam", (
                "Team nav link must navigate to the existing team section"
            )
    if desktop and data.get("media", {}).get("hero"):
        hero = data["media"]["hero"][0]
        expected_hero = hero if isinstance(hero, str) else hero.get("src")
        assert page.locator("#stdHeroMedia").first.get_attribute("src") == expected_hero, "Desktop hero did not use canonical hero"
    assert data["salon"]["name"][language] in page.title(), "Incorrect page title"
    cards = page.locator("#stdServiceList .dct-service-card" if desktop
                         else "#tn13Services .tn31-service-row")
    assert 0 < cards.count() <= len(data["services"]), "Wrong number of service cards"
    # Client service titles must wrap at whole words, never through automatic hyphens.
    if page.locator(".tanem-service-card").count():
        title_styles = page.locator(".tanem-service-title").evaluate_all("elements => elements.map(e => ({hyphens:getComputedStyle(e).hyphens, wrap:getComputedStyle(e).overflowWrap}))")
        assert all(style["hyphens"] == "none" and style["wrap"] == "normal" for style in title_styles), title_styles
        assert page.locator(".tanem-service-card .tanem-service-price").count() == cards.count()
        if desktop:
            assert page.locator('#stdServiceTabs [data-service-category="all"]').count() == 0
        # Select a category containing a real variant-priced service.
        variant_service = next((item for item in data["services"] if item.get("variants")), None)
        assert variant_service, "The production fixture must include a variant-priced service"
        category = variant_service["category"]
        category_button = (
            page.locator(f'#stdServiceTabs [data-service-category="{category}"]') if desktop
            else page.locator(f'#tn13Services [data-scat="{category}"]')
        )
        category_button.click(timeout=9000)
        catalogue_root = "#stdServiceList" if desktop else "#tn13Services"
        options = page.locator(f'{catalogue_root} .tanem-service-card .tanem-service-options').first
        assert options.count(), "The main service catalogue must expose its option-price controls"
        variant_card = page.locator(
            f'{catalogue_root} [data-eva-service-id="{variant_service["id"]}"] .tanem-service-options'
        )
        assert variant_card.count(), "Variant-priced service must remain in the main service catalogue"
        variant_label = variant_card.locator('.tanem-options-label')
        assert variant_label.evaluate('el => getComputedStyle(el).borderBottomWidth') == '1px'
        assert variant_card.locator('summary').evaluate(
            'el => getComputedStyle(el).textDecorationLine'
        ) == 'none', "Variant-priced service needs one thin underline, not a default text underline"

        if options.count():
            summary = options.locator('summary')
            label = summary.locator('.tanem-options-label')
            text = label.inner_text()
            assert text.endswith(' +'), 'The plus sign must share the same underline and animation as the label'
            summary_decoration = summary.evaluate('el => getComputedStyle(el).textDecorationLine')
            label_style = label.evaluate("""el => {
                const style = getComputedStyle(el);
                return {
                    base: style.getPropertyValue('--tanem-options-base').trim(),
                    border: style.borderBottomWidth,
                    shine: style.backgroundImage
                };
            }""")
            assert summary_decoration == 'none', 'The catalogue label must not receive a second underline'
            assert label_style['border'] == '1px', 'The catalogue underline must be a single normal 1px line'
            assert label_style['base'] == '#dedbd7', 'The main service catalogue needs a clearer light-grey base'
            assert '255, 255, 255' in label_style['shine'], 'The catalogue glint must travel toward white'

            # The master-profile palette is intentionally independent from the main catalogue.
            profile_palette = page.evaluate("""() => {
                const host = document.createElement('div');
                host.className = 'tanem-master-price-list';
                const details = document.createElement('details');
                details.className = 'tanem-service-options';
                const summary = document.createElement('summary');
                const label = document.createElement('span');
                label.className = 'tanem-options-label';
                summary.appendChild(label);
                details.appendChild(summary);
                host.appendChild(details);
                document.body.appendChild(host);
                const style = getComputedStyle(label);
                const result = {
                    base: style.getPropertyValue('--tanem-options-base').trim(),
                    shine: style.backgroundImage
                };
                host.remove();
                return result;
            }""")
            assert profile_palette['base'] == '#6f6258', 'Master-profile label colour must remain unchanged'
            assert '249, 224, 167' in profile_palette['shine'], 'Master-profile glint must keep its original colour'

            if mobile:
                assert summary.bounding_box()['height'] <= 30, 'Disclosure hit area must not inflate a service card'

            # Verify that opening and closing both visibly animate the panel.
            page.emulate_media(reduced_motion='no-preference')
            # Start and sample in one browser task so CI transport latency cannot
            # consume the entire 260 ms animation before it is inspected.
            opening = page.evaluate("""el => {
                el.querySelector('summary').click();
                const panel = el.querySelector('.tanem-options-panel');
                const animation = panel.getAnimations().find(a => a.playState === 'running');
                if (!animation) return {running:false, height:panel.getBoundingClientRect().height, contentHeight:panel.scrollHeight};
                animation.pause();
                animation.currentTime = 130;
                const height = panel.getBoundingClientRect().height;
                animation.play();
                return {running:true, height, contentHeight:panel.scrollHeight};
            }""", options.element_handle())
            assert opening['running'], 'Opening the option-price panel must animate'
            assert 0 < opening['height'] < opening['contentHeight'], (
                f'Opening must begin gradually, not jump to full height: {opening}'
            )
            page.wait_for_function(
                "el => { const panel = el.querySelector('.tanem-options-panel'); "
                "return el.open && !panel.getAnimations().some(a => a.playState === 'running') "
                "&& panel.getBoundingClientRect().height > 0; }",
                arg=options.element_handle(), timeout=2000
            )

            closing = page.evaluate("""el => {
                el.querySelector('summary').click();
                const panel = el.querySelector('.tanem-options-panel');
                const animation = panel.getAnimations().find(a => a.playState === 'running');
                if (!animation) return {running:false, height:panel.getBoundingClientRect().height, contentHeight:panel.scrollHeight};
                animation.pause();
                animation.currentTime = 130;
                const height = panel.getBoundingClientRect().height;
                animation.play();
                return {running:true, height, contentHeight:panel.scrollHeight};
            }""", options.element_handle())
            assert closing['running'], 'Closing the option-price panel must animate'
            assert 0 < closing['height'] < closing['contentHeight'], (
                f'Closing must collapse gradually: {closing}'
            )
            expect(options).not_to_have_attribute('open', '', timeout=2000)
            assert summary.get_attribute('aria-expanded') == 'false'

            # Exercise fast reversals while the height animation is still running.
            summary.click(timeout=9000)
            summary.click(timeout=9000)
            expect(options).not_to_have_attribute('open', '', timeout=2000)
            assert summary.get_attribute('aria-expanded') == 'false'

            summary.click(timeout=9000)
            summary.click(timeout=9000)
            summary.click(timeout=9000)
            expect(options).to_have_attribute('open', '', timeout=2000)
            panel = options.locator('.tanem-options-panel')
            page.wait_for_function(
                "(el) => { const panel = el.querySelector('.tanem-options-panel'); "
                "return el.open && Math.abs(panel.getBoundingClientRect().height - panel.scrollHeight) < 1; }",
                arg=options.element_handle(),
                timeout=2000
            )
            assert summary.get_attribute('aria-expanded') == 'true'
            assert panel.bounding_box()['height'] > 0, 'Expanded tariff panel must be fully visible'

            summary.click(timeout=9000)
            expect(options).not_to_have_attribute('open', '', timeout=2000)
            assert summary.get_attribute('aria-expanded') == 'false'
            page.emulate_media(reduced_motion='reduce')

    team_section = page.locator("#salonDesktopTeam" if desktop else "#tn13Team")
    reviews_section = page.locator("#salonDesktopReviews" if desktop else "#tn13Reviews")
    assert not team_section.is_hidden(), "Team is a permanent structural section"
    assert not reviews_section.is_hidden(), "Reviews are a permanent structural section"
    if not data["team"]:
        placeholder_cards = page.locator("#salonDesktopTeam .std-master.is-placeholder" if desktop else "#tn13Team .tn22-master-card.is-placeholder")
        assert placeholder_cards.count() == 4, "Empty team must preserve four neutral visual master cards"
        real_team_cards = page.locator("#salonDesktopTeam [data-desktop-master]" if desktop else "#tn13Team [data-mid]")
        assert real_team_cards.count() == 0, "Neutral team cards must not become invented specialists"
    if not data["reviews"]:
        review_cards = page.locator("#salonDesktopReviews .std-review-card" if desktop else "#tn13Reviews .br-review-card")
        assert review_cards.count() == 0, "Empty reviews state must not invent reviews"
    if not data["media"]["portfolio"]:
        portfolio_section = page.locator("#salonDesktopPortfolio" if desktop else "#tn13Portfolio")
        assert portfolio_section.is_hidden(), "Empty portfolio should remain optional"

    # The full gallery must render every configured image on both layouts.
    gallery_groups = data.get("media", {}).get("gallery", {})
    gallery_counts = {category: len(items) for category, items in gallery_groups.items()}
    gallery_total = sum(gallery_counts.values())
    gallery_sources = [
        item if isinstance(item, str) else item.get("src")
        for items in gallery_groups.values() for item in items
    ]
    if os.environ.get("EXPECT_UNLIMITED_GALLERY") == "1":
        assert gallery_total > 25, f"Unlimited-gallery regression needs more than 25 photos, got {gallery_total}"
        assert len(set(gallery_sources)) == gallery_total, "Gallery sources must be unique"
    if data["media"]["portfolio"]:
        if desktop:
            page.locator("#stdOpenGallery").click(timeout=9000)
            page.locator("#stdGalleryBrowser.open").wait_for(timeout=8000)
            for category, expected_count in gallery_counts.items():
                page.locator(f'#stdGalleryBrowserTabs [data-gallery-category="{category}"]').click(timeout=9000)
                actual_count = page.locator("#stdGalleryBrowserGrid .std-gallery-browser-tile").count()
                assert actual_count == expected_count, (
                    f"Desktop gallery category {category!r}: {actual_count} photos instead of {expected_count}"
                )
            page.locator("#stdGalleryBrowserBack").click(timeout=9000)
        else:
            page.locator("#tn13Portfolio .tn22-port-all").click(timeout=9000)
            page.locator("#tn13Gallery.open").wait_for(timeout=8000)
            for category, expected_count in gallery_counts.items():
                page.locator(f'#tn13Gallery [data-gcat="{category}"]').click(timeout=9000)
                actual_count = page.locator("#tn13Gallery .tn22-gallery-tile").count()
                assert actual_count == expected_count, (
                    f"Mobile gallery category {category!r}: {actual_count} photos instead of {expected_count}"
                )
            page.locator("#tn13Gallery .tn22-gallery-back").click(timeout=9000)
    messenger_card = page.locator('#salonDesktopContacts [data-contact-type="messenger"]' if desktop else '#tn13Visit [data-contact-type="messenger"]')
    if not data.get("contacts", {}).get("messengerUrl"):
        assert messenger_card.count() == 1 and messenger_card.is_hidden(), "Missing messenger must not leave a visible contact card"
    address_sub = page.locator('#salonDesktopContacts [data-contact-type="address"] .std-contact-card-sub' if desktop else '#tn13Visit [data-contact-type="address"] strong+span')
    expected_map_copy = ("Открыть в Яндекс Картах" if data.get("country") == "RU" else "Открыть в Google Maps") if language == "ru" else ("Open in Yandex Maps" if data.get("country") == "RU" else "Open in Google Maps")
    if language in ("ru", "en"):
        must_equal(address_sub, expected_map_copy, "map provider action")

    check_master_navigation(page, desktop)
    sample = page.locator("#stdHeaderBookBtn" if desktop else ".tn22-cta")
    sample.click(timeout=9000)
    links = page.locator("#stdBookOverlay .std-book-options a" if desktop
                         else "#tn13BookSheet .tn50-book-option")
    assert links.count() > 0, "Booking actions are missing"
    for href in [link.get_attribute("href") for link in links.all()]:
        assert href and href != "#" and (
            href.startswith(("https://", "tel:", "tg:", "viber:", "whatsapp:"))
        ), f"Invalid booking destination: {href}"
    visible = page.locator("body").inner_text()
    assert not re.search(r"SALON NAME|(?:Услуга|Service)\s+\d{2}\b", visible), (
        "Demo labels remain visible on a production page")
    # Third-party map widgets can raise known frame-only errors in local HTTP smoke tests.
    # Ignore only these exact provider errors; application errors still fail the run.
    google_maps_frame_noise = (
        'Could not load "search_impl".',
        'Could not load "util".',
        'maps.googleapis.com/maps/api/mapsjs/gen_204?csp_test=true due to access control checks.',
    )
    yandex_map_frame_noise = (
        'TypeError: undefined is not an object (evaluating '
        '\'window.document.getElementsByClassName("config-view")[0].textContent\')'
    )
    app_errors = [
        error for error in errors
        if not any(token in error for token in google_maps_frame_noise)
        and not (HOST.startswith("http://127.0.0.1") and error == yandex_map_frame_noise)
        and not (
            HOST.startswith("http://127.0.0.1")
            and "/yandex.ru" in error
            and "Protocols must match." in error
        )
        and not (
            HOST.startswith("http://127.0.0.1")
            and "/mc.yandex.com/watch/" in error
            and "due to access control checks." in error
        )
        and not (
            HOST.startswith("http://127.0.0.1")
            and error.startswith("/yandex.ru/ads/meta/")
            and error.endswith("due to access control checks.")
        )
    ]
    # The map's optional advertising script is not an application asset.
    if HOST.startswith("http://127.0.0.1"):
        app_errors = [error for error in app_errors if error != "Error: Failed to load https://yandex.ru/ads/system/context.js"]
    assert not app_errors, f"JavaScript errors: {app_errors}"
    assert not failed_assets, f"Missing site assets: {failed_assets}"
    context.close()
    print(f"PASS {width}x{height}, {'touch' if mobile else 'desktop'}, {language}: customer data, cards and booking")


def production_locales():
    source = Path(__file__).resolve().parents[1] / "site-data.js"
    content = source.read_text(encoding="utf-8")
    match = re.search(r"const data=(\{.*?\});\s*const rows=\[\];", content, re.S)
    assert match, "Could not parse production locales from site-data.js"
    data = json.loads(match.group(1))
    locales = data.get("locales", [])
    assert locales, "Production site must declare at least one locale"
    return locales


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--engine", choices=["chromium", "webkit"], default="chromium")
    args = parser.parse_args()
    locales = production_locales()
    cases = [(1366, 900, False, language) for language in locales]
    cases += [(390, 844, True, language) for language in locales]
    cases.append((1180, 820, True, locales[0]))
    with sync_playwright() as playwright:
        browser = getattr(playwright, args.engine).launch(headless=True)
        try:
            for case in cases:
                check(browser, *case)
        finally:
            browser.close()
    print("PASS actual production site on desktop, phone and touch tablet")


if __name__ == "__main__":
    main()
