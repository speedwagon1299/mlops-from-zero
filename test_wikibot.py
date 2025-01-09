from mylib.bot import scrape
from click.testing import CliRunner
from wikibot import cli

def test_scrape():
    assert "Microsoft" in scrape("Microsoft")    

def test_cli():
  runner = CliRunner()
  result = runner.invoke(cli, ['--name','Microsoft','--length','1'])
  assert result.exit_code == 0
  assert 'Microsoft' in result.output