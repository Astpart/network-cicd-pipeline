import pytest
from netmiko import ConnectHandler

def test_router_reachable():
    """Test if we can connect to R1"""
    device = {
        'device_type': 'cisco_ios',
        'host': '192.168.1.11',
        'username': 'ansible',
        'password': 'ansible123'
    }
    
    connection = ConnectHandler(**device)
    output = connection.send_command("show version")
    connection.disconnect()
    
    assert "Cisco IOS" in output

def test_ospf_running():
    """Test if OSPF is configured"""
    device = {
        'device_type': 'cisco_ios',
        'host': '192.168.1.11',
        'username': 'ansible',
        'password': 'ansible123'
    }
    
    connection = ConnectHandler(**device)
    output = connection.send_command("show ip ospf")
    connection.disconnect()
    
    assert "Routing Process" in output

