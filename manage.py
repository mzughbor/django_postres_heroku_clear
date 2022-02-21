#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import time


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'telegramBot.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)
    # time.sleep(1700)


    # scriptpath = ""
    # Add the directory containing your module to the Python path (wants absolute paths)
    # sys.path.append(os.path.abspath(scriptpath))

    # Do the import
    # import main_02

# while True:
if __name__ == '__main__':
    main()
