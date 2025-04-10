import os
import logging
from telegram import Bot
from telegram.error import TelegramError
from fetch_images import fetch_comic, save_comic
from dotenv import load_dotenv


def send_comic(bot, channel_id, comic_data, comic_image):
    """
    Отправляет комикс в Telegram-канал.
    """
    with open(comic_image, "rb") as photo:
        bot.send_photo(
            chat_id=channel_id,
            photo=photo,
            caption=f"{comic_data['title']}\n\n{comic_data['alt']}",
            timeout=60
        )
    logging.info(f"Комикс опубликован: {comic_image}")


def main():
    load_dotenv()
    logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
    
    try:
        telegram_bot_token = os.environ["TELEGRAM_BOT_TOKEN"]
        telegram_channel_id = os.environ["TELEGRAM_CHANNEL_ID"]
    except KeyError as key_error:
        logging.error(f"Обязательная переменная окружения не найдена: {key_error}")
        return
    
    files_dir = os.environ.get("FILES_DIR", "files")
    
    if not telegram_bot_token or not telegram_channel_id:
        logging.error("Не найдены TELEGRAM_BOT_TOKEN или TELEGRAM_CHANNEL_ID")
        return

    os.makedirs(files_dir, exist_ok=True)
    bot = Bot(token=telegram_bot_token)
    
    comic_image = None
    try:
        comic_data = fetch_comic()
        comic_image = save_comic(comic_data, files_dir)
        send_comic(bot, telegram_channel_id, comic_data, comic_image)
    except Exception as error:
        logging.error(f"Ошибка в процессе публикации комикса: {error}")
    finally:
        if comic_image:
            try:
                os.remove(comic_image)
                logging.info(f"Файл удален: {comic_image}")
            except Exception as error:
                logging.error(f"Ошибка при удалении файла: {error}")


if __name__ == "__main__":
    main()
