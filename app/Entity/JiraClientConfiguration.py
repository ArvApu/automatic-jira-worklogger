class JiraClientConfiguration:
    def __init__(self, baseUrl: str, token: str):
        self.baseUrl = baseUrl
        self.token = token

    def getHeaders(self) -> dict:
        return {
            'Authorization': f'Bearer {self.token}',
            'Content-Type': 'application/json'
        }
