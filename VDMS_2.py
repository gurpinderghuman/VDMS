import netaddr
from netaddr import IPNetwork, IPAddress
import sys
#from ipaddr import IPAddress as ip_address
IP_range= sys.argv[1]
IP_list = []
totalIP = []
IP_errorcheck = []
IP_errorcheck = IP_range.split('/')
if int(IP_errorcheck[1])>32:
    print "Subnet to be scanned is Invalid"
else:
    IP_list =  sys.argv[2].split(',')
    IP_output_list = []
    for ip in IPNetwork(IP_range):
        totalIP.append(str(ip))
    for i in range(len(IP_list)):
        if IPAddress(IP_list[i]) in IPNetwork(IP_range):
            #print IPNetwork(IP_range)
            IP_output_list.append(IP_list[i])
            print "Excluded IP address:", IP_list[i]
        else:
            print "IP address out of range, so, do not scan: ", IP_list[i]

    output_list = []
    for i in totalIP:
        if i not in IP_output_list:
            output_list.append(i)
    print "IP addresses to be scanned",output_list
    if len(totalIP) == len(output_list):
        print "List of excluded IPs is equal to total number of IPs in the subnet"
