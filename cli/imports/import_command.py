from cli.operations import Command


class ImportCommand:
     def create(self):
        default_commands = ['exec_shell', 'make_screenshot', 'get_ifaces',
            'download_remote', 'read_file']
        for command in default_commands:
             Command(command).create()
   
        return {'result':'success', 'message':'Finished importing base commands'}
