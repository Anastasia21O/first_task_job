from .bd import engine

from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()
Base.metadata.create_all(engine)

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String)
    sorname = Column(String)
    phone = Column(String)
    age = Column(Integer)
    salary = Column(Integer)
    def __repr__(self):
       return "<User(name='%s', sorname='%s', phone='%s', age='%s', salary='%s')>" % (
                            self.name, self.sorname, self.phone, self.age, self.salary)


session.commit()
