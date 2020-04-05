from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, Session

engine = create_engine('sqlite:///sport_app.db')
Base = declarative_base(bind=engine)


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    login = Column(String(40), nullable=False)
    password = Column(String(40), nullable=False)
    email = Column(String(40), nullable=False)

    person = relationship("Person", back_populates="user")


class Person(Base):
    __tablename__ = 'person'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey(User.id), nullable=False)
    fio = Column(String(40), nullable=False)
    date_birth = Column(String(12), nullable=True)
    type_person = Column(String(22), nullable=False)
    # type_person: 1)amateur ,2)fitness bloger

    user = relationship("User", back_populates="person")
    amateur = relationship("Amateur", back_populates="person")
    fitness_blogger = relationship("FitnessBlogger", back_populates="person")


class Amateur(Base):
    __tablename__ = 'amateur'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey(Person.user_id), nullable=False)
    cumir = Column(String(22), nullable=False)
    sport_kind = Column(String(22), nullable=False)

    person = relationship("Person", back_populates="amateur")


class FitnessBlogger(Base):
    __tablename__ = 'fitness_blogger'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey(Person.user_id), nullable=False)
    cumir = Column(String(22), nullable=False)
    sport_kind = Column(String(22), nullable=False)

    person = relationship("Person", back_populates="fitness_blogger")
    # contacts: 1)tel_number ,2)email


def create_user_amateur():
    session = Session()

    user = User(login="test_user", password="test_pswd", email="testmail@rambler.ru")
    session.add(user)
    session.flush(session)

    person = Person(user_id=1, fio="ivanov ivan ivanovich", type_person="amateur")
    session.add(person)
    session.flush(session)

    amateur = Amateur(user_id=1, cumir="floyd mayweather", sport_kind="box")
    session.add(amateur)
    session.flush(session)
    session.commit()
    session.close()


if __name__ == '__main__':
    Base.metadata.create_all()
    create_user_amateur()
