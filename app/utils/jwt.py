from typing import Dict

import jwt

from app.config import config
from app.exceptions import InvalidAuthorizationError, MissingAuthorizationError


def create_access_token(payload: Dict, key=config.SECRET_KEY) -> str:
    if type(payload) == dict:
        return jwt.encode(payload=payload, key=key, algorithm="HS256")

    raise TypeError("Payload must be a dictionary")


def get_jwt_token(auth_header) -> str:
    if not auth_header:
        raise MissingAuthorizationError("Authorization header not found")

    auth_header_split = auth_header.split(" ")

    if not auth_header.startswith("Bearer ") or len(auth_header_split) != 2:
        raise InvalidAuthorizationError("Authorization header should be a valid jwt token.")

    return auth_header_split[1]


def get_jwt_payload(token: str) -> Dict:
    try:
        return jwt.decode(token, config.SECRET_KEY, algorithms=["HS256"])
    except jwt.DecodeError as e:
        raise e
