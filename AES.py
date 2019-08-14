import json
import requests


class AES:
    def __init__(self):
        self.url = "https://cyvax.tk/api/dwebhooks/AES.php"

    def encrypt(self, rdata, discord_username):
        data = {
            "type": "encrypt",
            "username": discord_username,
            "data": json.dumps(rdata)
        }
        req = requests.post(self.url, data=json.dumps(data))
        return req.content.decode("utf-8")

    def send_issues(self, data, discord_username):
        encrypt = self.encrypt(data, discord_username)
        print(encrypt)
