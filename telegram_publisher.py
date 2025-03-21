import os
import logging
from telegram import Bot
from fetch_images import fetch_comic, save_comic
from config import get_config

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def publish_comic(bot, channel_id):
    """
    Скачивает случайный комикс и публикует его в Telegram-канале с комментариями.
    """
    try:
        comic_data = fetch_comic()
        comic_image = save_comic(comic_data)
        
        with open(comic_image, "rb") as photo:
            bot.send_photo(
                chat_id=channel_id,
                photo=photo,
                caption=f"{comic_data['title']}\n\n{comic_data['alt']}",
                timeout=60
            )
        
        logging.info(f"Комикс опубликован: {comic_image}")
        
        try:
            os.remove(comic_image)
        except Exception as e:
            logging.error(f"Ошибка при удалении файла: {e}")
            
    except Exception as e:
        logging.error(f"Ошибка при публикации комикса: {e}")

def main():
    config = get_config()
    bot_token = config["TELEGRAM_BOT_TOKEN"]
    channel_id = config["TELEGRAM_CHANNEL_ID"]

    if not bot_token or not channel_id:
        logging.error("Не найдены TELEGRAM_BOT_TOKEN или TELEGRAM_CHANNEL_ID")
        return

    bot = Bot(token=bot_token)
    publish_comic(bot, channel_id)

if __name__ == "__main__":
    main()
