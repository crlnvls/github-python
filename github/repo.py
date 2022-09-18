class Repo():
    all = []

    def __init__(self, data):
        self._name = data["name"]
        self._save()

    def _save(self):
        self.all.append(self)

    @property
    def name(self):
        return self._name
      



