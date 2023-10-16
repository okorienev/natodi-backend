from typer import Typer
from .commands import (
    generate_dotenv,
    generate_token,
    authorize_user
)

cli = Typer()
cli.add_typer(generate_dotenv, name="dotenv")
cli.add_typer(generate_token, name="auth")
cli.add_typer(authorize_user, name="auth")


if __name__ == "__main__":
    cli()
