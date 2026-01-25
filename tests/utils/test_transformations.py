import pytest

from src.utils.transformations import clean_domain, get_ip_addresses_from_cidr


@pytest.mark.parametrize(
	"raw,expected",
	[
		("https://www.Example.com/path?x=1#frag", "example.com"),
		("*.example.com", "example.com"),
		("example.com:8080", "example.com"),
		("example.com.", "example.com"),
		("api.example.com/path/to/resource", "api.example.com"),
	],
)
def test_clean_domain(raw, expected):
	assert clean_domain(raw) == expected


@pytest.mark.parametrize(
	"cidr,expected",
	[
		("192.168.1.0/30", ["192.168.1.1", "192.168.1.2"]),
		("10.0.0.0/31", ["10.0.0.0", "10.0.0.1"]),
		("10.0.0.1/32", ["10.0.0.1"]),
	],
)
def test_get_ip_addresses_from_cidr(cidr, expected):
	assert get_ip_addresses_from_cidr(cidr) == expected
