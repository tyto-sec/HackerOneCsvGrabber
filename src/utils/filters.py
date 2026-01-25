import re

def is_valid_domain(domain):
    if not domain or '.' not in domain:
        return False
    domain_pattern = r'^[a-zA-Z0-9][a-zA-Z0-9-\.]*[a-zA-Z0-9]\.[a-zA-Z]{2,}$'
    if not re.match(domain_pattern, domain):
        return False
    parts = domain.split('.')
    if all(part.isdigit() for part in parts):
        return False
    
    return True

def is_valid_ip(address):
    ip_pattern = r'^(\d{1,3}\.){3}\d{1,3}$'
    if re.match(ip_pattern, address):
        parts = address.split('.')
        return all(0 <= int(part) <= 255 for part in parts)
    return False

def is_valid_cidr(cidr):
    cidr_pattern = r'^(\d{1,3}\.){3}\d{1,3}/\d{1,2}$'
    if re.match(cidr_pattern, cidr):
        ip_part, prefix_length = cidr.split('/')
        parts = ip_part.split('.')
        if all(0 <= int(part) <= 255 for part in parts):
            if 0 <= int(prefix_length) <= 32:
                return True
    return False