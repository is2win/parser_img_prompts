from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime

Base = declarative_base()


class ParsPrompts(Base):
    __tablename__ = 'pars_prompts'

    img_id = Column(Integer, primary_key=True)
    status = Column(String)
    status_created_at = Column(DateTime, default=datetime.utcnow)
    img_created_at = Column(DateTime)