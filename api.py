from fastapi import FastAPI, Depends, HTTPException, Body, status, Query
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from the_api_encpoints import TheApi
from schema import User, UserBase
from utils import verify_jwt_token


app = FastAPI()
security = HTTPBearer()


@app.post("/refresh_token")
async def refresh_token(
    the_api: TheApi = Depends(),
):
    new_access_token = the_api.access_token()
    new_jwt_token = "TSTMY " + new_access_token
    return {"new_token": new_jwt_token}


@app.post("/register")
async def register(payload: User = Body(), the_api: TheApi = Depends()):
    the_api.register(user_info=payload)
    return {"message": "Registration successful!"}


@app.post("/authenticate")
async def authenticate(user: UserBase = Body(), the_api: TheApi = Depends()):
    access_token = the_api.authenticate(user)
    jwt_token = "TSTMY " + access_token
    return {"token": jwt_token}


@app.get("/profile")
async def profile(
    credentials: HTTPAuthorizationCredentials = Depends(security),
    the_api: TheApi = Depends(),
) -> UserBase:
    if not verify_jwt_token(credentials.credentials):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    res = the_api.profile()
    return res


@app.get("/articles/{id}")
async def get_article_endpoint(
    _id: int = Query(),
    the_api: TheApi = Depends()
):
    article = the_api.get_article(article_id=_id)
    return article
