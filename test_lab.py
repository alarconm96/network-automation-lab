from netmiko import ConnectHandler

# device object configuration
cisco_device={
    'device_type': 'cisco_xe',
    'host': 'devnetsandboxiosxec8k.cisco.com',
    'username': 'alarconm96',
    'password': 'J--oMiV6a02RyLHQ',
    'port': 22
}

def main():
    print(f'Connecting to {cisco_device["host"]}')

    # commands I will run (like String[] array)
    commands = [
        'show ip interface brief',
        'show clock',
        'show version | include uptime'
    ]

    print('Establishing SSH Connection...')

    try:
        # with statement handles opening/closing connection automatically
        with ConnectHandler(**cisco_device) as net_connect:
            print('Connection successful!')
            print('-' * 20)

            for cmd in commands:
                #send_command sends string cmd in array and waits for '#' prompt
                output = net_connect.send_command(cmd)
                print(f'COMMAND: {cmd}')
                print(output)
                print('-' * 20)
    except Exception as e:
        print(f'Connection failed: {e}')

    print('Script complete. Coonnection closed')

if __name__ == '__main__':
    main()