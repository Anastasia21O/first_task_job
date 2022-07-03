import sqlalchemy
import pymysql
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

pymysql.install_as_MySQLdb()

engine = create_engine("mysql+mysqldb://root:1111@localhost/my_first_task")
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

mass_query_first = session.query(User).filter(User.name.like('V%')).all()
mass_query_sod = session.query(User).filter(User.salary < 17000).all()

print(mass_query_sod)


