class Readme:
    def __init__(self, role):
        self._role = role
        self._required = {}
        self._optional = {}

    def add_var(self, name, value, optional = False):
        if optional:
            var_list = self._optional
        else:
            var_list = self._required

        var_list[name] = value

    def __str__(self):
        pass
