"""CLI entrypoint."""
from .cli import CLI


def main():
    """Start the CLI."""
    cli = CLI(config_path='./config.toml')
    cli.parse_arguments()
