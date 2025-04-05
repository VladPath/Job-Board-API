from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

USE_DATABASE = 'postgresql://postgres:vlad@localhost:5432/job-board'

engine = create_engine(USE_DATABASE)

session_local = sessionmaker(autocommit=False, autoflush=True, bind=engine)

Base = declarative_base()