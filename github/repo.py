class Repo():
    all = []

    def __init__(self, data):
        self._name = data["name"]
        self._created = data["created_at"]
        self._forks = data["forks"]
        self._language = data["language"]
        self._save()

    def _save(self):
        self.all.append(self)

    @property
    def name(self):
        return self._name
    
    @property
    def created(self):
        return self._created

    @property
    def forks(self):
        return self._forks

    @property
    def language(self):
        return self._language
    
    @classmethod
    def find_by_input(cls, user_input):
        return cls.all[int(user_input)-1]



