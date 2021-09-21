"""Send Configurations Script.


Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

Python - Netmiko library to connect to network devices via ssh
Manually enter creds
Connect to devices listed ini external text file
Send configuration commands from external file
Error handling performed before authenticating to the IP

"""

__author__ = "Jose Anda"
__email__ = "jose.anda@anm.com"
__version__ = "0.1.2"
__copyright__ = " "
__license__ = "Apache License, Version 2.0"


from netmiko import ConnectHandler
from getpass import getpass
from netmiko import ConnectHandler
from netmiko.ssh_exception import NetMikoTimeoutException
from paramiko.ssh_exception import SSHException
from netmiko.ssh_exception import AuthenticationException
import time

def main():
    while True:
        file1 = input("\nFILE WITH COMMANDS: ")
        try:
            with open(file1) as f:
                commands_to_send = f.read().splitlines()
        except FileNotFoundError as fnf_error:
            print('')
            print(fnf_error, "...try again...")
            continue
        else:
            while True:
                file2 = input("\nFILE WITH IP ADDRESS(ES): ")
                try:
                    with open(file2) as f:
                        devicelist = f.read().splitlines()
                except FileNotFoundError as fnf_error:
                    print('')
                    print(fnf_error, "...try again...")
                    continue
                else: 
                    break
            break

    username = input("\nEnter SSH Username: ")
    password = getpass()

    with open("Output_Report.txt", "a") as saveoutput:
        for device_ip in devicelist:
            print('\n\n---- CONNECTING TO IP: ' + str(device_ip))
            time.sleep(1)
            ios_device = {
            'device_type': 'cisco_ios',
            'ip': device_ip,
            'username': username,
            'password': password
            }
        #Script to perform error handling before attempting a connection to the device listed in Device_File file:
            try:
                net_connect = ConnectHandler(**ios_device)
            except (AuthenticationException):
                access_issue = (device_ip + ' Authentication failure')
                print ('\n!!! Authentication failure: ' + device_ip + ( ' !!!\n\n'))
                saveoutput.write(access_issue + ("\n"))
                saveoutput.write(' ')
                continue
            except (NetMikoTimeoutException):
                access_issue = (device_ip + ' Timeout')
                print('!!! Timeout to device: ' + device_ip + (' !!!\n\n'))
                saveoutput.write(access_issue + ("\n"))
                saveoutput.write(' ')
                continue
            except (EOFError):
                access_issue = (device_ip + ' Access Error')
                print('!!! End of file while attempting device ' + device_ip + ('!!!\n\n'))
                saveoutput.write(access_issue + ("\n"))
                saveoutput.write(' ')
                continue
            except (SSHException):
                access_issue = (device_ip + ' SSH not enable')
                print('!!! SSH Issue. Check SSH settings ' + device_ip + ('!!!\n\n'))
                saveoutput.write(access_issue + ("\n"))
                saveoutput.write(' ')
                continue
            except Exception as unknown_error:
                access_issue = (device_ip + ' Unknown error')
                print ('---- Cannot connect. Unknown error in device: ' + device_ip)
                print ('---- Unknown error: ' + str(unknown_error))
                saveoutput.write(access_issue + ("\n"))
                saveoutput.write(' ')
                continue
            
            print ('---- SUCCESSFULLY CONNECTED ')
            saveoutput.write('---- SUCCESSFULLY CONNECTED TO IP: ' +str(device_ip) + ('....'))
            time.sleep(2)
            print ('---- SENDING CONFIGURATIONS.... \n')
            saveoutput.write('---- SENDING CONFIGURATIONS.... \n')
            output1 = net_connect.send_config_set(commands_to_send)
            print (output1)
            saveoutput.write(" ")
            saveoutput.write(output1)
            saveoutput.write(" ")
            print ('\n---- CONFIGURATIONS COMPLETED FOR IP: ' + device_ip + '\n\n' )
            saveoutput.write('\n---- CONFIGURATIONS COMPLETED FOR IP: ' + device_ip + "\n")
            print('\n======================================')
            saveoutput.write(" ")

if __name__ == "__main__":
    main()
