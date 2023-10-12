#db connection using sqlalchemy

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

SQL_ALCHEMY_DATABASE = 'sqlite:///.todos.db'

# Create engine to open a database
engine = create_engine(SQL_ALCHEMY_DATABASE, connect_args={'check_same_thread': False})

SessionLocal = sessionmaker(autoflush=False, bind=engine, autocommit=False)

Base = declarative_base()
