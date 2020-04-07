from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker, scoped_session
from sqlalchemy_utils import EmailType, URLType, PasswordType, ChoiceType, ArrowType
import passlib
# from furl import furl
# from datetime import datetime
import arrow


engine = create_engine('sqlite:///sport_app.db')
Base = declarative_base(bind=engine)

session_factory = sessionmaker(bind=engine)
Session = scoped_session(session_factory)


class User(Base):

    TYPES = [
        (u'admin', u'Администратор ресурса'),
        (u'amateur', u'Любитель'),
        (u'fitness_blogger', u'Журналист')
    ]

    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    login = Column(String(40), nullable=False)
    password = Column(PasswordType(
        schemes=[
            'pbkdf2_sha512',
            'md5_crypt'
        ],

        deprecated=['md5_crypt']
    ))
    email = Column(EmailType, nullable=False)
    full_name = Column(String(40), nullable=False)
    date_birth = Column(ArrowType, nullable=True)
    user_type = Column(ChoiceType(TYPES), nullable=False)

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
    link_page = Column(URLType, nullable=False)
    contact = Column(String(22), nullable=False)

    user = relationship("User", back_populates="fitness_blogger")


def create_user_amateur():
    session = Session()

    user = User(login="beginner", password="b", email="testmail@rambler.ru",
                full_name="ivanov ivan ivanovich", user_type=u"amateur")
    session.add(user)
    session.flush(session)

    user1 = User(login="dUd", password="budedud", email="mai@dud.ru",
                 full_name="dud yurii yurievich", user_type=u"fitness_blogger")
    session.add(user1)
    session.flush(session)
    """if user.user_type == u"fitness_blogger":
        amateur = Amateur(user_id=1, idol="floyd mayweather", sport_kind="box")
        session.add(amateur)
        session.flush(session)"""
    amateur = Amateur(user_id=1, idol="floyd mayweather", sport_kind="box")
    session.add(amateur)
    session.flush(session)

    fitness_blogger = FitnessBlogger(user_id=2, link_page="www.sports.ru",
                                     contact="88005553535")
    session.add(fitness_blogger)
    session.flush(session)

    session.commit()
    session.close()


if __name__ == '__main__':
    Base.metadata.create_all()
    create_user_amateur()
