import os
import pytest
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_vim_is_installed(host):
    p = host.package("neovim")
    assert p.is_installed


@pytest.mark.parametrize("files", [
    ('.test_programrc'),
    ('skeleton.md'),
    ('filetype.vim'),
    ('spellfile.add')
])
def test_vimrc_is_symlink(host, files):
    f = host.file('/root/{}'.format(files))
    assert f.exists
    assert f.is_symlink


def test_config_file(host, files):
    f = host.file('/root/.rcfiles/vim/{}'.format(files))
    assert f.exists
    assert f.contains('Making Gentooza life easy')


def test_if_neovim_pip_package_is_installed(host):
    # pip_packages = host.pip_package.get_packages(pip_path=)
    pip_packages = host.pip_package.get_packages(pip_path='/usr/bin/pip3')
    assert 'neovim' in pip_packages


@pytest.mark.parametrize("nvim_ln_src, nvim_ln_dest", [
    ('.vim', '.config/nvim'),
    ('.vimrc', '.config/nvim/init.vim')
])
def test_neovim_required_symlinks(host, nvim_ln_src, nvim_ln_dest):
    ln_dest = host.file(nvim_ln_src).linked_to
    assert ln_dest is nvim_ln_dest


@pytest.mark.parametrize("vim_modules", [
    ('vim-colors-solarized'),
    ('vim-fugitive')
])
def test_if_there_are_some_modules_installed(host, vim_modules):
    f = host.file('/root/.vim/bundle/{}'.format(vim_modules))
    assert f.exists
