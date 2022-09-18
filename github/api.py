import requests 
from repo import Repo

username = "crlnvls"

URL = f"https://api.github.com/users/{username}/repos"

def get_repos():
    req = requests.get(URL)
   
    for data in req.json():
        Repo(data)
    return data
    
 
get_repos()

