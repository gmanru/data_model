from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, Session

engine = create_engine('sqlite:///sport_app.db')
Base = declarative_base(bind=engine)


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    login = Column(String(40), nullable=False)
    email = Column(String(40), nullable=False)
    last_first_name_patronymic = Column(String(40), nullable=False)
    date_birth = Column(String(12), nullable=True)
    type_user = Column(String(22), nullable=False)
    amateur = relationship("Amateur", back_populates="user")
    fitness_blogger = relationship("FitnessBlogger", back_populates="user")


class Amateur(Base):
    __tablename__ = 'amateur'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey(User.id), nullable=False)
    idol = Column(String(22), nullable=False)
    sport_kind = Column(String(22), nullable=False)

    user = relationship("User", back_populates="amateur")


class FitnessBlogger(Base):
    __tablename__ = 'fitness_blogger'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey(User.id), nullable=False)
    link_page = Column(String(22), nullable=False)
    contact = Column(String(22), nullable=False)

    user = relationship("User", back_populates="fitness_blogger")
    # contacts: 1)tel_number ,2)email


def create_user_amateur():
    session = Session()

    user = User(login="test_user", email="testmail@rambler.ru", last_first_name_patronymic="ivanov ivan ivanovich", type_user="amateur")
    session.add(user)
    session.flush(session)

    fitness_blogger = FitnessBlogger(user_id=1, link_page="http://sports.ru", contact="88005553535")
    session.add(fitness_blogger)
    session.flush(session)

    amateur = Amateur(user_id=1, idol="floyd mayweather", sport_kind="box")
    session.add(amateur)
    session.flush(session)

    session.commit()
    session.close()


if __name__ == '__main__':
    Base.metadata.create_all()
    create_user_amateur()
