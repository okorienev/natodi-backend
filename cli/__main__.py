from typer import Typer
from .commands import (
    dotenv_cli,
    auth_cli
)

cli = Typer()
cli.add_typer(dotenv_cli, name="dotenv")
cli.add_typer(auth_cli, name="auth")


if __name__ == "__main__":
    cli()
