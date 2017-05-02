Install and configure basic software
====================================

Ansible role to install basic software and configure some important settings.
List of configurations done with this role:
  - globally configure http_proxy, https_proxy, and no_proxy variables
  - create motd
  - configure locale (only on Ubuntu)
  - upgrade system and enable security upgrades
  - disable IPv6 networking
  - tune network performance
  - configure sysctl variables
Software installed by this role:
  - haveged
  - vim
  - lsof
  - tree
  - mlocate
  - curl
  - htop

Requirements
------------

None.

Examples
--------

Use it in a playbook as follows:
```yaml
- hosts: all
  become: true
  roles:
    - system
  vars:
    - system_upgrade: True
```

Have a look at the [defaults/main.yml](defaults/main.yml) for role variables
that can be overridden.
