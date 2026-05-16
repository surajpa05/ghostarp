from Core.NetworkDetails import main as GetNetwork
from Core.ArpForging import main as attackTarget
from collections import defaultdict

def main():
    ipList = GetNetwork()
    vicitmChoice = int(input(f"Choose a vcitim ip : choose(0-{len(ipList)})"))
    attackTarget(ipList[vicitmChoice-1])
   


if __name__ == "__main__":
    main()
