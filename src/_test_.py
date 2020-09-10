#TEST RUN
import click

@click.group()
def cli():
    pass

@cli.command(name = "lowercase")
@click.argument("value", type = click.STRING)
def lower(value):
    print(value.lower())


if __name__ == "__main__":
    cli()