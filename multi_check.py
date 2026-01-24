from netmiko import ConnectHandler

# device object configuration
device_template = {
    'device_type': 'cisco_xe',
    'username': 'alarconm96',
    'password': 'T5R2U__QZylf6',
    'secret': 'developer'
}

# main function
def main():
    # using with to safely read list of devices from file
    try:
        with open('devices.txt', 'r') as f:
            device_list = f.read().splitlines()
    except FileNotFoundError:
        print("Error: devices.txt not found.")
        return
    
    # iterate through each ip in list
    for ip in device_list:
        print(f'\n--- Connecting to {ip} ---')

        # create copy of device_template dict to use with each specific device
        current_device = device_template.copy()
        current_device['host'] = ip

        # try-catch block and with keyword to attempt connections
        try:
            with ConnectHandler(**current_device) as net_connect:
                net_connect.enable()
                output = net_connect.send_command("show ip interface brief")
                with open("audit_log.txt", "a") as log_file:
                    log_file.write(f"{ip}\n")
                    for line in output.splitlines()[2:]:
                        if "administratively down" in line:
                            output_string = line.split()
                            log_file.write(f"Interface {output_string[0]} (IP {output_string[1]}) is ADMIN DOWN\n")
                    log_file.write("-------------------------\n")
        except Exception as e:
            print(f"❌ WARNING: Connection failed wih {ip}: {e}")
        print(f'--- Disconnecting from {ip} ---\n')

if __name__ == "__main__":
    main()