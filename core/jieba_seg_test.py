import re
import unittest
import csv

from jieba import posseg


def tokenizer(text):
    pseg = posseg.cut(text)
    excludes = ['nnd', 'vshi', 'vyou', 'vf', 'vd', 'vx']
    words = []
    for w, p in pseg:
        # pos为nval开头或者NER & w长度>1 & pos不在excludes & w含有中文 (去除，需要支持英文)
        if re.match('[nal]', p) and len(w.strip()) > 1 and (p not in excludes):
            words.append(w)
    return ' '.join(words)


class MyTestCase(unittest.TestCase):
    def test_seg(self):
        text = '今天湖南沅江市检察院对陆勇涉嫌“妨害信用卡管理“和”销售假药”案做出最终决定，认为其行为不构成犯罪，决定不起诉。'
        words = []
        pseg = posseg.cut(text)
        for w, p in pseg:
            words.append('_'.join((w, p)))
        print(words)
        self.assertEqual(True, True)

    def test_csv_to_text1(self):
        filename_in = '/Users/lx/corpus/topic/test.csv'

        filename_out = '/Users/lx/corpus/topic/china-news-test.txt'
        self.test_csv_to_text()

    def test_csv_to_text2(self):
        filename_in = '/Users/lx/corpus/topic/train.csv'

        filename_out = '/Users/lx/corpus/topic/china-news-train.txt'
        self.test_csv_to_text(filename_in, filename_out)

    def test_csv_to_text(self, filename_in, filename_out):
        file_out = open(filename_out, 'wt')

        with open(filename_in) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',', quoting=csv.QUOTE_ALL)
            line_count = 0

            for row in csv_reader:
                print(' '.join((row[2], row[1])), file=file_out)
                line_count += 1
                if line_count % 1000 == 0:
                    print('%s is processed' % line_count)

            print(f'Processed {line_count} lines.')

        file_out.close()
        self.assertEqual(True, True)

    def test_seg_file(self):
        filename = '/Users/lx/corpus/topic/test.csv'

        out_filename = '/Users/lx/corpus/topic/test_seg.txt'
        fout = open(out_filename, 'wt')

        with open(filename) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',', quoting=csv.QUOTE_ALL)
            line_count = 0

            for row in csv_reader:
                words = []
                title_seg = posseg.cut(row[1])
                for w, p in title_seg:
                    words.append('_'.join((w, p)))

                body_seg = posseg.cut(row[2])
                for w, p in body_seg:
                    words.append('_'.join((w, p)))

                print(words, file=fout)
                line_count += 1
                if line_count % 100 == 0:
                    print('%s is processed' % line_count)

            print(f'Processed {line_count} lines.')

        fout.close()
        self.assertEqual(True, True)
