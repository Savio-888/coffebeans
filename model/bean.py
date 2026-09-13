from model.database import Database, Base, engine
from sqlalchemy import Column, String, Integer, DateTime, CheckConstraint
import datetime

class Bean(Base):
    __tablename__ = 'beans'

    id_bean = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)
    brewing_method = Column(String, nullable=False)
    rating = Column(Integer, CheckConstraint('rating >= 1 AND rating <= 10', name='check_rating_range'), nullable=False)
    date_creation = Column(DateTime, nullable=False)

class Bean_model():
    @staticmethod
    def insert_bean(name, brewing, rating):
        session = Database.create_session(engine)
        bean = Bean(name=name, brewing_method=brewing, rating=rating, date_creation=datetime.datetime.now())
        session.add(bean)
        session.commit()
        session.close()
    @staticmethod
    def list_beans():
        session = Database.create_session(engine)
        list = session.query(Bean).all()
        session.close()
        return list
    @staticmethod
    def list_bydate():
        session = Database.create_session(engine)
        list = session.query(Bean).order_by(Bean.date_creation.desc()).all()
        session.close()
        return list
    @staticmethod
    def list_byrating_best():
        session = Database.create_session(engine)
        list = session.query(Bean).order_by(Bean.rating.desc()).all()
        session.close()
        return list
    @staticmethod
    def list_byrating_worst():
        session = Database.create_session(engine)
        list = session.query(Bean).order_by(Bean.rating).all()
        session.close()
        return list