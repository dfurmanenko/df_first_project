import requests


class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class APIUtils(metaclass=Singleton):
    def __init__(self):
        self.requests = requests.Session()
        self.host = "https://api.meteonomiqs.com"
        self.user_id = "rlknl9m9vxwh91p4"
        self.headers = {
            "X-Application-TZ": "UTC",
            "X-BLOBR-KEY": "sCLMcPen12uk6iTKCz3EEhT7wUMSxuZc"
        }

    def make_request(self, url, method="GET", headers=None, body=None):
        print(f"Request to {url} with {method}, headers: {headers}")
        if method =="GET":
            self.requests.get(url=url, headers=headers)
        if method =="POST":
            self.requests.post(url=url, headers=headers)

    def get_weather(self, latitude, longitude, expected_code=200, headers=None):
        url = f"{self.host}/{self.user_id}/hood/weather/{latitude}/{longitude}/"
        response = self.requests.get(url=url, headers=self.headers)
        assert response.status_code == expected_code, f"Actual response code: {response.status_code} doesn't match with expected: {expected_code}"
        response_content = response.json()
        return response_content
