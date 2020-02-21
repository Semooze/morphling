import unittest
from cleanning.input import Reader
from cleanning.copy import Copy
from cleanning.output import Writer


class TestImportData(unittest.TestCase):
    def test_be_able_to_import_data_from_file(self):
        obj = Reader()
        actual = obj.read('test/test_file.csv')
        with open('test/test_file.csv', 'r') as reader:
            expect = reader.read()
        self.assertEqual(actual, expect)


class TestWriter(unittest.TestCase):
    def test_be_able_to_write_file(self):
        actual = 'test data'
        output_path = 'test/test_output/basic_write'
        obj = Writer()
        obj.write(actual, output_path)
        obj.write(actual, output_path)
        with open(output_path, 'r') as reader:
            expect = reader.read()
        self.assertEqual(actual, expect)

    def test_be_able_to_append_data_into_existing_file(self):
        actual = 'test data'
        output_path = 'test/test_output/basic_write'
        obj = Writer()
        obj.write(actual, output_path)
        obj.append(actual, output_path)
        with open(output_path, 'r') as reader:
            expect = reader.read()
        self.assertEqual(actual + actual, expect)

    def test_be_able_to_write_csv_file(self):
        data = [['name', 'age', 'color'], ['John hopskin', 15, 'Blue sky']]
        output_path = 'test/test_output/test_write_csv.csv'
        obj = Writer()
        obj.to_csv(data, output_path)
        with open(output_path, 'r') as reader:
            expect = reader.read()
        self.assertEqual('name,age,color\nJohn hopskin,15,Blue sky\n', expect)

    def test_be_able_to_write_csv_when_there_is_new_line_beween_data(self):
        data = [['name', 'age', 'color'], ['John\nhopskin', 15, 'Blue sky']]
        output_path = 'test/test_output/test_write_csv_new_line.csv'
        obj = Writer()
        obj.to_csv(data, output_path)
        with open(output_path, 'r') as reader:
            expect = reader.read()
        self.assertEqual('name,age,color\n"John\nhopskin",15,Blue sky\n', expect)

    def test_be_able_to_write_csv_when_there_is_comma_between_data(self):
        data = [['name', 'age', 'color'], ['John, hopskin', 15, 'Blue, sky']]
        output_path = 'test/test_output/test_write_csv_comma.csv'
        obj = Writer()
        obj.to_csv(data, output_path)
        with open(output_path, 'r') as reader:
            expect = reader.read()
        self.assertEqual('name,age,color\n"John, hopskin",15,"Blue, sky"\n', expect)


class TestCopyData(unittest.TestCase):
    def test_be_able_to_create_data_struct_from_intput_data(self):
        reader = Reader()
        writer = Writer()
        obj = Copy(reader, writer)
        obj.construct('test/test_input/basic_line')
        actual = obj.data
        self.assertEqual(
            actual,
            [['id', 'type', 'message', 'time', 'engagement', 'channel', 'owner id', 'owner name']],
        )

    def test_ba_able_to_create_data_struct_when_there_are_space_between_message(self):
        reader = Reader()
        writer = Writer()
        obj = Copy(reader, writer)
        obj.construct('test/test_input/space_between_message')
        actual = obj.data
        self.assertEqual(
            actual,
            [
                [
                    '079784245067829254',
                    'tweet',
                    'Happy New Years 2019🎉🎉 นะคะทุกคน ปีนี้ก็ขอฝากตัวด้วยค่ะ!\nปีที่แล้วถ้าทำอะไรผิดพลาดหรือทำให้ไม่พอใจอะไรไปต้องขอโทษด้วยนะคะ🙏\nดีใจที่ได้รู้จักกับทุกคนค่ะ แล้วก็ขอบคุณที่มาเวิ่นเว้อด้วยกันนะคะ ดีใจมากเลย',
                    '2019-01-01 00:00:00',
                    '9857',
                    'twitter',
                    '2161099140',
                    '🎄FreSan☕59 days countdown to wmtsb3',
                ]
            ],
        )

    # def test_be_able_to_write_data_into__file_with_csv_format(self):
    #     reader = Reader()
    #     writer = Writer()
    #     obj = Copy(reader, writer)
    #     obj.construct('test/test_input/basic_line')
    #     obj.to_csv('test/test_input/')


if __name__ == '__main__':
    unittest.main()
