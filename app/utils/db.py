from furl import furl


def prepare_connect_args(url: str) -> tuple[str, dict]:
    """
    :param url: postgres dsn
    :return: url, connect_args
    """
    parsed = furl(url)
    connect_args = {'timeout': 20}

    # Digitalocean does not allow us to specify driver for the sting
    if parsed.scheme == 'postgresql':
        parsed.scheme = 'postgresql+asyncpg'

    # https://github.com/sqlalchemy/sqlalchemy/issues/6275
    for key, value in parsed.query.params.items():
        connect_args[key] = value
    parsed.query.load('')

    return parsed.url, connect_args
