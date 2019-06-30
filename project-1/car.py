from sqlalchemy import Column, Integer, String
from database import session_factory
from database import Base





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
        return '<Car(make={make}, model={model}, type={vehicle_type}, passenger_seats={seat_numbers}>'. \
            format(make=self.make, model=self.model, vehicle_type=self.type, seat_numbers=self.passenger_seats)

    def save_to_db(self):
        session = session_factory()
        session.add(self)
        session.commit()

    @classmethod
    def find_by_model(cls, model):
        '''
        Returns the vehicle of the queried model
        :param model:
        :return Car:
        '''
        session = session_factory()
        query = session.query(Car).filter_by(model=model).first()
        return query

    @classmethod
    def find_by_type(cls, type):
        session = session_factory()
        return session.query(Car).filter_by(type=type).all()

    @classmethod
    def find_by_number_of_passanger_seats(cls, passenger_seats):
        session = session_factory()
        return session.query(Car).filter_by(passenger_seats=passenger_seats).all()