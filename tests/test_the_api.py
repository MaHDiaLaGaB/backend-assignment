from the_api_encpoints import TheApi

the_api = TheApi()


def test_register():
    payload = {
        "username": "mad@gmail.com",
        "password": "dummypass",
        "first_name": "mahdi",
        "last_name": "agb",
        "telephone": "123456",
        "profile_image": "imag",
        "address": "dumm: address",
        "city": "Paris",
        "province": "don'tknow",
        "country": "france",
    }

    res = the_api.register(payload)
    # it's working and asking for file for profile_image and real phone number
    # can be done in the endpoint by
    # with open(file_path, "rb") as file:
    #     response = requests.post(url, files={"image": file})
    assert res["message"] == "Registration successful!"
