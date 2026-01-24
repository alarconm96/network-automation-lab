# Network Automation Practice: Cisco IOS-XE
This project practices the use of Python and Netmiko to automate configuration and state-checking on Cisco networking equipment.

## 🛠️ Skills Practiced
* **Python Automation:** Utilizing the Netmiko library for SSH connectivity.
* **Version Control:** Managed via Git/GitHub with industry-standard commit conventions.
* **Environment Management:** Use of Python Virtual Environments (venv) for dependency isolation.

## 🚀 How to Run
1. Clone this repository.
2. Create a virtual environment: `python -m venv net-auto`.
3. Activate the environment and install dependencies: `pip install netmiko`.
4. Run the script: `python test_lab.py`.

## 📋 Script Output
The current script checks devices.txt, connects to each hostname listed, executes `show ip interface brief`, and writes any `administratively down` interfaces into an audit_log.txt file