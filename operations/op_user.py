from operations.models import Users
from generic import Random
import hashlib
import mongoengine
import json

class User:
    def get(user_id):
        try:
            user_object = Users.objects.get(id=user_id)
            result = {'username': user_object['username'], 'groups': [],
                      'email': user_object['email'],
                      'role': user_object['role'],
                      'id': str(user_object['id'])}

        except mongoengine.errors.DoesNotExist:
            result = {"result": "failed", "message": "User does not exist"}

        except Exception as err:
            result = {"result": "failed", "message": "Gonna' catch them all"}

        return result

    def create(username, password, email, role):
        try:
            salt = Random.create(20)
            password_hash = hashlib.sha512()
            password_string = salt + password
            password_hash.update(password_string.encode('utf-8'))
            password_hash = str(password_hash.hexdigest())

            user = Users(
                username=username,
                salt=salt,
                password=password_hash,
                email=email,
                role = role
            ).save()

            result = {"result": "created",
                      "message": "Succesfully created user"}

        except mongoengine.errors.NotUniqueError:
            result = {"result": "failed", "message": "User already exists"}

        except Exception as err:
            result = {"result": "failed", "message": "Failed to create user"}

        return result

    def delete(user_id):
        try:
            user_object = Users.objects.get(id=user_id).delete()
            result = {"result": "deleted", "message": "Deleted user from DB"}

        except mongoengine.errors.DoesNotExist:
            result = {"result": "failed", "message": "User does not exist"}


        return result