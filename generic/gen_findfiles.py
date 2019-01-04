import os


class FindFiles:
    def extension(path, ext):
        file_list = []
        for dirpath, dirnames, filenames in os.walk(path):
            for filename in [f for f in filenames if f.endswith(ext)]:
                file_list.append(os.path.join(dirpath, filename))
        return file_list