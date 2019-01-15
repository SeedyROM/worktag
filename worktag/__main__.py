"""CLI entrypoint."""
from .cli import CLI

if __name__ == '__main__':
    cli = CLI(config_path='./config.toml')
    cli.parse_arguments()
