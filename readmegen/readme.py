import logging

import yaml
try:
    from yaml import CLoader as Loader
except ImportError:
    from yaml import Loader

log = logging.getLogger(__name__)

class Readme:
    def __init__(self, role):
        log.debug('Role name is ' + role)
        self._role = role
        self._required = {}
        self._optional = {}
        self._playbook = None

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
        return 'Not implemented yet'

    def read_defaults(self, path):
        log.debug('Reading defaults from "{}"'.format(path))
        try:
            pass
        except Exception as e:
            log.error(str(e))

    def read_playbook(self, playbook_file):
        log.debug('Reading playbook from "{}"'.format(playbook_file.name))
        try:
            self._playbook = playbook_file.read()
            playbook_file.close()
        except Exception as e:
            log.error(str(e))
