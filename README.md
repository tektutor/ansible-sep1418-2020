# Ansible Overview
* is an open source tool
* Ansible is developed by Michael Deehan ( a former RedHat employee )
* Michael Deehan incorporated Ansible Inc and developed Ansible Core as an Open source tool
* is developed in Python
* is an agentless tool
* is a configuration management tool
* is used to automate software installations
* is used to automate system administration activities
* helps in automating user/system configuration
* to automate it is not required to learn Python
* Domain Specific Language (DSL)
* DSL used by Ansible is YAML ( Yet Another Markup Language )
* YAML is a superset of JSON ( JavaScript Object Notation )
* RedHat acquired Ansible Inc, hence Ansible Core became RedHat's product
* IBM acquired RedHat, hence Ansible and Ansible Tower became IBM's product
* Ansible comes in flavours ( Ansible Core and Ansible Tower)
* Ansible Core is an Open Source Tool developed by Ansible Inc
* Ansible Tower is an Enterprise Tool developed by RedHat on top of Ansible Core

# Language Types
* Imperative
. Java
. C++
- Shell Scripting
- Windows Batch Scripts
- Powershell
- Python/Perl
- Imperative are powerful languages with many programming features
- Automation
* What? -  you wanted to automate
* How? - you need to write code to explain the logic that must be followed to perform the automation

* Declarative

** Ansible YAML Script is declarative
** You just need mention what you wanted to automate
** Ansible will take care of the how part(logic)

# Ansible Alternates
* Puppet - Client/Server Architecture
** Puppet Proprietary Agent must be installed on the Nodes(Servers) managed by Puppet
** Pull based architecture
* Chef - Client/Server Architecture
** Chef Proprietary Agent must be installed on the Nodes(Servers) managed by Chef
** Pull based architecture
* Salt/SaltStack

# Installing SSH Server in Ubuntu Ansible Node

apt update && apt install -y openssh-server

## You may check the SSH Server status as shown below

service ssh status

## You may start the SSH Server in case not running already

service ssh start


# Verifying if ansible nodes are reachable for Ansible Controller Machine(ACM)

## SSH into CentOS Ansible Node ( You need to type the password when prompted )

ssh anisble@192.168.112.130

Assumptions
* SSH User - anisble
* IP Address of CentOS Ansible Node is 192.168.112.130
* Password is Abridge@123

## SSH into Ubuntu Ansible Node ( You need to type the password when prompted )

ssh ansible@192.168.112.130

Assumptions
* SSH User - ansible
* IP Address of Ubuntu Ansible Node is 192.168.112.131
* Password is Abridge@123


