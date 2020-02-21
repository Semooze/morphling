import unittest
from cleanning.input import Reader
from cleanning.copy import Copy
from cleanning.output import Writer


class TestCopyData(unittest.TestCase):
    def test_be_able_to_create_data_struct_from_intput_data(self):
        reader = Reader()
        writer = Writer()
        obj = Copy(reader, writer)
        obj.construct('test/input_file/basic_line')
        actual = obj.data
        self.assertEqual(
            actual,
            [
                [
                    '1079784248112951296',
                    'reply',
                    '@PNchP_ เสียจัยอะ เพื่อนงัย นี่เพื่อนเอง',
                    '2019-01-01 00:00:00',
                    '560',
                    'twitter',
                    '1904452146',
                    'หมีชมพู',
                ]
            ],
        )

    def test_ba_able_to_create_data_struct_when_there_are_space_between_message(self):
        reader = Reader()
        writer = Writer()
        obj = Copy(reader, writer)
        obj.construct('test/input_file/space_between_message')
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

    def test_be_able_to_create_data_when_there_is_comma_between_message(self):
        reader = Reader()
        writer = Writer()
        obj = Copy(reader, writer)
        obj.construct('test/input_file/comma_between_message')
        actual = obj.data
        self.assertEqual(
            actual,
            [
                [
                    '1079784248717070336',
                    'tweet',
                    'dear past ,\nthank you for all the lessons.\n\n.\n#HappyNewYear2019 https://t.co/LNIo1hGeoR',
                    '2019-01-01 00:00:00',
                    '5209',
                    'twitter',
                    '1192256738',
                    'Maink มองโลก',
                ]
            ],
        )

    def test_be_able_to_construct_when_owner_id_is_emoji(self):
        reader = Reader()
        writer = Writer()
        obj = Copy(reader, writer)
        obj.construct('test/input_file/owner_name_end_with_emoji')
        actual = obj.data
        self.assertEqual(
            actual,
            [
                [
                    '1079784244640010240',
                    'tweet',
                    'จุดพลุกันสนุกมากนะ',
                    '2019-01-01 00:00:00',
                    '9672',
                    'twitter',
                    '1013618778',
                    '💖',
                ]
            ],
        )

    def test_be_able_to_construct_from_multiple_line(self):
        reader = Reader()
        writer = Writer()
        obj = Copy(reader, writer)
        obj.construct('test/input_file/multiple_line')
        actual = obj.data
        self.assertEqual(
            actual,
            [
                [
                    '1079784244640010240',
                    'tweet',
                    'จุดพลุกันสนุกมากนะ',
                    '2019-01-01 00:00:00',
                    '9672',
                    'twitter',
                    '1013618778',
                    '💖',
                ],
                [
                    '1079784248112951296',
                    'reply',
                    '@PNchP_ เสียจัยอะ เพื่อนงัย นี่เพื่อนเอง',
                    '2019-01-01 00:00:00',
                    '560',
                    'twitter',
                    '1904452146',
                    'หมีชมพู',
                ],
            ],
        )

    def test_be_able_to_construct_data_from_csv_file(self):
        reader = Reader()
        writer = Writer()
        obj = Copy(reader, writer)
        obj.construct_csv('test/input_file/csv_format')
        actual = obj.data
        print('*******************************')
        print(actual)
        self.assertEqual(
            actual,
            [
                [
                    'id',
                    'type',
                    'message',
                    'time',
                    'engagement',
                    'channel',
                    'owner id',
                    'owner name',
                ],
                [
                    '1079784248717070336',
                    'tweet',
                    'dear past ,\nthank you for all the lessons.\n\n.\n#HappyNewYear2019 https://t.co/LNIo1hGeoR',
                    '2019-01-01 00:00:00',
                    '5209',
                    'twitter',
                    '1192256738',
                    'Maink มองโลก',
                ]
            ],
        )
    def test_be_able_to_write_data_into_file_with_csv_format(self):
        reader = Reader()
        writer = Writer()
        obj = Copy(reader, writer)
        obj.construct('test/input_file/basic_line')
        output_path = 'test/output_file/basic_data_to_csv'
        obj.to_csv(output_path)
        with open(output_path, 'r') as reader:
            expect = reader.read()
        self.assertEqual(
            '1079784248112951296,reply,@PNchP_ เสียจัยอะ เพื่อนงัย นี่เพื่อนเอง,2019-01-01 00:00:00,560,twitter,1904452146,หมีชมพู\n',
            expect,
        )
