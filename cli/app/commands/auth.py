from datetime import datetime, timedelta
from jose import jwt, JWTError
from typer import Typer, Option
from app.settings import settings


def create_access_token(data: dict, expires_delta: timedelta, secret_key: str, algorithm: str) -> str:
    to_encode = data.copy()
    expire = datetime.utcnow() + expires_delta
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, secret_key,
                             algorithm=algorithm)
    return encoded_jwt


cli = Typer()


@cli.command(name="generate")
def generate_token(
    username: str = Option(..., "-u", "--username",
                           help="credentials for the token"),
    secret_key: str = Option(settings.SECRET_KEY, "-k", "--key",
                             help="secret key for token generation"),
    expire_delta: int = Option(
        settings.ACCESS_TOKEN_EXPIRE_DAYS, "-e", "--expire", help="expire time for the token (days)")
) -> str:
    access_token = create_access_token(
        data={"sub": username}, expires_delta=timedelta(days=expire_delta), secret_key=secret_key, algorithm=settings.ALGORITHM)
    token_data = {
        "credentials": username,
        "token_type": "bearer",
        "time_left_days": expire_delta,
        "access_token": access_token,
    }
    for key, value in token_data.items(): print(key, ": ", value)
    return access_token


@cli.command(name="authorize")
def authorize_user(
    username: str = Option(..., "-u", "--username",
                           help="credentials for the token"),
    token: str = Option(..., "-t", "--token",
                             help="token for authorization"),
):
    try:
        payload = jwt.decode(token, settings.SECRET_KEY,
                             algorithms=[settings.ALGORITHM])
    except JWTError as error:
        print(f"Unable to decode the token: {error}")
        return

    token_sub = payload.get("sub")
    if username != "admin" or username != token_sub:
        print("Could not validate credentials")
    else:
        print(f"User: '{username}' authorized successfully! \nToken will be active untill: {datetime.fromtimestamp(payload.get('exp'))}")
