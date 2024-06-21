
# Укоротитель ссылок YaCut

Укоротитель длинных ссылок YaCut, с возможностью указания собственного идентификатора ссылки.


## Возможности

- Укорачивание длинных ссылок
- Указание собственного идентификатора ссылки


## Установка

1. Склонируйте проект:

```bash
  git clone git@github.com:basmdev/yacut.git
```

2. Создайте и активируйте виртуальное окружение:

```bash
  python -m venv venv
  source venv/Scripts/activate
```


3. Установите зависимости:

```bash
  pip install -r requirements.txt
```


4. Создайте файл .env и заполните его по образцу .env.example

5. Инициализируйте базу данных:
```
  flask db init
```

6. Создайте и примените миграции:
```bash
  flask db migrate
```
```bash
  flask db upgrade
```


7. Запустите проект:

```bash
  flask run
```

## Технологии

- Python
- SQL Alchemy
- Flask


## Автор

Mohammed Baskhanov (basmdev)

