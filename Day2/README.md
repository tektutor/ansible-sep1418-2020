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


# Generating SSH key pairs to authenticat ACM root user to login onto Ansible Nodes without password(key based login authentication)

## On your Ansible Controller Machine (ACM)

Assumptions:-
* You have logged in as root user
* Create the ssh-keygen with all default values (Hit Enter 3 times)
* You have already created /home/ansible/.ssh folders in Ubuntu and CentOS ansible nodes
* Ubuntu ansible node IP is 192.168.112.131 ( You need to substitue this IP with your Ubuntu node IP )
* CentOS ansible node IP is 192.168.112.130 ( You need to substitue this IP with your CentOS node IP )
* You have already created ansible user in the CentOS ansible node with the below command executed as root
    useradd ansible -d /home/ansible
    
    passwd ansible
* You have changed ansible user password to 'ansible' on Ubuntu and CentOS ansible nodes

    ssh-keygen
    
* Once the ssh key pairs are generated for ACM root user, you may copy the public key of ACM root user to your Day2 folder

   cd /root/Ansible/Day2

   cp /root/.ssh/id_rsa.pub authorized_keys
   
* Copy the ACM root user public key to Ubuntu ansible node
    scp authorized_keys ansible@192.168.112.131:/home/ansible/.ssh/authorized_keys

* Copy the ACM root user public key to CentOS ansible node
    scp authorized_keys ansible@192.168.112.130:/home/ansible/.ssh/authorized_keys
    
# Testing key based login authentication

## Manual verification
    ssh ansible@192.168.112.130

    ssh ansible@192.168.112.131
    
## Verify thru Ansible
    ansible -i inventory all -m ping

In order the above ansible ping to work, you need to edit your inventory as shown below

inventory

    [all]
    ubuntu ansible_host=192.168.112.131
    centos ansible_host=192.168.112.130
    
    [all:vars]
    ansible_user=ansible
    ansible_become_user=root
    ansible_become_password=root

