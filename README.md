Send Configurations.
________________________


This repo contains a function to send configuration commands to Cisco ios devices.

Prerequisite:
Before running the script, is required to create two text files and save them in the same directory where the send_configs.py is located:
 - Text file with the list of IP address the script will connect to send the configuration commands
 - Text file with the Cisco IOS commands. (conf t is not required to add in the list of commands)
 
Once execute the script, it will ask for the file's names that contain the commands and the list of the device's IP address(es).
Then, the script will perform error handling before authenticating to each IP address. Credentials will need to be entered manually for all the devices to SSH.
Last, the commands listed in the commands_file will be sent to each device.


Installation
________________________

This code requires Python 3 and has been tested with Python 3.8.8.
The following libraries and modules are required to be installed in the virtual environment:
 - netmiko
 - time
 - getpass


https://github.com/anmms-network/send_configs.git
cd send_configs/
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt


To Run
________________________

python3 send_configs.py


Technologies & Frameworks Used
________________________


Cisco Products & Services:

    ASA OS Software
    Catalyst IOS Software
    

Tools & Frameworks:
________________________

    Python 3.8.8
    
    
Authors & Maintainers
________________________


    Jose Anda jose.anda@anm.com
    
