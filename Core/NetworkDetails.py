import socket
from scapy.layers.l2 import Ether, ARP
from scapy.sendrecv import srp
from mac_vendor_lookup import MacLookup
from collections import defaultdict


def subnetMask(localip):
    subRange = int(localip[0:3])
    if subRange < 127:
        return 8
    elif subRange < 191:
        return 16
    elif subRange < 223:
        return 24
    else:
        return "Class D or E" 


def hostDiscovery(ipaddress, subnetMask):
    iplisting = []
    ip = ipaddress.split('.')
    if subnetMask == 24:
        packet = Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(pdst=f"{ip[0]}.{ip[1]}.{ip[2]}.0/24")
        result = srp(packet, timeout=3, verbose=False)[0]
        i=0
        for sent, received, in result:
            print(f"{i+1}) IP: {received.psrc}, MAC: {received.hwsrc}", end=" ")
            i +=1
            iplisting.append(f"{received.psrc},{received.hwsrc}")
            try:
                print(f"Vendor: {MacLookup().lookup(received.hwsrc)}")
            except:
                print("Unknown")
        return iplisting
def main():
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)
    submask = subnetMask(local_ip)
    return hostDiscovery(local_ip, submask)

