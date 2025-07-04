Сайт-витрина ZMO

По продаже земельных участков и строительстве частных домов в Москве и Московской области

Сайт включает в себя разделы:

- Поселки
- Готовые дома
- Оформление
- Контакты
- О Компании

Настройка:

Виртуальное окружение используемое для проекта: venv

1) После настройки виртуального окружения установите зависимости из файла requirements.txt

```bash
  pip install -r requirements.txt
```

3.1. создайте Базу данных при помощи команды

```bash
  python manage.py ccdb
```

3.2. Создайте миграции при помощи команды

```bash
  python manage.py makemigrations
```

3.3. Примените созданные миграции при помощи команды

```bash
  python manage.py migrate
```

3.4. Выполните команду для создания пользователей

```bash
  python manage.py ccsu
```

3.5. Выполните команду для заполнения базы данных используя фикстуры

```bash
   python manage.py loaddata houses.json
   python manage.py loaddata partners.json
   python manage.py loaddata villages.json
```

3.6. Выполните команду для запуска приложения

```bash
  python manage.py runserver
```

4) Работа с Docker

Для работы с Docker выполните следующие действия:

```bash
  docker-compose up -d --build
```

Модели используемые в проекте:

House:

- name (str): Название дома.
- preview_image (ImageField): Превью-изображение для карточки.
- price (str): Цена дома (строка, чтобы можно было добавить валюту или доп. условия).
- size (str): Габариты дома (например, '10x15м').
- photo_house (ImageField): Основное фото дома.
- floor (int): Количество этажей.
- total_area (str): Общая строительная площадь (например, '150 кв.м').
- bedroom (int): Количество спален.
- bathroom (int): Количество санузлов.
- living_room_area (str): Площадь гостиной.
- terrace_count (int): Количество террас/балконов.
- description (str): Подробное описание дома.

HousePlan:

- plan (ForeignKey): Связь с основной моделью дома (House).
- plan_image (ImageField): Изображение плана дома/фасадов.
- order (int): Порядок сортировки планов (для отображения в нужной последовательности).

HouseImage:

- house (ForeignKey): Связь с основным объектом дома.
- image (ImageField): Файл изображения дома. 
- order (PositiveIntegerField): Порядковый номер для сортировки изображений.

Partners:
- name (CharField): Название компании-партнера 
- image (ImageField): Логотип партнера 
- registration (PositiveIntegerField): Услуги по оформлению 
- reservation (PositiveIntegerField): Услуги по платной брони 
- address (TextField): Полный адрес партнера 
- yandex_map (TextField): Код или ссылка для встраивания Яндекс.Карт

Village:
- name (CharField): Название поселка 
- preview_image (ImageField): Превью-изображение для карточки.
- address (CharField): Адрес поселка
- yandex_map_embed (TextField): месторасположение на яндекс карте
- photo_village (ImageField): Основное фото поселка
- price (PositiveIntegerField): Цена за сотку
- distance_mkad (PositiveIntegerField): расстояние от МКАД
- communications (CharField): Коммуникации
- video_url (URLField): URL видео с youtube или rutube
- description (TextField): Описание