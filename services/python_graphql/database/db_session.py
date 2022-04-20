from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from config import config
from models.base import BaseModel
from models.characters import Characters
from models.genres import Genres
from models.books import Books

engine = create_engine(config.DB_URL)
BaseModel.metadata.create_all(bind=engine)
db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))
BaseModel.query = db_session.query_property()
