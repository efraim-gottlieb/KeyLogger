def change_password(users_list,user,new_password):
    users_list[user] = new_password
    return 'Password changed successfully.'


def check_user(users_list,input_user):
    if input_user in users_list:
        return True
    else:
        print('User not found !')
        return False


def check_password(users_list,input_user,input_password):
    if input_password == users_list[input_user]:
        return True
    else:
        print('Incorrect password ! ')
        return False


def login(users_list,attempts):
    user_check = None
    while not user_check:
        user = input('Enter user name ')
        user_check = check_user(users_list,user)
    password_check = None
    password = None
    while not password_check and attempts:
        attempts = attempts -1
        password = input('Enter your password ')
        password_check = check_password(users_list,user,password)
    if password_check:
        return [True , user]
    else:
        return False


def add_user(users_list,user_name,password):
    users_list[user_name] = password
    return 'The user was created successfully.'
def delete_user(users_list,user):
    delete = input('Are you sure you want to delete the current (y/n) ')
    if delete == 'y':
        users_list.pop(user)
        print(user,'deleted !')
    else:
        print('Cancelled !')
