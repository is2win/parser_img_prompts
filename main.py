import asyncio
from parsing.parsing_job import start_parsing
from loguru import logger
from tg_bot_app.tg_bot import bot
from config.main_config import CONFIG


async def main():
    while True:
        try:
            await start_parsing()
            logger.success("Выполнен Круг")
            # await bot.send_message(CONFIG.tg_bot.admin_id, "Отправил Сообщение")
            await asyncio.sleep(5 * 60)
        except Exception as ex:
            await bot.send_message(CONFIG.tg_bot.admin_id, f"Глобальная ошибка: {ex}")


if __name__ == '__main__':
    asyncio.run(main())