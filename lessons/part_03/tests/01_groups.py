from .base import BaseTutorialLesson


class TestTutorialBasicSubcommands(BaseTutorialLesson):
    def test_00_cli_without_command_prints_usage(self):
        result = self.run_command()
        assert result.output.startswith("Usage: cli [OPTIONS] COMMAND [ARGS]...")
        assert result.exit_code == 0

    def test_01_cli_with_hello_command(self):
        result = self.run_command(["hello"])
        assert result.output == "Hello!\n"
        assert result.exit_code == 0

    def test_02_cli_wth_invalid_command(self):
        result = self.run_command(["invalid-subcommand"])
        assert 'Error: No such command "invalid-subcommand".' in result.stderr
        assert result.exit_code == 2
