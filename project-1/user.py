from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from database import get_connection
from sqlalchemy.orm import sessionmaker


Base = declarative_base()

class User:
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

    @staticmethod
    def create_db_session():
        db = get_connection('postgres', 'password123', 'app')
        Base.metadata.create_all(db)
        new_session = sessionmaker(db)
        generate_session = new_session()
        return generate_session

    def save_to_db(self):
        session = User.create_db_session()
        session.add(self)
        session.commit()

    @classmethod
    def find_by_email(cls, email):
        session = User.create_db_session()
        query = session.query()
        return query.filter_by(email=email).first()



