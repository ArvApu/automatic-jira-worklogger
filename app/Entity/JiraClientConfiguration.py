from base64 import b64encode

class JiraClientConfiguration:
    def __init__(self, baseUrl: str, username: str, token: str):
        self.baseUrl = baseUrl
        self.username = username
        self.token = token

    def getHeaders(self) -> dict:
        token = b64encode(f"{self.username}:{self.token}".encode('utf-8')).decode("ascii")

        return {
            'Authorization': f'Basic {token}',
            'Content-Type': 'application/json',
            'Accept': 'application/json',
        }
