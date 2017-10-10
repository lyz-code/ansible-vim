# vim

Install vim, based on [this generic role](https://git.fok.systems/ansible-roles/generic_program_install)

## Requirements

`git` should be installed

## Role Variables
* `program`    : Dictionary with the information of the program
  * `name`     : Program name
  * `packages` : List of packages to install

* `config`: Dictionary with the information of the configuration
  * `directory`: Base directory to perform the clone of the configuration
    directory
  * `git_repo`: Git repository of your dotfiles. It's assumed that the
    repository has the same structure as your home directory. For example, in
    the root of my vim configuration git repository I've got a directory called
    `.vim` and a `.vimrc` file.

## Example playbook

```yaml
- hosts: all
  roles:
    - vim
```

## License

GPLv2

## Author Information
Lyz (lyz@riseup.net)
