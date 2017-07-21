from testinfra.utils.ansible_runner import AnsibleRunner

testinfra_hosts = AnsibleRunner('.molecule/ansible_inventory').get_hosts('all')


def test_files(File):
    present = [
        "/etc/motd",
        "/etc/motd.d/01logo",
        "/etc/motd.d/02text",
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


def test_sysctl_vars(Sysctl):
    assert Sysctl("net.ipv6.conf.all.disable_ipv6")

    # cannot test in Docker

    # assert Sysctl("net.core.somaxconn") == 1024
    # assert Sysctl("net.ipv4.tcp_max_syn_backlog") == 4096
    # assert Sysctl("net.ipv4.tcp_tw_reuse")
    # assert not Sysctl("net.ipv4.tcp_tw_recycle")


def test_locale(File, SystemInfo):
    if SystemInfo.distribution == "ubuntu":
        locale = "/etc/locale.gen"
        f = File(locale)
        assert f.is_file
        assert (
            not f.contains("# en_US.UTF-8 UTF-8") and
            f.contains("en_US.UTF-8 UTF-8")
            )


def test_unattended(File):
    if File("/etc/apt").is_directory:
        present = [
            "/etc/apt/apt.conf.d/20auto-upgrades",
            "/etc/apt/apt.conf.d/50unattended-upgrades"
        ]
        if present:
            for f in present:
                ff = File(f)
                assert ff.is_file
    elif File("/etc/yum").is_directory:
        present = [
            "/etc/yum/yum-cron.conf"
        ]
        if present:
            for f in present:
                ff = File(f)
                assert ff.is_file
