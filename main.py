from Core.NetworkDetails import main as GetNetwork,netWorkInterfaces
from Core.ArpForging import main as attackTarget
from collections import defaultdict
from Core.utils.Banner import randombanner as banner
from Core.utils.Display import display_interfaces
from scapy.all import get_if_addr, conf

from InquirerPy import inquirer

def option_menu():
    choice = inquirer.select(
        message="Choose an option from below ",
        choices=[
            {"name": "[ 1 ] Set Active Network Interface",       "value": "interface"},
            {"name": "[ 2 ] Discover Hosts on Network",          "value": "scan"},
            {"name": "[ 3 ] Launch ARP Spoofing Attack",         "value": "exploit"},
            {"name": "[ 4 ] Quit GhostARP",                      "value": "exit"},
        ],
    ).execute()
    return choice

def main():
    banner()
    #Choose a network interface
    selectedInterface = 0
    availInterface,availTargetlist = "",""
    try:
        while True:
            choice = option_menu()
            if (choice == "interface"):
                availInterface = netWorkInterfaces()
                display_interfaces(availInterface)
                selectedInterface = int(input("Choose an interface: "))

            elif(choice == "scan"):
                print(f"Scanning for host in {availInterface[selectedInterface-1]}")
                try:
                    if selectedInterface > 0 and selectedInterface <= len(availInterface):
                        availTargetlist = GetNetwork(availInterface[selectedInterface-1])
                except:
                    print("Error occured while scanning")
                    

            elif(choice == "exploit"):
                target = int(input("Choose a target from the above listing: "))
                try:
                    attackTarget(availTargetlist[target-1])
                except:
                    print("Invalid target or errror occured while exploiting !")

            elif(choice == "exit"):
                print("Exiting GhostARP")
                exit()
    except:
        print("Exiting GhostARP")
        exit();

        # while True:
        #     
        #         
        #         
        #         # 
        #        
        #         #print(availTargetlist[target-1])
        #         
        #     else:
        #         print("Invlid input !")
if __name__ == "__main__":
    main()
