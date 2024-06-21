import pytest
from lecture18_19.application.app import User
import re
import datetime


@pytest.mark.parametrize('username', ['Jon Smith'])
@pytest.mark.parametrize('password', ['jon1234'])
@pytest.mark.parametrize('email', ['jonesmith@gmail.com'])
def test_data_user(username, password, email):
    user = User(username, password, email)

    assert user.username.replace(' ', '').isalpha(), f'Username {user.username} is not valid'
    assert re.match(r'[a-zA-Z0-9]', user.password), f'Password {user.password} is not valid'
    assert re.match(r'^[a-zA-Z0-9]+@[a-zA-Z0-9]+\.[a-zA-Z0-9]+$', user.email), f'Email {user.email} is not valid'


@pytest.mark.parametrize('username', ['Jon Smith'])
@pytest.mark.parametrize('password', ['jon1234'])
@pytest.mark.parametrize('email', ['jon@gmail.com'])
def test_random_string(username, password, email):
    user = User(username, password, email)
    assert len(user.random_string(user.password, 22)) == 22, 'Length password of random string is not 22'


# Other version
def test_arrival_date():
    user = User('Jon Smith', 'jon1234', 'jon@gmail.com')
    assert user.arrival_date() != datetime.datetime.now().strftime('%d-%m-%Y %H:%M'), 'Date is not valid'


@pytest.mark.parametrize('username', ['Jon Smith'])
@pytest.mark.parametrize('password', ['jon1234'])
@pytest.mark.parametrize('email', ['jon@gmail.com'])
def test_add_user(username, password, email):
    user = User(username, password, email)
    user.add_user(username)
    assert user.get_user_data() == f'User: {user.users}', 'User data is not valid'
    assert user.username in user.users[0].values(), 'User is not added'


@pytest.mark.parametrize('username', ['Jon Smith'])
@pytest.mark.parametrize('password', ['jon1234'])
@pytest.mark.parametrize('email', ['jon@gmail.com'])
def test_registration(username, password, email):
    user = User(username, password, email)
    assert user.registration() == user.add_user(username), 'Registration not passed'


@pytest.mark.parametrize('username', ['Jon Smith'])
@pytest.mark.parametrize('password', ['jon1234'])
@pytest.mark.parametrize('email', ['jon@gmail.com'])
def test_login(username, password, email):
    user = User(username, password, email)
    user.add_user(username)
    assert user.login() == f'Welcome {username}! You are logged in!', 'Login is not valid'
    assert user.username in user.users[0].values(), 'User is not added'


@pytest.mark.parametrize('username', ['Jon Smith'])
@pytest.mark.parametrize('password', ['jon1234'])
@pytest.mark.parametrize('email', ['jon@gmail.com'])
def test_create_order(username, password, email):
    user = User(username, password, email)
    user.add_user(username)
    assert user.create_order(1, 'order') == f'{username} your order has been successfully processed and added ', 'Create order is not valid'
    assert user.username in user.orders[0].values(), 'Order is not added'
    assert user.username in user.users[0].values(), 'User is not added'


@pytest.mark.parametrize('username', ['Jon Smith'])
@pytest.mark.parametrize('password', ['jon1234'])
@pytest.mark.parametrize('email', ['jon@gmail.com'])
def test_get_orders(username, password, email):
    user = User(username, password, email)
    user.add_user(username)
    user.create_order(1, 'order')
    assert user.get_orders(username) == f'{username} your orders -> \n' \
                                        f'{user.orders}\n', 'Get orders is not valid'
    assert user.username in user.orders[0].values(), 'Order is not added'
    assert user.username in user.users[0].values(), 'User is not added'


@pytest.mark.parametrize('username', ['Jon Smith'])
@pytest.mark.parametrize('password', ['jon1234'])
@pytest.mark.parametrize('email', ['jon@gmail.com'])
def test_delete_order(username, password, email):
    user = User(username, password, email)
    user.add_user(username)
    user.create_order(1, 'order')
    assert user.delete_order(1) == f'{username} your order 1 is deleted successfully!', 'Delete order is not valid'
    assert user.orders == [], 'Order is not deleted'
    assert user.username not in user.users, 'User is not deleted'











