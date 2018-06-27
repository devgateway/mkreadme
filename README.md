# mkreadme

Generate Readme boilerplate from Ansible roles.

## Synopsis

`mkreadme` `[ -h ]` `[ --roledir` `| -r ROLEDIR ]` `[ --playbook` `| -p PLAYBOOK ]`

## Description

**mkreadme** is a utility that reads default variables from a role and optionally a
minimal example playbook, and produces a boilerplate `README.md` file.

## Options

*   **`-h`**, **`--help`**

    Show usage information, and exit.

*   **`--roledir`** *`ROLEDIR`*, **`-r`** *`ROLEDIR`*

    The role directory, which contains `defaults/main.yml` file. The role name is deduced from the
    base name (real) of this directory.

    Default is current directory.

*   **`--playbook`** *`PLAYBOOK`*, **`-p`** *`PLAYBOOK`*

    A minimal playbook invoking this role using `include_role` or `import_role`, possibly providing
    some `vars`.

## Exit Status

Returns zero on success.

## Environment

### `LOG_LEVEL`

Sets verbosity of logging sent to standard error. Recognized levels are:

* `CRITICAL`
* `ERROR`
* `WARNING` (default)
* `INFO`
* `DEBUG`

## Files

*   `$XDG_CONFIG_HOME/mkreadme.yml`, `~/.config/mkreadme.yml`

    YAML file with default settings. Currently, two fields are recognized:

    *   **author**: copyright holder for the playbook.
    *   **license**: the license under which the playbook is distributed.

## Conforming to

[XDG Base Directory
Specification](https://specifications.freedesktop.org/basedir-spec/basedir-spec-0.6.html)

## See Also

**markdown**(1), **ansible**(1)
