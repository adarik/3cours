from sqlalchemy.orm.scoping import scoped_session

from project.dao.models import Genre


class GenreDAO:
    def __init__(self, session: scoped_session):
        self._db_session = session

    def get_one(self, gid):
        return self._db_session.query(Genre).filter(Genre.id == gid).one_or_none()

    def get_all(self):
        return self._db_session.query(Genre).all()