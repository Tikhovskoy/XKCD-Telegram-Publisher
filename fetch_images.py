import os
import requests
import random
import logging
from datetime import datetime
from config import get_config

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def fetch_comic():
    """
    Загружает случайный комикс с сайта XKCD.
    Возвращает JSON с данными о комиксе.
    """
    last_comic_url = "https://xkcd.com/info.0.json"
    response = requests.get(last_comic_url)
    response.raise_for_status()

    last_comic_num = response.json()["num"]
    random_comic_num = random.randint(1, last_comic_num)

    comic_url = f"https://xkcd.com/{random_comic_num}/info.0.json"
    response = requests.get(comic_url)
    response.raise_for_status()

    return response.json()


def save_comic(comic_data, directory="images"):
    """
    Сохраняет изображение комикса на диск.
    Возвращает путь к сохраненному изображению.
    """
    os.makedirs(directory, exist_ok=True)

    image_url = comic_data["img"]
    title = comic_data["title"].replace(" ", "_").replace("/", "-")
    image_path = os.path.join(directory, f"{title}.png")

    response = requests.get(image_url)
    response.raise_for_status()

    with open(image_path, "wb") as file:
        file.write(response.content)

    logging.info(f"Сохранен комикс: {image_path}")

    return image_path
