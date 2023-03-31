# Программа для работы с чат ботом
Учебная задача в рамках модуля "Чат ьоты — Урок 1. Отправляем уведомления о проверке работ" для учебной платформы dvmn.org
Проект решает следующую задачу:
- Автоматизация проверки ревью 

# Установка:
- Скачать файлы из [репозитория](https://github.com/AndreyShukatka/work_review_notifications/archive/refs/heads/main.zip)
- Создать виртуальное окружение:
```
python -m venv env
```
- Распаковать архив в папку с вашим виртуальным окружением
- Прописать в виртуальном окружении:
```
pip install -r requirements.txt
```

# Установка и запуск через Docker
- Установить докер
```shell
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
```
- Установить контейнер
```shell
docker pull slon1k/work_review_notifications
```
- Запустить установленный контейнер с переменными окружения
```shell
sudo docker run -d --restart always 
-e DEVMAN_TOKEN='Ваш токен Devman' 
-e TELEGRAM_TOKEN='Ваш токен телеграмма' 
-e TGM_ID='Ваш ID телеграмма' slon1k/work_review_notifications
```

# Для запуска необходимо:
- Создать бота и получить токен, инструкция по ссылке: [Кликни тут](https://smmplanner.com/blog/otlozhennyj-posting-v-telegram/).
- Найти токен для [Devman](https://dvmn.org) по [этой ссылке](https://dvmn.org/api/docs/)
- Узнать свой ID в телеграме `Чтобы получить свой chat_id, напишите в Telegram специальному боту: @userinfobot`
- Создайте файл `.env` в основной директории программы
- Заполните файл `.env` следующим образом:
```
DEVMAN_TOKEN=Тут ваш токен с девмана
TELEGRAM_TOKEN=Тут ваш токен с телеграма
TGM_ID=Тут ваш ID в телеграме
```

- После окончания всех настроек запускаем скрипт:
```
python main.py
```

Если всё установлено верно, то при очередной проверке вашей работы вы получите уведомление от вашего бота прошли вы проверку или нужны будут доработки

![reviews](https://user-images.githubusercontent.com/106096891/198392592-292b82b7-65b2-4134-9383-0cf11285c9fd.jpg)

