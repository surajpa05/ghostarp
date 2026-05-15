from scapy.layers.l2 import Ether, ARP
from scapy.sendrecv import srp
from mac_vendor_lookup import MacLookup


def main(ipaddress,subnetMask):
    ip = ipaddress.split('.')
    if subnetMask == 24:
        packet = Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(pdst=f"{ip[0]}.{ip[1]}.{ip[2]}.0/24")
        result = srp(packet, timeout=3, verbose=False)[0]
        for sent, received in result:
            print(f"IP: {received.psrc}, MAC: {received.hwsrc}",end=" ")
            try:
                print(f"Vendor: {MacLookup().lookup(received.hwsrc)}")
            except:
                print("Unknow")