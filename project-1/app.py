from car import Car
from user import User

car = Car.find_by_model('sharan')
print(car)

user = User.find_by_email('moezayub@gmail.com')
print(user)
