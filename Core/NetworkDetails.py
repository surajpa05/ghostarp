import socket
from scapy.layers.l2 import Ether, ARP
from scapy.all import get_if_addr, conf
from scapy.sendrecv import srp
from mac_vendor_lookup import MacLookup
from collections import defaultdict
import psutil
import ipaddress
import netifaces
from Core.utils.Display import display_network_results, render_network_results

def get_interface_cidr(iface_name):
    for network, netmask, _, iface, _, _ in conf.route.routes:
        if iface == iface_name:
            cidr_bits = ipaddress.IPv4Network(f"0.0.0.0/{netmask}").prefixlen
            return cidr_bits
            
    raise ValueError(f"Interface {iface_name} has no valid routes.")

def netWorkInterfaces():
    ilist = []
    interfaces = psutil.net_if_addrs().keys()
    return list(interfaces)

def hostDiscovery(ipaddress, subnetMask):
    mac_lookup = MacLookup()
    iplisting = []
    ip = ipaddress.split('.')
    packet = Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(pdst=f"{ip[0]}.{ip[1]}.{ip[2]}.0/{subnetMask}")
    result = srp(packet, timeout=3, verbose=False)[0]
    for sent, received in result:
        try:
            vendor = mac_lookup.lookup(received.hwsrc)
        except (KeyError, ValueError):
            vendor = "Unknown"
        iplisting.append(f"{received.psrc},{received.hwsrc},{vendor}")

    rendered = render_network_results(iplisting, ipaddress, subnetMask)
    for line in rendered:
        print(line)
    return iplisting, rendered

def main(netInterface):
    print(f"Scanning for active host in: {netInterface}")
    #Host id (This systsem)
    HostIP_address = netifaces.ifaddresses(netInterface)

    #Subnet mask in cidr form 
    ipv4_info = HostIP_address[netifaces.AF_INET][0]
    netmask = ipv4_info['netmask']
    cidr_bits = ipaddress.IPv4Network(f"0.0.0.0/{netmask}").prefixlen

    # print(f"Host ip: {ipv4_info['addr']}, Cidr Notation: {cidr_bits}")
    return hostDiscovery(ipv4_info['addr'],cidr_bits)

