def ip_to_int(ip_address):
    # Split the IP address into its octets
    octets = ip_address.split('.')
    
    # Convert each octet to an integer
    octets = [int(octet) for octet in octets]
    
    # Calculate the integer value of the IP address
    ip_int = (octets[0] << 24) + (octets[1] << 16) + (octets[2] << 8) + octets[3]
    
    return ip_int

