import getpass
import re


class UserDetails:
    def prompt():
        userdetails = dict.fromkeys(['username', 'password', 'email', 'role'])
        while userdetails['username'] is None:
            userdetails['username'] = input("Username: ")

        while userdetails['password'] is None:
            userdetails['password'] = getpass.getpass()

        while userdetails['email'] is None:
            emailUnparsed = input("Email: ")
            regexMail = re.search(
                "(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)",
                emailUnparsed)
            if regexMail:
                userdetails['email'] = emailUnparsed
            else:
                print("Invalid email format")
                quit()
        
        while userdetails['role'] is None:
            userdetails['role'] = input("Role (user/admin): ")


        return userdetails

