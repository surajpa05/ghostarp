from Core.NetworkDetails import main as GetNetwork,netWorkInterfaces
from Core.ArpForging import main as attackTarget
from collections import defaultdict
from Core.utils.Banner import randombanner as banner
from Core.utils.Display import display_interfaces
from scapy.all import get_if_addr, conf
import argparse


def main():

    banner()
    #Choose a network interface
    availInterface = netWorkInterfaces()
    display_interfaces(availInterface)

    while True:
        selectedInterface = int(input("Choose an interface: "))
        if selectedInterface > 0 and selectedInterface <= len(availInterface):
            #Networkdetails function
            availTargetlist = GetNetwork(availInterface[selectedInterface-1])
            # print(f"Scanning for host in {availInterface[selectedInterface-1]}")
            target = int(input("Choose a target from the above listing: "))
            #print(availTargetlist[target-1])
            attackTarget(availTargetlist[target-1])
        else:
            print("Invlid input !")

if __name__ == "__main__":
    main()
