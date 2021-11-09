from scapy.all import ARP, Ether, srp

target_ip = str(input("TARGET IP >> "))

arp = ARP(pdst=str(target_ip))
ether = Ether(dst="ff:ff:ff:ff:ff:ff")
packet = ether/arp

result = srp(packet, timeout=3)[0]

clients = []

for sent,received in result:
	clients.append({"ip": received.psrc, "mac":received.hwsrc})

print("Available clients in the network: ")
print("IP"+" "*18+"MAC")
for client in clients:
    print("{:16}    {}".format(client['ip'], client['mac']))