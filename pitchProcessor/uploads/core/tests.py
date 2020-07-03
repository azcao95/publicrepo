from django.test import TestCase

from .models import FileData
# Create your tests here.


class FileDataModelTests(TestCase):
    def test_process_file_returns_stored_data_with_all_lines_valid(self):
        test_lines = ["S28961443ABK27GA0001C1S000100TWM   0000701400Y",
                      "S28800166A9K27G60000DIS000500QQQQ  0000497400Y"]

        test_file_data = FileData()

        self.assertEqual(test_file_data.process_file(
            test_lines), test_file_data.data)

    def test_process_file_returns_None_with_invalid_line(self):
        test_lines = ["S28961443ABK27GA0001C1S000100TWM   0000701400Y",
                      "Obviously Invalid",
                      "S28800166A9K27G60000DIS000500QQQQ  0000497400Y"]

        test_file_data = FileData()
        self.assertIs(test_file_data.process_file(test_lines), None)

    def test_process_file_returns_stored_data_with_blank_line(self):
        test_lines = ["S28961443ABK27GA0001C1S000100TWM   0000701400Y",
                      "",
                      "S28800166A9K27G60000DIS000500QQQQ  0000497400Y"]
        test_file_data = FileData()

        self.assertEqual(test_file_data.process_file(
            test_lines), test_file_data.data)
