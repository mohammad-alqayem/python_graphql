from database.db_session import db_session, engine
from models.base import BaseModel
from models.books import Books
from models.characters import Characters
from models.genres import Genres


def init_db():
    """
    Generate dummy data
    """

    BaseModel.metadata.drop_all(bind=engine)
    BaseModel.metadata.create_all(bind=engine)

    fantasy = Genres(name='Fantasy')
    db_session.add(fantasy)
    political_fiction = Genres(name='Political Fiction')
    db_session.add(political_fiction)
    philosophical_novel = Genres(name='Philosophical Novel')
    db_session.add(philosophical_novel)

    peter_wendy = Books(name='Peter & Wendy', author='J.M. Barrie', genre=fantasy)
    db_session.add(peter_wendy)
    crooked_kingdom = Books(name='Crooked Kingdom', author='Leigh Bardugo', genre=political_fiction)
    db_session.add(crooked_kingdom)
    crime_punishment = Books(name='Crime and Punishment', author='Fyodor Dostoyevsky',
                             genre=philosophical_novel)
    db_session.add(crime_punishment)

    peter_pan = Characters(name='Peter Pan', book=peter_wendy)
    db_session.add(peter_pan)
    wendy_darling = Characters(name='Wendy Darling', book=peter_wendy)
    db_session.add(wendy_darling)
    inej_ghafa = Characters(name='Inej Ghafa', book=crooked_kingdom)
    db_session.add(inej_ghafa)

    db_session.commit()
