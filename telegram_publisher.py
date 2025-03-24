import os
import logging
from telegram import Bot
from telegram.error import TelegramError
from publisher_utils import get_comic_data, download_comic, cleanup_comic
from dotenv import load_dotenv

def send_comic(bot, channel_id, comic_data, comic_image):
    """
    Отправляет комикс в Telegram-канал.
    """
    try:
        with open(comic_image, "rb") as photo:
            bot.send_photo(
                chat_id=channel_id,
                photo=photo,
                caption=f"{comic_data['title']}\n\n{comic_data['alt']}",
                timeout=60
            )
        logging.info(f"Комикс опубликован: {comic_image}")
        return True
    except TelegramError as e:
        logging.error(f"Ошибка при отправке комикса в Telegram: {e}")
        return False
    except Exception as e:
        logging.error(f"Неожиданная ошибка при отправке комикса: {e}")
        return False

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
    
    comic_data = get_comic_data()
    if comic_data is None:
        return

    comic_image = download_comic(comic_data, files_dir)
    if comic_image is None:
        return

    if send_comic(bot, TELEGRAM_CHANNEL_ID, comic_data, comic_image):
        cleanup_comic(comic_image)

if __name__ == "__main__":
    main()
