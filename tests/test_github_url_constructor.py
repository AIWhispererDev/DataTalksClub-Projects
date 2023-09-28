import pytest
from utils.github_url_constructor import GithubURLConstructor

class TestGithubURLConstructor:
    @pytest.fixture
    def constructor(self):
        return GithubURLConstructor()

    def test_get_readme_filename(self, constructor):
        # Add your test cases here
        assert constructor.get_readme_filename('owner', 'repo', 'path') == 'expected_result'

    def test_construct_readme_api_url(self, constructor):
        # Add your test cases here
        assert constructor.construct_readme_api_url('url') == ('expected_result_1', 'expected_result_2')