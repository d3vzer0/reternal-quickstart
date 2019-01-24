from cli.imports import Mapping
from cli.imports import ImportMitre
from cli.imports import ImportUser
from cli.imports import ImportCommand


class Install:
    def all(self):
        print(ImportUser().create())
        print(ImportCommand().create())
        print(ImportMitre().update())
        print(Mapping().update())
        return {'result':'success', 'message':'Finished importing all objects'}
  


