 
<font <link href='https://fonts.googleapis.com/css?family=Lato:400,700|Roboto+Slab:400,700|Inconsolata:400,700' rel='stylesheet' type='text/css'>
<link href='https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.0.3/css/font-awesome.min.css' rel='stylesheet' type='text/css'>


# Ansible Static Inventory

* Ansible static inventory file is a text file that looks like an INI file
* It contains SSH connection details in case the Ansible node OS is Unix/Linux 
* It contains WinRM connection details in case the Ansible node OS is Windows 10 or later

## For example, a simple static inventory can be written as below

    [all]
    ubuntu ansible_user=ansible ansible_password=ansible ansible_host=192.168.112.131
    centos ansible_user=ansible ansible_password=ansible ansible_host=192.168.112.130

### Note
* all - indicates a built-in ansible inventory group
* all group contains all the ansible nodes listed in the inventory file
* ubuntu - is a user-defined string used to point out the ansible node
* ansible_user - is a built-in host varaible that indicates the SSH username or the Windows username that must be used to login
* ansible_password - is the password that must be used to login to the ansible node
* ansible_host - is the ansible node IP address
