from utils.attck import import_attck
from utils.techniques import import_techniques
from utils.products import import_products
from utils.sigma import import_sigma
import typer
import asyncio

app = typer.Typer()

@app.command()
def attck(api_url: str, access_token: str = typer.Option(
    ..., prompt=True, hide_input=True, envvar="RT_TOKEN"),
    cti_url: str = typer.Option('https://raw.githubusercontent.com/mitre/cti/master/enterprise-attack/enterprise-attack.json'),
    magma_path: str = typer.Option('./mitre/magma_mapping.json')):
    """
    Attaches an access token.

    Args:
        api_url: (str): write your description
        access_token: (str): write your description
        typer: (todo): write your description
        Option: (todo): write your description
        prompt: (todo): write your description
        hide_input: (str): write your description
        envvar: (todo): write your description
        cti_url: (str): write your description
        typer: (todo): write your description
        Option: (todo): write your description
        magma_path: (str): write your description
        typer: (todo): write your description
        Option: (todo): write your description
    """
    typer.echo(f'Started import of ATTCK CTI')
    asyncio.run(import_attck(api_url=api_url, cti_url=cti_url, magma_path=magma_path, access_token=access_token))
    typer.echo(f'Finished import of ATTCK CTI')

@app.command()
def products(api_url: str, path: str = typer.Option('./mitre/datasource_mapping.json'),
    access_token: str = typer.Option(..., prompt=True, hide_input=True, envvar="RT_TOKEN")):
    """
    Get access token files.

    Args:
        api_url: (str): write your description
        path: (str): write your description
        typer: (todo): write your description
        Option: (todo): write your description
        access_token: (str): write your description
        typer: (todo): write your description
        Option: (todo): write your description
        prompt: (todo): write your description
        hide_input: (str): write your description
        envvar: (todo): write your description
    """
    typer.echo(f'Started import of products and datasource mapping')
    asyncio.run(import_products(api_url=api_url, path=path, access_token=access_token))
    typer.echo(f'Finished import of products and datasource mapping')

@app.command()
def sigma(api_url: str, path: str = typer.Option('./mitre/validations'),
    access_token: str = typer.Option(..., prompt=True, hide_input=True, envvar="RT_TOKEN")):
    """
    R sigma environment.

    Args:
        api_url: (str): write your description
        path: (str): write your description
        typer: (todo): write your description
        Option: (todo): write your description
        access_token: (str): write your description
        typer: (todo): write your description
        Option: (todo): write your description
        prompt: (todo): write your description
        hide_input: (str): write your description
        envvar: (todo): write your description
    """
    typer.echo(f'Started import of SIGMA rules')
    asyncio.run(import_sigma(api_url=api_url, path=path, access_token=access_token))
    typer.echo(f'Finished import of SIGMA rules')

@app.command()
def techniques(api_url: str, path: str = typer.Option('./mitre/techniques'),
    access_token: str = typer.Option(..., prompt=True, hide_input=True, envvar="RT_TOKEN")):
    """
    Takes an api call.

    Args:
        api_url: (str): write your description
        path: (str): write your description
        typer: (todo): write your description
        Option: (todo): write your description
        access_token: (str): write your description
        typer: (todo): write your description
        Option: (todo): write your description
        prompt: (array): write your description
        hide_input: (str): write your description
        envvar: (array): write your description
    """
    typer.echo(f'Started import of mapped techniques rules')
    asyncio.run(import_techniques(api_url=api_url, path=path, access_token=access_token))
    typer.echo(f'Finished import of mapped techniques rules')

if __name__ == "__main__":
    app()