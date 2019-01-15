"""The CLI interface module."""
from docopt import docopt

from .usage import __doc__ as WORKTAG_DOCOPT


class CLI:
    """Class to handle CLI interactions."""

    def __init__(self, config_path):
        """Initialize the CLI interface."""
        self.config_path = config_path
        print(config_path)

    def parse_arguments(self):
        """Use docopt to parse command line arguments."""
        self.argument_parser = docopt(WORKTAG_DOCOPT, version='worktag 0.0.1')
