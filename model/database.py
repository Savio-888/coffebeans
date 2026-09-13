from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()
engine = create_engine('sqlite:///database.db')

class Database():
    @staticmethod
    def create_database():
        Base.metadata.create_all(engine)
    @staticmethod
    def create_session(engine):
        _session = sessionmaker(engine)
        session = _session()
        return session


