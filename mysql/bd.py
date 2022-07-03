import pymysql
from sqlalchemy import create_engine

pymysql.install_as_MySQLdb()

engine = create_engine("mysql+mysqldb://root:1111@localhost/my_first_task")

