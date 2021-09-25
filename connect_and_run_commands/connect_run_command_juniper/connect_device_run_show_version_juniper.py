from getpass import getpass
from netmiko import ConnectHandler

username = input("Please enter your SSH Username: ")
password = getpass()

#Configuration file
with open("../connect_run_commands_cisco/commands.txt") as f:
 command_list = f.read().splitlines()

#Device list file
with open("../connect_run_commands_cisco/device_list.txt") as f:
 device_list = f.read().splitlines()



for devices in device_list:
 print("\n\n===================================\n\n")
 print ("Connecting to device  " + devices)
 ip_address_of_device = devices

 iosv_l2_s3 = {'device_type': 'juniper_junos', 'ip': ip_address_of_device, 'username': username, 'password': password }

 net_connect = ConnectHandler(**iosv_l2_s3)
 #output = net_connect.send_config_set(command_list)
 output = net_connect.send_command("show version")
 print(output)
