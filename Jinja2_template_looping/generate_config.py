from jinja2 import Environment, FileSystemLoader
ENV = Environment(loader=FileSystemLoader('.'))
template = ENV.get_template("template.j2")


intlist = ["GigabitEthernet0/1", "GigabitEthernet0/2", "GigabitEthernet0/3"]

print(template.render(interface_list=intlist))


