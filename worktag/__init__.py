"""Worktag global module."""

from .cli import CLI

if __name__ == '__main__':
    cli = CLI('./config.toml')
    cli.parse_arguments()
