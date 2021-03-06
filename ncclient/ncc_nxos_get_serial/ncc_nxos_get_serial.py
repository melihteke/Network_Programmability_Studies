#!/usr/bin/env python
"""
Code sample for use with the DevNet Sandbox Always On Open NX-OS Programmability
"""

from ncclient import manager
import sys
from lxml import etree


# Set the device variables

DEVICES = ['172.16.30.101', '172.16.30.102']
USER = 'admin'
PASS = 'admin'
PORT = 830
DEVICE_NAMES = {'172.16.30.101': '(nx-osv9000-1)',
                '172.16.30.102': '(nx-osv9000-2)' }

DEVICE = "sandbox-nxos-1.cisco.com"
USER = 'admin'
PASS = 'Admin_1234!'
PORT = 830


# create a main() method
def main():
    """
    Main method that prints netconf capabilities of remote device.
    """
    serial_number = """
    <System xmlns="http://cisco.com/ns/yang/cisco-nx-os-device">
    <serial/>
    </System>
    """



    with manager.connect(host=DEVICE, port=PORT, username=USER,
                         password=PASS, hostkey_verify=False,
                         device_params={'name': 'nexus'},
                         look_for_keys=False, allow_agent=False) as m:

        # Collect the NETCONF response
        netconf_response = m.get(('subtree', serial_number))
        # Parse the XML and print the data
        xml_data = netconf_response.data_ele
        serial =  xml_data.find(".//{http://cisco.com/ns/yang/cisco-nx-os-device}serial").text

        print("The serial number for {} is {}".format(DEVICE, serial))




if __name__ == '__main__':
    sys.exit(main())