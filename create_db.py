from settings_db import Base, Session
from models import User, Amateur, FitnessBlogger


def create_user_amateur():

    session = Session()

    user = User(login="beginner", password="b", email="testmail@rambler.ru",
                full_name="ivanov ivan ivanovich", date_birth="1995.03.08",
                user_type=u"amateur")
    session.add(user)
    session.flush(session)

    user1 = User(login="dUd", password="budedud", email="mai@dud.ru",
                 full_name="dud yurii yurievich", date_birth="2001.02.21",
                 user_type=u"fitness_blogger")
    session.add(user1)
    session.flush(session)

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
