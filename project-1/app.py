from car import Car
from user import User

# first_user = User.load_from_db_by_email('aisha.ayub@gmail.com')
# print(first_user.email)
# print(first_user.id)
# second_user = User('asiya1.ayub@gmail.com', 'Asiya', 'Ayub', None)
# second_user.save_to_db()
# third_user = User('mohammad1@gmail.com', 'Mohammad', 'Mohammad', None)
# third_user.save_to_db()
# forth_user = User.load_from_db_by_email('moez.ayub@gmail.com')
# print(forth_user)
my_car = Car('Ford', 'Mondeo', 'saloon', 5)
my_car.save_to_db()
new_user = User('zaki@gmail.com', 'Ahmed', 'Zaki')
new_user.save_to_db()
print(my_car)
print(new_user)
