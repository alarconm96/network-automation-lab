import getpass
from net_utils import load_inventory, get_device_info

def run_automation():
    # load devices from devices.yaml
    devices = load_inventory('devices.yaml')

    print(f"Loaded {len(devices)} total devices")

    # collect credentials once at the start
    # getpass hides the text as you type it
    username = input("Enter SSH username: ")
    password = getpass.getpass("Enter SSH password: ")

    # loop - iterate through each device
    for device in devices:
        # only run against our routers
        if device['role'] == 'edge-router':
            print(f"\n--- Processing {device['hostname']} ---")

            # call function from net_utils
            result = get_device_info(device, username, password)

            # print result ('show ip interface brief' output)
            print(result)
        else:
            print(f"\nSkipping {device['hostname']} - not an edge router")

if __name__ == "__main__":
    run_automation()