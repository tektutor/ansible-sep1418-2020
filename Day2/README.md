Ansible ad-hoc command
ansible -i hosts all -m ping

ansible - utlity use to issue adhoc commands
-i - inventory
hosts - inventory file
all -  every machine under the all group of inventory file
-m - indicates ansible module
ping - ping.py is an ansible module