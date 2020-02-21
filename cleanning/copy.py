import re

class Copy:

    def __init__(self, reader, writer):
        self.reader = reader
        self.writer = writer
        self.data = list()

    def construct(self, file_path):
        string = self.reader.read(file_path)
        new_list = re.split(',', string)
        field = 0
        message_tmps = list()
        tmp_list = list()
        index_check = [ '\d+', '\w+', '\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}', '\d+', '\w+', '\d+', '\w\n{0,1}']
        for string in new_list:
            if field != 2 and re.search(index_check[field], string):
                tmp_list.append(string)
                field += 1
            elif field == 2 and re.search(index_check[field], string):
                tmp_list.append(','.join(message_tmps))
                message_tmps = list()
                tmp_list.append(string)
                field += 1
            elif field == 2 and not re.search(index_check[field], string):
                message_tmps.append(string)
            if field == 7:
                self.data.append(tmp_list)
                tmp_list = list()
                field = 0

    def to_csv(self, file_path):
        self.writer.to_csv(self.data, file_path)