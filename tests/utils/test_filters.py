import pytest

from src.utils.filters import is_valid_domain, is_valid_ip, is_valid_cidr


# is_valid_domain
@pytest.mark.parametrize(
	"domain,expected",
	[
		("example.com", True),
		("sub.example.co.uk", True),
		("123.456", False), 
		("-example.com", False),
		("example-.com", False),
		("example", False),
		("", False),
	],
)
def test_is_valid_domain(domain, expected):
	assert is_valid_domain(domain) is expected


# is_valid_ip
@pytest.mark.parametrize(
	"ip,expected",
	[
		("192.168.0.1", True),
		("255.255.255.255", True),
		("0.0.0.0", True),
		("256.0.0.1", False),
		("192.168.0", False),
		("192.168.0.1.5", False),
		("192.168.0.one", False),
	],
)
def test_is_valid_ip(ip, expected):
	assert is_valid_ip(ip) is expected


# is_valid_cidr
@pytest.mark.parametrize(
	"cidr,expected",
	[
		("192.168.0.0/24", True),
		("10.0.0.0/8", True),
		("255.255.255.255/32", True),
		("192.168.0.0/33", False),
		("300.168.0.0/24", False),
		("192.168.0.0", False),
		("192.168.0/24", False),
	],
)
def test_is_valid_cidr(cidr, expected):
	assert is_valid_cidr(cidr) is expected
