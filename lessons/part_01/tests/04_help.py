#!/usr/bin/env python
import re

from .base import BaseTutorialLesson


class TestTutorialBasicUsageDocumentation(BaseTutorialLesson):
    def test_00_cli_gets_help_output_from_docstring(self):
        result = self.run_command(["--help"])
        assert result.output.startswith("Usage: greet")
        assert "Displays a greeting." in result.output

    def test_01_cli_includes_help_text_from_option(self):
        result = self.run_command(["--help"])
        assert re.search(
            r"--question / --no-question\W+Make the greeting a question\.",
            result.output,
        )

    def test_03_cli_with_subcommand_shows_short_help(self):
        result = self.run_command(["--help"])
        assert re.search(
            r"-g, --greeting TEXT\W+The greeting to display.", result.output
        )
