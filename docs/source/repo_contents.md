# Repository Contents

The following directories and files contain the Ansible deployment of
JupyterHub for Teaching.

## Overview

| Directory or File Name | Description                                                |
| ---------------------- | ---------------------------------------------------------- |
| **ansible-conda**      | submodule for using conda with ansible                     |
| **group_vars**         | group variables directory for Ansible                      |
| **host_vars**          | host variables directory for Ansible                       |
| **roles**              | roles directory for Ansible                                |
| **security**           | security directory for Ansible                             |
| README.md              | basic information about the repo                           |
| ansible.cfg            | custom configuration settings for Ansible                  |
| deploy.yml             | playbook to deploy JupyterHub                              |
| deploy_formgrade.yml   | playbook to deploy nbgrader's formgrader                   |
| hosts.example          | inventory file of servers (hosts) being managed by Ansible |
| saveusers.yml          | save users playbook (useful for backups)                   |



## Roles (Ansible)

The `roles` directory provides plays for deploying various functionality.

- bash

- common

- cull_idle

- formgrade

- jupyterhub

- nbgrader

- newrelic

- nginx

- python

- r

- saveusers

- supervisor

