#!/usr/bin/env python
from .base import BaseTutorialLesson

class TestTutorialBasicOptions(BaseTutorialLesson):

    def test_00_cli_with_single_option(self):
        result = self.run_command(['--single', 'single-value'])
        assert result.output.startswith('single: single-value\n')

    def test_01_cli_with_single_short_option(self):
        result = self.run_command(['-s', 'single-value'])
        assert result.output.startswith('single: single-value\n')

    def test_02_cli_with_single_option_not_passed(self):
        result = self.run_command()
        assert result.output.startswith('single: None\n')

    def test_03_cli_with_multiple_value_options(self):
        result = self.run_command(['--multi', 'first-value', '--multi', 'second-value'])
        assert 'multi: first-value\nmulti: second-value' in result.output

    def test_04_cli_with_flag_on(self):
        result = self.run_command(['--enable-feature'])
        assert 'enable_feature: True\n' in result.output

    def test_05_cli_with_flag_off(self):
        result = self.run_command(['--no-enable-feature'])
        assert 'enable_feature: False\n' in result.output

    def test_06_cli_with_flag_not_passed(self):
        result = self.run_command()
        assert 'enable_feature: False\n' in result.output

    def test_07_cli_with_explicit_flag(self):
        result = self.run_command(['--flag'])
        assert 'flag: True' in result.output

    def test_08_cli_with_explicit_flag_not_passed(self):
        result = self.run_command()
        assert 'flag: False' in result.output

    def test_09_cli_with_counting_option_not_passed(self):
        result = self.run_command()
        assert 'verbose: 0' in result.output

    def test_10_cli_with_counting_option_passed_many_times(self):
        result = self.run_command(['-vvvv', '-v', '--verbose'])
        assert 'verbose: 6' in result.output
