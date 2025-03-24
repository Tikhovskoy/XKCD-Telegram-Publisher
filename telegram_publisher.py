import os
import logging
import requests
from telegram import Bot
from telegram.error import TelegramError
from fetch_images import fetch_comic, save_comic
from dotenv import load_dotenv

def publish_comic(bot, channel_id):
    """
    Скачивает случайный комикс и публикует его в Telegram-канале с комментариями.
    """
    try:
        comic_data = fetch_comic()
    except requests.exceptions.RequestException as e:
        logging.error(f"Ошибка при получении комикса: {e}")
        return

    try:
        files_dir = os.getenv("FILES_DIR", "files")
        comic_image = save_comic(comic_data, files_dir)
    except (requests.exceptions.RequestException, OSError) as e:
        logging.error(f"Ошибка при сохранении комикса: {e}")
        return

    try:
        with open(comic_image, "rb") as photo:
            bot.send_photo(
                chat_id=channel_id,
                photo=photo,
                caption=f"{comic_data['title']}\n\n{comic_data['alt']}",
                timeout=60
            )
        logging.info(f"Комикс опубликован: {comic_image}")
    except TelegramError as e:
        logging.error(f"Ошибка при отправке комикса в Telegram: {e}")
        return
    except Exception as e:
        logging.error(f"Неожиданная ошибка при отправке комикса: {e}")
        return

    try:
        os.remove(comic_image)
    except OSError as e:
        logging.error(f"Ошибка при удалении файла: {e}")

def main():
    load_dotenv() 
    logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

    TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
    TELEGRAM_CHANNEL_ID = os.getenv("TELEGRAM_CHANNEL_ID")
    files_dir = os.getenv("FILES_DIR", "files")

    if not TELEGRAM_BOT_TOKEN or not TELEGRAM_CHANNEL_ID:
        logging.error("Не найдены TELEGRAM_BOT_TOKEN или TELEGRAM_CHANNEL_ID")
        return

    os.makedirs(files_dir, exist_ok=True)
    bot = Bot(token=TELEGRAM_BOT_TOKEN)
    publish_comic(bot, TELEGRAM_CHANNEL_ID)

if __name__ == "__main__":
    main()
