import os
import pytest
from netmiko import ConnectHandler
from netmiko.exceptions import NetmikoTimeoutException, NetmikoAuthenticationException

# Check if we're in CI environment
IN_CI = os.getenv('CI', 'false').lower() == 'true'

ROUTER_CONFIG = {
    'device_type': 'cisco_ios',
    'host': '192.168.1.11',
    'username': 'ansible',
    'password': 'ansible123',
    'secret': 'cisco123',
}

@pytest.mark.skipif(IN_CI, reason="Skipping in CI - requires local network access")
def test_router_reachable():
    """Test if router is reachable via SSH"""
    try:
        connection = ConnectHandler(**ROUTER_CONFIG)
        connection.disconnect()
        assert True
    except (NetmikoTimeoutException, NetmikoAuthenticationException) as e:
        pytest.fail(f"Failed to connect to router: {e}")

@pytest.mark.skipif(IN_CI, reason="Skipping in CI - requires local network access")
def test_ospf_running():
    """Test if OSPF is running on the router"""
    try:
        connection = ConnectHandler(**ROUTER_CONFIG)
        output = connection.send_command('show ip ospf neighbor')
        connection.disconnect()
        assert 'FULL' in output or 'Neighbor ID' in output
    except Exception as e:
        pytest.fail(f"OSPF test failed: {e}")
