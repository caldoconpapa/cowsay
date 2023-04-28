from cow import Cow

class FileCow:
    def __init__(self, name, filename):
        Cow.__init__(self, name)
        self.filename = filename


