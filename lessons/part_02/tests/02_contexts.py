from .base import BaseTutorialLesson


class TestTutorialBasicSubcommands(BaseTutorialLesson):
    def test_00_cli_without_passed_option_doesnt_print_verbose(self):
        result = self.run_command(["hello"])
        assert result.output == "Hello!\n"
        assert result.exit_code == 0

    def test_01_cli_with_verbose_passed_in_context(self):
        result = self.run_command(["--verbose", "hello"])
        assert result.stderr == "VERBOSE is on\n"
        assert result.stdout == "Hello!\n"
        assert result.exit_code == 0

    def test_02_cli_with_verbose_passed_in_object(self):
        result = self.run_command(["--verbose", "goodbye"])
        assert result.stderr == "VERBOSE is on\n"
        assert result.stdout == "Goodbye!\n"
        assert result.exit_code == 0
