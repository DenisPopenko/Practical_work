class File():

    def __init__(self, name_file, mode):
        self.name_file = name_file
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.name_file, self.mode, encoding='utf8')
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()
        return True


with File('example.txt', 'w') as file:

    file.write('Всем привет!')

