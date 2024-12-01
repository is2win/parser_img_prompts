from loguru import logger
import logging
from aiogram import Bot, Dispatcher
from config.main_config import CONFIG

# Отключаем стандартный логгер aiogram и заменяем его на loguru
logging.getLogger('aiogram').handlers = [logging.NullHandler()]  # Отключаем стандартный логгер


class InterceptHandler(logging.Handler):
    def emit(self, record):
        # Передаем все логи из aiogram в loguru
        level = logger.level(record.levelname).name if logger.level(record.levelname, None) else record.levelno
        logger.log(level, record.getMessage())

logging.basicConfig(handlers=[InterceptHandler()], level=logging.INFO)


logger.success("Starting TG Bot")

bot = Bot(
    token=CONFIG.tg_bot.token,
)

dp = Dispatcher()
# main menu

# routers



