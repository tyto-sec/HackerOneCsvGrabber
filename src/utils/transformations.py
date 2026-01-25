import re
from ipaddress import ip_network


def clean_domain(domain):
    domain = domain.strip()
    domain = re.sub(r'^https?://', '', domain)
    domain = re.sub(r'^(\*\.|\*|www\.)+', '', domain)
    domain = domain.split('/')[0]
    domain = domain.split(':')[0]
    if domain.endswith('.'):
        domain = domain[:-1]
    domain = domain.split('?')[0]
    domain = domain.split('#')[0]
    
    return domain.strip().lower()

def get_ip_addresses_from_cidr(cidr):
    network = ip_network(cidr, strict=False)
    return [str(ip) for ip in network.hosts()]