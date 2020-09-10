import click
from src._test_ import *
from src._01_ import *

@click.group()
def cli():
    pass

cli.add_command(lower)

if __name__ == "__main__":
    cli()