from cli.operations import User, Command
from cli.generic import UserDetails


class ImportUser:
    def create(self):
        userdetails = UserDetails().prompt()
        create_user = User(userdetails['username']).create(userdetails['password'],
            userdetails['role'])
        return create_user
