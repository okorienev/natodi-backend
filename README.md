# Natodi mobile app back-end application

## System requirements
- linux-based OS (or Windows + WSL)
- [docker](https://docs.docker.com/engine/install/) + [docker-compose](https://docs.docker.com/compose/install/)

## How to run project for the first time:

### Install required system dependencies
```shell
sudo apt update
sudo apt install \
    build-essential \
    curl \
    libbz2-dev \
    libffi-dev \
    liblzma-dev \
    libncursesw5-dev \
    libreadline-dev \
    libsqlite3-dev \
    libssl-dev \
    libxml2-dev \
    libxmlsec1-dev \
    llvm \
    make \
    tk-dev \
    wget \
    xz-utils \
    zlib1g-dev
```

### Install pyenv [Pyenv](https://github.com/pyenv/pyenv#getting-pyenv)
```shell
curl https://pyenv.run | bash
```

Add these lines to your ~/.bashrc, reload your shell
```shell
export PYENV_ROOT="$HOME/.pyenv"
command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init -)"
```

Run `pyenv version`, it should be the same as in `.python-version` file in repository root

Run `pyenv install`

### Install poetry [Poetry](https://python-poetry.org/docs/#installation):
```shell
  curl -sSL https://install.python-poetry.org | python3 -
```

Add this line to your ~/.bashrc, reload your shell
```shell
export PATH="$HOME/local/bin:$PATH"
```

Check that everything is ok with `poetry --version`

### Install lets [lets](https://lets-cli.org/docs/installation)
```shell
curl --proto '=https' --tlsv1.2 -sSf https://lets-cli.org/install.sh | sh -s -- -b ~/bin
```

Add this line to your ~/.bashrc, reload your shell
```shell
export PATH=$PATH:$HOME/bin
```

Check that everything is ok with `lets --version`

### Run:
```shell
lets run
```

## Commands (check `lets --help` for full list of commands)

- `lets run` to run project
- `lets migrate-generate -m <revision_name>` to create new db migration
- `lets generate-token` to create a token for access you can also add `-k <secret key (256bit)>` to provide non-default key for token encription, and `-e <expire time (days)>` for specific token duration (7 days by default)
- `lets check-auth -t <token>` to check the token activity
- `lets lint` to run linter & formatter
