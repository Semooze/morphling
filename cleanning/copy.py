import re

class Copy:

    def __init__(self, reader, writer):
        self.reader = reader
        self.writer = writer
        self.data = list()
    
    def __construct(self, data):
        field = 0
        message_tmps = list()
        tmp_list = list()
        index_check = [ '\d+', '\w+', '\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}', '\d+', '\w+', '\d+', '.*\n{0,1}']
        for string in data:
            if field == 6 and string.find('\n') != -1:
                words = string.split('\n')
                tmp_list.append(words[0])
                self.data.append(tmp_list)
                tmp_list = [words[1]]
                field = 1
            elif field != 2 and re.search(index_check[field], string):
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

    def construct_csv(self, file_path):
        string = self.reader.read(file_path)
        new_list = re.split(',', string)
        header = new_list[0:7]
        tmp = new_list[7]
        last_header, first_field = tmp.split('\n')
        header.append(last_header)
        self.data.append(header)
        del new_list[0:8]
        new_list.insert(0, first_field)
        self.__construct(new_list)

    def construct(self, file_path):
        string = self.reader.read(file_path)
        new_list = re.split(',', string)
        self.__construct(new_list)

    def to_csv(self, file_path):
        self.writer.to_csv(self.data, file_path)