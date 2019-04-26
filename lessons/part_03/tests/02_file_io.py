from .base import BaseTutorialLesson


class TestFileTypes(BaseTutorialLesson):
    def test_00_cli_reads_input_file(self):
        with self.runner.isolated_filesystem():
            with open("infile.txt", "w") as f:
                f.write("Input data.")
            result = self.run_command(["infile.txt"])
            assert "Input data." in result.output

    def test_01_cli_writes_output_file(self):
        with self.runner.isolated_filesystem():
            with open("infile.txt", "w") as f:
                f.write("Input data.")
            result = self.run_command(["infile.txt", "outfile.txt"])
            with open("outfile.txt", "r") as f:
                data = f.read()
            assert data == "Input data."
            assert "Input data." not in result.output

    def test_02_cli_reads_stdin_writes_output_file(self):
        with self.runner.isolated_filesystem():
            result = self.run_command(["-", "outfile.txt"], input="Input data.")
            with open("outfile.txt", "r") as f:
                data = f.read()
            assert data == "Input data."
            assert "Input data." not in result.output

    def test_03_cli_writes_length_to_stderr(self):
        with self.runner.isolated_filesystem():
            result = self.run_command(["-", "outfile.txt"], input="Input data.")
            assert "Input data." not in result.output
            assert "Input length: 11" in result.stderr
