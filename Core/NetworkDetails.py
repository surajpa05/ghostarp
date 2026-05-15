from .Hostdiscovery import main as discorvery
import socket
import ipaddress


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

def main():
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)
    submask = subnetMask(local_ip)
    # print("local ip : ",local_ip,"\nsubnetmask : ",submask)
    discorvery(local_ip,submask)

