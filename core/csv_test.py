import csv
import unittest


class MyTestCase(unittest.TestCase):
    def test_read(self):
        with open('employee_file.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    print(f'Column names are {", ".join(row)}')
                    line_count += 1
                else:
                    print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
                    line_count += 1
            print(f'Processed {line_count} lines.')
        self.assertEqual(True, True)

    def test_write(self):
        with open('employee_file.csv', mode='w') as employee_file:
            employee_writer = csv.writer(employee_file, delimiter=',', quoting=csv.QUOTE_MINIMAL)

            employee_writer.writerow(['John Smith', 'Accounting', 'November'])
            employee_writer.writerow(['Erica Meyers', 'IT', 'March\n'])
            employee_writer.writerow(['Erica Meyers', 'IT', 'Mar"ch\n'])
        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()