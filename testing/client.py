import requests


class Client:
    def __init__(self, base_url, username=None, password=None):
        self.base_url = base_url
        self.token = self._get_token(username, password) if username and password else None

    def _get_token(self, username, password):
        response = requests.post(f"{self.base_url}/token/", data={"username": username, "password": password})
        response.raise_for_status()
        return response.json()["access"]

    def _get_headers(self):
        headers = {}
        if self.token:
            headers["Authorization"] = f"Bearer {self.token}"
        return headers

    def get(self, path, **kwargs):
        return requests.get(f"{self.base_url}{path}", headers=self._get_headers(), **kwargs)

    def post(self, path, data, **kwargs):
        return requests.post(f"{self.base_url}{path}", headers=self._get_headers(), json=data, **kwargs)

    def put(self, path, data, **kwargs):
        return requests.put(f"{self.base_url}{path}", headers=self._get_headers(), json=data, **kwargs)

    def delete(self, path, **kwargs):
        return requests.delete(f"{self.base_url}{path}", headers=self._get_headers(), **kwargs)
