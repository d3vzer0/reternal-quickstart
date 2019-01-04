from operations import User, Command
from generic import UserDetails

class ImportUser:
    def create():
        userdetails = UserDetails.prompt()
        create_user = User.create(userdetails['username'], userdetails['password'],
            userdetails['email'], userdetails['role'])
        return create_user
