from pydantic import BaseModel


class User(BaseModel):
    username: str
    password: str
    first_name: str
    last_name: str
    telephone: str
    profile_image: str
    address: str
    city: str
    province: str
    country: str


class UserBase(BaseModel):
    username: str
    password: str
