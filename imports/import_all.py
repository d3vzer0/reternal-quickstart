from imports import Mapping
from imports import ImportMitre
from imports import ImportUser
from imports import ImportCommand

class Install:
    def all(self):
        print(ImportUser().create())
        print(ImportCommand().create())
        print(ImportMitre().update())
        print(Mapping().update())
        return {'result':'success', 'message':'Finished importing all objects'}
  


