import logging

import PyYAML

log = logging.getLogger(__name__)

class Readme:
    def __init__(self, role):
        log.debug('Role name is ' + role)
        self._role = role
        self._required = {}
        self._optional = {}

    def add_var(self, name, value, optional = False):
        if optional:
            var_list = self._optional
            var_kind = 'optional'
        else:
            var_list = self._required
            var_kind = 'required'

        log.debug('Add {} variable {}'.format(var_kind, name))
        var_list[name] = value

    def __str__(self):
        pass

    def read_defaults(self, path):
        log.debug('Reading defaults from "{}"'.format(path))
        try:
            pass
        except Exception as e:
            log.error(str(e))

    def read_playbook(self, path):
        log.debug('Reading playbook from "{}"'.format(path))
        try:
            pass
        except Exception as e:
            log.error(str(e))
