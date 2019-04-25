from .base import BaseTutorialLesson

class TestTutorialBasicArguments(BaseTutorialLesson):

    def test_00_cli_with_single_argument(self):
        result = self.run_command(['Tutorial'])
        assert result.output == 'Hello, Tutorial!\n'

    def test_01_cli_with_multiple_arguments(self):
        result = self.run_command(['Tutorial', 'Cleveland', 'Everybody'])
        assert result.output == "Hello, Tutorial!\nHello, Cleveland!\nHello, Everybody!\n"

    def test_02_cli_with_no_argument(self):
        result = self.run_command()
        assert result.output == ''
