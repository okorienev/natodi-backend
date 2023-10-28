from furl import furl

# https://github.com/MagicStack/asyncpg/issues/737#issuecomment-861005508
PARAM_OVERWRITE = {
    'sslmode': 'ssl'
}


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

    for key, value in parsed.query.params.items():
        connect_args[PARAM_OVERWRITE.get(key, key)] = value
    parsed.query.load('')

    return parsed.url, connect_args
