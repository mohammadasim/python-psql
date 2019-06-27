from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from database import get_connection
from sqlalchemy.orm import sessionmaker



Base = declarative_base()


class Car(Base):
    def __init__(self, make, model, type, passenger_seats):
        self.make = make
        self.model = model
        self.type = type
        self.passenger_seats = passenger_seats

    __tablename__ = 'cars'

    id = Column(Integer, primary_key=True)
    make = Column(String)
    model = Column(String)
    type = Column(String)
    passenger_seats = Column(Integer)

    def __repr__(self):
        return '<Car(make={make}, model={model}, type={vehicle_type}, passenger_seats={seat_numbers}'.\
            format(make=self.make, model=self.model, vehicle_type=self.type, seat_numbers=self.passenger_seats)

    @staticmethod
    def create_db_session():
        db = get_connection('postgres', 'password123', 'app')
        Base.metadata.create_all(db)
        new_session = sessionmaker(db)
        generate_session = new_session()
        return generate_session

    def save_to_db(self):
        session = Car.create_db_session()
        session.add(self)
        session.commit()



