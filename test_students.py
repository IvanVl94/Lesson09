import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database import Base, Student, get_bd

# "postgresql://postgres:123@localhost:5432/postgres"

@pytest.fixture(scope='module')
def test_db():
    
    # Создание тестовой базы данных
    bd = get_bd()
    Base.metadata.create_all(bd)
    yield bd
    Base.metadata.drop_all(bd)


@pytest.fixture(scope='function')

def session(test_db):
    connection = test_db.connect()
    transaction = connection.begin()
    Session = sessionmaker(bind=connection)
    session = Session()
    yield session
    session.close()
    transaction.rollback()
    connection.close()

#Создание
def test_add_student(session):
    new_student = Student(name='Власов Иван', age=20)
    session.add(new_student)
    session.commit()
    student = session.query(Student).filter_by(name='Власов Иван').first()
    assert student is not None
    assert student.age == 20
    session.delete(student)
    session.commit()


# Изменение
def test_update_student(session):
    student = Student(name='Власов Иван', age=20)
    session.add(student)
    session.commit()
    student.age = 21
    session.commit()
    updated_student = session.query(Student).filter_by(name='Власов Иван').first()
    assert updated_student.age == 21
    session.delete(updated_student)
    session.commit()

# Удаление
def test_delete_student(session):
    student = Student(name='Власов Иван', age=20)
    session.add(student)
    session.commit()
    student.age = 21
    session.commit()
    student = session.query(Student).filter_by(name='Власов Иван').first()
    session.delete(student)
    session.commit()
    deleted_student = session.query(Student).filter_by(name='Власов Иван').first()
    assert deleted_student is None


