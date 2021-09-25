from getpass import getpass
from netmiko import ConnectHandler
from jinja2 import Environment, FileSystemLoader
ENV = Environment(loader=FileSystemLoader('.'))
template = ENV.get_template("basic_report_temp.j2")


username = input("Please enter your SSH Username: ")
password = getpass()

#Configuration file
with open("commands.txt") as f:
 command_list = f.read().splitlines()

#Device list file
with open("device_list.txt") as f:
 device_list = f.read().splitlines()


print("----------------------------------------")
print("| Interface  | IP address  |  Status     |")
for devices in device_list:
 print("=" * 30 )
 print ("Connecting to device  " + devices)
 ip_address_of_device = devices

 iosv_l2_s3 = {'device_type': 'cisco_ios', 'ip': ip_address_of_device, 'username': username, 'password': password }

 net_connect = ConnectHandler(**iosv_l2_s3)
 #output = net_connect.send_config_set(command_list)
 output = net_connect.send_command("show ip int brief", use_textfsm=True)
 print(output)
 print(type(output))
 print(template.render(ints=output))