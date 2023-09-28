import pytest
import os
from utils.scraping_handler import ScrapingHandler

class TestScrapingHandler:
    @pytest.fixture
    def handler(self):
        return ScrapingHandler('your_url_here', 'your_folder_path_here', 'your_course_here', 'your_year_here')

    def test_scrape_data(self, handler):
        # Add your test cases here
        filenames = handler.scrape_data()
        assert all(os.path.exists(f"{handler.subdirectory}/{filename}") for filename in filenames)

    def test_get_course_info(self, handler):
        # Add your test cases here
        course_info = handler.get_course_info()
        assert course_info == ('your_course_here', 'your_year_here')

    def test_get_file_path(self, handler):
        # Add your test cases here
        file_path = handler.get_file_path('filename')
        assert file_path == 'your_folder_path_here/filename'

    def test_create_directory(self, handler):
        # Add your test cases here
        handler.create_directory()
        assert os.path.exists('your_folder_path_here')

    def test_download_file(self, handler):
        # Add your test cases here
        handler.download_file('url', 'filename')
        assert os.path.exists(f"{handler.subdirectory}/filename")

    def test_parse_html(self, handler):
        # Add your test cases here
        html = "<html><body><h1>Test HTML</h1></body></html>"
        parsed_html = handler.parse_html(html)
        assert parsed_html == "Test HTML"

    def test_save_html(self, handler):
        # Add your test cases here
        handler.save_html('html_content', 'filename')
        assert os.path.exists(f"{handler.subdirectory}/filename.html")

    def test_save_text(self, handler):
        # Add your test cases here
        handler.save_text('text_content', 'filename')
        assert os.path.exists(f"{handler.subdirectory}/filename.txt")

    def test_save_json(self, handler):
        # Add your test cases here
        handler.save_json({'key': 'value'}, 'filename')
        assert os.path.exists(f"{handler.subdirectory}/filename.json")