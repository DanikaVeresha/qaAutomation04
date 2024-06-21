import datetime
import random
import time
import uuid


class User:

    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email
        self.UUID = uuid.uuid4()

        self.users = []
        self.orders = []

    @staticmethod
    def random_string(string, length):
        return ''.join(random.choices(string, k=length))

    @staticmethod
    def arrival_date():
        res = datetime.datetime.now() + datetime.timedelta(days=random.randint(1, 4))
        return res.strftime('%d-%m-%Y %H:%M')

    def add_user(self, username):
        user_info = {
            'ID': id(self.username),
            'USERNAME': username,
            'USER PASSWORD': self.random_string(self.password, 22),
            'USER EMAIL': self.email
        }
        self.users.append(user_info)

    def get_user_data(self):
        return f'User: {self.users}'

    def registration(self):
        print(f'{self.username} registration was successful')
        return self.add_user(self.username)

    def login(self):
        for item in self.users:
            if self.username == item['USERNAME']:
                return f'Welcome {self.username}! You are logged in!'
            else:
                return f'User {self.username} not found!'

    def create_order(self, num, order):
        for item in self.users:
            if self.username == item['USERNAME']:
                description_order = {
                    '#': num,
                    'ID': self.UUID,
                    'date_created_of_order': time.ctime(),
                    'client': self.username,
                    'order': order,
                    'date_arrival': self.arrival_date(),
                }
                self.orders.append(description_order)
                return f'{self.username} your order has been successfully processed and added '
            else:
                return f'User {self.username} not found!'

    def get_orders(self, username):
        if self.username == username and self.orders != []:
            for item in self.orders:
                if item['client'] == username:
                    return f'{self.username} your orders -> \n' \
                           f'{self.orders}\n'
        else:
            return f'User {self.username} don`t have orders!'

    def delete_order(self, num):
        for order_item in self.orders:
            if order_item['client'] == self.username and order_item['#'] == num:
                self.orders.remove(order_item)
                return f'{self.username} your order {num} is deleted successfully!'

    def __str__(self):
        return f'Username: {self.username}\n' \
               f'Description order -> {self.get_orders()}\n' \



# obj1 = User(
#     'Jon Doe',
#     'jon1234',
#     'jondoe@gmail.com'
# )
#
# obj2 = User(
#     'Jeyn Doe',
#     'jeyn1234',
#     'jeyndoe@gmail.com'
# )
# print('-----Registration-----')
# obj1.registration()
# obj2.registration()
# time.sleep(3)
# print('-----Login-----')
# print(obj1.login())
# print(obj2.login())
# time.sleep(3)
# print('-----Create Order-----')
# print(obj1.create_order(1,
#                         'https://longnails.com.ua/p2118545290-zhenskij-delovoj-kostyum.html?source=merchant_center&gad_source=1&gclid=CjwKCAjwg8qzBhAoEiwAWagLrEFjK0rJIT1jLpbmp17clgohyqU-LEQhTlWmIVx_SQu9HGRlf2lkcRoCjm4QAvD_BwE'))
# print(obj1.create_order(2,
#                         'https://longnails.com.ua/p2118545290-zhenskij-delovoj-kostyum.html?source=merchant_center&gad_source=1&gclid=CjwKCAjwg8qzBhAoEiwAWagLrEFjK0rJIT1jLpbmp17clgohyqU-LEQhTlWmIVx_SQu9HGRlf2lkcRoCjm4QAvD_BwE'))
#
# print(obj2.create_order(1,
#                         'https://longnails.com.ua/p2118545290-zhenskij-delovoj-kostyum.html?source=merchant_center&gad_source=1&gclid=CjwKCAjwg8qzBhAoEiwAWagLrEFjK0rJIT1jLpbmp17clgohyqU-LEQhTlWmIVx_SQu9HGRlf2lkcRoCjm4QAvD_BwE'))
# time.sleep(3)
# print('-----Get Order-----')
# print(obj1.get_orders('Jon Doe'))
# print(obj2.get_orders('Jeyn Doe'))
# time.sleep(3)
# print('-----Delete Order-----')
# print(obj1.delete_order(2))
# time.sleep(3)
# print('-----Get Order-----')
# print(obj1.get_orders('Jon Doe'))
# print(obj2.get_orders('Jeyn Doe'))
# time.sleep(3)
# print('-----Get User Data-----')
# print(obj1.get_user_data())
# print(obj2.get_user_data())

