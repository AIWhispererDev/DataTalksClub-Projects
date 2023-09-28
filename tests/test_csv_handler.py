import pytest
import os
from utils.csv_handler import CSVHandler

class TestCSVHandler:
    @pytest.fixture
    def handler(self):
        return CSVHandler('your_csv_path_here')

    def test_update_titles(self, handler):
        # Add your test cases here
        handler.update_titles(['title1', 'title2'])
        assert handler.df['project_title'].tolist() == ['title1', 'title2']

    def test_save(self, handler):
        # Add your test cases here
        handler.save('new_path')
        assert os.path.exists('new_path')

    def test_clean_and_deduplicate(self, handler):
        # Add your test cases here
        handler.clean_and_deduplicate('column_name')
        assert handler.df['column_name'].duplicated().sum() == 0

    def test_get_readme_filename(self, handler):
        # Add your test cases here
        assert handler.get_readme_filename('owner', 'repo', 'path') == 'expected_result'

    def test_construct_readme_api_url(self, handler):
        # Add your test cases here
        assert handler.construct_readme_api_url('url') == ('expected_result_1', 'expected_result_2')