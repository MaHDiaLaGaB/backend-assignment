import requests
from routes import REFRESH, REGISTER, ARTICLE, PROFILE, TOKEN, GET_ARTICLE
from typing import Dict

from schema import User, UserBase


class TheApi:
    def __init__(self):
        self.base_url = "http://13.212.226.116:8000/api/"
        self.access_token = None

    def register(self, user_info: User) -> Dict:
        url = self.base_url + REGISTER
        response = requests.post(url, json=user_info)
        print(response.status_code)
        print(response.json())
        if response.status_code == 200:
            return {"message": "successful"}
        else:
            return {"message": "failed"}

    def authenticate(self, payload: UserBase):
        url = self.base_url + TOKEN
        response = requests.post(url, json=payload)
        if response.status_code == 200:
            self.access_token = response.json()["access"]
            return {"token": self.access_token}
        else:
            return {"message": "failed"}

    def profile(self):
        url = self.base_url + PROFILE
        headers = {"Authorization": "Bearer " + self.access_token}
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return {
                "username": response.json()["username"],
                "email": response.json()["email"],
            }
        else:
            return {"message": "failed"}

    def articles(self):
        url = self.base_url + ARTICLE
        headers = {"Authorization": "Bearer " + self.access_token}
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return {"articles": response.json()}
        else:
            return {"message": "failed"}

    def get_article(self, article_id: int) -> dict:
        headers = {
            "Authorization": f"Bearer {self.access_token}",
            "Content-Type": "application/json"
        }
        response = requests.get(GET_ARTICLE.format(article_id), headers=headers)
        if response.status_code == 200:
            article = response.json()
            return article
        else:
            return {"message": "failed"}

    def refresh_token(self):
        url = self.base_url + REFRESH
        payload = {"refresh": self.access_token}
        response = requests.post(url, json=payload)
        if response.status_code == 200:
            self.access_token = response.json()["access"]
            return {"new_token": self.access_token}
        else:
            return {"message": "failed"}
