from testinfra.utils.ansible_runner import AnsibleRunner

testinfra_hosts = AnsibleRunner('.molecule/ansible_inventory').get_hosts('all')


def test_files(host):
    present = [
        "/etc/motd",
        "/etc/motd.d/01logo",
        "/etc/motd.d/02text",
        "/etc/motd.d/03end",
        "/etc/pam.d/login",
        "/etc/systemd/system.conf",
        "/etc/rsyslog.d/90-logforwarder.conf"
    ]
    if present:
        for file in present:
            f = host.file(file)
            assert f.exists
            assert f.is_file


def test_service(host):
    present = [
        "haveged"
    ]
    if present:
        for service in present:
            s = host.service(service)
            assert s.is_enabled


def test_packages(host):
    if host.system_info.distribution == 'centos':
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
        "htop",
        "rsyslog"
    ]
    if present:
        for package in present:
            p = host.package(package)
            assert p.is_installed


def test_sysctl_vars(host):
    assert host.sysctl("net.ipv6.conf.all.disable_ipv6")

    # cannot test in Docker

    # assert host.sysctl("net.core.somaxconn") == 1024
    # assert host.sysctl("net.ipv4.tcp_max_syn_backlog") == 4096
    # assert host.sysctl("net.ipv4.tcp_tw_reuse")
    # assert not host.sysctl("net.ipv4.tcp_tw_recycle")


def test_locale(host):
    if host.system_info.distribution == "ubuntu":
        locale = "/etc/locale.gen"
        f = host.file(locale)
        assert f.is_file
        assert (
            not f.contains("# en_US.UTF-8 UTF-8") and
            f.contains("en_US.UTF-8 UTF-8")
            )


def test_unattended(host):
    if host.file("/etc/apt").is_directory:
        present = [
            "/etc/apt/apt.conf.d/20auto-upgrades",
            "/etc/apt/apt.conf.d/50unattended-upgrades"
        ]
        if present:
            for f in present:
                ff = host.file(f)
                assert ff.is_file
        elif host.file("/etc/yum").is_directory:
        present = [
            "/etc/yum/yum-cron.conf"
        ]
        if present:
            for f in present:
                ff = host.file(f)
                assert ff.is_file
