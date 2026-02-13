import yaml
from netmiko import ConnectHandler

def load_inventory(filepath):
    """load yaml devices"""
    with open(filepath, 'r') as f:
        data = yaml.safe_load(f)
    return data['devices']

def get_device_info(device_dict, username, password):
    """
    establish SSH connection, run commands, and return output
    """
    # map YAML data to format netmiko understands
    connection_params = {
        'device_type': 'cisco_xe' if device_dict['os'] == 'ios_xe' else 'linux',
        'host': device_dict['address'],
        'username': username,
        'password': password,
        'port': 22,
        'secret': password, # why are we able to leave tis comma here?
    }

    print(f"\n>>>Attempting to connect to: {device_dict['hostname']} {device_dict['address']}")

    # use try-except to catch connection errors

    try:
        with ConnectHandler(**connection_params) as net_connect:
            print(f"Connected successfully to {device_dict['hostname']}")
            
            # standard cisco verification command
            output = net_connect.send_command("show ip interface brief")
            return output
        
    except Exception as e:
        # catches errors like timed out or auth failure
        return f"Failed to connect to {device_dict['hostname']}: ({e})"