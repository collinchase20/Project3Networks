# Initialize the netmask and calculate based on CIDR mask




def get_netmask_from_cidr(cidr):
    mask = [0, 0, 0, 0]
    for i in range(cidr):
        mask[i / 8] = mask[i / 8] + (1 << (7 - i % 8))
    netmask = "{}.{}.{}.{}".format(mask[0], mask[1], mask[2], mask[3])
    return netmask


def get_cidr_from_netmask(netmask):
    # For later use
    return (sum([bin(int(bits)).count("1") for bits in netmask.split(".")]))




#print(get_cidr_from_netmask("255.0.0.0"))


print(get_netmask_from_cidr(24))

print(get_netmask_from_cidr(23))


print(get_netmask_from_cidr(22))

print(get_netmask_from_cidr(21))

print(get_netmask_from_cidr(20))

print(get_netmask_from_cidr(19))
