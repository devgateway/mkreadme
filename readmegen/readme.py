import logging
from io import SEEK_SET

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
        yaml_file = open(path, 'rb')
        defaults = yaml.load(yaml_file)
        for name, value in defaults.items():
            self.add_var(name, value, optional = True)
        yaml_file.close()

    def read_playbook(self, playbook_file):
        log.debug('Reading playbook from "{}"'.format(playbook_file.name))
        self._playbook = playbook_file.read()

        playbook_file.seek(0, SEEK_SET)
        playbook = yaml.load(playbook_file)
        playbook_file.close()
        for play in playbook:
            task_number = 0
            for task in play['tasks']:
                try:
                    task_desc = '"{}"'.format(task['name'])
                except KeyError:
                    task_desc = '#' + str(task_number)
                log.debug('Examining task ' + task_desc)

                for module in ['import_role', 'include_role']:
                    if module in task and task[module]['name'] == self._role:
                        log.debug('Found {}: {}'.format(module, self._role))
                        try:
                            for name, value in task['vars'].items():
                                if name in self._optional:
                                    msg = 'Skipping {} because it\'s optional'
                                    log.info(msg.format(name))
                                else:
                                    self.add_var(name, value, optional = False)
                            break
                        except KeyError:
                            msg = 'No vars defined for {} in task {}'
                            log.info(msg.format(module, task_desc))

                task_number = task_number + 1
