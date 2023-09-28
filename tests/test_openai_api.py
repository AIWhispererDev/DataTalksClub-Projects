import pytest
from utils.openai_api import OpenAIAPI

class TestOpenAIAPI:
    @pytest.fixture
    def api(self):
        return OpenAIAPI('your_api_key_here')

    def test_generate_summary(self, api):
        # Add your test cases here
        assert api.generate_summary('content') == 'expected_result'

    def test_generate_multiple_titles(self, api):
        # Add your test cases here
        assert api.generate_multiple_titles('summary') == ['expected_result_1', 'expected_result_2', 'expected_result_3']

    def test_evaluate_and_revise_titles(self, api):
        # Add your test cases here
        assert api.evaluate_and_revise_titles(['title1', 'title2', 'title3']) == ('expected_feedback', 'expected_revised_title')