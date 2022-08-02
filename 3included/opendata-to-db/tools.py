import requests
import os
import json
import random


# Fetching a random user agent from a saved text file to make requests to the server. There are 1000 user-agents in the text file:
class UserAgent:
    def get(self):
        with open('user-agents.txt') as f:
            agents = f.read().split("\n")
        return random.choice(agents)


# Making a custom reading api object:
class DownloadJSON:
    def __init__(self, api_url):
        self.api_url = api_url
        self.req = requests.get(self.api_url, headers={"User-Agent": UserAgent().get()})
    

    def read_JSON(self):
        try:
            read_content = json.loads(self.req.content)
            return read_content
        except requests.JSONDecodeError:
            return "Unauthorized access!"

