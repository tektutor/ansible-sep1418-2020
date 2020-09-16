# Creating ansible user in CentOS ansible node

Please follow the below steps

It would prompt for root password

    su -
    
You may create a new user called 'ansible'

    useradd ansible -d /home/ansible

Change the password of ansible user to 'ansible' without quotes

    passwd ansible
    
Try to login as 'ansible' user with 'ansible' as the password

    su - ansible
    

# You may add the 'ansible' user to /etc/sudoers file as shown below
    
    vim /etc/sudoers
    
You need to now look for a line that appears shown below

    root ALL=(ALL) ALL

You need to add a new line as shown below

    root    ALL=(ALL) ALL
    ansible ALL=(ALL) ALL    
    
You need to force write and quit the file

    :wq!
 
# Configure CentOS node for key pair based login authentication

You need to create .ssh folder

    mkdir -p /home/ansible/.ssh
    
    chmod 700 /home/ansible/.ssh
    
From the Ansible Controller Machine(ACM), you need to try the below. Assuming 192.168.112.130 is the Centos ansible node IP, you may change this to yours.

The expectation here is that you should be able do ssh into CentOS node as ansible user by typing the password when prompted

    ssh ansible@192.168.112.130

You need to logout by typing exit and return back to ACM root user shell prompt

    exit

You need to copy the public key of root user as shown below
    
    cp /root/.ssh/id_rsa.pub authorized_keys
    
You are expected to type 'ansible' as the password for 'ansible' user when prompted
    
    scp authorized_keys ansible@192.168.112.130:/home/ansible/.ssh/authorized_keys
    
You may now see if you are able to ssh into CentOS node without password prompt
    
    ssh ansible@192.168.112.130
    
If all the above steps were successfuly, you should be able to ping CentOS node as shown below
    
    ansible -i /root/Training/hosts centos -m ping
