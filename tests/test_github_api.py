import pytest
from utils.github_api import GitHubAPI

class TestGitHubAPI:
    @pytest.fixture
    def api(self):
        return GitHubAPI('your_token_here')

    def test_get_readme_content(self, api):
        # Add your test cases here
        assert api.get_readme_content('url') == 'expected_result'

    def test_get_readme_filename(self, api):
        # Add your test cases here
        assert api.get_readme_filename('owner', 'repo', 'path') == 'expected_result'

    def test_construct_readme_api_url(self, api):
        # Add your test cases here
        assert api.construct_readme_api_url('url') == ('expected_result_1', 'expected_result_2')