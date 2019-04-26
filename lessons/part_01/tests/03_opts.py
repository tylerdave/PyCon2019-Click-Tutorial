#!/usr/bin/env python
from .base import BaseTutorialLesson


class TestTutorialBasicOptions(BaseTutorialLesson):
    def test_00_greeting_option(self):
        result = self.run_command(["--greeting", "Ahoy", "Tutorial"])
        assert result.output == "Ahoy, Tutorial!\n"

    def test_01_greeting_short_option(self):
        result = self.run_command(["-g", "Ahoy", "Tutorial"])
        assert result.output == "Ahoy, Tutorial!\n"

    def test_02_greeting_default(self):
        result = self.run_command(["Tutorial"])
        assert result.output == "Hello, Tutorial!\n"

    def test_03_question_option(self):
        result = self.run_command(["--question", "Tutorial"])
        assert result.output == "Hello, Tutorial?\n"

    def test_04_no_question_option(self):
        result = self.run_command(["--no-question", "Tutorial"])
        assert result.output == "Hello, Tutorial!\n"
