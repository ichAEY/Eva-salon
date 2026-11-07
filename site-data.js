(function(global){
  'use strict';
  const data={
  "schemaVersion": 1,
  "mode": "production",
  "country": "RU",
  "locales": [
    "ru",
    "en"
  ],
  "defaultLocale": "ru",
  "salon": {
    "name": {
      "ru": "Ева",
      "en": "Eva"
    },
    "kind": {
      "ru": "Салон красоты",
      "en": "Beauty salon"
    },
    "city": {
      "ru": "Балашиха",
      "en": "Balashikha"
    },
    "address": {
      "ru": "д. Павлино, 69",
      "en": "Pavlino village, 69"
    },
    "fullAddress": {
      "ru": "Московская область, городской округ Балашиха, деревня Павлино, 69, 143988",
      "en": "69 Pavlino village, Balashikha urban district, Moscow Region, 143988, Russia"
    },
    "heroDescription": {
      "ru": "Ваша красота. Ваша уверенность.",
      "en": "Your beauty. Your confidence."
    },
    "about": {
      "ru": "В основе нашей работы — профессиональный подход, внимание к деталям и уважение к индивидуальности каждого гостя. Мы создаём комфортное пространство, где качество и забота остаются главным приоритетом.",
      "en": "Our work is built on professionalism, attention to detail, and respect for every guest’s individuality. We create a comfortable space where quality and care remain our highest priorities."
    }
  },
  "schedule": {
    "timezone": "Europe/Moscow",
    "periods": [
      {
        "days": [
          1,
          2,
          3,
          4,
          5,
          6,
          7
        ],
        "open": "10:00",
        "close": "21:00"
      }
    ],
    "fallback": {
      "ru": "Ежедневно 10:00–21:00",
      "en": "Daily 10:00–21:00"
    }
  },
  "contacts": {
    "phone": "+7 (926) 006-39-22",
    "phoneLabel": {
      "ru": "Позвонить",
      "en": "Call"
    },
    "messengerUrl": "https://wa.me/message/AOFH2DWF7BJWJ1?text=%D0%9E%D0%B1%D1%80%D0%B0%D1%89%D0%B5%D0%BD%D0%B8%D0%B5+%D0%B8%D0%B7+%D0%AF%D0%BD%D0%B4%D0%B5%D0%BA%D1%81+%D0%9A%D0%B0%D1%80%D1%82%0A%D0%97%D0%B4%D1%80%D0%B0%D0%B2%D1%81%D1%82%D0%B2%D1%83%D0%B9%D1%82%D0%B5!+%D0%9C%D0%B5%D0%BD%D1%8F+%D0%B7%D0%B0%D0%B8%D0%BD%D1%82%D0%B5%D1%80%D0%B5%D1%81%D0%BE%D0%B2%D0%B0%D0%BB%D0%BE+%D0%B2%D0%B0%D1%88%D0%B5+%D0%BF%D1%80%D0%B5%D0%B4%D0%BB%D0%BE%D0%B6%D0%B5%D0%BD%D0%B8%D0%B5",
    "messengerLabel": {
      "ru": "WhatsApp",
      "en": "WhatsApp"
    },
    "messengerHandle": "",
    "mapUrl": "https://yandex.com/maps/org/yeva/1179517154/?ll=37.961682%2C55.729239&z=15",
    "mapEmbedUrl": "https://yandex.ru/map-widget/v1/?ll=37.961682%2C55.729239&z=15&mode=search&text=%D0%95%D0%B2%D0%B0%2C%20%D0%9F%D0%B0%D0%B2%D0%BB%D0%B8%D0%BD%D0%BE%2C%2069",
    "reviewsUrl": "https://yandex.com/maps/org/yeva/1179517154/",
    "booking": [
      {
        "type": "telegram",
        "label": {
          "ru": "Telegram",
          "en": "Telegram"
        },
        "url": "https://t.me/evapavlino"
      }
    ]
  },
  "rating": {
    "value": 4.8,
    "count": 310
  },
  "media": {
    "logo": "logo.png",
    "hero": [
      {
        "src": "hero.webp",
        "alt": {
          "ru": "Цветочная композиция в интерьере салона",
          "en": "Floral arrangement in the salon"
        }
      }
    ],
    "about": "profile.webp",
    "portfolio": [
      {
        "src": "gallery-09.webp",
        "alt": {
          "ru": "Маникюр с покрытием",
          "en": "Manicure with polish"
        }
      },
      {
        "src": "gallery-12.webp",
        "alt": {
          "ru": "Маникюр с дизайном",
          "en": "Nail art"
        }
      },
      {
        "src": "gallery-14.webp",
        "alt": {
          "ru": "Наращивание ресниц",
          "en": "Lash extensions"
        }
      },
      {
        "src": "gallery-17.webp",
        "alt": {
          "ru": "Оформление бровей",
          "en": "Brow styling"
        }
      },
      {
        "src": "gallery-20.webp",
        "alt": {
          "ru": "Косметологическая процедура",
          "en": "Cosmetic treatment"
        }
      },
      {
        "src": "gallery-22.webp",
        "alt": {
          "ru": "Окрашивание волос",
          "en": "Hair coloring"
        }
      },
      {
        "src": "gallery-24.webp",
        "alt": {
          "ru": "Стрижка и укладка",
          "en": "Haircut and styling"
        }
      }
    ],
    "gallery": {
      "Салон": [
        {
          "src": "gallery-01.webp",
          "alt": {
            "ru": "Интерьер салона с цветочным декором",
            "en": "Salon interior with floral decor"
          }
        },
        {
          "src": "gallery-02.webp",
          "alt": {
            "ru": "Косметические средства в салоне",
            "en": "Beauty products in the salon"
          }
        },
        {
          "src": "gallery-03.webp",
          "alt": {
            "ru": "Рабочее место мастера маникюра",
            "en": "Manicurist workstation"
          }
        },
        {
          "src": "gallery-04.webp",
          "alt": {
            "ru": "Рабочие места парикмахерского зала",
            "en": "Hair salon workstations"
          }
        },
        {
          "src": "gallery-05.webp",
          "alt": {
            "ru": "Солярий",
            "en": "Tanning room"
          }
        },
        {
          "src": "gallery-06.webp",
          "alt": {
            "ru": "Цветочный декор салона",
            "en": "Floral salon decor"
          }
        },
        {
          "src": "gallery-07.webp",
          "alt": {
            "ru": "Кабинет косметолога",
            "en": "Cosmetology room"
          }
        },
        {
          "src": "gallery-08.webp",
          "alt": {
            "ru": "Кабинет для процедур",
            "en": "Treatment room"
          }
        },
        {
          "src": "gallery-26.webp",
          "alt": {
            "ru": "Декоративные фигуры в интерьере салона",
            "en": "Decorative figures in the salon interior"
          }
        },
        {
          "src": "gallery-27.webp",
          "alt": {
            "ru": "Витрина с украшениями в салоне",
            "en": "Jewelry display in the salon"
          }
        },
        {
          "src": "gallery-28.webp",
          "alt": {
            "ru": "Цветочная композиция в интерьере салона",
            "en": "Floral arrangement in the salon interior"
          }
        },
        {
          "src": "gallery-29.webp",
          "alt": {
            "ru": "Рабочее место парикмахера",
            "en": "Hair salon workstation"
          }
        },
        {
          "src": "gallery-30.webp",
          "alt": {
            "ru": "Кресло в кабинете для процедур",
            "en": "Treatment room chair"
          }
        },
        {
          "src": "gallery-31.webp",
          "alt": {
            "ru": "Рабочее место мастера маникюра",
            "en": "Manicurist workstation"
          }
        }
      ],
      "Ногти": [
        {
          "src": "gallery-09.webp",
          "alt": {
            "ru": "Маникюр с покрытием",
            "en": "Manicure with polish"
          }
        },
        {
          "src": "gallery-11.webp",
          "alt": {
            "ru": "Маникюр",
            "en": "Manicure"
          }
        },
        {
          "src": "gallery-12.webp",
          "alt": {
            "ru": "Маникюр с дизайном",
            "en": "Nail art"
          }
        },
        {
          "src": "gallery-13.webp",
          "alt": {
            "ru": "Маникюр с покрытием",
            "en": "Polished manicure"
          }
        }
      ],
      "Брови и ресницы": [
        {
          "src": "gallery-10.webp",
          "alt": {
            "ru": "Оформление бровей",
            "en": "Brow shaping"
          }
        },
        {
          "src": "gallery-14.webp",
          "alt": {
            "ru": "Наращивание ресниц",
            "en": "Lash extensions"
          }
        },
        {
          "src": "gallery-15.webp",
          "alt": {
            "ru": "Работа с ресницами",
            "en": "Lash work"
          }
        },
        {
          "src": "gallery-16.webp",
          "alt": {
            "ru": "Наращивание ресниц",
            "en": "Lash extensions"
          }
        },
        {
          "src": "gallery-17.webp",
          "alt": {
            "ru": "Оформление бровей",
            "en": "Brow styling"
          }
        },
        {
          "src": "gallery-18.webp",
          "alt": {
            "ru": "Работа с бровями",
            "en": "Brow treatment"
          }
        },
        {
          "src": "gallery-19.webp",
          "alt": {
            "ru": "Результат работы с ресницами",
            "en": "Lash result"
          }
        }
      ],
      "Косметология": [
        {
          "src": "gallery-20.webp",
          "alt": {
            "ru": "Косметологическая процедура",
            "en": "Cosmetic treatment"
          }
        },
        {
          "src": "gallery-21.webp",
          "alt": {
            "ru": "Процедура ухода за кожей",
            "en": "Skin care treatment"
          }
        }
      ],
      "Волосы": [
        {
          "src": "gallery-22.webp",
          "alt": {
            "ru": "Окрашивание волос",
            "en": "Hair coloring"
          }
        },
        {
          "src": "gallery-23.webp",
          "alt": {
            "ru": "Результат окрашивания волос",
            "en": "Hair color result"
          }
        },
        {
          "src": "gallery-24.webp",
          "alt": {
            "ru": "Стрижка и укладка",
            "en": "Haircut and styling"
          }
        },
        {
          "src": "gallery-25.webp",
          "alt": {
            "ru": "Работа парикмахера",
            "en": "Hair styling result"
          }
        }
      ],
      "Сертификаты": [
        {
          "src": "gallery-32.webp",
          "alt": {
            "ru": "Сертификат об обучении работе с BioRePeelCl3",
            "en": "BioRePeelCl3 training certificate"
          }
        },
        {
          "src": "gallery-33.webp",
          "alt": {
            "ru": "Сертификат об обучении работе на аппарате Pacer One",
            "en": "Pacer One device training certificate"
          }
        },
        {
          "src": "gallery-34.webp",
          "alt": {
            "ru": "Сертификат о семинаре по ботулиническому токсину",
            "en": "Botulinum toxin seminar certificate"
          }
        },
        {
          "src": "gallery-35.webp",
          "alt": {
            "ru": "Сертификат об обучении Barex",
            "en": "Barex training certificate"
          }
        },
        {
          "src": "gallery-36.webp",
          "alt": {
            "ru": "Сертификат о повышении квалификации по комбинированному маникюру",
            "en": "Combined manicure advanced training certificate"
          }
        },
        {
          "src": "gallery-37.webp",
          "alt": {
            "ru": "Сертификат о повышении квалификации по комбинированному маникюру",
            "en": "Combined manicure advanced training certificate"
          }
        },
        {
          "src": "gallery-38.webp",
          "alt": {
            "ru": "Сертификат о прохождении онлайн-курса Combi Guru",
            "en": "Combi Guru online course certificate"
          }
        },
        {
          "src": "gallery-39.webp",
          "alt": {
            "ru": "Диплом по моделированию ногтей, маникюру и педикюру",
            "en": "Nail modeling, manicure and pedicure diploma"
          }
        },
        {
          "src": "gallery-40.webp",
          "alt": {
            "ru": "Сертификат о семинаре Perfect Blond",
            "en": "Perfect Blond seminar certificate"
          }
        }
      ]
    }
  },
  "categoryLabels": {
    "Маникюр": {
      "ru": "Маникюр и педикюр",
      "en": "Manicure & pedicure"
    },
    "Волосы": {
      "ru": "Парикмахерский зал",
      "en": "Hair salon"
    },
    "Брови и ресницы": {
      "ru": "Брови и ресницы",
      "en": "Brows & lashes"
    },
    "Макияж": {
      "ru": "Перманентный макияж",
      "en": "Permanent makeup"
    },
    "Косметология": {
      "ru": "Косметология",
      "en": "Cosmetology"
    },
    "Массаж": {
      "ru": "Массаж",
      "en": "Massage"
    },
    "Комплексы": {
      "ru": "Комплексы",
      "en": "Packages"
    },
    "Другое": {
      "ru": "Солярий и дополнительные услуги",
      "en": "Tanning & extras"
    }
  },
  "categoryOrder": [
    "Маникюр",
    "Волосы",
    "Брови и ресницы",
    "Макияж",
    "Косметология",
    "Массаж",
    "Комплексы",
    "Другое"
  ],
  "services": [
    {
      "id": "nail-classic-manicure",
      "category": "Маникюр",
      "title": {
        "ru": "Маникюр классический /обрезной/",
        "en": "Classic manicure (cuticle trim)"
      },
      "price": "1 100–1 400 ₽",
      "duration": "",
      "description": {
        "ru": "Мастер: 1 100 ₽; ТОП мастер: 1 400 ₽",
        "en": "Master: 1 100 ₽; Top master: 1 400 ₽"
      },
      "variants": [
        {
          "label": {
            "ru": "Мастер",
            "en": "Master"
          },
          "duration": "",
          "price": "1 100 ₽"
        },
        {
          "label": {
            "ru": "ТОП мастер",
            "en": "Top master"
          },
          "duration": "",
          "price": "1 400 ₽"
        }
      ]
    },
    {
      "id": "nail-gel-coating",
      "category": "Маникюр",
      "title": {
        "ru": "Покрытие /гель, гель-лак/",
        "en": "Gel coating / gel polish"
      },
      "price": "1 400–1 800 ₽",
      "duration": "",
      "description": {
        "ru": "Мастер: 1 400 ₽; ТОП мастер: 1 800 ₽",
        "en": "Master: 1 400 ₽; Top master: 1 800 ₽"
      },
      "variants": [
        {
          "label": {
            "ru": "Мастер",
            "en": "Master"
          },
          "duration": "",
          "price": "1 400 ₽"
        },
        {
          "label": {
            "ru": "ТОП мастер",
            "en": "Top master"
          },
          "duration": "",
          "price": "1 800 ₽"
        }
      ]
    },
    {
      "id": "nail-removal-with-manicure",
      "category": "Маникюр",
      "title": {
        "ru": "Снятие при дальнейшем маникюре",
        "en": "Removal with subsequent manicure"
      },
      "price": "400 ₽",
      "duration": "",
      "description": {
        "ru": "Мастер: 400 ₽; ТОП мастер: 400 ₽",
        "en": "Master: 400 ₽; Top master: 400 ₽"
      },
      "variants": [
        {
          "label": {
            "ru": "Мастер",
            "en": "Master"
          },
          "duration": "",
          "price": "400 ₽"
        },
        {
          "label": {
            "ru": "ТОП мастер",
            "en": "Top master"
          },
          "duration": "",
          "price": "400 ₽"
        }
      ]
    },
    {
      "id": "nail-removal-only",
      "category": "Маникюр",
      "title": {
        "ru": "Снятие без дальнейшей процедуры",
        "en": "Removal without a follow-up service"
      },
      "price": "600 ₽",
      "duration": "",
      "description": {
        "ru": "Мастер: 600 ₽; ТОП мастер: 600 ₽",
        "en": "Master: 600 ₽; Top master: 600 ₽"
      },
      "variants": [
        {
          "label": {
            "ru": "Мастер",
            "en": "Master"
          },
          "duration": "",
          "price": "600 ₽"
        },
        {
          "label": {
            "ru": "ТОП мастер",
            "en": "Top master"
          },
          "duration": "",
          "price": "600 ₽"
        }
      ]
    },
    {
      "id": "nail-turnkey-manicure",
      "category": "Маникюр",
      "title": {
        "ru": "Маникюр под ключ /снятие+маникюр+покрытие/",
        "en": "Complete manicure /removal + manicure + coating/"
      },
      "price": "2 700–3 200 ₽",
      "duration": "",
      "description": {
        "ru": "Мастер: 2 700 ₽; ТОП мастер: 3 200 ₽",
        "en": "Master: 2 700 ₽; Top master: 3 200 ₽"
      },
      "variants": [
        {
          "label": {
            "ru": "Мастер",
            "en": "Master"
          },
          "duration": "",
          "price": "2 700 ₽"
        },
        {
          "label": {
            "ru": "ТОП мастер",
            "en": "Top master"
          },
          "duration": "",
          "price": "3 200 ₽"
        }
      ]
    },
    {
      "id": "nail-french-coating",
      "category": "Маникюр",
      "title": {
        "ru": "Покрытие /френч/",
        "en": "French coating"
      },
      "price": "500 ₽",
      "duration": "",
      "description": {
        "ru": "Мастер: 500 ₽; ТОП мастер: 500 ₽",
        "en": "Master: 500 ₽; Top master: 500 ₽"
      },
      "variants": [
        {
          "label": {
            "ru": "Мастер",
            "en": "Master"
          },
          "duration": "",
          "price": "500 ₽"
        },
        {
          "label": {
            "ru": "ТОП мастер",
            "en": "Top master"
          },
          "duration": "",
          "price": "500 ₽"
        }
      ]
    },
    {
      "id": "nail-design-one-nail",
      "category": "Маникюр",
      "title": {
        "ru": "Дизайн 1 ногтя",
        "en": "Design for one nail"
      },
      "price": "100 ₽",
      "duration": "",
      "description": {
        "ru": "Мастер: 100 ₽; ТОП мастер: 100 ₽",
        "en": "Master: 100 ₽; Top master: 100 ₽"
      },
      "variants": [
        {
          "label": {
            "ru": "Мастер",
            "en": "Master"
          },
          "duration": "",
          "price": "100 ₽"
        },
        {
          "label": {
            "ru": "ТОП мастер",
            "en": "Top master"
          },
          "duration": "",
          "price": "100 ₽"
        }
      ]
    },
    {
      "id": "nail-repair",
      "category": "Маникюр",
      "title": {
        "ru": "Ремонт",
        "en": "Nail repair"
      },
      "price": "от 200 ₽",
      "duration": "",
      "description": {
        "ru": "Мастер: от 200 ₽; ТОП мастер: от 200 ₽",
        "en": "Master: от 200 ₽; Top master: от 200 ₽"
      },
      "variants": [
        {
          "label": {
            "ru": "Мастер",
            "en": "Master"
          },
          "duration": "",
          "price": "от 200 ₽"
        },
        {
          "label": {
            "ru": "ТОП мастер",
            "en": "Top master"
          },
          "duration": "",
          "price": "от 200 ₽"
        }
      ]
    },
    {
      "id": "nail-extensions",
      "category": "Маникюр",
      "title": {
        "ru": "Наращивание ногтей",
        "en": "Nail extensions"
      },
      "price": "4 500 ₽",
      "duration": "",
      "description": {
        "ru": "Мастер: —; ТОП мастер: 4 500 ₽",
        "en": "Master: —; Top master: 4 500 ₽"
      },
      "variants": [
        {
          "label": {
            "ru": "Мастер",
            "en": "Master"
          },
          "duration": "",
          "price": "—"
        },
        {
          "label": {
            "ru": "ТОП мастер",
            "en": "Top master"
          },
          "duration": "",
          "price": "4 500 ₽"
        }
      ]
    },
    {
      "id": "pedicure-smart-20",
      "category": "Маникюр",
      "title": {
        "ru": "Педикюр смарт 2.0 /без покрытия/",
        "en": "Smart pedicure 2.0 /without coating/"
      },
      "price": "2 700 ₽",
      "duration": "",
      "description": {
        "ru": "Мастер: —; ТОП мастер: 2 700 ₽",
        "en": "Master: —; Top master: 2 700 ₽"
      },
      "variants": [
        {
          "label": {
            "ru": "Мастер",
            "en": "Master"
          },
          "duration": "",
          "price": "—"
        },
        {
          "label": {
            "ru": "ТОП мастер",
            "en": "Top master"
          },
          "duration": "",
          "price": "2 700 ₽"
        }
      ]
    },
    {
      "id": "pedicure-smart-half-foot",
      "category": "Маникюр",
      "title": {
        "ru": "Педикюр смарт 1/2 /обработка стопы/",
        "en": "Smart pedicure 1/2 /foot treatment/"
      },
      "price": "1 800 ₽",
      "duration": "",
      "description": {
        "ru": "Мастер: —; ТОП мастер: 1 800 ₽",
        "en": "Master: —; Top master: 1 800 ₽"
      },
      "variants": [
        {
          "label": {
            "ru": "Мастер",
            "en": "Master"
          },
          "duration": "",
          "price": "—"
        },
        {
          "label": {
            "ru": "ТОП мастер",
            "en": "Top master"
          },
          "duration": "",
          "price": "1 800 ₽"
        }
      ]
    },
    {
      "id": "pedicure-half-toes",
      "category": "Маникюр",
      "title": {
        "ru": "Педикюр 1/2 /обработка пальцев/",
        "en": "Pedicure 1/2 /toe treatment/"
      },
      "price": "1 300–1 800 ₽",
      "duration": "",
      "description": {
        "ru": "Мастер: 1 300 ₽; ТОП мастер: 1 800 ₽",
        "en": "Master: 1 300 ₽; Top master: 1 800 ₽"
      },
      "variants": [
        {
          "label": {
            "ru": "Мастер",
            "en": "Master"
          },
          "duration": "",
          "price": "1 300 ₽"
        },
        {
          "label": {
            "ru": "ТОП мастер",
            "en": "Top master"
          },
          "duration": "",
          "price": "1 800 ₽"
        }
      ]
    },
    {
      "id": "pedicure-smart-turnkey",
      "category": "Маникюр",
      "title": {
        "ru": "Смарт под ключ",
        "en": "Complete Smart pedicure"
      },
      "price": "4 000 ₽",
      "duration": "",
      "description": {
        "ru": "Мастер: —; ТОП мастер: 4 000 ₽",
        "en": "Master: —; Top master: 4 000 ₽"
      },
      "variants": [
        {
          "label": {
            "ru": "Мастер",
            "en": "Master"
          },
          "duration": "",
          "price": "—"
        },
        {
          "label": {
            "ru": "ТОП мастер",
            "en": "Top master"
          },
          "duration": "",
          "price": "4 000 ₽"
        }
      ]
    },
    {
      "id": "pedicure-nail-shaping",
      "category": "Маникюр",
      "title": {
        "ru": "Педикюр: придание формы ногтям",
        "en": "Pedicure: toenail shaping"
      },
      "price": "400 ₽",
      "duration": "",
      "description": {
        "ru": "Мастер: 400 ₽; ТОП мастер: 400 ₽",
        "en": "Master: 400 ₽; Top master: 400 ₽"
      },
      "variants": [
        {
          "label": {
            "ru": "Мастер",
            "en": "Master"
          },
          "duration": "",
          "price": "400 ₽"
        },
        {
          "label": {
            "ru": "ТОП мастер",
            "en": "Top master"
          },
          "duration": "",
          "price": "400 ₽"
        }
      ]
    },
    {
      "id": "pedicure-half-with-coating",
      "category": "Маникюр",
      "title": {
        "ru": "Педикюр 1/2 с покрытием",
        "en": "Pedicure 1/2 with coating"
      },
      "price": "2 300–2 800 ₽",
      "duration": "",
      "description": {
        "ru": "Мастер: 2 300 ₽; ТОП мастер: 2 800 ₽",
        "en": "Master: 2 300 ₽; Top master: 2 800 ₽"
      },
      "variants": [
        {
          "label": {
            "ru": "Мастер",
            "en": "Master"
          },
          "duration": "",
          "price": "2 300 ₽"
        },
        {
          "label": {
            "ru": "ТОП мастер",
            "en": "Top master"
          },
          "duration": "",
          "price": "2 800 ₽"
        }
      ]
    },
    {
      "id": "smarticure-no-coating",
      "category": "Маникюр",
      "title": {
        "ru": "Смартикюр /без покрытия/",
        "en": "Smarticure /without coating/"
      },
      "price": "3 700 ₽",
      "duration": "",
      "description": {
        "ru": "Мастер: —; ТОП мастер: 3 700 ₽",
        "en": "Master: —; Top master: 3 700 ₽"
      },
      "variants": [
        {
          "label": {
            "ru": "Мастер",
            "en": "Master"
          },
          "duration": "",
          "price": "—"
        },
        {
          "label": {
            "ru": "ТОП мастер",
            "en": "Top master"
          },
          "duration": "",
          "price": "3 700 ₽"
        }
      ]
    },
    {
      "id": "smarticure-with-coating",
      "category": "Маникюр",
      "title": {
        "ru": "Смартикюр /с покрытием/",
        "en": "Smarticure /with coating/"
      },
      "price": "5 000 ₽",
      "duration": "",
      "description": {
        "ru": "Мастер: —; ТОП мастер: 5 000 ₽",
        "en": "Master: —; Top master: 5 000 ₽"
      },
      "variants": [
        {
          "label": {
            "ru": "Мастер",
            "en": "Master"
          },
          "duration": "",
          "price": "—"
        },
        {
          "label": {
            "ru": "ТОП мастер",
            "en": "Top master"
          },
          "duration": "",
          "price": "5 000 ₽"
        }
      ]
    },
    {
      "id": "smarticure-half-foot",
      "category": "Маникюр",
      "title": {
        "ru": "Смартикюр 1/2 /стопа/",
        "en": "Smarticure 1/2 /foot/"
      },
      "price": "2 800 ₽",
      "duration": "",
      "description": {
        "ru": "Мастер: —; ТОП мастер: 2 800 ₽",
        "en": "Master: —; Top master: 2 800 ₽"
      },
      "variants": [
        {
          "label": {
            "ru": "Мастер",
            "en": "Master"
          },
          "duration": "",
          "price": "—"
        },
        {
          "label": {
            "ru": "ТОП мастер",
            "en": "Top master"
          },
          "duration": "",
          "price": "2 800 ₽"
        }
      ]
    },
    {
      "id": "mens-manicure",
      "category": "Маникюр",
      "title": {
        "ru": "Маникюр мужской",
        "en": "Men’s manicure"
      },
      "price": "1 100–1 500 ₽",
      "duration": "",
      "description": {
        "ru": "Мастер: 1 100 ₽; ТОП мастер: 1 500 ₽",
        "en": "Master: 1 100 ₽; Top master: 1 500 ₽"
      },
      "variants": [
        {
          "label": {
            "ru": "Мастер",
            "en": "Master"
          },
          "duration": "",
          "price": "1 100 ₽"
        },
        {
          "label": {
            "ru": "ТОП мастер",
            "en": "Top master"
          },
          "duration": "",
          "price": "1 500 ₽"
        }
      ]
    },
    {
      "id": "mens-smart-pedicure",
      "category": "Маникюр",
      "title": {
        "ru": "Педикюр смарт мужской",
        "en": "Men’s Smart pedicure"
      },
      "price": "2 700–3 500 ₽",
      "duration": "",
      "description": {
        "ru": "Мастер: 2 700 ₽; ТОП мастер: 3 500 ₽",
        "en": "Master: 2 700 ₽; Top master: 3 500 ₽"
      },
      "variants": [
        {
          "label": {
            "ru": "Мастер",
            "en": "Master"
          },
          "duration": "",
          "price": "2 700 ₽"
        },
        {
          "label": {
            "ru": "ТОП мастер",
            "en": "Top master"
          },
          "duration": "",
          "price": "3 500 ₽"
        }
      ]
    },
    {
      "id": "mens-pedicure-half",
      "category": "Маникюр",
      "title": {
        "ru": "Педикюр 1/2 (обработка пальцев/стопы)",
        "en": "Men’s pedicure 1/2 (toes/feet treatment)"
      },
      "price": "1 800–2 100 ₽",
      "duration": "",
      "description": {
        "ru": "Мастер: 1 800 ₽; ТОП мастер: 2 100 ₽",
        "en": "Master: 1 800 ₽; Top master: 2 100 ₽"
      },
      "variants": [
        {
          "label": {
            "ru": "Мастер",
            "en": "Master"
          },
          "duration": "",
          "price": "1 800 ₽"
        },
        {
          "label": {
            "ru": "ТОП мастер",
            "en": "Top master"
          },
          "duration": "",
          "price": "2 100 ₽"
        }
      ]
    },
    {
      "id": "mens-smarticure",
      "category": "Маникюр",
      "title": {
        "ru": "Смартикюр",
        "en": "Men’s Smarticure"
      },
      "price": "4 500 ₽",
      "duration": "",
      "description": {
        "ru": "Мастер: —; ТОП мастер: 4 500 ₽",
        "en": "Master: —; Top master: 4 500 ₽"
      },
      "variants": [
        {
          "label": {
            "ru": "Мастер",
            "en": "Master"
          },
          "duration": "",
          "price": "—"
        },
        {
          "label": {
            "ru": "ТОП мастер",
            "en": "Top master"
          },
          "duration": "",
          "price": "4 500 ₽"
        }
      ]
    },
    {
      "id": "mens-smarticure-foot",
      "category": "Маникюр",
      "title": {
        "ru": "Смартикюр (обработка стопы)",
        "en": "Smarticure (foot treatment)"
      },
      "price": "3 100 ₽",
      "duration": "",
      "description": {
        "ru": "Мастер: —; ТОП мастер: 3 100 ₽",
        "en": "Master: —; Top master: 3 100 ₽"
      },
      "variants": [
        {
          "label": {
            "ru": "Мастер",
            "en": "Master"
          },
          "duration": "",
          "price": "—"
        },
        {
          "label": {
            "ru": "ТОП мастер",
            "en": "Top master"
          },
          "duration": "",
          "price": "3 100 ₽"
        }
      ]
    },
    {
      "id": "child-manicure",
      "category": "Маникюр",
      "title": {
        "ru": "Маникюр детский (до 12 лет)",
        "en": "Children’s manicure (up to 12 years)"
      },
      "price": "500–600 ₽",
      "duration": "",
      "description": {
        "ru": "Мастер: 500 ₽; ТОП мастер: 600 ₽",
        "en": "Master: 500 ₽; Top master: 600 ₽"
      },
      "variants": [
        {
          "label": {
            "ru": "Мастер",
            "en": "Master"
          },
          "duration": "",
          "price": "500 ₽"
        },
        {
          "label": {
            "ru": "ТОП мастер",
            "en": "Top master"
          },
          "duration": "",
          "price": "600 ₽"
        }
      ]
    },
    {
      "id": "teen-manicure",
      "category": "Маникюр",
      "title": {
        "ru": "Маникюр подростковый (до 18 лет)",
        "en": "Teen manicure (up to 18 years)"
      },
      "price": "800–900 ₽",
      "duration": "",
      "description": {
        "ru": "Мастер: 800 ₽; ТОП мастер: 900 ₽",
        "en": "Master: 800 ₽; Top master: 900 ₽"
      },
      "variants": [
        {
          "label": {
            "ru": "Мастер",
            "en": "Master"
          },
          "duration": "",
          "price": "800 ₽"
        },
        {
          "label": {
            "ru": "ТОП мастер",
            "en": "Top master"
          },
          "duration": "",
          "price": "900 ₽"
        }
      ]
    },
    {
      "id": "child-pedicure",
      "category": "Маникюр",
      "title": {
        "ru": "Педикюр детский (до 12 лет, обработка пальцев)",
        "en": "Children’s pedicure (up to 12 years, toe treatment)"
      },
      "price": "500–600 ₽",
      "duration": "",
      "description": {
        "ru": "Мастер: 500 ₽; ТОП мастер: 600 ₽",
        "en": "Master: 500 ₽; Top master: 600 ₽"
      },
      "variants": [
        {
          "label": {
            "ru": "Мастер",
            "en": "Master"
          },
          "duration": "",
          "price": "500 ₽"
        },
        {
          "label": {
            "ru": "ТОП мастер",
            "en": "Top master"
          },
          "duration": "",
          "price": "600 ₽"
        }
      ]
    },
    {
      "id": "teen-pedicure",
      "category": "Маникюр",
      "title": {
        "ru": "Педикюр подростковый (до 18 лет, обработка пальцев)",
        "en": "Teen pedicure (up to 18 years, toe treatment)"
      },
      "price": "800–900 ₽",
      "duration": "",
      "description": {
        "ru": "Мастер: 800 ₽; ТОП мастер: 900 ₽",
        "en": "Master: 800 ₽; Top master: 900 ₽"
      },
      "variants": [
        {
          "label": {
            "ru": "Мастер",
            "en": "Master"
          },
          "duration": "",
          "price": "800 ₽"
        },
        {
          "label": {
            "ru": "ТОП мастер",
            "en": "Top master"
          },
          "duration": "",
          "price": "900 ₽"
        }
      ]
    },
    {
      "id": "nail-callus-treatment",
      "category": "Маникюр",
      "title": {
        "ru": "Обработка мозоля",
        "en": "Callus treatment"
      },
      "price": "от 500 до 1 000 ₽",
      "duration": "",
      "description": {
        "ru": "",
        "en": ""
      },
      "variants": []
    },
    {
      "id": "nail-onycholysis-treatment",
      "category": "Маникюр",
      "title": {
        "ru": "Обработка онихолизиса",
        "en": "Onycholysis treatment"
      },
      "price": "от 300 до 1 000 ₽",
      "duration": "",
      "description": {
        "ru": "",
        "en": ""
      },
      "variants": []
    },
    {
      "id": "brow-architecture",
      "category": "Брови и ресницы",
      "title": {
        "ru": "Архитектура",
        "en": "Brow architecture"
      },
      "price": "1 600 ₽",
      "duration": "",
      "description": {
        "ru": "",
        "en": ""
      },
      "variants": []
    },
    {
      "id": "brow-lamination",
      "category": "Брови и ресницы",
      "title": {
        "ru": "Ламинирование бровей",
        "en": "Brow lamination"
      },
      "price": "2 500 ₽",
      "duration": "",
      "description": {
        "ru": "",
        "en": ""
      },
      "variants": []
    },
    {
      "id": "lash-lamination",
      "category": "Брови и ресницы",
      "title": {
        "ru": "Ламинирование ресниц",
        "en": "Lash lamination"
      },
      "price": "2 500 ₽",
      "duration": "",
      "description": {
        "ru": "",
        "en": ""
      },
      "variants": []
    },
    {
      "id": "double-lash-lamination",
      "category": "Брови и ресницы",
      "title": {
        "ru": "Двойное ламинирование (верхние + нижние ресницы)",
        "en": "Double lamination (upper + lower lashes)"
      },
      "price": "3 400 ₽",
      "duration": "",
      "description": {
        "ru": "",
        "en": ""
      },
      "variants": []
    },
    {
      "id": "brow-lash-lamination-complex",
      "category": "Брови и ресницы",
      "title": {
        "ru": "Комплекс ламинирование бровей и ресниц",
        "en": "Brow and lash lamination package"
      },
      "price": "4 500 ₽",
      "duration": "",
      "description": {
        "ru": "",
        "en": ""
      },
      "variants": []
    },
    {
      "id": "brow-double-lash-complex",
      "category": "Брови и ресницы",
      "title": {
        "ru": "Комплекс ламинирование бровей и двойное ламинирование ресниц",
        "en": "Brow lamination + double lash lamination package"
      },
      "price": "5 400 ₽",
      "duration": "",
      "description": {
        "ru": "",
        "en": ""
      },
      "variants": []
    },
    {
      "id": "brow-coloring",
      "category": "Брови и ресницы",
      "title": {
        "ru": "Окрашивание бровей",
        "en": "Brow tinting"
      },
      "price": "900 ₽",
      "duration": "",
      "description": {
        "ru": "",
        "en": ""
      },
      "variants": []
    },
    {
      "id": "brow-correction",
      "category": "Брови и ресницы",
      "title": {
        "ru": "Коррекция бровей",
        "en": "Brow shaping"
      },
      "price": "900 ₽",
      "duration": "",
      "description": {
        "ru": "",
        "en": ""
      },
      "variants": []
    },
    {
      "id": "lash-coloring",
      "category": "Брови и ресницы",
      "title": {
        "ru": "Окрашивание ресниц",
        "en": "Lash tinting"
      },
      "price": "800 ₽",
      "duration": "",
      "description": {
        "ru": "",
        "en": ""
      },
      "variants": []
    },
    {
      "id": "lash-extensions-classic",
      "category": "Брови и ресницы",
      "title": {
        "ru": "Наращивание ресниц классика",
        "en": "Classic lash extensions"
      },
      "price": "3 000 ₽",
      "duration": "",
      "description": {
        "ru": "",
        "en": ""
      },
      "variants": []
    },
    {
      "id": "lash-extensions-15d",
      "category": "Брови и ресницы",
      "title": {
        "ru": "Наращивание ресниц 1/5 D",
        "en": "Lash extensions 1/5 D"
      },
      "price": "3 200 ₽",
      "duration": "",
      "description": {
        "ru": "",
        "en": ""
      },
      "variants": []
    },
    {
      "id": "lash-extensions-2d",
      "category": "Брови и ресницы",
      "title": {
        "ru": "Наращивание ресниц 2 D",
        "en": "Lash extensions 2D"
      },
      "price": "3 500 ₽",
      "duration": "",
      "description": {
        "ru": "",
        "en": ""
      },
      "variants": []
    },
    {
      "id": "lash-extensions-3d",
      "category": "Брови и ресницы",
      "title": {
        "ru": "Наращивание ресниц 3 D",
        "en": "Lash extensions 3D"
      },
      "price": "3 900 ₽",
      "duration": "",
      "description": {
        "ru": "",
        "en": ""
      },
      "variants": []
    },
    {
      "id": "lash-extensions-corners",
      "category": "Брови и ресницы",
      "title": {
        "ru": "Наращивание уголки",
        "en": "Lash extensions — corners"
      },
      "price": "2 000–2 500 ₽",
      "duration": "",
      "description": {
        "ru": "",
        "en": ""
      },
      "variants": []
    },
    {
      "id": "lash-removal",
      "category": "Брови и ресницы",
      "title": {
        "ru": "Снятие",
        "en": "Lash extension removal"
      },
      "price": "600 ₽",
      "duration": "",
      "description": {
        "ru": "",
        "en": ""
      },
      "variants": []
    },
    {
      "id": "pm-brows",
      "category": "Макияж",
      "title": {
        "ru": "Перманент бровей",
        "en": "Permanent eyebrow makeup"
      },
      "price": "8 000 ₽",
      "duration": "",
      "description": {
        "ru": "",
        "en": ""
      },
      "variants": []
    },
    {
      "id": "pm-eyeliner-shading",
      "category": "Макияж",
      "title": {
        "ru": "Перманент стрелка с растушевкой",
        "en": "Permanent eyeliner with shading"
      },
      "price": "8 000 ₽",
      "duration": "",
      "description": {
        "ru": "",
        "en": ""
      },
      "variants": []
    },
    {
      "id": "pm-eyeliner-classic",
      "category": "Макияж",
      "title": {
        "ru": "Перманент стрелка классика",
        "en": "Classic permanent eyeliner"
      },
      "price": "8 000 ₽",
      "duration": "",
      "description": {
        "ru": "",
        "en": ""
      },
      "variants": []
    },
    {
      "id": "pm-lashline",
      "category": "Макияж",
      "title": {
        "ru": "Перманент межресничка",
        "en": "Permanent lash-line enhancement"
      },
      "price": "6 000 ₽",
      "duration": "",
      "description": {
        "ru": "",
        "en": ""
      },
      "variants": []
    },
    {
      "id": "pm-lashline-shading",
      "category": "Макияж",
      "title": {
        "ru": "Перманент межресничка с растушевкой",
        "en": "Permanent lash-line enhancement with shading"
      },
      "price": "7 000 ₽",
      "duration": "",
      "description": {
        "ru": "",
        "en": ""
      },
      "variants": []
    },
    {
      "id": "pm-lips",
      "category": "Макияж",
      "title": {
        "ru": "Перманент губ",
        "en": "Permanent lip makeup"
      },
      "price": "8 000 ₽",
      "duration": "",
      "description": {
        "ru": "",
        "en": ""
      },
      "variants": []
    },
    {
      "id": "pm-lips-tint",
      "category": "Макияж",
      "title": {
        "ru": "Перманент губ в технике тинт",
        "en": "Permanent lip makeup — tint technique"
      },
      "price": "8 000 ₽",
      "duration": "",
      "description": {
        "ru": "",
        "en": ""
      },
      "variants": []
    },
    {
      "id": "pm-lips-watercolor",
      "category": "Макияж",
      "title": {
        "ru": "Перманент губ в технике акварель",
        "en": "Permanent lip makeup — watercolor technique"
      },
      "price": "8 000 ₽",
      "duration": "",
      "description": {
        "ru": "",
        "en": ""
      },
      "variants": []
    },
    {
      "id": "pm-brows-correction",
      "category": "Макияж",
      "title": {
        "ru": "Коррекция перманента бровей",
        "en": "Permanent eyebrow makeup correction"
      },
      "price": "6 000 ₽",
      "duration": "",
      "description": {
        "ru": "",
        "en": ""
      },
      "variants": []
    },
    {
      "id": "pm-eyeliner-correction",
      "category": "Макияж",
      "title": {
        "ru": "Коррекция перманента стрелка",
        "en": "Permanent eyeliner correction"
      },
      "price": "6 000 ₽",
      "duration": "",
      "description": {
        "ru": "",
        "en": ""
      },
      "variants": []
    },
    {
      "id": "pm-lashline-correction",
      "category": "Макияж",
      "title": {
        "ru": "Коррекция перманента межресничка",
        "en": "Permanent lash-line correction"
      },
      "price": "4 000 ₽",
      "duration": "",
      "description": {
        "ru": "",
        "en": ""
      },
      "variants": []
    },
    {
      "id": "pm-lips-correction",
      "category": "Макияж",
      "title": {
        "ru": "Коррекция перманента губы",
        "en": "Permanent lip makeup correction"
      },
      "price": "6 000 ₽",
      "duration": "",
      "description": {
        "ru": "",
        "en": ""
      },
      "variants": []
    },
    {
      "id": "pm-laser-removal",
      "category": "Макияж",
      "title": {
        "ru": "Лазерное удаление перманента",
        "en": "Laser removal of permanent makeup"
      },
      "price": "4 000 ₽",
      "duration": "",
      "description": {
        "ru": "",
        "en": ""
      },
      "variants": []
    },
    {
      "id": "cosmo-biorepeel-cleansing",
      "category": "Косметология",
      "title": {
        "ru": "Чистка лица Biorepeel",
        "en": "Biorepeel facial cleansing"
      },
      "price": "5 500 ₽",
      "duration": "",
      "description": {
        "ru": "",
        "en": ""
      },
      "variants": []
    },
    {
      "id": "cosmo-facial-cleansing",
      "category": "Косметология",
      "title": {
        "ru": "Чистка лица /препараты/ультразвуковая/механическая/",
        "en": "Facial cleansing /products / ultrasonic / mechanical/"
      },
      "price": "4 500 ₽",
      "duration": "",
      "description": {
        "ru": "",
        "en": ""
      },
      "variants": []
    },
    {
      "id": "cosmo-teen-cleansing",
      "category": "Косметология",
      "title": {
        "ru": "Чистка лица подростковая",
        "en": "Teen facial cleansing"
      },
      "price": "3 200 ₽",
      "duration": "",
      "description": {
        "ru": "",
        "en": ""
      },
      "variants": []
    },
    {
      "id": "cosmo-cleansing-carbon-peel",
      "category": "Косметология",
      "title": {
        "ru": "Комплекс: чистка лица + карбоновый пилинг",
        "en": "Package: facial cleansing + carbon peel"
      },
      "price": "5 000 ₽",
      "duration": "",
      "description": {
        "ru": "",
        "en": ""
      },
      "variants": []
    },
    {
      "id": "cosmo-rf-radiofrequency-face-neck",
      "category": "Косметология",
      "title": {
        "ru": "РФ-лифтинг радиочастотный /лицо+шея/",
        "en": "Radiofrequency RF lifting /face + neck/"
      },
      "price": "3 500 ₽",
      "duration": "",
      "description": {
        "ru": "",
        "en": ""
      },
      "variants": []
    },
    {
      "id": "cosmo-rf-microneedling-face",
      "category": "Косметология",
      "title": {
        "ru": "РФ-лифтинг микроигольчатый /лицо/",
        "en": "Microneedling RF lifting /face/"
      },
      "price": "20 000 ₽",
      "duration": "",
      "description": {
        "ru": "",
        "en": ""
      },
      "variants": []
    },
    {
      "id": "cosmo-rf-microneedling-eyes",
      "category": "Косметология",
      "title": {
        "ru": "РФ-лифтинг микроигольчатый /глаза/",
        "en": "Microneedling RF lifting /eyes/"
      },
      "price": "10 000 ₽",
      "duration": "",
      "description": {
        "ru": "",
        "en": ""
      },
      "variants": []
    },
    {
      "id": "cosmo-rf-microneedling-neck",
      "category": "Косметология",
      "title": {
        "ru": "РФ-лифтинг микроигольчатый /шея/",
        "en": "Microneedling RF lifting /neck/"
      },
      "price": "15 000 ₽",
      "duration": "",
      "description": {
        "ru": "",
        "en": ""
      },
      "variants": []
    },
    {
      "id": "cosmo-rf-microneedling-face-neck",
      "category": "Косметология",
      "title": {
        "ru": "РФ-лифтинг микроигольчатый /лицо+шея/",
        "en": "Microneedling RF lifting /face + neck/"
      },
      "price": "30 000 ₽",
      "duration": "",
      "description": {
        "ru": "",
        "en": ""
      },
      "variants": []
    },
    {
      "id": "cosmo-rf-microneedling-eyes-face-neck",
      "category": "Косметология",
      "title": {
        "ru": "РФ-лифтинг микроигольчатый /глаза+лицо+шея/",
        "en": "Microneedling RF lifting /eyes + face + neck/"
      },
      "price": "35 000 ₽",
      "duration": "",
      "description": {
        "ru": "",
        "en": ""
      },
      "variants": []
    },
    {
      "id": "cosmo-rf-microneedling-body",
      "category": "Косметология",
      "title": {
        "ru": "РФ-лифтинг микроигольчатый /тело 10*10/",
        "en": "Microneedling RF lifting /body 10*10/"
      },
      "price": "10 000 ₽",
      "duration": "",
      "description": {
        "ru": "",
        "en": ""
      },
      "variants": []
    },
    {
      "id": "cosmo-rf-microneedling-abdomen",
      "category": "Косметология",
      "title": {
        "ru": "РФ-лифтинг микроигольчатый /живот/",
        "en": "Microneedling RF lifting /abdomen/"
      },
      "price": "25 000 ₽",
      "duration": "",
      "description": {
        "ru": "",
        "en": ""
      },
      "variants": []
    },
    {
      "id": "cosmo-rf-microneedling-buttocks",
      "category": "Косметология",
      "title": {
        "ru": "РФ-лифтинг микроигольчатый /ягодицы/",
        "en": "Microneedling RF lifting /buttocks/"
      },
      "price": "25 000 ₽",
      "duration": "",
      "description": {
        "ru": "",
        "en": ""
      },
      "variants": []
    },
    {
      "id": "cosmo-rf-massage-microcurrents-complex",
      "category": "Косметология",
      "title": {
        "ru": "Комплекс: РФ-лифтинг+массаж/микротоки",
        "en": "Package: RF lifting + massage / microcurrents"
      },
      "price": "5 000 ₽",
      "duration": "",
      "description": {
        "ru": "",
        "en": ""
      },
      "variants": []
    },
    {
      "id": "cosmo-microcurrents-chiro-complex",
      "category": "Косметология",
      "title": {
        "ru": "Комплекс: микротоки+хиропластический массаж",
        "en": "Package: microcurrents + chiroplastic massage"
      },
      "price": "5 000 ₽",
      "duration": "",
      "description": {
        "ru": "",
        "en": ""
      },
      "variants": []
    },
    {
      "id": "cosmo-microcurrents-20",
      "category": "Косметология",
      "title": {
        "ru": "Микротоки /20 минут/",
        "en": "Microcurrent therapy /20 minutes/"
      },
      "price": "1 700 ₽",
      "duration": "",
      "description": {
        "ru": "",
        "en": ""
      },
      "variants": []
    },
    {
      "id": "cosmo-microcurrents-40",
      "category": "Косметология",
      "title": {
        "ru": "Микротоки /40 минут/",
        "en": "Microcurrent therapy /40 minutes/"
      },
      "price": "3 200 ₽",
      "duration": "",
      "description": {
        "ru": "",
        "en": ""
      },
      "variants": []
    },
    {
      "id": "cosmo-papilloma-removal",
      "category": "Косметология",
      "title": {
        "ru": "Удаление папилломы 1 единица",
        "en": "Papilloma removal, per unit"
      },
      "price": "400 ₽",
      "duration": "",
      "description": {
        "ru": "",
        "en": ""
      },
      "variants": []
    },
    {
      "id": "cosmo-milium-removal",
      "category": "Косметология",
      "title": {
        "ru": "Удаление милиума 1 единица",
        "en": "Milium removal, per unit"
      },
      "price": "400 ₽",
      "duration": "",
      "description": {
        "ru": "",
        "en": ""
      },
      "variants": []
    },
    {
      "id": "cosmo-ear-piercing",
      "category": "Косметология",
      "title": {
        "ru": "Прокол ушей + медицинские серьги",
        "en": "Ear piercing + medical earrings"
      },
      "price": "1 800 ₽",
      "duration": "",
      "description": {
        "ru": "",
        "en": ""
      },
      "variants": []
    },
    {
      "id": "depilation-face-full",
      "category": "Косметология",
      "title": {
        "ru": "Депиляция лицо /полностью/",
        "en": "Full-face waxing"
      },
      "price": "1 200 ₽",
      "duration": "",
      "description": {
        "ru": "",
        "en": ""
      },
      "variants": []
    },
    {
      "id": "depilation-nose-lip-chin",
      "category": "Косметология",
      "title": {
        "ru": "Депиляция нос/верхняя губа/подбородок",
        "en": "Waxing: nose / upper lip / chin"
      },
      "price": "600 ₽",
      "duration": "",
      "description": {
        "ru": "",
        "en": ""
      },
      "variants": []
    },
    {
      "id": "depilation-underarms",
      "category": "Косметология",
      "title": {
        "ru": "Депиляция подмышечные впадины",
        "en": "Underarm waxing"
      },
      "price": "1 000 ₽",
      "duration": "",
      "description": {
        "ru": "",
        "en": ""
      },
      "variants": []
    },
    {
      "id": "depilation-forearms",
      "category": "Косметология",
      "title": {
        "ru": "Депиляция предплечья",
        "en": "Forearm waxing"
      },
      "price": "900 ₽",
      "duration": "",
      "description": {
        "ru": "",
        "en": ""
      },
      "variants": []
    },
    {
      "id": "depilation-arms-to-elbow",
      "category": "Косметология",
      "title": {
        "ru": "Депиляция руки до локтя",
        "en": "Arms to elbows waxing"
      },
      "price": "1 200 ₽",
      "duration": "",
      "description": {
        "ru": "",
        "en": ""
      },
      "variants": []
    },
    {
      "id": "depilation-arms-full",
      "category": "Косметология",
      "title": {
        "ru": "Депиляция руки /полностью/",
        "en": "Full-arm waxing"
      },
      "price": "1 600 ₽",
      "duration": "",
      "description": {
        "ru": "",
        "en": ""
      },
      "variants": []
    },
    {
      "id": "depilation-back",
      "category": "Косметология",
      "title": {
        "ru": "Депиляция спина",
        "en": "Back waxing"
      },
      "price": "2 000 ₽",
      "duration": "",
      "description": {
        "ru": "",
        "en": ""
      },
      "variants": []
    },
    {
      "id": "depilation-abdomen",
      "category": "Косметология",
      "title": {
        "ru": "Депиляция живот",
        "en": "Abdomen waxing"
      },
      "price": "1 200 ₽",
      "duration": "",
      "description": {
        "ru": "",
        "en": ""
      },
      "variants": []
    },
    {
      "id": "depilation-legs-thigh-shin",
      "category": "Косметология",
      "title": {
        "ru": "Депиляция ноги бедро/голень",
        "en": "Leg waxing: thigh / lower leg"
      },
      "price": "1 500 ₽",
      "duration": "",
      "description": {
        "ru": "",
        "en": ""
      },
      "variants": []
    },
    {
      "id": "depilation-legs-full",
      "category": "Косметология",
      "title": {
        "ru": "Депиляция ноги полностью",
        "en": "Full-leg waxing"
      },
      "price": "2 500 ₽",
      "duration": "",
      "description": {
        "ru": "",
        "en": ""
      },
      "variants": []
    },
    {
      "id": "depilation-bikini-classic",
      "category": "Косметология",
      "title": {
        "ru": "Депиляция бикини классика",
        "en": "Classic bikini waxing"
      },
      "price": "1 200 ₽",
      "duration": "",
      "description": {
        "ru": "",
        "en": ""
      },
      "variants": []
    },
    {
      "id": "depilation-bikini-deep",
      "category": "Косметология",
      "title": {
        "ru": "Депиляция глубокое бикини",
        "en": "Deep bikini waxing"
      },
      "price": "2 500 ₽",
      "duration": "",
      "description": {
        "ru": "",
        "en": ""
      },
      "variants": []
    },
    {
      "id": "depilation-buttocks",
      "category": "Косметология",
      "title": {
        "ru": "Депиляция ягодицы",
        "en": "Buttocks waxing"
      },
      "price": "800 ₽",
      "duration": "",
      "description": {
        "ru": "",
        "en": ""
      },
      "variants": []
    },
    {
      "id": "laser-face-full",
      "category": "Косметология",
      "title": {
        "ru": "Лазерная эпиляция лицо /полностью/",
        "en": "Full-face laser hair removal"
      },
      "price": "1 200 ₽",
      "duration": "",
      "description": {
        "ru": "",
        "en": ""
      },
      "variants": []
    },
    {
      "id": "laser-upper-lip-chin",
      "category": "Косметология",
      "title": {
        "ru": "Лазерная эпиляция верхняя губа/подбородок",
        "en": "Laser hair removal: upper lip / chin"
      },
      "price": "400 ₽",
      "duration": "",
      "description": {
        "ru": "",
        "en": ""
      },
      "variants": []
    },
    {
      "id": "laser-neck-abdomen",
      "category": "Косметология",
      "title": {
        "ru": "Лазерная эпиляция шея/живот",
        "en": "Laser hair removal: neck / abdomen"
      },
      "price": "500 ₽",
      "duration": "",
      "description": {
        "ru": "",
        "en": ""
      },
      "variants": []
    },
    {
      "id": "laser-underarms",
      "category": "Косметология",
      "title": {
        "ru": "Лазерная эпиляция подмышечные впадины",
        "en": "Underarm laser hair removal"
      },
      "price": "800 ₽",
      "duration": "",
      "description": {
        "ru": "",
        "en": ""
      },
      "variants": []
    },
    {
      "id": "laser-forearms",
      "category": "Косметология",
      "title": {
        "ru": "Лазерная эпиляция предплечья",
        "en": "Forearm laser hair removal"
      },
      "price": "1 000 ₽",
      "duration": "",
      "description": {
        "ru": "",
        "en": ""
      },
      "variants": []
    },
    {
      "id": "laser-back",
      "category": "Косметология",
      "title": {
        "ru": "Лазерная эпиляция спина",
        "en": "Back laser hair removal"
      },
      "price": "2 500 ₽",
      "duration": "",
      "description": {
        "ru": "",
        "en": ""
      },
      "variants": []
    },
    {
      "id": "laser-bikini-classic",
      "category": "Косметология",
      "title": {
        "ru": "Лазерная эпиляция бикини классическое",
        "en": "Classic bikini laser hair removal"
      },
      "price": "1 000 ₽",
      "duration": "",
      "description": {
        "ru": "",
        "en": ""
      },
      "variants": []
    },
    {
      "id": "laser-bikini-deep",
      "category": "Косметология",
      "title": {
        "ru": "Лазерная эпиляция бикини глубокое",
        "en": "Deep bikini laser hair removal"
      },
      "price": "2 000 ₽",
      "duration": "",
      "description": {
        "ru": "",
        "en": ""
      },
      "variants": []
    },
    {
      "id": "laser-bikini-total",
      "category": "Косметология",
      "title": {
        "ru": "Лазерная эпиляция бикини тотальное",
        "en": "Full bikini laser hair removal"
      },
      "price": "2 500 ₽",
      "duration": "",
      "description": {
        "ru": "",
        "en": ""
      },
      "variants": []
    },
    {
      "id": "laser-buttocks",
      "category": "Косметология",
      "title": {
        "ru": "Лазерная эпиляция ягодицы",
        "en": "Buttocks laser hair removal"
      },
      "price": "1 000 ₽",
      "duration": "",
      "description": {
        "ru": "",
        "en": ""
      },
      "variants": []
    },
    {
      "id": "cosmo-chemical-peel",
      "category": "Косметология",
      "title": {
        "ru": "Химический пилинг",
        "en": "Chemical peel"
      },
      "price": "3 200 ₽",
      "duration": "",
      "description": {
        "ru": "",
        "en": ""
      },
      "variants": []
    },
    {
      "id": "cosmo-retinol-peel",
      "category": "Косметология",
      "title": {
        "ru": "Ретиноловый пилинг",
        "en": "Retinol peel"
      },
      "price": "4 500 ₽",
      "duration": "",
      "description": {
        "ru": "",
        "en": ""
      },
      "variants": []
    },
    {
      "id": "cosmo-face-neck-peel",
      "category": "Косметология",
      "title": {
        "ru": "Пилинг лицо+шея",
        "en": "Face + neck peel"
      },
      "price": "4 200 ₽",
      "duration": "",
      "description": {
        "ru": "",
        "en": ""
      },
      "variants": []
    },
    {
      "id": "cosmo-carbon-peel",
      "category": "Косметология",
      "title": {
        "ru": "Карбоновый пилинг",
        "en": "Carbon peel"
      },
      "price": "3 200 ₽",
      "duration": "",
      "description": {
        "ru": "",
        "en": ""
      },
      "variants": []
    },
    {
      "id": "cosmo-carboxytherapy",
      "category": "Косметология",
      "title": {
        "ru": "Карбокситерапия",
        "en": "Carboxytherapy"
      },
      "price": "3 500 ₽",
      "duration": "",
      "description": {
        "ru": "",
        "en": ""
      },
      "variants": []
    },
    {
      "id": "massage-back",
      "category": "Массаж",
      "title": {
        "ru": "Спина",
        "en": "Back massage"
      },
      "price": "2 500–3 000 ₽",
      "duration": "",
      "description": {
        "ru": "1 час: 2 500 ₽; 1,5 часа: 3 000 ₽",
        "en": "1 hour: 2 500 ₽; 1.5 hours: 3 000 ₽"
      },
      "variants": [
        {
          "label": {
            "ru": "1 час",
            "en": "1 hour"
          },
          "duration": "",
          "price": "2 500 ₽"
        },
        {
          "label": {
            "ru": "1,5 часа",
            "en": "1.5 hours"
          },
          "duration": "",
          "price": "3 000 ₽"
        }
      ]
    },
    {
      "id": "massage-general",
      "category": "Массаж",
      "title": {
        "ru": "Общий массаж",
        "en": "Full-body massage"
      },
      "price": "3 500–5 000 ₽",
      "duration": "",
      "description": {
        "ru": "1 час: 3 500 ₽; 1,5 часа: 5 000 ₽",
        "en": "1 hour: 3 500 ₽; 1.5 hours: 5 000 ₽"
      },
      "variants": [
        {
          "label": {
            "ru": "1 час",
            "en": "1 hour"
          },
          "duration": "",
          "price": "3 500 ₽"
        },
        {
          "label": {
            "ru": "1,5 часа",
            "en": "1.5 hours"
          },
          "duration": "",
          "price": "5 000 ₽"
        }
      ]
    },
    {
      "id": "complex-chiroplastic-massage",
      "category": "Комплексы",
      "title": {
        "ru": "Хиропластический массаж",
        "en": "Chiroplastic massage"
      },
      "price": "2 500 ₽",
      "duration": "",
      "description": {
        "ru": "",
        "en": ""
      },
      "variants": []
    },
    {
      "id": "complex-sculptural-massage",
      "category": "Комплексы",
      "title": {
        "ru": "Скульптурный массаж",
        "en": "Sculptural massage"
      },
      "price": "2 500 ₽",
      "duration": "",
      "description": {
        "ru": "",
        "en": ""
      },
      "variants": []
    },
    {
      "id": "tanning-minute",
      "category": "Другое",
      "title": {
        "ru": "Солярий — 1 минута",
        "en": "Tanning bed — 1 minute"
      },
      "price": "40 ₽",
      "duration": "",
      "description": {
        "ru": "",
        "en": ""
      },
      "variants": []
    },
    {
      "id": "tanning-stikini",
      "category": "Другое",
      "title": {
        "ru": "Стикини",
        "en": "Disposable tanning sticker"
      },
      "price": "30 ₽",
      "duration": "",
      "description": {
        "ru": "",
        "en": ""
      },
      "variants": []
    },
    {
      "id": "tanning-cream",
      "category": "Другое",
      "title": {
        "ru": "Крем в ассортименте",
        "en": "Cream (assorted)"
      },
      "price": "200 ₽",
      "duration": "",
      "description": {
        "ru": "",
        "en": ""
      },
      "variants": []
    },
    {
      "id": "tanning-cap-mat",
      "category": "Другое",
      "title": {
        "ru": "Шапочка + коврик (одноразовые)",
        "en": "Disposable cap + mat"
      },
      "price": {
        "ru": "Бесплатно",
        "en": "Free"
      },
      "duration": "",
      "description": {
        "ru": "",
        "en": ""
      },
      "variants": []
    },
    {
      "id": "hair-root-coloring",
      "category": "Волосы",
      "title": {
        "ru": "Окрашивание корней",
        "en": "Root coloring"
      },
      "price": "3 600–4 300 ₽",
      "duration": "",
      "description": {
        "ru": "Kezy: 3 600 ₽; JOC: 3 900 ₽; Permesse: 4 300 ₽",
        "en": "Kezy: 3 600 ₽; JOC: 3 900 ₽; Permesse: 4 300 ₽"
      },
      "variants": [
        {
          "label": {
            "ru": "Kezy",
            "en": "Kezy"
          },
          "duration": "",
          "price": "3 600 ₽"
        },
        {
          "label": {
            "ru": "JOC",
            "en": "JOC"
          },
          "duration": "",
          "price": "3 900 ₽"
        },
        {
          "label": {
            "ru": "Permesse",
            "en": "Permesse"
          },
          "duration": "",
          "price": "4 300 ₽"
        }
      ]
    },
    {
      "id": "hair-root-bleaching",
      "category": "Волосы",
      "title": {
        "ru": "Блондирование корней",
        "en": "Root bleaching"
      },
      "price": "3 500 ₽",
      "duration": "",
      "description": {
        "ru": "Kezy: 3 500 ₽; JOC: 3 500 ₽; Permesse: 3 500 ₽",
        "en": "Kezy: 3 500 ₽; JOC: 3 500 ₽; Permesse: 3 500 ₽"
      },
      "variants": [
        {
          "label": {
            "ru": "Kezy",
            "en": "Kezy"
          },
          "duration": "",
          "price": "3 500 ₽"
        },
        {
          "label": {
            "ru": "JOC",
            "en": "JOC"
          },
          "duration": "",
          "price": "3 500 ₽"
        },
        {
          "label": {
            "ru": "Permesse",
            "en": "Permesse"
          },
          "duration": "",
          "price": "3 500 ₽"
        }
      ]
    },
    {
      "id": "hair-root-bleaching-premium",
      "category": "Волосы",
      "title": {
        "ru": "Блондирование корней (пастой premium)",
        "en": "Root bleaching (premium paste)"
      },
      "price": "4 500 ₽",
      "duration": "",
      "description": {
        "ru": "Kezy: 4 500 ₽; JOC: 4 500 ₽; Permesse: 4 500 ₽",
        "en": "Kezy: 4 500 ₽; JOC: 4 500 ₽; Permesse: 4 500 ₽"
      },
      "variants": [
        {
          "label": {
            "ru": "Kezy",
            "en": "Kezy"
          },
          "duration": "",
          "price": "4 500 ₽"
        },
        {
          "label": {
            "ru": "JOC",
            "en": "JOC"
          },
          "duration": "",
          "price": "4 500 ₽"
        },
        {
          "label": {
            "ru": "Permesse",
            "en": "Permesse"
          },
          "duration": "",
          "price": "4 500 ₽"
        }
      ]
    },
    {
      "id": "hair-length-color-kezy",
      "category": "Волосы",
      "title": {
        "ru": "Окрашивание длины Kezy",
        "en": "Kezy hair-length coloring"
      },
      "price": "3 900–5 500 ₽",
      "duration": "",
      "description": {
        "ru": "Короткие: 3 900 ₽; Средние: 4 500 ₽; Длинные: 5 000 ₽; Очень длинные: 5 500 ₽",
        "en": "Short: 3 900 ₽; Medium: 4 500 ₽; Long: 5 000 ₽; Very long: 5 500 ₽"
      },
      "variants": [
        {
          "label": {
            "ru": "Короткие",
            "en": "Short"
          },
          "duration": "",
          "price": "3 900 ₽"
        },
        {
          "label": {
            "ru": "Средние",
            "en": "Medium"
          },
          "duration": "",
          "price": "4 500 ₽"
        },
        {
          "label": {
            "ru": "Длинные",
            "en": "Long"
          },
          "duration": "",
          "price": "5 000 ₽"
        },
        {
          "label": {
            "ru": "Очень длинные",
            "en": "Very long"
          },
          "duration": "",
          "price": "5 500 ₽"
        }
      ],
      "variantType": "length"
    },
    {
      "id": "hair-length-color-joc",
      "category": "Волосы",
      "title": {
        "ru": "Окрашивание длины JOC",
        "en": "JOC hair-length coloring"
      },
      "price": "4 500–7 600 ₽",
      "duration": "",
      "description": {
        "ru": "Короткие: 4 500 ₽; Средние: 5 500 ₽; Длинные: 6 600 ₽; Очень длинные: 7 600 ₽",
        "en": "Short: 4 500 ₽; Medium: 5 500 ₽; Long: 6 600 ₽; Very long: 7 600 ₽"
      },
      "variants": [
        {
          "label": {
            "ru": "Короткие",
            "en": "Short"
          },
          "duration": "",
          "price": "4 500 ₽"
        },
        {
          "label": {
            "ru": "Средние",
            "en": "Medium"
          },
          "duration": "",
          "price": "5 500 ₽"
        },
        {
          "label": {
            "ru": "Длинные",
            "en": "Long"
          },
          "duration": "",
          "price": "6 600 ₽"
        },
        {
          "label": {
            "ru": "Очень длинные",
            "en": "Very long"
          },
          "duration": "",
          "price": "7 600 ₽"
        }
      ],
      "variantType": "length"
    },
    {
      "id": "hair-length-color-permesse",
      "category": "Волосы",
      "title": {
        "ru": "Окрашивание длины Permesse",
        "en": "Permesse hair-length coloring"
      },
      "price": "5 500–8 600 ₽",
      "duration": "",
      "description": {
        "ru": "Короткие: 5 500 ₽; Средние: 6 500 ₽; Длинные: 7 500 ₽; Очень длинные: 8 600 ₽",
        "en": "Short: 5 500 ₽; Medium: 6 500 ₽; Long: 7 500 ₽; Very long: 8 600 ₽"
      },
      "variants": [
        {
          "label": {
            "ru": "Короткие",
            "en": "Short"
          },
          "duration": "",
          "price": "5 500 ₽"
        },
        {
          "label": {
            "ru": "Средние",
            "en": "Medium"
          },
          "duration": "",
          "price": "6 500 ₽"
        },
        {
          "label": {
            "ru": "Длинные",
            "en": "Long"
          },
          "duration": "",
          "price": "7 500 ₽"
        },
        {
          "label": {
            "ru": "Очень длинные",
            "en": "Very long"
          },
          "duration": "",
          "price": "8 600 ₽"
        }
      ],
      "variantType": "length"
    },
    {
      "id": "hair-complex-color-kezy",
      "category": "Волосы",
      "title": {
        "ru": "Сложное окрашивание длины Kezy",
        "en": "Kezy complex hair-length coloring"
      },
      "price": "9 000–11 500 ₽",
      "duration": "",
      "description": {
        "ru": "Короткие: —; Средние: 9 000 ₽; Длинные: 10 500 ₽; Очень длинные: 11 500 ₽",
        "en": "Short: —; Medium: 9 000 ₽; Long: 10 500 ₽; Very long: 11 500 ₽"
      },
      "variants": [
        {
          "label": {
            "ru": "Короткие",
            "en": "Short"
          },
          "duration": "",
          "price": "—"
        },
        {
          "label": {
            "ru": "Средние",
            "en": "Medium"
          },
          "duration": "",
          "price": "9 000 ₽"
        },
        {
          "label": {
            "ru": "Длинные",
            "en": "Long"
          },
          "duration": "",
          "price": "10 500 ₽"
        },
        {
          "label": {
            "ru": "Очень длинные",
            "en": "Very long"
          },
          "duration": "",
          "price": "11 500 ₽"
        }
      ],
      "variantType": "length"
    },
    {
      "id": "hair-complex-color-joc",
      "category": "Волосы",
      "title": {
        "ru": "Сложное окрашивание длины JOC",
        "en": "JOC complex hair-length coloring"
      },
      "price": "11 000–13 000 ₽",
      "duration": "",
      "description": {
        "ru": "Короткие: —; Средние: 11 000 ₽; Длинные: 12 000 ₽; Очень длинные: 13 000 ₽",
        "en": "Short: —; Medium: 11 000 ₽; Long: 12 000 ₽; Very long: 13 000 ₽"
      },
      "variants": [
        {
          "label": {
            "ru": "Короткие",
            "en": "Short"
          },
          "duration": "",
          "price": "—"
        },
        {
          "label": {
            "ru": "Средние",
            "en": "Medium"
          },
          "duration": "",
          "price": "11 000 ₽"
        },
        {
          "label": {
            "ru": "Длинные",
            "en": "Long"
          },
          "duration": "",
          "price": "12 000 ₽"
        },
        {
          "label": {
            "ru": "Очень длинные",
            "en": "Very long"
          },
          "duration": "",
          "price": "13 000 ₽"
        }
      ],
      "variantType": "length"
    },
    {
      "id": "hair-complex-color-permesse",
      "category": "Волосы",
      "title": {
        "ru": "Сложное окрашивание длины Permesse",
        "en": "Permesse complex hair-length coloring"
      },
      "price": "12 000–14 000 ₽",
      "duration": "",
      "description": {
        "ru": "Короткие: —; Средние: 12 000 ₽; Длинные: 13 000 ₽; Очень длинные: 14 000 ₽",
        "en": "Short: —; Medium: 12 000 ₽; Long: 13 000 ₽; Very long: 14 000 ₽"
      },
      "variants": [
        {
          "label": {
            "ru": "Короткие",
            "en": "Short"
          },
          "duration": "",
          "price": "—"
        },
        {
          "label": {
            "ru": "Средние",
            "en": "Medium"
          },
          "duration": "",
          "price": "12 000 ₽"
        },
        {
          "label": {
            "ru": "Длинные",
            "en": "Long"
          },
          "duration": "",
          "price": "13 000 ₽"
        },
        {
          "label": {
            "ru": "Очень длинные",
            "en": "Very long"
          },
          "duration": "",
          "price": "14 000 ₽"
        }
      ],
      "variantType": "length"
    },
    {
      "id": "haircut",
      "category": "Волосы",
      "title": {
        "ru": "Стрижка",
        "en": "Haircut"
      },
      "price": "1 400–2 000 ₽",
      "duration": "",
      "description": {
        "ru": "Короткие: 1 400 ₽; Средние: 1 600 ₽; Длинные: 1 800 ₽; Очень длинные: 2 000 ₽",
        "en": "Short: 1 400 ₽; Medium: 1 600 ₽; Long: 1 800 ₽; Very long: 2 000 ₽"
      },
      "variants": [
        {
          "label": {
            "ru": "Короткие",
            "en": "Short"
          },
          "duration": "",
          "price": "1 400 ₽"
        },
        {
          "label": {
            "ru": "Средние",
            "en": "Medium"
          },
          "duration": "",
          "price": "1 600 ₽"
        },
        {
          "label": {
            "ru": "Длинные",
            "en": "Long"
          },
          "duration": "",
          "price": "1 800 ₽"
        },
        {
          "label": {
            "ru": "Очень длинные",
            "en": "Very long"
          },
          "duration": "",
          "price": "2 000 ₽"
        }
      ],
      "variantType": "length"
    },
    {
      "id": "haircut-hot-scissors",
      "category": "Волосы",
      "title": {
        "ru": "Стрижка горячими ножницами",
        "en": "Hot-scissor haircut"
      },
      "price": "1 700–2 600 ₽",
      "duration": "",
      "description": {
        "ru": "Короткие: 1 700 ₽; Средние: 2 200 ₽; Длинные: 2 400 ₽; Очень длинные: 2 600 ₽",
        "en": "Short: 1 700 ₽; Medium: 2 200 ₽; Long: 2 400 ₽; Very long: 2 600 ₽"
      },
      "variants": [
        {
          "label": {
            "ru": "Короткие",
            "en": "Short"
          },
          "duration": "",
          "price": "1 700 ₽"
        },
        {
          "label": {
            "ru": "Средние",
            "en": "Medium"
          },
          "duration": "",
          "price": "2 200 ₽"
        },
        {
          "label": {
            "ru": "Длинные",
            "en": "Long"
          },
          "duration": "",
          "price": "2 400 ₽"
        },
        {
          "label": {
            "ru": "Очень длинные",
            "en": "Very long"
          },
          "duration": "",
          "price": "2 600 ₽"
        }
      ],
      "variantType": "length"
    },
    {
      "id": "haircut-bangs",
      "category": "Волосы",
      "title": {
        "ru": "Стрижка челки",
        "en": "Bangs trim"
      },
      "price": "450 ₽",
      "duration": "",
      "description": {
        "ru": "Короткие: 450 ₽; Средние: 450 ₽; Длинные: 450 ₽; Очень длинные: 450 ₽",
        "en": "Short: 450 ₽; Medium: 450 ₽; Long: 450 ₽; Very long: 450 ₽"
      },
      "variants": [
        {
          "label": {
            "ru": "Короткие",
            "en": "Short"
          },
          "duration": "",
          "price": "450 ₽"
        },
        {
          "label": {
            "ru": "Средние",
            "en": "Medium"
          },
          "duration": "",
          "price": "450 ₽"
        },
        {
          "label": {
            "ru": "Длинные",
            "en": "Long"
          },
          "duration": "",
          "price": "450 ₽"
        },
        {
          "label": {
            "ru": "Очень длинные",
            "en": "Very long"
          },
          "duration": "",
          "price": "450 ₽"
        }
      ],
      "variantType": "length"
    },
    {
      "id": "hair-trim-one-cut",
      "category": "Волосы",
      "title": {
        "ru": "Подравнивание одним срезом",
        "en": "One-length trim"
      },
      "price": "800 ₽",
      "duration": "",
      "description": {
        "ru": "Короткие: 800 ₽; Средние: 800 ₽; Длинные: 800 ₽; Очень длинные: 800 ₽",
        "en": "Short: 800 ₽; Medium: 800 ₽; Long: 800 ₽; Very long: 800 ₽"
      },
      "variants": [
        {
          "label": {
            "ru": "Короткие",
            "en": "Short"
          },
          "duration": "",
          "price": "800 ₽"
        },
        {
          "label": {
            "ru": "Средние",
            "en": "Medium"
          },
          "duration": "",
          "price": "800 ₽"
        },
        {
          "label": {
            "ru": "Длинные",
            "en": "Long"
          },
          "duration": "",
          "price": "800 ₽"
        },
        {
          "label": {
            "ru": "Очень длинные",
            "en": "Very long"
          },
          "duration": "",
          "price": "800 ₽"
        }
      ],
      "variantType": "length"
    },
    {
      "id": "hair-trim-hot-scissors",
      "category": "Волосы",
      "title": {
        "ru": "Подравнивание горячими ножницами",
        "en": "Hot-scissor trim"
      },
      "price": "1 200 ₽",
      "duration": "",
      "description": {
        "ru": "Короткие: 1 200 ₽; Средние: 1 200 ₽; Длинные: 1 200 ₽; Очень длинные: 1 200 ₽",
        "en": "Short: 1 200 ₽; Medium: 1 200 ₽; Long: 1 200 ₽; Very long: 1 200 ₽"
      },
      "variants": [
        {
          "label": {
            "ru": "Короткие",
            "en": "Short"
          },
          "duration": "",
          "price": "1 200 ₽"
        },
        {
          "label": {
            "ru": "Средние",
            "en": "Medium"
          },
          "duration": "",
          "price": "1 200 ₽"
        },
        {
          "label": {
            "ru": "Длинные",
            "en": "Long"
          },
          "duration": "",
          "price": "1 200 ₽"
        },
        {
          "label": {
            "ru": "Очень длинные",
            "en": "Very long"
          },
          "duration": "",
          "price": "1 200 ₽"
        }
      ],
      "variantType": "length"
    },
    {
      "id": "hair-care-kezy",
      "category": "Волосы",
      "title": {
        "ru": "Уход Kezy",
        "en": "Kezy hair treatment"
      },
      "price": "1 500–2 500 ₽",
      "duration": "",
      "description": {
        "ru": "Короткие: 1 500 ₽; Средние: 1 800 ₽; Длинные: 2 200 ₽; Очень длинные: 2 500 ₽",
        "en": "Short: 1 500 ₽; Medium: 1 800 ₽; Long: 2 200 ₽; Very long: 2 500 ₽"
      },
      "variants": [
        {
          "label": {
            "ru": "Короткие",
            "en": "Short"
          },
          "duration": "",
          "price": "1 500 ₽"
        },
        {
          "label": {
            "ru": "Средние",
            "en": "Medium"
          },
          "duration": "",
          "price": "1 800 ₽"
        },
        {
          "label": {
            "ru": "Длинные",
            "en": "Long"
          },
          "duration": "",
          "price": "2 200 ₽"
        },
        {
          "label": {
            "ru": "Очень длинные",
            "en": "Very long"
          },
          "duration": "",
          "price": "2 500 ₽"
        }
      ],
      "variantType": "length"
    },
    {
      "id": "hair-care-hemp",
      "category": "Волосы",
      "title": {
        "ru": "Уход HEMP «Конопля»",
        "en": "HEMP “Hemp” hair treatment"
      },
      "price": "2 000–3 500 ₽",
      "duration": "",
      "description": {
        "ru": "Короткие: 2 000 ₽; Средние: 2 500 ₽; Длинные: 3 000 ₽; Очень длинные: 3 500 ₽",
        "en": "Short: 2 000 ₽; Medium: 2 500 ₽; Long: 3 000 ₽; Very long: 3 500 ₽"
      },
      "variants": [
        {
          "label": {
            "ru": "Короткие",
            "en": "Short"
          },
          "duration": "",
          "price": "2 000 ₽"
        },
        {
          "label": {
            "ru": "Средние",
            "en": "Medium"
          },
          "duration": "",
          "price": "2 500 ₽"
        },
        {
          "label": {
            "ru": "Длинные",
            "en": "Long"
          },
          "duration": "",
          "price": "3 000 ₽"
        },
        {
          "label": {
            "ru": "Очень длинные",
            "en": "Very long"
          },
          "duration": "",
          "price": "3 500 ₽"
        }
      ],
      "variantType": "length"
    },
    {
      "id": "hair-care-black-caviar",
      "category": "Волосы",
      "title": {
        "ru": "Уход ONCAP BLAK «Черная икра»",
        "en": "ONCAP BLAK “Black Caviar” treatment"
      },
      "price": "2 000–3 500 ₽",
      "duration": "",
      "description": {
        "ru": "Короткие: 2 000 ₽; Средние: 2 500 ₽; Длинные: 3 000 ₽; Очень длинные: 3 500 ₽",
        "en": "Short: 2 000 ₽; Medium: 2 500 ₽; Long: 3 000 ₽; Very long: 3 500 ₽"
      },
      "variants": [
        {
          "label": {
            "ru": "Короткие",
            "en": "Short"
          },
          "duration": "",
          "price": "2 000 ₽"
        },
        {
          "label": {
            "ru": "Средние",
            "en": "Medium"
          },
          "duration": "",
          "price": "2 500 ₽"
        },
        {
          "label": {
            "ru": "Длинные",
            "en": "Long"
          },
          "duration": "",
          "price": "3 000 ₽"
        },
        {
          "label": {
            "ru": "Очень длинные",
            "en": "Very long"
          },
          "duration": "",
          "price": "3 500 ₽"
        }
      ],
      "variantType": "length"
    },
    {
      "id": "hair-care-barex-silk",
      "category": "Волосы",
      "title": {
        "ru": "Уход BAREX «Протеины шёлка»",
        "en": "BAREX “Silk Proteins” treatment"
      },
      "price": "3 000–4 500 ₽",
      "duration": "",
      "description": {
        "ru": "Короткие: 3 000 ₽; Средние: 3 500 ₽; Длинные: 4 000 ₽; Очень длинные: 4 500 ₽",
        "en": "Short: 3 000 ₽; Medium: 3 500 ₽; Long: 4 000 ₽; Very long: 4 500 ₽"
      },
      "variants": [
        {
          "label": {
            "ru": "Короткие",
            "en": "Short"
          },
          "duration": "",
          "price": "3 000 ₽"
        },
        {
          "label": {
            "ru": "Средние",
            "en": "Medium"
          },
          "duration": "",
          "price": "3 500 ₽"
        },
        {
          "label": {
            "ru": "Длинные",
            "en": "Long"
          },
          "duration": "",
          "price": "4 000 ₽"
        },
        {
          "label": {
            "ru": "Очень длинные",
            "en": "Very long"
          },
          "duration": "",
          "price": "4 500 ₽"
        }
      ],
      "variantType": "length"
    },
    {
      "id": "hair-care-oncare-scalp",
      "category": "Волосы",
      "title": {
        "ru": "Уход ONCARE SCALP /для кожи головы/",
        "en": "ONCARE SCALP treatment /for the scalp/"
      },
      "price": "2 000 ₽",
      "duration": "",
      "description": {
        "ru": "Короткие: 2 000 ₽; Средние: 2 000 ₽; Длинные: 2 000 ₽; Очень длинные: 2 000 ₽",
        "en": "Short: 2 000 ₽; Medium: 2 000 ₽; Long: 2 000 ₽; Very long: 2 000 ₽"
      },
      "variants": [
        {
          "label": {
            "ru": "Короткие",
            "en": "Short"
          },
          "duration": "",
          "price": "2 000 ₽"
        },
        {
          "label": {
            "ru": "Средние",
            "en": "Medium"
          },
          "duration": "",
          "price": "2 000 ₽"
        },
        {
          "label": {
            "ru": "Длинные",
            "en": "Long"
          },
          "duration": "",
          "price": "2 000 ₽"
        },
        {
          "label": {
            "ru": "Очень длинные",
            "en": "Very long"
          },
          "duration": "",
          "price": "2 000 ₽"
        }
      ],
      "variantType": "length"
    },
    {
      "id": "hair-styling-brush",
      "category": "Волосы",
      "title": {
        "ru": "Укладка феном на брашинг",
        "en": "Blow-dry with a round brush"
      },
      "price": "1 100–1 800 ₽",
      "duration": "",
      "description": {
        "ru": "Короткие: 1 100 ₽; Средние: 1 400 ₽; Длинные: 1 600 ₽; Очень длинные: 1 800 ₽",
        "en": "Short: 1 100 ₽; Medium: 1 400 ₽; Long: 1 600 ₽; Very long: 1 800 ₽"
      },
      "variants": [
        {
          "label": {
            "ru": "Короткие",
            "en": "Short"
          },
          "duration": "",
          "price": "1 100 ₽"
        },
        {
          "label": {
            "ru": "Средние",
            "en": "Medium"
          },
          "duration": "",
          "price": "1 400 ₽"
        },
        {
          "label": {
            "ru": "Длинные",
            "en": "Long"
          },
          "duration": "",
          "price": "1 600 ₽"
        },
        {
          "label": {
            "ru": "Очень длинные",
            "en": "Very long"
          },
          "duration": "",
          "price": "1 800 ₽"
        }
      ],
      "variantType": "length"
    },
    {
      "id": "hair-styling-tongs",
      "category": "Волосы",
      "title": {
        "ru": "Укладка на щипцы",
        "en": "Styling with curling tongs"
      },
      "price": "1 300–2 100 ₽",
      "duration": "",
      "description": {
        "ru": "Короткие: 1 300 ₽; Средние: 1 500 ₽; Длинные: 1 800 ₽; Очень длинные: 2 100 ₽",
        "en": "Short: 1 300 ₽; Medium: 1 500 ₽; Long: 1 800 ₽; Very long: 2 100 ₽"
      },
      "variants": [
        {
          "label": {
            "ru": "Короткие",
            "en": "Short"
          },
          "duration": "",
          "price": "1 300 ₽"
        },
        {
          "label": {
            "ru": "Средние",
            "en": "Medium"
          },
          "duration": "",
          "price": "1 500 ₽"
        },
        {
          "label": {
            "ru": "Длинные",
            "en": "Long"
          },
          "duration": "",
          "price": "1 800 ₽"
        },
        {
          "label": {
            "ru": "Очень длинные",
            "en": "Very long"
          },
          "duration": "",
          "price": "2 100 ₽"
        }
      ],
      "variantType": "length"
    },
    {
      "id": "hair-styling-flat-iron",
      "category": "Волосы",
      "title": {
        "ru": "Укладка утюжком",
        "en": "Flat-iron styling"
      },
      "price": "1 620 ₽",
      "duration": "",
      "description": {
        "ru": "Короткие: 1 620 ₽; Средние: 1 620 ₽; Длинные: 1 620 ₽; Очень длинные: 1 620 ₽",
        "en": "Short: 1 620 ₽; Medium: 1 620 ₽; Long: 1 620 ₽; Very long: 1 620 ₽"
      },
      "variants": [
        {
          "label": {
            "ru": "Короткие",
            "en": "Short"
          },
          "duration": "",
          "price": "1 620 ₽"
        },
        {
          "label": {
            "ru": "Средние",
            "en": "Medium"
          },
          "duration": "",
          "price": "1 620 ₽"
        },
        {
          "label": {
            "ru": "Длинные",
            "en": "Long"
          },
          "duration": "",
          "price": "1 620 ₽"
        },
        {
          "label": {
            "ru": "Очень длинные",
            "en": "Very long"
          },
          "duration": "",
          "price": "1 620 ₽"
        }
      ],
      "variantType": "length"
    },
    {
      "id": "hair-styling-evening",
      "category": "Волосы",
      "title": {
        "ru": "Укладка вечерняя",
        "en": "Evening styling"
      },
      "price": "1 500–3 000 ₽",
      "duration": "",
      "description": {
        "ru": "Короткие: 1 500 ₽; Средние: 2 000 ₽; Длинные: 2 500 ₽; Очень длинные: 3 000 ₽",
        "en": "Short: 1 500 ₽; Medium: 2 000 ₽; Long: 2 500 ₽; Very long: 3 000 ₽"
      },
      "variants": [
        {
          "label": {
            "ru": "Короткие",
            "en": "Short"
          },
          "duration": "",
          "price": "1 500 ₽"
        },
        {
          "label": {
            "ru": "Средние",
            "en": "Medium"
          },
          "duration": "",
          "price": "2 000 ₽"
        },
        {
          "label": {
            "ru": "Длинные",
            "en": "Long"
          },
          "duration": "",
          "price": "2 500 ₽"
        },
        {
          "label": {
            "ru": "Очень длинные",
            "en": "Very long"
          },
          "duration": "",
          "price": "3 000 ₽"
        }
      ],
      "variantType": "length"
    },
    {
      "id": "hair-color-cleanse",
      "category": "Волосы",
      "title": {
        "ru": "Чистка цвета",
        "en": "Color cleansing"
      },
      "price": "1 000–1 350 ₽",
      "duration": "",
      "description": {
        "ru": "Короткие: 1 000 ₽; Средние: 1 100 ₽; Длинные: 1 200 ₽; Очень длинные: 1 350 ₽",
        "en": "Short: 1 000 ₽; Medium: 1 100 ₽; Long: 1 200 ₽; Very long: 1 350 ₽"
      },
      "variants": [
        {
          "label": {
            "ru": "Короткие",
            "en": "Short"
          },
          "duration": "",
          "price": "1 000 ₽"
        },
        {
          "label": {
            "ru": "Средние",
            "en": "Medium"
          },
          "duration": "",
          "price": "1 100 ₽"
        },
        {
          "label": {
            "ru": "Длинные",
            "en": "Long"
          },
          "duration": "",
          "price": "1 200 ₽"
        },
        {
          "label": {
            "ru": "Очень длинные",
            "en": "Very long"
          },
          "duration": "",
          "price": "1 350 ₽"
        }
      ],
      "variantType": "length"
    },
    {
      "id": "hair-color-cleanse-acid",
      "category": "Волосы",
      "title": {
        "ru": "Чистка цвета кислотная смывка",
        "en": "Color cleansing with an acid remover"
      },
      "price": "2 000–3 000 ₽",
      "duration": "",
      "description": {
        "ru": "Короткие: 2 000 ₽; Средние: 2 500 ₽; Длинные: 3 000 ₽; Очень длинные: —",
        "en": "Short: 2 000 ₽; Medium: 2 500 ₽; Long: 3 000 ₽; Very long: —"
      },
      "variants": [
        {
          "label": {
            "ru": "Короткие",
            "en": "Short"
          },
          "duration": "",
          "price": "2 000 ₽"
        },
        {
          "label": {
            "ru": "Средние",
            "en": "Medium"
          },
          "duration": "",
          "price": "2 500 ₽"
        },
        {
          "label": {
            "ru": "Длинные",
            "en": "Long"
          },
          "duration": "",
          "price": "3 000 ₽"
        },
        {
          "label": {
            "ru": "Очень длинные",
            "en": "Very long"
          },
          "duration": "",
          "price": "—"
        }
      ],
      "variantType": "length"
    },
    {
      "id": "hair-color-bath",
      "category": "Волосы",
      "title": {
        "ru": "Цветовая баня",
        "en": "Color bath"
      },
      "price": "1 000 ₽",
      "duration": "",
      "description": {
        "ru": "Короткие: 1 000 ₽; Средние: 1 000 ₽; Длинные: 1 000 ₽; Очень длинные: 1 000 ₽",
        "en": "Short: 1 000 ₽; Medium: 1 000 ₽; Long: 1 000 ₽; Very long: 1 000 ₽"
      },
      "variants": [
        {
          "label": {
            "ru": "Короткие",
            "en": "Short"
          },
          "duration": "",
          "price": "1 000 ₽"
        },
        {
          "label": {
            "ru": "Средние",
            "en": "Medium"
          },
          "duration": "",
          "price": "1 000 ₽"
        },
        {
          "label": {
            "ru": "Длинные",
            "en": "Long"
          },
          "duration": "",
          "price": "1 000 ₽"
        },
        {
          "label": {
            "ru": "Очень длинные",
            "en": "Very long"
          },
          "duration": "",
          "price": "1 000 ₽"
        }
      ],
      "variantType": "length"
    },
    {
      "id": "hair-repigmentation",
      "category": "Волосы",
      "title": {
        "ru": "Репигментация",
        "en": "Repigmentation"
      },
      "price": "1 000–1 500 ₽",
      "duration": "",
      "description": {
        "ru": "Короткие: 1 000 ₽; Средние: 1 500 ₽; Длинные: —; Очень длинные: —",
        "en": "Short: 1 000 ₽; Medium: 1 500 ₽; Long: —; Very long: —"
      },
      "variants": [
        {
          "label": {
            "ru": "Короткие",
            "en": "Short"
          },
          "duration": "",
          "price": "1 000 ₽"
        },
        {
          "label": {
            "ru": "Средние",
            "en": "Medium"
          },
          "duration": "",
          "price": "1 500 ₽"
        },
        {
          "label": {
            "ru": "Длинные",
            "en": "Long"
          },
          "duration": "",
          "price": "—"
        },
        {
          "label": {
            "ru": "Очень длинные",
            "en": "Very long"
          },
          "duration": "",
          "price": "—"
        }
      ],
      "variantType": "length"
    },
    {
      "id": "hair-decapitation",
      "category": "Волосы",
      "title": {
        "ru": "Декапирование (кислотная смывка)",
        "en": "Decapitation (acid remover)"
      },
      "price": "2 000–3 000 ₽",
      "duration": "",
      "description": {
        "ru": "Короткие: 2 000 ₽; Средние: 2 450 ₽; Длинные: 3 000 ₽; Очень длинные: —",
        "en": "Short: 2 000 ₽; Medium: 2 450 ₽; Long: 3 000 ₽; Very long: —"
      },
      "variants": [
        {
          "label": {
            "ru": "Короткие",
            "en": "Short"
          },
          "duration": "",
          "price": "2 000 ₽"
        },
        {
          "label": {
            "ru": "Средние",
            "en": "Medium"
          },
          "duration": "",
          "price": "2 450 ₽"
        },
        {
          "label": {
            "ru": "Длинные",
            "en": "Long"
          },
          "duration": "",
          "price": "3 000 ₽"
        },
        {
          "label": {
            "ru": "Очень длинные",
            "en": "Very long"
          },
          "duration": "",
          "price": "—"
        }
      ],
      "variantType": "length"
    },
    {
      "id": "hair-wash",
      "category": "Волосы",
      "title": {
        "ru": "Мытьё головы",
        "en": "Hair wash"
      },
      "price": "300–700 ₽",
      "duration": "",
      "description": {
        "ru": "Короткие: 300 ₽; Средние: 400 ₽; Длинные: 500 ₽; Очень длинные: 700 ₽",
        "en": "Short: 300 ₽; Medium: 400 ₽; Long: 500 ₽; Very long: 700 ₽"
      },
      "variants": [
        {
          "label": {
            "ru": "Короткие",
            "en": "Short"
          },
          "duration": "",
          "price": "300 ₽"
        },
        {
          "label": {
            "ru": "Средние",
            "en": "Medium"
          },
          "duration": "",
          "price": "400 ₽"
        },
        {
          "label": {
            "ru": "Длинные",
            "en": "Long"
          },
          "duration": "",
          "price": "500 ₽"
        },
        {
          "label": {
            "ru": "Очень длинные",
            "en": "Very long"
          },
          "duration": "",
          "price": "700 ₽"
        }
      ],
      "variantType": "length"
    },
    {
      "id": "hair-wash-dry",
      "category": "Волосы",
      "title": {
        "ru": "Мытьё + сушка волос",
        "en": "Hair wash + blow-dry"
      },
      "price": "500–900 ₽",
      "duration": "",
      "description": {
        "ru": "Короткие: 500 ₽; Средние: 600 ₽; Длинные: 700 ₽; Очень длинные: 900 ₽",
        "en": "Short: 500 ₽; Medium: 600 ₽; Long: 700 ₽; Very long: 900 ₽"
      },
      "variants": [
        {
          "label": {
            "ru": "Короткие",
            "en": "Short"
          },
          "duration": "",
          "price": "500 ₽"
        },
        {
          "label": {
            "ru": "Средние",
            "en": "Medium"
          },
          "duration": "",
          "price": "600 ₽"
        },
        {
          "label": {
            "ru": "Длинные",
            "en": "Long"
          },
          "duration": "",
          "price": "700 ₽"
        },
        {
          "label": {
            "ru": "Очень длинные",
            "en": "Very long"
          },
          "duration": "",
          "price": "900 ₽"
        }
      ],
      "variantType": "length"
    },
    {
      "id": "hair-styling-products",
      "category": "Волосы",
      "title": {
        "ru": "Лак, гель, пенка, воск для волос",
        "en": "Hairspray, gel, mousse, hair wax"
      },
      "price": "1 000 ₽",
      "duration": "",
      "description": {
        "ru": "",
        "en": ""
      },
      "variants": []
    },
    {
      "id": "hair-color-one-strand",
      "category": "Волосы",
      "title": {
        "ru": "Окрашивание одной пряди",
        "en": "Single-strand coloring"
      },
      "price": "1 100 ₽",
      "duration": "",
      "description": {
        "ru": "",
        "en": ""
      },
      "variants": []
    },
    {
      "id": "hair-braiding",
      "category": "Волосы",
      "title": {
        "ru": "Плетение кос",
        "en": "Braiding"
      },
      "price": "800 ₽",
      "duration": "",
      "description": {
        "ru": "",
        "en": ""
      },
      "variants": []
    },
    {
      "id": "haircut-mens-buzz",
      "category": "Волосы",
      "title": {
        "ru": "Стрижка мужская наголо",
        "en": "Men’s buzz cut"
      },
      "price": "500 ₽",
      "duration": "",
      "description": {
        "ru": "",
        "en": ""
      },
      "variants": []
    },
    {
      "id": "haircut-mens-sport",
      "category": "Волосы",
      "title": {
        "ru": "Стрижка мужская спортивная",
        "en": "Men’s sports haircut"
      },
      "price": "700 ₽",
      "duration": "",
      "description": {
        "ru": "",
        "en": ""
      },
      "variants": []
    },
    {
      "id": "haircut-mens-model",
      "category": "Волосы",
      "title": {
        "ru": "Стрижка мужская модельная",
        "en": "Men’s model haircut"
      },
      "price": "1 500 ₽",
      "duration": "",
      "description": {
        "ru": "",
        "en": ""
      },
      "variants": []
    },
    {
      "id": "haircut-eyebrows",
      "category": "Волосы",
      "title": {
        "ru": "Стрижка бровей",
        "en": "Eyebrow trim"
      },
      "price": "150 ₽",
      "duration": "",
      "description": {
        "ru": "",
        "en": ""
      },
      "variants": []
    },
    {
      "id": "haircut-beard",
      "category": "Волосы",
      "title": {
        "ru": "Стрижка бороды",
        "en": "Beard trim"
      },
      "price": "250 ₽",
      "duration": "",
      "description": {
        "ru": "",
        "en": ""
      },
      "variants": []
    },
    {
      "id": "hair-outline",
      "category": "Волосы",
      "title": {
        "ru": "Окантовка волос",
        "en": "Hairline edging"
      },
      "price": "500 ₽",
      "duration": "",
      "description": {
        "ru": "",
        "en": ""
      },
      "variants": []
    },
    {
      "id": "haircut-child",
      "category": "Волосы",
      "title": {
        "ru": "Стрижка детская",
        "en": "Children’s haircut"
      },
      "price": "1 000 ₽",
      "duration": "",
      "description": {
        "ru": "",
        "en": ""
      },
      "variants": []
    },
    {
      "id": "haircut-child-bangs",
      "category": "Волосы",
      "title": {
        "ru": "Стрижка детской челки",
        "en": "Children’s bangs trim"
      },
      "price": "450 ₽",
      "duration": "",
      "description": {
        "ru": "",
        "en": ""
      },
      "variants": []
    },
    {
      "id": "hair-root-highlights-kezy-3cm",
      "category": "Волосы",
      "title": {
        "ru": "Прикорневое мелирование Kezy /до 3 см/",
        "en": "Kezy root highlights /up to 3 cm/"
      },
      "price": "3 700 ₽",
      "duration": "",
      "description": {
        "ru": "Короткие: 3 700 ₽; Средние: 3 700 ₽; Длинные: 3 700 ₽; Очень длинные: 3 700 ₽",
        "en": "Short: 3 700 ₽; Medium: 3 700 ₽; Long: 3 700 ₽; Very long: 3 700 ₽"
      },
      "variants": [
        {
          "label": {
            "ru": "Короткие",
            "en": "Short"
          },
          "duration": "",
          "price": "3 700 ₽"
        },
        {
          "label": {
            "ru": "Средние",
            "en": "Medium"
          },
          "duration": "",
          "price": "3 700 ₽"
        },
        {
          "label": {
            "ru": "Длинные",
            "en": "Long"
          },
          "duration": "",
          "price": "3 700 ₽"
        },
        {
          "label": {
            "ru": "Очень длинные",
            "en": "Very long"
          },
          "duration": "",
          "price": "3 700 ₽"
        }
      ],
      "variantType": "length"
    },
    {
      "id": "hair-root-highlights-kezy",
      "category": "Волосы",
      "title": {
        "ru": "Прикорневое мелирование Kezy",
        "en": "Kezy root highlights"
      },
      "price": "4 000 ₽",
      "duration": "",
      "description": {
        "ru": "Короткие: 4 000 ₽; Средние: 4 000 ₽; Длинные: 4 000 ₽; Очень длинные: 4 000 ₽",
        "en": "Short: 4 000 ₽; Medium: 4 000 ₽; Long: 4 000 ₽; Very long: 4 000 ₽"
      },
      "variants": [
        {
          "label": {
            "ru": "Короткие",
            "en": "Short"
          },
          "duration": "",
          "price": "4 000 ₽"
        },
        {
          "label": {
            "ru": "Средние",
            "en": "Medium"
          },
          "duration": "",
          "price": "4 000 ₽"
        },
        {
          "label": {
            "ru": "Длинные",
            "en": "Long"
          },
          "duration": "",
          "price": "4 000 ₽"
        },
        {
          "label": {
            "ru": "Очень длинные",
            "en": "Very long"
          },
          "duration": "",
          "price": "4 000 ₽"
        }
      ],
      "variantType": "length"
    },
    {
      "id": "hair-highlights-kezy",
      "category": "Волосы",
      "title": {
        "ru": "Мелирование Kezy",
        "en": "Kezy highlights"
      },
      "price": "4 100–6 700 ₽",
      "duration": "",
      "description": {
        "ru": "Короткие: 4 100 ₽; Средние: 4 700 ₽; Длинные: 5 700 ₽; Очень длинные: 6 700 ₽",
        "en": "Short: 4 100 ₽; Medium: 4 700 ₽; Long: 5 700 ₽; Very long: 6 700 ₽"
      },
      "variants": [
        {
          "label": {
            "ru": "Короткие",
            "en": "Short"
          },
          "duration": "",
          "price": "4 100 ₽"
        },
        {
          "label": {
            "ru": "Средние",
            "en": "Medium"
          },
          "duration": "",
          "price": "4 700 ₽"
        },
        {
          "label": {
            "ru": "Длинные",
            "en": "Long"
          },
          "duration": "",
          "price": "5 700 ₽"
        },
        {
          "label": {
            "ru": "Очень длинные",
            "en": "Very long"
          },
          "duration": "",
          "price": "6 700 ₽"
        }
      ],
      "variantType": "length"
    },
    {
      "id": "hair-highlights-barex",
      "category": "Волосы",
      "title": {
        "ru": "Мелирование BAREX",
        "en": "BAREX highlights"
      },
      "price": "4 000–6 700 ₽",
      "duration": "",
      "description": {
        "ru": "Короткие: 4 000 ₽; Средние: 4 700 ₽; Длинные: 5 700 ₽; Очень длинные: 6 700 ₽",
        "en": "Short: 4 000 ₽; Medium: 4 700 ₽; Long: 5 700 ₽; Very long: 6 700 ₽"
      },
      "variants": [
        {
          "label": {
            "ru": "Короткие",
            "en": "Short"
          },
          "duration": "",
          "price": "4 000 ₽"
        },
        {
          "label": {
            "ru": "Средние",
            "en": "Medium"
          },
          "duration": "",
          "price": "4 700 ₽"
        },
        {
          "label": {
            "ru": "Длинные",
            "en": "Long"
          },
          "duration": "",
          "price": "5 700 ₽"
        },
        {
          "label": {
            "ru": "Очень длинные",
            "en": "Very long"
          },
          "duration": "",
          "price": "6 700 ₽"
        }
      ],
      "variantType": "length"
    },
    {
      "id": "hair-toning-kezy",
      "category": "Волосы",
      "title": {
        "ru": "Тонирование длины Kezy",
        "en": "Kezy hair-length toning"
      },
      "price": "3 400–5 000 ₽",
      "duration": "",
      "description": {
        "ru": "Короткие: 3 400 ₽; Средние: 3 900 ₽; Длинные: 4 600 ₽; Очень длинные: 5 000 ₽",
        "en": "Short: 3 400 ₽; Medium: 3 900 ₽; Long: 4 600 ₽; Very long: 5 000 ₽"
      },
      "variants": [
        {
          "label": {
            "ru": "Короткие",
            "en": "Short"
          },
          "duration": "",
          "price": "3 400 ₽"
        },
        {
          "label": {
            "ru": "Средние",
            "en": "Medium"
          },
          "duration": "",
          "price": "3 900 ₽"
        },
        {
          "label": {
            "ru": "Длинные",
            "en": "Long"
          },
          "duration": "",
          "price": "4 600 ₽"
        },
        {
          "label": {
            "ru": "Очень длинные",
            "en": "Very long"
          },
          "duration": "",
          "price": "5 000 ₽"
        }
      ],
      "variantType": "length"
    },
    {
      "id": "hair-toning-joc",
      "category": "Волосы",
      "title": {
        "ru": "Тонирование длины JOC",
        "en": "JOC hair-length toning"
      },
      "price": "3 700–6 900 ₽",
      "duration": "",
      "description": {
        "ru": "Короткие: 3 700 ₽; Средние: 4 900 ₽; Длинные: 6 200 ₽; Очень длинные: 6 900 ₽",
        "en": "Short: 3 700 ₽; Medium: 4 900 ₽; Long: 6 200 ₽; Very long: 6 900 ₽"
      },
      "variants": [
        {
          "label": {
            "ru": "Короткие",
            "en": "Short"
          },
          "duration": "",
          "price": "3 700 ₽"
        },
        {
          "label": {
            "ru": "Средние",
            "en": "Medium"
          },
          "duration": "",
          "price": "4 900 ₽"
        },
        {
          "label": {
            "ru": "Длинные",
            "en": "Long"
          },
          "duration": "",
          "price": "6 200 ₽"
        },
        {
          "label": {
            "ru": "Очень длинные",
            "en": "Very long"
          },
          "duration": "",
          "price": "6 900 ₽"
        }
      ],
      "variantType": "length"
    },
    {
      "id": "hair-toning-permesse",
      "category": "Волосы",
      "title": {
        "ru": "Тонирование длины Permesse",
        "en": "Permesse hair-length toning"
      },
      "price": "5 000–8 000 ₽",
      "duration": "",
      "description": {
        "ru": "Короткие: 5 000 ₽; Средние: 6 000 ₽; Длинные: 7 000 ₽; Очень длинные: 8 000 ₽",
        "en": "Short: 5 000 ₽; Medium: 6 000 ₽; Long: 7 000 ₽; Very long: 8 000 ₽"
      },
      "variants": [
        {
          "label": {
            "ru": "Короткие",
            "en": "Short"
          },
          "duration": "",
          "price": "5 000 ₽"
        },
        {
          "label": {
            "ru": "Средние",
            "en": "Medium"
          },
          "duration": "",
          "price": "6 000 ₽"
        },
        {
          "label": {
            "ru": "Длинные",
            "en": "Long"
          },
          "duration": "",
          "price": "7 000 ₽"
        },
        {
          "label": {
            "ru": "Очень длинные",
            "en": "Very long"
          },
          "duration": "",
          "price": "8 000 ₽"
        }
      ],
      "variantType": "length"
    }
  ],
  "team": [
    {
      "id": "julia-cosmetologist",
      "name": {
        "ru": "Юлия",
        "en": "Julia"
      },
      "role": {
        "ru": "Косметолог",
        "en": "Cosmetologist"
      },
      "about": {
        "ru": "Занимаюсь уходом за кожей лица и косметологическими процедурами. В моей работе важны деликатность, внимание к состоянию кожи и вашим пожеланиям. Хочу, чтобы забота о себе была понятной и комфортной — от выбора процедуры до ежедневного ухода.",
        "en": "I work with skincare and facial treatments. A gentle approach, attention to your skin and your wishes are central to my work. I want caring for yourself to feel clear and comfortable, from choosing a treatment to your daily routine."
      },
      "photo": "team-01.webp",
      "categories": [
        "Косметология"
      ],
      "work": [],
      "reviewIds": [
        "master-review-0-3",
        "master-review-0-11"
      ]
    },
    {
      "id": "elvira-hairdresser",
      "name": {
        "ru": "Эльвира",
        "en": "Elvira"
      },
      "role": {
        "ru": "Парикмахер",
        "en": "Hair stylist"
      },
      "about": {
        "ru": "Работаю со стрижками и окрашиванием волос. Мне важно, чтобы форма и цвет сочетались с вашим образом, а причёска радовала и в повседневной жизни. Люблю продуманные перемены, в которых сохраняется ваша индивидуальность.",
        "en": "I work with haircuts and hair coloring. I value a shape and color that suit your look and a hairstyle you enjoy every day. I like thoughtful changes that preserve your individuality."
      },
      "photo": "team-02.webp",
      "categories": [
        "Волосы"
      ],
      "work": [],
      "reviewIds": [
        "master-review-1-55"
      ]
    },
    {
      "id": "darya-hairdresser",
      "name": {
        "ru": "Дарья",
        "en": "Darya"
      },
      "role": {
        "ru": "Парикмахер",
        "en": "Hair stylist"
      },
      "about": {
        "ru": "Занимаюсь стрижками и окрашиванием, в том числе работой с блондом. Для меня красивый образ складывается из деталей — оттенка, формы и того, как волосы выглядят в движении. Мне важно услышать ваши пожелания и помочь найти решение, с которым вам будет комфортно.",
        "en": "I work with haircuts and coloring, including blonde shades. To me, a beautiful look comes from the details: color, shape and the way hair moves. I value listening to your wishes and helping you find a look you feel comfortable with."
      },
      "photo": "team-03.webp",
      "categories": [
        "Волосы"
      ],
      "work": [],
      "reviewIds": [
        "master-review-2-2",
        "master-review-2-6"
      ]
    },
    {
      "id": "anna-brow-lash",
      "name": {
        "ru": "Анна",
        "en": "Anna"
      },
      "role": {
        "ru": "Бровист / лэшмейкер",
        "en": "Brow & lash artist"
      },
      "about": {
        "ru": "Оформляю брови и работаю с ресницами. Мне близки выразительные образы, в которых каждая деталь подчёркивает природную красоту. Важны и форма, и оттенок, и общий баланс — чтобы результат гармонично сочетался с вашими чертами и привычным стилем.",
        "en": "I work with brows and lashes. I appreciate expressive looks where each detail enhances natural beauty. Shape, shade and overall balance all matter, so the result feels harmonious with your features and everyday style."
      },
      "photo": "team-04.webp",
      "categories": [
        "Брови и ресницы"
      ],
      "work": [],
      "reviewIds": []
    },
    {
      "id": "marina-manicure",
      "name": {
        "ru": "Марина",
        "en": "Marina"
      },
      "role": {
        "ru": "Мастер маникюра",
        "en": "Manicurist"
      },
      "about": {
        "ru": "Выполняю маникюр и педикюр. Ценю аккуратность, внимание к деталям и спокойную атмосферу во время процедуры. Для меня важно, чтобы ухоженные руки и стопы радовали вас каждый день, а выбранные форма и покрытие были удобными в привычном ритме жизни.",
        "en": "I provide manicures and pedicures. I value precision, attention to detail and a calm atmosphere during your appointment. I want you to enjoy well-groomed hands and feet, with a shape and finish that feel comfortable in everyday life."
      },
      "photo": "team-05.webp",
      "categories": [
        "Маникюр"
      ],
      "work": [],
      "reviewIds": [
        "master-review-4-4",
        "master-review-4-5"
      ]
    },
    {
      "id": "olesya-manicure",
      "name": {
        "ru": "Олеся",
        "en": "Olesya"
      },
      "role": {
        "ru": "Мастер маникюра",
        "en": "Manicurist"
      },
      "about": {
        "ru": "Занимаюсь маникюром и оформлением ногтей. Люблю, когда цвет и дизайн отражают ваше настроение — будь то сдержанное покрытие или заметный акцент. В работе для меня важны аккуратные детали и возможность воплотить ваши пожелания в цельный, продуманный образ.",
        "en": "I work with manicures and nail design. I enjoy color and design that reflect your mood, from an understated finish to a distinctive accent. Careful details and bringing your wishes together into a considered look are important to me."
      },
      "photo": "team-06.webp",
      "categories": [
        "Маникюр"
      ],
      "work": [],
      "reviewIds": [
        "master-review-5-3",
        "master-review-5-6"
      ]
    }
  ],
  "reviews": [
    {
      "id": "review-natalia-temnikova",
      "author": {
        "ru": "Наталия Темникова",
        "en": "Natalia Temnikova"
      },
      "text": {
        "ru": "Открыла для себя салон \"Ева\" недавно и хочу поделиться впечатлением. Это действительно то место, где можно получить качественные услуги по уходу. На рецепшен работают приветливые компетентные администраторы. Время назначенных процедур соблюдается чётко по записи. Пользуюсь услугами мастера парикмахера Дарьи. Осталась очень довольна стрижкой и покраской волос. Чувствуется рука профессионала высокого уровня. Качество используемой итальянской косметики великолепное. Попробовала процедуру чистки лица с биореталем у врача косметолога Ирины и была приятно удивлена отличным результатом. Спектр косметических услуг большой, чем постараюсь воспользоваться в ближайшее время. Используемые препараты и косметика не вызывают аллергии и оставляют на лице приятное ощущение. Моя искренняя благодарность коллективу салона за отличную работу и профессионализм !",
        "en": "I recently discovered Eva salon and would like to share my impressions. This is truly a place where you can receive quality beauty-care services. The reception team is friendly and competent, and appointments are kept on schedule. I visit Darya for haircuts and coloring and have been very pleased with the results. Her work shows a high level of professionalism. The Italian cosmetics used here are excellent. I also tried a facial cleansing with Biorepeel with cosmetologist Irina and was pleasantly surprised by the result. The range of cosmetology services is extensive, and I hope to try more soon. The products and cosmetics do not cause allergic reactions and leave the skin feeling pleasant. My sincere thanks to the whole salon team for their excellent work and professionalism!"
      },
      "rating": 5,
      "source": {
        "ru": "Яндекс Карты",
        "en": "Yandex Maps"
      },
      "url": "https://yandex.com/maps/org/yeva/1179517154/"
    },
    {
      "id": "review-ekaterina-filina",
      "author": {
        "ru": "Екатерина Филина",
        "en": "Ekaterina Filina"
      },
      "text": {
        "ru": "Больше, я и моя дочь, посещаем салон красоты Ева. Пользуемся услугами косметолога Юлии.Осталась довольна результатом после процедуры.Юлия ответственная, аккуратная. Профессионал своего дела. Хочу выразить благодарность мастеру маникюра Олесе.Мастер с большой буквы. Все маникюрные фантазии воплощает в реальность. Директор волшебная женщина. Салон часто радует клиентскими днями, бонусами и подарками. Администраторы приветливые, всегда предложат чай, кофе.В салоне очень благоприятная атмосфера. Спасибо большое за вашу заботу о нас. Процветания салону.",
        "en": "My daughter and I have been visiting Eva beauty salon. We use the services of cosmetologist Yulia, and I was pleased with the result of my treatment. Yulia is responsible, careful and a true professional. I would also like to thank Olesya, the manicurist — a master in the fullest sense of the word. She brings every nail-design idea to life. The director is a wonderful woman. The salon often delights clients with special days, bonuses and gifts. The administrators are friendly and always offer tea or coffee. The atmosphere is very welcoming. Thank you for taking such good care of us. I wish the salon continued success."
      },
      "rating": 5,
      "source": {
        "ru": "Яндекс Карты",
        "en": "Yandex Maps"
      },
      "url": "https://yandex.com/maps/org/yeva/1179517154/"
    },
    {
      "id": "review-irina-t",
      "author": {
        "ru": "Ирина Т.",
        "en": "Irina T."
      },
      "text": {
        "ru": "Хочу сказать несколько слов о салоне! Года полтора хожу к мастеру маникюра и педикюра Марине. Она очень любит то, чем занимается. Качество работы на высочайшем уровне. Всегда в хорошем настроении. Приятная в общении. Ничего не навязывает, все очень деликатно. Все мастера регулярно повышают свою квалификацию. Анна- администратор приветливая, коммуникабельная девушка. Директор салона- Марина все сделала для того, чтобы клиентам было комфортно. Каждый клиент окружен вниманием и заботой. Рекомендую всем девушкам. Моя мама ходит на стрижку и окрашивание к Эле.",
        "en": "I would like to say a few words about the salon. For about a year and a half, I have been visiting Marina for manicures and pedicures. She truly loves her work, and the quality is outstanding. She is always in a good mood and pleasant to talk to. She never pushes extra services and is very tactful. All the specialists regularly improve their qualifications. Anna at reception is friendly and communicative. The salon’s director, Marina, has made sure clients feel comfortable; everyone is treated with care and attention. I recommend the salon to everyone. My mother visits Ela for haircuts and coloring."
      },
      "rating": 5,
      "source": {
        "ru": "Яндекс Карты",
        "en": "Yandex Maps"
      },
      "url": "https://yandex.com/maps/org/yeva/1179517154/"
    },
    {
      "id": "review-antonina-bazhina",
      "author": {
        "ru": "Антонина Бажина",
        "en": "Antonina Bazhina"
      },
      "text": {
        "ru": "⭐ 5/5 – Мастер Марина Орлова с золотыми руками ! ⭐ К Марине хожу уже очень,очень давно, и это не просто маникюр – это ритуал красоты, комфорта и душевного общения! Марина использует только лучшие материалы, а её работа держится идеально долго. Никаких сколов, отслоек – только безупречный результат. Всегда прислушивается к пожеланиям, а её интерессны идеи делают каждый маникюр особенным. Не могу не сказать о том,сколько раз она спасала мои ногти в экстренных ситуациях! Даже если график плотный, Марина найдёт время помочь – это дорогого стоит. После сеанса уходишь не только с красивыми ногтями, но и с отличным настроением. Спасибо за ваш труд и теплоту! 🤍",
        "en": "⭐ 5/5 — Marina Orlova has golden hands! ⭐ I have been going to Marina for a very, very long time, and it is more than a manicure — it is a ritual of beauty, comfort and warm conversation. Marina uses excellent materials, and her work lasts beautifully. No chips or lifting, just a flawless result. She always listens to what I want, and her interesting ideas make every manicure special. I cannot count how many times she has rescued my nails in an emergency. Even when her schedule is full, Marina finds time to help, and that is priceless. You leave not only with beautiful nails but in a great mood. Thank you for your work and warmth! 🤍"
      },
      "rating": 5,
      "source": {
        "ru": "Яндекс Карты",
        "en": "Yandex Maps"
      },
      "url": "https://yandex.com/maps/org/yeva/1179517154/"
    },
    {
      "id": "review-masha-raduga",
      "author": {
        "ru": "Маша Радуга",
        "en": "Masha Raduga"
      },
      "text": {
        "ru": "Очень нравится салон, приятная атмосфера. Хожу в салон Ева больше 3х лет на маникюр к мастеру Олесе. Любовь с первого взгляда)Супер мастер! Также хожу к мастеру Дарье на окрашивание волос, около 2х лет, всегда отличный цвет блонд. Рекомендую!",
        "en": "I really like the salon and its pleasant atmosphere. I have been visiting Eva for more than three years for manicures with Olesya. Love at first sight — she is a fantastic specialist! I also visit Darya for hair coloring and have done so for about two years; the blonde color is always excellent. I recommend them!"
      },
      "rating": 5,
      "source": {
        "ru": "Яндекс Карты",
        "en": "Yandex Maps"
      },
      "url": "https://yandex.com/maps/org/yeva/1179517154/"
    },
    {
      "id": "review-aliyeva-olya",
      "author": {
        "ru": "Алиева Оля",
        "en": "Olya Alieva"
      },
      "text": {
        "ru": "Это самый лучший Салон, который я знаю!!! Попала сюда случайно, 4 года назад и воюбилась. Полозуюсь всеми услугами, которые тут могут предложить ( манекюр, педикюр, парикмахер, косметологии, массаж, солярий) Тут работают действительно проффесионалы своего дела. Мастер манекюра Олеся действительно ногтевая фея, педикюр от Марины выше всех похвал. Парикмахер Даша и Эля волшебницы, косметолог Ирина специалист с Большой буквы. Желаю любимому Салону, и особенно владельце Марине, дальнейшего процветания и развития, благодарных гостей и удачи!!",
        "en": "This is the best salon I know! I found it by chance four years ago and fell in love with it. I use all the services offered here — manicure, pedicure, hairdressing, cosmetology, massage and tanning. The people who work here are true professionals. Manicurist Olesya is truly a nail fairy, and Marina’s pedicures are beyond praise. Hairdressers Dasha and Ela are wonderful, and cosmetologist Irina is an outstanding specialist. I wish my favorite salon, especially its owner Marina, continued growth and success, grateful guests and good luck!"
      },
      "rating": 5,
      "source": {
        "ru": "Яндекс Карты",
        "en": "Yandex Maps"
      },
      "url": "https://yandex.com/maps/org/yeva/1179517154/"
    },
    {
      "id": "review-nyuta-uralova",
      "author": {
        "ru": "Нюта Уралова",
        "en": "Nyuta Uralova"
      },
      "text": {
        "ru": "Хочу сказать большое спасибо нашим незаменимым мастерам Дарье и Эле , которые делают нас красивыми каждый раз. Так же они очень позитивные и общительные , могут даже пообщаться с ребёнком в момент стрижки , ребенку с ними очень комфортно и радостно 😊 Мы долго не могли найти подходящего нам мастера для детской стрижке, но именно в Eva нас услышали и приняли наши запросы. Сын бежит с удовольствием на стрижку ,и это радует. Персонал замечательный , чуткий и отзывчивый 👍 спасибо Вам большое , вы лучшие ! 🌹🙌❤️",
        "en": "A huge thank-you to our indispensable stylists Darya and Ela, who make us look beautiful every time. They are positive and friendly, and can even chat with a child during a haircut, making the experience comfortable and happy. We had been looking for the right person for our son’s haircut for a long time, but at Eva they listened to us and understood what we needed. Our son now happily runs off to his haircut, which makes us so glad. The staff are wonderful, caring and responsive. Thank you so much — you are the best! 🌹🙌❤️"
      },
      "rating": 5,
      "source": {
        "ru": "Яндекс Карты",
        "en": "Yandex Maps"
      },
      "url": "https://yandex.com/maps/org/yeva/1179517154/"
    },
    {
      "id": "master-review-0-3",
      "author": {
        "ru": "Екатерина Филина",
        "en": "Екатерина Филина"
      },
      "text": {
        "ru": "Пользуемся услугами косметолога Юлии.Осталась довольна результатом после процедуры.Юлия ответственная, аккуратная. Профессионал своего дела.",
        "en": "Пользуемся услугами косметолога Юлии.Осталась довольна результатом после процедуры.Юлия ответственная, аккуратная. Профессионал своего дела."
      },
      "rating": 5,
      "source": {
        "ru": "Яндекс Карты",
        "en": "Yandex Maps"
      },
      "url": "https://yandex.com/maps/org/yeva/1179517154/"
    },
    {
      "id": "master-review-0-11",
      "author": {
        "ru": "Елена Ш.",
        "en": "Елена Ш."
      },
      "text": {
        "ru": "Хочу сказать огромное спасибо замечательному косметологу Юлии за ее внимательность, профессионализм, доброту и индивидуальный подход. Однозначно Юлия великолепный мастер своего дела!",
        "en": "Хочу сказать огромное спасибо замечательному косметологу Юлии за ее внимательность, профессионализм, доброту и индивидуальный подход. Однозначно Юлия великолепный мастер своего дела!"
      },
      "rating": 5,
      "source": {
        "ru": "Яндекс Карты",
        "en": "Yandex Maps"
      },
      "url": "https://yandex.com/maps/org/yeva/1179517154/"
    },
    {
      "id": "master-review-1-55",
      "author": {
        "ru": "Helga Krios",
        "en": "Helga Krios"
      },
      "text": {
        "ru": "Замечательное место! Мастер Эльвира (парикмахер) точно знает свое дело! Сделала супер-стрижку, посмеялись, очень общительная и приятная 🥰 Очень рада что пришла в этот салон, спасибо!",
        "en": "Замечательное место! Мастер Эльвира (парикмахер) точно знает свое дело! Сделала супер-стрижку, посмеялись, очень общительная и приятная 🥰 Очень рада что пришла в этот салон, спасибо!"
      },
      "rating": 5,
      "source": {
        "ru": "Яндекс Карты",
        "en": "Yandex Maps"
      },
      "url": "https://yandex.com/maps/org/yeva/1179517154/"
    },
    {
      "id": "master-review-2-2",
      "author": {
        "ru": "Наталия Темникова",
        "en": "Наталия Темникова"
      },
      "text": {
        "ru": "Пользуюсь услугами мастера парикмахера Дарьи. Осталась очень довольна стрижкой и покраской волос. Чувствуется рука профессионала высокого уровня.",
        "en": "Пользуюсь услугами мастера парикмахера Дарьи. Осталась очень довольна стрижкой и покраской волос. Чувствуется рука профессионала высокого уровня."
      },
      "rating": 5,
      "source": {
        "ru": "Яндекс Карты",
        "en": "Yandex Maps"
      },
      "url": "https://yandex.com/maps/org/yeva/1179517154/"
    },
    {
      "id": "master-review-2-6",
      "author": {
        "ru": "Маша Радуга",
        "en": "Маша Радуга"
      },
      "text": {
        "ru": "Также хожу к мастеру Дарье на окрашивание волос, около 2х лет, всегда отличный цвет блонд.",
        "en": "Также хожу к мастеру Дарье на окрашивание волос, около 2х лет, всегда отличный цвет блонд."
      },
      "rating": 5,
      "source": {
        "ru": "Яндекс Карты",
        "en": "Yandex Maps"
      },
      "url": "https://yandex.com/maps/org/yeva/1179517154/"
    },
    {
      "id": "master-review-4-4",
      "author": {
        "ru": "Ирина Т.",
        "en": "Ирина Т."
      },
      "text": {
        "ru": "Года полтора хожу к мастеру маникюра и педикюра Марине. Она очень любит то, чем занимается. Качество работы на высочайшем уровне. Всегда в хорошем настроении. Приятная в общении. Ничего не навязывает, все очень деликатно. Все мастера регулярно повышают свою квалификацию.",
        "en": "Года полтора хожу к мастеру маникюра и педикюра Марине. Она очень любит то, чем занимается. Качество работы на высочайшем уровне. Всегда в хорошем настроении. Приятная в общении. Ничего не навязывает, все очень деликатно. Все мастера регулярно повышают свою квалификацию."
      },
      "rating": 5,
      "source": {
        "ru": "Яндекс Карты",
        "en": "Yandex Maps"
      },
      "url": "https://yandex.com/maps/org/yeva/1179517154/"
    },
    {
      "id": "master-review-4-5",
      "author": {
        "ru": "Антонина Бажина",
        "en": "Антонина Бажина"
      },
      "text": {
        "ru": "⭐ 5/5 – Мастер Марина Орлова с золотыми руками ! ⭐ К Марине хожу уже очень,очень давно, и это не просто маникюр – это ритуал красоты, комфорта и душевного общения! Марина использует только лучшие материалы, а её работа держится идеально долго. Никаких сколов, отслоек – только безупречный результат. Всегда прислушивается к пожеланиям, а её интерессны идеи делают каждый маникюр особенным. Не могу не сказать о том,сколько раз она спасала мои ногти в экстренных ситуациях! Даже если график плотный, Марина найдёт время помочь – это дорогого стоит. После сеанса уходишь не только с красивыми ногтями, но и с отличным настроением. Спасибо за ваш труд и теплоту! 🤍",
        "en": "⭐ 5/5 – Мастер Марина Орлова с золотыми руками ! ⭐ К Марине хожу уже очень,очень давно, и это не просто маникюр – это ритуал красоты, комфорта и душевного общения! Марина использует только лучшие материалы, а её работа держится идеально долго. Никаких сколов, отслоек – только безупречный результат. Всегда прислушивается к пожеланиям, а её интерессны идеи делают каждый маникюр особенным. Не могу не сказать о том,сколько раз она спасала мои ногти в экстренных ситуациях! Даже если график плотный, Марина найдёт время помочь – это дорогого стоит. После сеанса уходишь не только с красивыми ногтями, но и с отличным настроением. Спасибо за ваш труд и теплоту! 🤍"
      },
      "rating": 5,
      "source": {
        "ru": "Яндекс Карты",
        "en": "Yandex Maps"
      },
      "url": "https://yandex.com/maps/org/yeva/1179517154/"
    },
    {
      "id": "master-review-5-3",
      "author": {
        "ru": "Екатерина Филина",
        "en": "Екатерина Филина"
      },
      "text": {
        "ru": "Хочу выразить благодарность мастеру маникюра Олесе.Мастер с большой буквы. Все маникюрные фантазии воплощает в реальность.",
        "en": "Хочу выразить благодарность мастеру маникюра Олесе.Мастер с большой буквы. Все маникюрные фантазии воплощает в реальность."
      },
      "rating": 5,
      "source": {
        "ru": "Яндекс Карты",
        "en": "Yandex Maps"
      },
      "url": "https://yandex.com/maps/org/yeva/1179517154/"
    },
    {
      "id": "master-review-5-6",
      "author": {
        "ru": "Маша Радуга",
        "en": "Маша Радуга"
      },
      "text": {
        "ru": "Хожу в салон Ева больше 3х лет на маникюр к мастеру Олесе. Любовь с первого взгляда)Супер мастер!",
        "en": "Хожу в салон Ева больше 3х лет на маникюр к мастеру Олесе. Любовь с первого взгляда)Супер мастер!"
      },
      "rating": 5,
      "source": {
        "ru": "Яндекс Карты",
        "en": "Yandex Maps"
      },
      "url": "https://yandex.com/maps/org/yeva/1179517154/"
    }
  ],
  "masterReviews": {
    "enabled": false,
    "previewMasterId": null
  }
};
  const rows=[];
  const translated=new Set();
  const collect=value=>{
    if(!value||typeof value!=='object')return;
    if(typeof value.ru==='string'&&typeof value.en==='string'){
      // Preserve the legacy translation lookup without copying inactive locales.
      // Repeated untranslated reviews must not replace an existing translation.
      if(value.ru&&!(value.en===value.ru&&translated.has(value.ru))){
        rows.push([value.ru,value.ru,value.en]);
        if(value.en!==value.ru)translated.add(value.ru);
      }
      return;
    }
    if(Array.isArray(value))value.forEach(collect);
    else Object.values(value).forEach(collect);
  };
  collect(data);
  global.TANEM_SITE_DATA=data;
  global.TANEM_SITE_I18N_ROWS=rows;
})(window);
