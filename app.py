from github.repo import Repo
from github.api import get_repos, username


import requests 


class Design():
    
    RED = '\033[91m'
    BG_RED = '\033[41m'
    BOLD = '\033[1m'
    RESET = '\033[0m'
 
    

class CLI():

    def __init__(self):
        self._user_input = ""
    
    def start(self):
        username
        try:
            get_repos()
            self.all_repos()
        except:
            print(f"\n{Design.RED}Invalid username. Please try again!{Design.RESET}\n")
    

    def all_repos(self):
        for idx, repo in enumerate(Repo.all, start=1):
            print(f'{idx}. {repo.name}')
        self.get_choice()

    def get_choice(self):
        try:
            self._user_input = input(f"\n{Design.BG_RED}Which repository would you like to have more info? (type 'exit' to quit the program){Design.RESET}\n")
            if self._user_input == 'exit':
                return self.goodbye()
            if not self.valid_input(self._user_input):
                raise ValueError
            self.show_repo()
            self.get_choice()
        except ValueError:
            print(f'{Design.RED}Sorry,that is not a valid input. PLease try again{Design.RESET}\n')
            self.all_repos()

    def show_repo(self):
        repo = Repo.find_by_input(self._user_input)
        print(f'\n{Design.RED}{Design.BOLD}{repo.name}{Design.RESET}')
        print(f'\tCreated at: {repo.created}')
        print(f'\tForks: {repo.forks}')
        print(f'\tLanguage: {repo.language}')

    @staticmethod
    def valid_input(i):
        return int(i) > 0 and int(i) <= len(Repo.all)

    @staticmethod
    def goodbye():
        print(f"\n{Design.BG_RED}Sorry to see you go!{Design.RESET}\n")

        


if __name__ == '__main__':
    CLI().start()
