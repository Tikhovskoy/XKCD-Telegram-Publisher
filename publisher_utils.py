import os
import logging
import requests
from fetch_images import fetch_comic, save_comic

def get_comic_data():
    """
    Получает данные случайного комикса с XKCD.
    """
    try:
        comic_data = fetch_comic()
        return comic_data
    except requests.exceptions.RequestException as e:
        logging.error(f"Ошибка при получении комикса: {e}")
        return None

def download_comic(comic_data, files_dir):
    """
    Сохраняет комикс на диск и возвращает путь к файлу.
    Предполагается, что каталог files_dir уже существует.
    """
    try:
        comic_image = save_comic(comic_data, files_dir)
        return comic_image
    except (requests.exceptions.RequestException, OSError) as e:
        logging.error(f"Ошибка при сохранении комикса: {e}")
        return None

def cleanup_comic(comic_image):
    """
    Удаляет локально сохраненный файл комикса.
    """
    try:
        os.remove(comic_image)
        logging.info(f"Файл удален: {comic_image}")
        return True
    except OSError as e:
        logging.error(f"Ошибка при удалении файла: {e}")
        return False
