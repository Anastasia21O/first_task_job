import sqlite3
from sqlalchemy import create_engine
from sqlalchemy.pool import StaticPool
engine = create_engine('sqlite:///my_first_task.db',
                    connect_args={'check_same_thread':False},
                    poolclass=StaticPool)
#engine = create_engine("sqlite+pysqlite:////my_first_task.db")

