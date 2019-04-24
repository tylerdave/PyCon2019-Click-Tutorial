from click.testing import CliRunner

from lessons.part_01.cli import cli


class BaseTutorialLesson:

    def setup(self):
        self.runner = CliRunner()
        self.command = cli

    def run_command(self, arguments=None, **kwargs):
        result = self.runner.invoke(self.command, arguments, **kwargs)
        return result
