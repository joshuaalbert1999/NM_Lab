#importing netmiko
from netmiko import ConnectHandler
#importing time function for DHCP
import time


def R2():
#defining router2 commands
    iosv2={
        'device_type':'cisco_ios',
        'ip':'198.51.100.21',
        'username': 'netman',
        'password': 'netman'
        }
    net_connect = ConnectHandler(**iosv2)
    config_commands1 = ['int f0/0', 'ip address dhcp', 'no shut', 'exit']
    net_connect.send_config_set(config_commands1)
#time function 
    time.sleep(10)
    config_commands = ['do show ip interface brief']
    net_connect.enable ()
    output_1 = net_connect.send_config_set(config_commands)
    print(output_1)

#defining router3 commands
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
#defining router4 commands.
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
#show inerface command for listing interface
    config_commands = ['do show ip interface brief']
    net_connect.enable ()
    output_1 = net_connect.send_config_set(config_commands)
    print(output_1)


#calling the function
R2()
R3()
R4()





