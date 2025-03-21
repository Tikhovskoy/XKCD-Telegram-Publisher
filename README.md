# XKCD Telegram Publisher

## Описание
Данный проект автоматически загружает случайный комикс с популярного веб-комикса XKCD и публикует его в указанном Telegram-канале с комментариями. Проект состоит из скриптов для загрузки и отправки комиксов, а также настроек для удобного использования через переменные окружения.

Функциональность:
- Загрузка случайного комикса с сайта XKCD.
- Публикация комикса в Telegram-канале с названием и описанием комикса.
- Автоматическое удаление изображения с диска после публикации.

## Установка

### Windows

Откройте командную строку (CMD) или PowerShell и выполните:
```bash
git clone <URL вашего репозитория>
cd <имя репозитория>
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

### Linux и macOS

Откройте терминал и выполните:
```bash
git clone <URL вашего репозитория>
cd <имя репозитория>
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Настройка

Создайте файл `.env` в корне проекта со следующими параметрами:

```env
TELEGRAM_BOT_TOKEN=ваш_токен_телеграм_бота
TELEGRAM_CHANNEL_ID=ваш_ID_телеграм_канала
FILES_DIR=files
```

- **`TELEGRAM_BOT_TOKEN`** — токен Telegram-бота, полученный через [@BotFather](https://t.me/BotFather).
- **`TELEGRAM_CHANNEL_ID`** — ID вашего Telegram-канала (например, `-1001234567890`).
- **`FILES_DIR`** — директория для временного сохранения комиксов (по умолчанию используется папка `files`).

## Использование

### Windows

Запустите публикацию комикса с помощью команды:
```bash
venv\Scripts\activate
python telegram_publisher.py
```

### Linux и macOS

Запустите публикацию комикса с помощью команды:
```bash
source venv/bin/activate
python telegram_publisher.py
```

## Требования
- `python-dotenv==1.0.1`
- `python-telegram-bot==13.15`
- `requests==2.32.3`

Все зависимости уже включены в файл `requirements.txt`.


