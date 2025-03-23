from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)

# Создание базы данных
def get_bd():
    return create_engine('"postgresql://postgres:123@localhost:5432/postgres"')

def get_session():
    bd = get_bd()
    Session = sessionmaker(bind=bd)
    return Session()