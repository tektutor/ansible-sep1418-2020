
# Cloning this lab exercises 

On your Ansible Lab machine, login as root user

    su -
    
    mkdir Training
    cd Training
    git clone https://github.com/tektutor/ansible-sep1418-2020.git

You need to create a inventory file with name hosts under the Training folder with the below contents

    [all]
    ubuntu ansible_host=192.168.112.131
    centos ansible_host=192.168.112.130

    [all:vars]
    ansible_user=ansible
    ansible_become_user=root
    ansible_become_password=ansible
    ansible_private_key_file=/root/.ssh/id_rsa

You may have to change the IP address of Ubuntu and Ansible Node with IP details of your ansible nodes.

Whenever you need to pull latest code from this GitHub, you need to do the below

    cd /root/ansible-sep1418-2020
    git pull
    
Now you will have the latest code!

If you need to execute any playbook, you may try as below

    cd ansible-sep1418-2020/Day2
    ansible-playbook -i /root/Training/hosts install-nginx.yml
    
> Note
* you need to use the inventory that you created under the Training folder every time.

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

## Automation
* As automation is done by System Administrators, Developers and QA, the language choice (DSL) is crucial.
* Though imperative languages are powerful it is not suitable as not everyone will find it easy to learn and work.
* More code must be written to achieve the same stuff in imperative languages as compared to declarative languages.

## Automation mainly has two parts
<ul>
  <li>What? - what you wanted to automate</li>
  <li>How? - the logic that must be followed to perform the automation</li>
</ul

# Language Types
## Imperative
* If imperative languages are used for automation, you must write code to explain "What" and "How"
* Many lines of code must be written to achieve the automation
* Maintenance of code is difficult as more lines of code 
* More lines of code means chances of bugs are more

### Examples
<ul>
  <li>Java</li>
  <li>C++</li>
  <li>Shell Scripting</li>
  <li>Windows Batch Scripts</li>
  <li>Powershell</li>
  <li>Python/Perl</li>
  <li>Imperative are powerful languages with many programming features</li>
</ul>

## Declarative
<ul>
  <li>Ansible Playbook is declarative</li>
  <li>What? -In declarative language, you just need to mention what you want to automate</li>
  <li>How? - Ansible will take care of the how part(logic)</li>
</ul>

# Ansible Alternates
<ul>
  <li>Puppet - Client/Server Architecture</li>
  <li>Puppet Proprietary Agent must be installed on the Nodes(Servers) managed by Puppet</li>
  <li>Pull based architecture</li>
  <li>Chef - Client/Server Architecture</li>
  <li>Chef Proprietary Agent must be installed on the Nodes(Servers) managed by Chef</li>
  <li>Pull based architecture</li>
  <li>Salt/SaltStack</li>
</ul>

# Puppet/Chef High-Level Architecture
<img src=https://github.com/tektutor/ansible-sep1418-2020/blob/master/PuppetChefArchitecture.png />


# Ansible High-Level Architecture
<img src=https://github.com/tektutor/ansible-sep1418-2020/blob/master/Ansible%20Architecture.png />

# Installing SSH Server in Ubuntu Ansible Node
    apt update && apt install -y openssh-server
    
# Installing SSH Server in CentOS Ansible Node
    yum install -y epel-release
    yum install -y openssh-server

## You may chek the SSH Server status in CentOS as shown below
    systemctl status sshd
You are expected to see to Active(green) if SSH Service is running normally.

## You may check the SSH Server status in Ubuntu as shown below
    service ssh status
You are expected to see to Active(green) if SSH Service is running normally.

## You may start the SSH Server in case not running already
    service ssh start

# Verifying if ansible nodes are reachable for Ansible Controller Machine(ACM)
## SSH into CentOS Ansible Node ( You need to type the password when prompted )
    ssh anisble@192.168.112.130

### Assumptions
* SSH User - anisble
* IP Address of CentOS Ansible Node is 192.168.112.130
* Password is Abridge@123

## SSH into Ubuntu Ansible Node ( You need to type the password when prompted )
    ssh ansible@192.168.112.130

### Assumptions
* SSH User - ansible
* IP Address of Ubuntu Ansible Node is 192.168.112.131
* Password is Abridge@123
