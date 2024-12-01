from dataclasses import dataclass
from environs import Env
from loguru import logger


@dataclass
class TgBot:
    token: str # TG token access
    chat_id: int
    admin_id: str


@dataclass
class DB:
    url: str
    file: str


@dataclass
class Config:
    tg_bot: TgBot
    db: DB


def load_config(path: str | None = None) -> Config:
    env = Env()
    env.read_env(path)
    return Config(
        tg_bot=TgBot(
            token=env("TG_BOT_TOKEN"),
            chat_id=env("TG_CHAT_ID_SEND"),
            admin_id=env("ADMIN_ID"),
        ),
        db=DB(
            url=env("DB_URL"),
            file=env("DB_FILE")
        ),
    )


try:
    CONFIG = load_config()
    logger.success("Loaded config")
except Exception as ex:
    logger.critical(f"Config load error = {ex}")
    raise ValueError(f"Config load error = {ex}")



