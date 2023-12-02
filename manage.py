#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""

    # Set the default Django settings module for the 'config' project    
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
    try:
        # Try to import the 'execute_from_command_line' function from 'django.core.management'        
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        # Handle the case where Django is not installed
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    # Execute administrative tasks from the command line using the provided arguments
    execute_from_command_line(sys.argv)

# Check if the script is being run directly
if __name__ == '__main__':
    # Call the main function to run administrative tasks
    main()
