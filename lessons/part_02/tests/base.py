from click.testing import CliRunner

from lessons.part_03.cli import cli


class BaseTutorialLesson:
    def setup(self):
        self.runner = CliRunner(mix_stderr=False)
        self.command = cli

    def run_command(self, arguments=None, **kwargs):
        result = self.runner.invoke(self.command, arguments, **kwargs)
        return result
