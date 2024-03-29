from database import session_factory
from sqlalchemy import Column, Integer, String
from database import Base


class User(Base):
    def __init__(self, email, first_name, last_name):
        self.email = email
        self.first_name = first_name
        self.last_name = last_name

    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    email = Column(String)
    first_name = Column(String)
    last_name = Column(String)

    def __repr__(self):
        return "<User {}>".format(self.email)

    def save_to_db(self):
        session = session_factory()
        session.add(self)
        session.commit()

    @classmethod
    def find_by_email(cls, email):
        session = session_factory()
        query = session.query(User).filter_by(email=email).first()
        return query
