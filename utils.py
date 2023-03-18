import jwt
from jwt.exceptions import InvalidKeyTypeError


# i didn't test it and i know it's not working
def verify_jwt_token(token: str) -> bool:
    try:
        payload = jwt.JWT.decode(token, message="")
        if payload["sub"] == "user_id":
            return True
        return False
    except InvalidKeyTypeError:
        return False
