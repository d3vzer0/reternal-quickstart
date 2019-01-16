from operations import Command

class ImportCommand:
    def create():
        create_command = Command.create("exec_shell")
        create_command = Command.create("make_screenshot")
        create_command = Command.create("get_ifaces")
        create_command = Command.create("download_remote")
        create_command = Command.create("read_file")
        return create_command
