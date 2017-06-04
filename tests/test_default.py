from testinfra.utils.ansible_runner import AnsibleRunner

testinfra_hosts = AnsibleRunner('.molecule/ansible_inventory').get_hosts('all')


def test_files(File):
    present = [
        "/etc/motd",
        "/etc/pam.d/login",
        "/etc/systemd/system.conf"
    ]
    if present:
        for file in present:
            f = File(file)
            assert f.exists
            assert f.is_file


def test_service(Service):
    present = [
        "haveged"
    ]
    if present:
        for service in present:
            s = Service(service)
            assert s.is_enabled


def test_packages(Package, SystemInfo):
    if SystemInfo.distribution == 'centos':
        VIM = 'vim-enhanced'
    else:
        VIM = 'vim'
    present = [
        VIM,
        "tree",
        "lsof",
        "mlocate",
        "haveged",
        "curl",
        "htop"
    ]
    if present:
        for package in present:
            p = Package(package)
            assert p.is_installed
