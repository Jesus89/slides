import click

@click.command()
@click.option('--count', default=1, help='Number of Hello! messages.')
def hello(count):
    for x in range(count):
        click.echo('Hello!')

if __name__ == '__main__':
    hello()
