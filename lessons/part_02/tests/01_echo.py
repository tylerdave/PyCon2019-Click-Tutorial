from .base import BaseTutorialLesson


class TestTutorialEchoAndStyle(BaseTutorialLesson):
    def test_00_cli_echo_to_stdout(self):
        result = self.run_command()
        assert "Hello!" in result.stdout

    def test_01_cli_echo_to_stderr(self):
        result = self.run_command()
        assert "Printing..." in result.stderr

    def test_02_cli_secho_with_red_option(self):
        result = self.run_command(["--red"], color=True)
        assert result.output == "\x1b[31mHello!\x1b[0m\n"
