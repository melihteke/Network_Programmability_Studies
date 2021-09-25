from getpass import getpass
from netmiko import ConnectHandler

username = input("Please enter your SSH Username: ")
password = getpass()

#Configuration file
with open("commands.txt") as f:
 command_list = f.read().splitlines()

#Device list file
with open("device_list.txt") as f:
 device_list = f.read().splitlines()



for devices in device_list:
 print("\n" * 2)
 print("=" * 50 )
 print ("Connecting to device  " + devices)
 ip_address_of_device = devices

 iosv_l2_s3 = {'device_type': 'cisco_ios', 'ip': ip_address_of_device, 'username': username, 'password': password }

 net_connect = ConnectHandler(**iosv_l2_s3)
 #output = net_connect.send_config_set(command_list)
 output = net_connect.send_command("show runn | inc username", use_textfsm=True)
 print(output)
 with open("device_username_check.txt", "a") as df:
  df.write(output)
 df.close()
 print("=" * 50)
