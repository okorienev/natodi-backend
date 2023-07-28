from typer import Typer
from .commands import (
    generate_dotenv,
)

cli = Typer()
cli.add_typer(generate_dotenv, name="dotenv")


if __name__ == "__main__":
    cli()
