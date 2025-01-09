from mylib.bot import scrape
import click

@click.command()
@click.option('--name', prompt='Wikipedia Page to Scrape', help='Web page we want to scrape')
@click.option('--length', prompt='Number of lines', help='Length of summary')
def cli(name='Microsoft', length=1):
    result = scrape(name, length=length)
    click.echo(click.style(f'{result}', fg="cyan"))

if __name__ == '__main__':
    cli()