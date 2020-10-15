import click
from oscli.config import Config
from oscli.auth import fetch_token
from oscli.metadata import file_hash
from oscli.find import find
from oscli.download import download


@click.group(invoke_without_command=False)
# @click.pass_context
def cli():
    pass
    # TODO: oscli . 
    # TODO: logging verbosity
    # if ctx.invoked_subcommand is None:
    #     pass


@cli.command()
@click.option('--username', prompt=True)
@click.option('--password', prompt=True, hide_input=True,
              confirmation_prompt=False)  # TODO: change to true after encrypt
def login(username, password):
    # TODO: prompt for username & password only if not present in config file
    # TODO: fail more friendly if failed to login
    cfg = Config()
    cfg.update_username(username)
    cfg.update_password(password)
    cfg.update_token(
        fetch_token(username,password)
    )
    cfg.save()


@cli.command()
@click.argument('title', type=click.STRING) #=click.Path(exists=True))
@click.option('--verbose', default=False)
def find_movie(title, verbose):
    # TODO: sometimes API returns subtitles for movies with similar name, but not exactly the one one's looking for. This is tricky, because it's supposed to return similarly named subtitles. Is there a way to filter out junk from response?
    import json
    response = json.loads(find(title).text)
    for subtitle in response['data']:
        print('file_id file_name')
        for subtitle_file in subtitle['attributes']['files']:
            print(f"{subtitle_file['file_id']} {subtitle_file['file_name']}")
        print('')
    print("use the 1st number to download subtitle file, for example 'oscli download 12345")
    if(verbose):
        print('Full response:')
        print(json.dumps(response, sort_keys=True, indent=2))


@cli.command()
@click.argument('file_id', type=click.INT)
@click.argument('file_name', type=click.STRING)
def download_subtitle(file_id, file_name):
    download(file_id, file_name)
