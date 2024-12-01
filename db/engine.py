from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from config.main_config import CONFIG
from db.models.pars_prompts import Base, ParsPrompts
from loguru import logger
from sqlalchemy.future import select
from datetime import datetime

engine = create_async_engine(CONFIG.db.url)
async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


# Функция для создания элемента
async def create_prompt_id(img_id: str, img_created_at: datetime):
    async with async_session() as session:
        async with session.begin():
            try:
                new_prompt = ParsPrompts(
                    img_id=img_id,
                    status="Done",
                    img_created_at=img_created_at
                )
                session.add(new_prompt)
                await session.commit()
                logger.success(f"Успешно добавлена запись img_id = {img_id}")
                return True
            except Exception as ex:
                await session.rollback()
                logger.error(f"Ошибка добавления записи img_id = {img_id}: {ex}")
                return False


async def is_img_id_exists(img_id: str):
    async with async_session() as session:
        async with session.begin():
            result = await session.execute(
                select(ParsPrompts).where(ParsPrompts.img_id == img_id)
            )

            if result.first() is None:
                return False
            else:
                return True
