#!/usr/bin/python
from ansible.module_utils.basic import AnsibleModule

def sayHello(msg1, msg2):
    return msg1 + " " + msg2 + " !"

def main():
    module = AnsibleModule(
        argument_spec=dict(
            msg1=dict(type='str'),
            msg2=dict(type='str')
        )
    )

    message1 = module.params['msg1']
    message2 = module.params['msg2']

    result = sayHello( message1, message2 )

    module.exit_json(output=result, changed=False)
    #module.fail_json(msg="Some error occurred")

if __name__ == '__main__':
    main()
