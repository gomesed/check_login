def login(user, password):
    if user == '12345' and password == '12345':
        print('Welcome', user)
    else:
        print('Sorry, your username or password was incorrect.')

if __name__ == '__main__':
    user = input('User: ')
    password = input('Password: ')
    login(user, password)
