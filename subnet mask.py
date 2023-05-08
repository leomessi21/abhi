# Function to calculate the subnet mask for a given IP address
def calculate_subnet_mask(ip_address):
    # Split the IP address into its octets
    octets = ip_address.split('.')

    # Determine the default subnet mask based on the first octet
    if int(octets[0]) <= 127:
        default_subnet_mask = '255.0.0.0'
    elif int(octets[0]) >= 128 and int(octets[0]) <= 191:
        default_subnet_mask = '255.255.0.0'
    elif int(octets[0]) >= 192 and int(octets[0]) <= 223:
        default_subnet_mask = '255.255.255.0'
    else:
        print('Invalid IP address')

    # Print the default subnet mask
    print('Default Subnet Mask: ' + default_subnet_mask)

    # Convert the default subnet mask to binary
    binary_subnet_mask = ''
    for octet in default_subnet_mask.split('.'):
        binary_subnet_mask += bin(int(octet))[2:].zfill(8)

    # Print the binary subnet mask
    print('Binary Subnet Mask: ' + binary_subnet_mask)

# Example usage of the function
calculate_subnet_mask('206.198.22.10')
