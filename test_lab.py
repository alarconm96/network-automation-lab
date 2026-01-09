from netmiko import ConnectHandler

# device object configuration
cisco_device={
    'device-type': 'cisco-xe',
    'host': 'devnetsandboxiosxec8k.cisco.com',
    'username': 'alarconm96',
    'password': 'J--oMiV6a02RyLHQ',
    'port': 22
}

# commands I will run (like String[] array)
commands = [
    'show ip interfaces brief',
    'show clock',
    'show version | include uptime'
]

print('Establishing SSH Connection...')

# with statement handles opening/closing connection automatically
with ConnectHandler(**cisco_device) as net_connect:
    print('Successfully connected!')
    print('-' * 20)

    for cmd in commands:
        #send_command sends string cmd in array and waits for '#' prompt
        output = net_connect.send_command(cmd)

        print(f'COMMAND: {cmd}')
        print(output)
        print('-' * 20)

print('Script complete. Coonnection closed')