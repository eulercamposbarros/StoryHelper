#!/usr/bin/env python
"""
Command-line utility for administrative tasks.
"""

import os, sys, dotenv

if __name__ == "__main__":
    dotenv.read_dotenv()

    os.environ.setdefault(
        "DJANGO_SETTINGS_MODULE",
        "StoryHelper.settings"
    )

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
