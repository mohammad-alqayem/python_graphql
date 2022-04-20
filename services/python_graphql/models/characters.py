from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import backref, relationship
from models.base import BaseModel
from models.books import Books


class Characters(BaseModel):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    book_id = Column(Integer, ForeignKey('books.id'))
    book = relationship(
        Books,
        backref=backref('character', uselist=True, cascade='delete,all')
    )
