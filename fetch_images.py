import os
import requests
import random
import logging
from config import get_config

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def fetch_comic(comic_num=None):
    """
    Загружает комикс с сайта XKCD.
    Если comic_num не указан, загружается случайный комикс.
    Возвращает JSON с данными о комиксе.
    """
    if comic_num:
        comic_url = f"https://xkcd.com/{comic_num}/info.0.json"
    else:
        last_comic_url = "https://xkcd.com/info.0.json"
        response = requests.get(last_comic_url)
        response.raise_for_status()

        last_comic_num = response.json()["num"]
        random_comic_num = random.randint(1, last_comic_num)
        comic_url = f"https://xkcd.com/{random_comic_num}/info.0.json"

    response = requests.get(comic_url)
    response.raise_for_status()
    
    return response.json()

def save_comic(comic_data, directory="files"):
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

if __name__ == "__main__":
    config = get_config()
    print("Конфигурация загружена:", config)
    
    comic_data = fetch_comic()
    print("Скачан комикс:", comic_data["title"])
    print("Комментарий к комиксу:", comic_data["alt"])

    image_path = save_comic(comic_data)
    print("Комикс сохранён по пути:", image_path)
