<p><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/35/Tux.svg/1200px-Tux.svg.png" alt="linux logo" title="linux" align="right" height="60" /></p>

Ansible Role: system
====================

[![Build Status](https://travis-ci.org/SoInteractive/ansible-system.svg?branch=master)](https://travis-ci.org/SoInteractive/ansible-system) [![License](https://img.shields.io/badge/license-MIT%20License-brightgreen.svg)](https://opensource.org/licenses/MIT) [![Ansible Role](https://img.shields.io/badge/ansible%20role-SoInteractive.system-blue.svg)](https://galaxy.ansible.com/SoInteractive/system/) [![GitHub tag](https://img.shields.io/github/tag/sointeractive/ansible-system.svg)](https://github.com/SoInteractive/ansible-system/tags) [![Twitter URL](https://img.shields.io/twitter/follow/sointeractive.svg?style=social&label=Follow%20%40SoInteractive)](https://twitter.com/sointeractive)

Ansible role to install basic software and configure some important settings.

Overview
--------

This role privides basic system configuration. Basically it:
  - configures global http proxy settings
  - creates motd
  - configures locale (only on Ubuntu)
  - upgrades system and enables security upgrades
  - disables IPv6 networking
  - tunes network performance
  - configures sysctl variables

It also installs following software:
  - haveged
  - vim
  - lsof
  - tree
  - mlocate
  - curl
  - htop

Example usage
-------------

Use it in a playbook as follows:
```yaml
- hosts: all
  become: true
  roles:
    - SoInteractive.system
  vars:
    - system_upgrade: True
```

Have a look at the [defaults/main.yml](defaults/main.yml) for role variables
that can be overridden.
