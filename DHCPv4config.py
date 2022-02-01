
from netmiko import ConnectHandler
import time


def R2():

    iosv2={
        'device_type':'cisco_ios',
        'ip':'198.51.100.21',
        'username': 'netman',
        'password': 'netman'
        }
    net_connect = ConnectHandler(**iosv2)
    config_commands1 = ['int f0/0', 'ip address dhcp', 'no shut', 'exit']
    net_connect.send_config_set(config_commands1)
    time.sleep(10)
    config_commands = ['do show ip interface brief']
    net_connect.enable ()
    output_1 = net_connect.send_config_set(config_commands)
    print(output_1)


def R3():

    iosv2={
        'device_type':'cisco_ios',
        'ip':'198.51.100.20',
        'username': 'netman',
        'password': 'netman'
        }
    net_connect = ConnectHandler(**iosv2)
    config_commands1 = ['int f0/0', 'ip address dhcp', 'no shut', 'exit']
    net_connect.send_config_set(config_commands1)
    time.sleep(10)
    config_commands = ['do show ip interface brief']
    net_connect.enable ()
    output_1 = net_connect.send_config_set(config_commands)
    print(output_1)

def R4():

    iosv2={
        'device_type':'cisco_ios',
        'ip':'198.51.100.22',
        'username': 'netman',
        'password': 'netman'
        }
    net_connect = ConnectHandler(**iosv2)
    config_commands1 = ['int f0/0', 'ip address dhcp', 'no shut', 'exit']
    net_connect.send_config_set(config_commands1)
    time.sleep(10)
    config_commands = ['do show ip interface brief']
    net_connect.enable ()
    output_1 = net_connect.send_config_set(config_commands)
    print(output_1)



R2()
R3()
R4()





