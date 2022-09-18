import requests 
from .repo import Repo


class Color():
    
    RESET = '\033[0m'
    BG_RED = '\033[41m'  


username = input(f"\n{Color.BG_RED}What is your github username?{Color.RESET}\n")
           

URL = f"https://api.github.com/users/{username}/repos"

def get_repos():
    try:
        req = requests.get(URL)
        for data in req.json():
            Repo(data)
        return data
    except:
         print(f"\n{Color.BG_RED}Invalid user name. Please try again!{Color.RESET}\n")
        


