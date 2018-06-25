import logging
from io import SEEK_SET
from datetime import date

import yaml
try:
    from yaml import CLoader as Loader
except ImportError:
    from yaml import Loader
import jinja2

log = logging.getLogger(__name__)

class Readme:
    def __init__(self, role, author = None, license = None):
        log.debug('Role name is ' + role)
        self._role = role
        self._required = {}
        self._optional = {}
        self._playbook = None
        self._author = author
        self._license = license

    def add_var(self, name, value, optional = False):
        if optional:
            var_list = self._optional
            var_kind = 'optional'
        else:
            var_list = self._required
            var_kind = 'required'

        log.debug('Adding {} variable {}'.format(var_kind, name))
        var_list[name] = value

    def __str__(self):
        loader = jinja2.PackageLoader(__name__, '.')
        env = jinja2.Environment(
            loader = loader,
            autoescape = False,
            trim_blocks = True
        )
        template = env.get_template('readme.j2')
        today = date.today()
        content = template.render(
            role = self._role,
            required_vars = self._required,
            optional_vars = self._optional,
            playbook = self._playbook,
            license = self._license,
            year = today.year,
            author = self._author
        )

        return content

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
