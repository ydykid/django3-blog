#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django3_test.settings.production')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)

    current_path = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(current_path)
    sys.path.append(os.path.join(current_path, "django3_test"))
    sys.path.append(os.path.join(current_path, "apps"))
    sys.path.append(os.path.join(current_path, "apps_extra"))


if __name__ == '__main__':
    main()
