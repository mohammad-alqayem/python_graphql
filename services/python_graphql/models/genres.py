from sqlalchemy import Column, Integer, String
from models.base import BaseModel


class Genres(BaseModel):
    __tablename__ = 'genres'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
