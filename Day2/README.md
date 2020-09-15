Ansible ad-hoc command
ansible -i hosts all -m ping

ansible - utlity use to issue adhoc commands
-i - inventory
hosts - inventory file
all -  every machine under the all group of inventory file
-m - indicates ansible module
ping - ping.py is an ansible module

# Ansible Modules
* python scripts
* modules are installed as part of Ansible installation

ping.yml

    - name: Simple playbook
      hosts: all
      tasks:
        - name: Gathering facts
          setup:
      
        - name: Ping the ansible node
          ping:
          
ansible-playbook -i hosts ping.yml

# Ansible Playbook Execution 
1. Ansible opens a SSH connections parallely to the remote ansible nodes(ubuntu and centos)
2. It creates a tmp folder in ansible nodes(ubuntu and centos)
3. It copies the setup.py from ACM to Ubuntu and CentOS ansible node
4. From ACM ansible executes the python scripts onto the ansible node
5. Ansible then waits for the responses to come out from all ansible nodes.
6. On ACM, ansible give a summary of the playbook execution outcome

The above steps will repeated for each tasks written in the Playbook.

# Playbook Structure
1. Playbook is a YAML file
2. Each Playbook may contain a list of Play
3. Each Play contains a hosts section and tasks section
4. The hosts section tell the ansible nodes on which the automation must be done. 
5. The connection details to the Ansible nodes are available in the inventory file.
6. The tasks section, may contain a list of Tasks
7. Each Task can invoke exactly one Ansible module.
