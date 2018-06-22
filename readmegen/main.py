# Copyright 2018, Development Gateway, Inc.
# This file is part of readmegen, see COPYING.

import logging, sys, os, argparse

from .readme import Readme

log = None

def _set_log_level():
    valid_levels = ['CRITICAL', 'ERROR', 'WARNING', 'INFO', 'DEBUG']
    try:
        env_level = os.environ['LOG_LEVEL']
        valid_levels.remove(env_level)
        level = getattr(logging, env_level)
    except KeyError:
        level = logging.WARNING
    except ValueError:
        msg = 'Expected log level: %s, got: %s. Using default level WARNING.' \
                % ('|'.join(valid_levels), env_level)
        print(msg, file = sys.stderr)
        level = logging.WARNING

    logging.basicConfig(level = level)
    global log
    log = logging.getLogger(__name__)

def main():
    _set_log_level()

    ap = argparse.ArgumentParser(description = 'Generate Readme for Ansible roles')
    ap.add_argument('--roledir', '-r',
            default = '.',
            help = 'Path to the role; default: current directory')
    ap.add_argument('--playbook', '-p',
            type = argparse.FileType('r'),
            help = 'A minimal playbook for this role')
    args = ap.parse_args()

    try:
        role_name = os.path.basename(os.path.realpath(args.roledir))
        log.debug('Role name is ' + role_name)
        readme = Readme(role_name)

    except Exception as e:
        if log.isEnabledFor(logging.DEBUG):
            raise RuntimeError() from e
        else:
            sys.exit(str(e))

if __name__ == '__main__':
    main()
