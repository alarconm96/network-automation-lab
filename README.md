# Network Automation Practice: Cisco IOS-XE
This project practices the use of Python and Netmiko to automate configuration and state-checking on Cisco networking equipment.

## 🛠️ Key Features
* **Data-Driven Inventory Management** - Externalized device inventory using YAML, enabling the addition or removal of network devices without modifying the core codebase.
* **Automated Network Device State Checks** - Automation script cycles through devices ingested from YAML devices list and returns output for auditing commands (e.g. cycle through interfaces and notify user of unassigned IP addresses)
* **Secure Credential Handling** - Implemented secure credential injection using the getpass library to prevent sensitive data exposure in terminal history or source control.

## 🔰 Skills Practiced
* **Python Automation:** Utilizing the Netmiko library for SSH connectivity.
* **Version Control:** Managed via Git/GitHub with industry-standard commit conventions.
* **Environment Management:** Use of Python Virtual Environments (venv) for dependency isolation.

## 🚀 How to Run
1. Clone this repository.
2. Create a virtual environment: `python -m venv net-auto`.
3. Activate the environment and install dependencies from requirements file: `pip install -r requirements.txt`.
4. Run the script: `python3 multi_check.py`.

## 📋 Script Output
The current script grabs data from a devices YAML file and imports the device dictionaries using net_utils.py. It then connects via SSH using user-provided username and password credentials and runs a hard-coded "show ip interface brief' command on any devices with the 'edge-router' role and prints the output before closing the connection.
