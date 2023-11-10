from typer import Typer, Option
from yaml import safe_load

cli = Typer()

@cli.command(name='generate')
def generate_dotenv(
    source_file: str = Option('settings.yaml', '-s', '--source-file', help='.yaml to read settings from'),
    output_file: str = Option('.env', '-o', '--output-file', help='file to write env to'),
    environment: str = Option('local', '-e', '--environment', help='environment to write to dotenv'),
):
    with open(source_file) as fd:
        data = safe_load(fd)

    env = data["environments"][environment]

    with open(output_file, 'w') as fd:
        for key, value in env.items():
            fd.write(f"{key.upper()}={value}\n")


if __name__ == "__main__":
    cli()

