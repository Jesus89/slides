# content of hello.py
import click

@click.command()
@click.option(
    '-c',
    '--count',
    default=1,
    help='Number of Hello! messages.')
def hello(count=1):
    for x in range(count):
        click.echo('Hello!')

if __name__ == '__main__':
    hello()
