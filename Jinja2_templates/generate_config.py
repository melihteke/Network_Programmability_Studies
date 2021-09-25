from jinja2 import Environment, FileSystemLoader
ENV = Environment(loader=FileSystemLoader('.'))
template = ENV.get_template("sw_port_int.j2")


interface_dict = { "name": "GigabitEthernet0/2", "description": "Server Port", "vlan": 10, "uplink": False }
print(template.render(interface=interface_dict))


