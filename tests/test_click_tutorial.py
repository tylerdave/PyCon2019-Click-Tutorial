#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `click_tutorial` package."""

import pytest

from click.testing import CliRunner

from click_tutorial import cli


def test_cli_with_no_arguments():
    """Test the CLI."""
    runner = CliRunner()
    result = runner.invoke(cli.tutorial)
    assert result.exit_code == 0
    assert "Click tutorial runner." in result.output


def test_cli_help():
    runner = CliRunner()
    help_result = runner.invoke(cli.tutorial, ["--help"])
    assert help_result.exit_code == 0
    assert "--help  Show this message and exit." in help_result.output
