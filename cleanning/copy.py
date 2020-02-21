class Copy:


    def __init__(self, reader, writer):
        self.reader = reader
        self.write = reader
        self.data = list()

    def construct(self, file_path):
        string = self.reader.read(file_path)
        new_list = string.split(',')
        self.data.append(new_list)