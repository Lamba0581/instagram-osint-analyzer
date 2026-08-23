from scapy.all import sniff, IP, TCP, UDP, ICMP, Raw
from datetime import datetime


def analyze_packet(packet):
    if not packet.haslayer(IP):
        return

    ip = packet[IP]
    print("\n" + "=" * 60)
    print("Time       :", datetime.now().strftime("%H:%M:%S"))
    print("Source IP  :", ip.src)
    print("Dest IP    :", ip.dst)

    if packet.haslayer(TCP):
        print("Protocol   : TCP")
        print("Source Port:", packet[TCP].sport)
        print("Dest Port  :", packet[TCP].dport)
    elif packet.haslayer(UDP):
        print("Protocol   : UDP")
        print("Source Port:", packet[UDP].sport)
        print("Dest Port  :", packet[UDP].dport)
    elif packet.haslayer(ICMP):
        print("Protocol   : ICMP")
    else:
        print("Protocol   :", ip.proto)

    print("Packet Size:", len(packet), "bytes")

    if packet.haslayer(Raw):
        payload = bytes(packet[Raw].load)
        preview = "".join(chr(b) if 32 <= b <= 126 else "." for b in payload[:50])
        print("Payload    :", preview)


print("Basic Network Packet Sniffer")
print("Authorized/educational use only. Press Ctrl+C to stop.")

try:
    sniff(filter="ip", prn=analyze_packet, store=False)
except KeyboardInterrupt:
    print("\nPacket capture stopped.")
