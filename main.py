from Core.NetworkDetails import main as GetNetwork,netWorkInterfaces
from Core.ArpForging import main as attackTarget
from collections import defaultdict
from Core.utils.Banner import randombanner as banner
from Core.utils.Display import display_interfaces
from scapy.all import get_if_addr, conf
import os

from InquirerPy import inquirer
RED   = "\033[1;91m"
RESET = "\033[0m"

CURSOR_UP   = "\033[{}A"  
ERASE_LINE  = "\033[2K"   

def reprint_table(rendered_lines, previous_line_count):
    if previous_line_count > 0:
        for _ in range(previous_line_count):
            print(CURSOR_UP.format(1) + ERASE_LINE, end="")
    for line in rendered_lines:
        print(line)

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
    selectedInterface = 0
    availInterface, availTargetlist = "", ""
    network_table   = []  
    try:
        while True:
            os.system("clear")
            banner()

            if network_table:
                for line in network_table:
                    print(line)

            choice = option_menu()

            if choice == "interface":
                availInterface = netWorkInterfaces()
                display_interfaces(availInterface)
                try:
                    selectedInterface = int(input("Choose an interface: "))
                except ValueError:
                    print(f"\n{RED}Invalid input{RESET}\n")

            elif choice == "scan":
                try:
                    print(f"Scanning for host in {availInterface[selectedInterface-1]}")
                    if selectedInterface > 0 and selectedInterface <= len(availInterface):
                        availTargetlist, network_table = GetNetwork(availInterface[selectedInterface-1])
                except (IndexError, TypeError):
                    print(f"\n{RED}Select a valid interface first.{RESET}\n")
                    input("Press Enter to continue...")
                except PermissionError:
                    print(f"\n{RED}Permission denied. Run as root.{RESET}\n")
                    input("Press Enter to continue...")
                except OSError as e:
                    print(f"\n{RED}Scan failed: {e}{RESET}\n")
                    input("Press Enter to continue...")

            elif choice == "exploit":
                try:
                    target = int(input("Choose a target from the above listing: "))
                except ValueError:
                    print(f"\n{RED}Enter a valid number.{RESET}\n")
                    input("Press Enter to continue...")
                    continue
                try:
                    attackTarget(availTargetlist[target-1])
                except (IndexError, TypeError):
                    print(f"\n{RED}Invalid target. Run a network scan first and choose a valid target number.{RESET}\n")
                    input("Press Enter to continue...")

            elif choice == "exit":
                print("Exiting GhostARP")
                exit()
    except KeyboardInterrupt:
        print("Exiting GhostARP")
        exit()

if __name__ == "__main__":
    main()
