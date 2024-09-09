import unittest
import pandas as pd
from unittest.mock import patch, mock_open, MagicMock
import os
import sys

# Asumimos que el script principal está en el directorio padre
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from AnalizadorEstadisticoJudicial import (
    sort_key_func, sorted_files, process_excel_files, process_sheets,
    process_rows, consolidate_data, create_consolidated_file
)

class TestAnalizadorEstadisticoJudicial(unittest.TestCase):

    def test_sort_key_func(self):
        test_cases = [
            ("Primer Trimestre.xls", (0, 0)),
            ("Segundo Trimestre_1.xls", (1, 1)),
            ("Tercer Trimestre.xls", (2, 0)),
            ("Cuarto Trimestre_2.xls", (3, 2)),
        ]
        for file_name, expected in test_cases:
            self.assertEqual(sort_key_func([None, file_name]), expected)

    def test_sorted_files(self):
        files = [
            "Tercer Trimestre.xls",
            "Primer Trimestre.xls",
            "Cuarto Trimestre_1.xls",
            "Segundo Trimestre.xls",
        ]
        expected = [
            "Primer Trimestre.xls",
            "Segundo Trimestre.xls",
            "Tercer Trimestre.xls",
            "Cuarto Trimestre_1.xls",
        ]
        self.assertEqual(sorted_files(files), expected)

    @patch('pandas.ExcelFile')
    @patch('AnalizadorEstadisticoJudicial.process_sheets')
    def test_process_excel_files(self, mock_process_sheets, mock_excel_file):
        mock_excel_file.return_value = MagicMock()
        mock_process_sheets.return_value = None

        files = ["Primer Trimestre.xls", "Segundo Trimestre.xls"]
        subfolder = "test_subfolder/"

        result = process_excel_files(files, subfolder)
        
        self.assertEqual(len(mock_process_sheets.call_args_list), 2)
        self.assertIsInstance(result, dict)

    @patch('pandas.read_excel')
    def test_process_sheets(self, mock_read_excel):
        mock_read_excel.return_value = pd.DataFrame({
            0: ['Total'] + [None] * 19,
            1: range(20)
        })

        mock_xls = MagicMock()
        mock_xls.sheet_names = ['Sheet1']

        all_sheets_data = {}
        writer = MagicMock()
        file_table = MagicMock()

        process_sheets(mock_xls, 'test.xls', all_sheets_data, writer, file_table)

        self.assertIn('Sheet1', all_sheets_data)

    def test_process_rows(self):
        data = pd.DataFrame({
            0: [''] * 19 + ['Total'],
            1: range(20)
        })
        file = 'test.xls'
        all_sheets_data = {}
        writer = MagicMock()
        sheet = 'Sheet1'
        file_table = MagicMock()

        process_rows(data, file, all_sheets_data, writer, sheet, file_table)

        self.assertIn('Sheet1', all_sheets_data)
        self.assertEqual(len(all_sheets_data['Sheet1']), 2)  # Titles and data

    def test_consolidate_data(self):
        data = [
            ['Title1', 'Title2'],
            ['Total', 10, 20, 'Primer Trimestre'],
            ['Total', 30, 40, 'Segundo Trimestre'],
        ]
        result = consolidate_data(data)
        self.assertEqual(len(result), 3)  # Titles and two consolidated rows
        self.assertEqual(result[1], ['Total', 10, 20, 'Primer Trimestre'])
        self.assertEqual(result[2], ['Total', 30, 40, 'Segundo Trimestre'])

    @patch('openpyxl.Workbook')
    def test_create_consolidated_file(self, mock_workbook):
        mock_wb = MagicMock()
        mock_workbook.return_value = mock_wb

        all_sheets_data = {
            'Sheet1': [
                ['Title1', 'Title2'],
                ['Total', 10, 20, 'Primer Trimestre'],
                ['Total', 30, 40, 'Segundo Trimestre'],
            ]
        }
        subfolder = 'test_subfolder/'

        create_consolidated_file(all_sheets_data, subfolder)

        mock_wb.create_sheet.assert_called_once_with(title='Sheet1')

if __name__ == '__main__':
    unittest.main()