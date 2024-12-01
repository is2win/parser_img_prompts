import requests
from fake_useragent import UserAgent
from tg_bot_app.tg_bot import bot
from config.main_config import CONFIG
from db.engine import create_prompt_id, is_img_id_exists
from loguru import logger
from datetime import datetime
import re


async def start_parsing():
    images, next_url = await send_request()
    while True:
        print(next_url)
        result = await choose_and_answer(images)
        if not result:
            images, next_url = await send_next_request(next_url)
        else:
            break


async def send_request(url: str | None = "https://civitai.com/api/v1/images"):
    url = url
    params = {
        "sort": "Most Reactions",
        "period": "Day",
    }
    user_agent = UserAgent()

    headers = {
        "User-Agent": user_agent.random,
    }
    response = requests.get(url, params=params, headers=headers)
    images = response.json()['items']
    next_url = response.json()['metadata']['nextPage']
    return images, next_url


async def send_next_request(url: str):
    user_agent = UserAgent()
    headers = {
        "User-Agent": user_agent.random,
    }
    response = requests.get(url, headers=headers)
    images = response.json()['items']
    next_url = response.json()['metadata']['nextPage']
    return images, next_url


async def choose_and_answer(images):
    for image in images:
        try:
            img_url = image.get('url')
            img_id = image.get('id')
            img_created_at = datetime.strptime(image.get('createdAt'), "%Y-%m-%dT%H:%M:%S.%fZ")
            prompt = image.get('meta').get('prompt')

            if prompt:
                prompt = re.sub(r'[<>]', '', prompt)
                prompt = f"Промпт для этой картинки: \n\n<blockquote> {prompt} </blockquote>"
                if len(prompt) > 1024:
                    prompt = prompt[:1024]

                if not await is_img_id_exists(img_id):
                    await create_prompt_id(img_id, img_created_at)
                    await bot.send_photo(
                        CONFIG.tg_bot.chat_id,
                        photo=img_url,
                        caption=prompt,
                        parse_mode="HTML"
                    )
                    return True
        except Exception as ex:
            logger.error(f"Не удалось запостить так как возникла ошибка: {ex}")
    return False


