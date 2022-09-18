from github.repo import Repo
from github.api import get_repos, username

import requests 


class Design():
    
    RED = '\033[91m'
    BOLD = '\033[1m'
    RESET = '\033[0m'
 
    

class CLI():

    def __init__(self):
        self._user_input = ""
    
    def start(self):
        username
        get_repos()
        self.all_repos()
    

    def all_repos(self):
        for idx, repo in enumerate(Repo.all, start=1):
            print(f'{idx}. {repo.name}')
        self.get_choice()

    def get_choice(self):
        try:
            self._user_input = input(f"\n{Design.RED}{Design.BOLD}Invalid user name. Please try again!{Design.RESET}\n")
            if self._user_input == 'exit':
                return self.goodbye()
            if not self.valid_input(self._user_input):
                raise ValueError
            self.show_house()
            self.get_user_choice()
        except ValueError:
            print(f'{Format.RED}Sorry,that is not a valid input.{Format.CLEAR}\n')
            self.menu()

    def show_house(self):
        house = House.find_by_input(self._user_input)
        print(f'\n{Format.BLUE}{Format.BOLD}{house.name}{Format.CLEAR}')
        print(f'\tRegion: {house.region}')
        print(f'\tInsignia: {house.insignia}')

    @staticmethod
    def valid_input(i):
        return int(i) > 0 and int(i) <= len(Repo.all)

    @staticmethod
    def goodbye():
        print(f"\n{Design.RED}{Design.BOLD}Sorry to see you go!{Design.RESET}\n")

        


if __name__ == '__main__':
    CLI().start()
