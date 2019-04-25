from .base import BaseTutorialLesson

class TestTutorialHelloWorld(BaseTutorialLesson):

    def test_cli_outputs_hello_message(self):
        result = self.run_command()
        assert result.output == 'Hello!\n'
             