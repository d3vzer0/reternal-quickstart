import getpass
import re


class UserDetails:
    def prompt():
        userdetails = dict.fromkeys(['username', 'password', 'email', 'role'])
        while userdetails['username'] is None:
            userdetails['username'] = input("Username: ")

        while userdetails['password'] is None:
            userdetails['password'] = getpass.getpass()

        while userdetails['role'] is None:
            user_role =  input("Role (User/Admin): ")
            if user_role == "Admin" or user_role == "User":
                userdetails['role'] = user_role


        return userdetails

