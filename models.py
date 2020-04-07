from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy_utils import EmailType, URLType, PasswordType, ChoiceType, ArrowType
from settings_db import Base


class User(Base):

    TYPES = [
        (u'amateur', u'Любитель'),
        (u'fitness_blogger', u'Журналист')
    ]

    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    login = Column(String(40), unique=True, nullable=False)
    password = Column(PasswordType(
        schemes=[
            'pbkdf2_sha512',
            'md5_crypt'
        ],

        deprecated=['md5_crypt']
    ))
    email = Column(EmailType, unique=True, nullable=False)
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
