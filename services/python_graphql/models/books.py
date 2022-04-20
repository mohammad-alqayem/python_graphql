from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import backref, relationship
from models.base import BaseModel
from models.genres import Genres


class Books(BaseModel):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    author = Column(String, nullable=False)
    genre_id = Column(Integer, ForeignKey('genres.id'))
    genre = relationship(
        Genres,
        backref=backref('books', uselist=True, cascade='delete,all')
    )

    def __repr__(self):
        return f"<Book name={self.name} author={self.author}>"
