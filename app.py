from github.api import get_repos
from github.repo import Repo

class Design():
    
    RED = '\033[91m'
    BOLD = '\033[1m'
    RESET = '\033[0m'
    PURPLE = '\033[35m'
    BLACK = '\033[30m'
    BG_PURPLE = '\033[45m'

class CLI():

    def __init__(self):
        self._user_input = ""

    def start(self):
        print(f'\n{Format.RED}{Format.BOLD}Winter is Coming...{Format.RESET}\n')
        get_repos()
        self.menu()

    def menu(self):
        for idx, repo in enumerate(Repo.all, start=1):
            print(f'{idx}. {repo.name}')
        


if __name__ == '__main__':
    CLI()
