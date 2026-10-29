packets = [
    {"source": "192.168.1.2", "destination": "8.8.8.8", "protocol": "UDP"},
    {"source": "192.168.1.2", "destination": "142.250.1.1", "protocol": "TCP"},
    {"source": "192.168.1.3", "destination": "8.8.8.8", "protocol": "UDP"},
    {"source": "192.168.1.4", "destination": "192.168.1.2", "protocol": "TCP"},
    {"source": "192.168.1.2", "destination": "8.8.8.8", "protocol": "DNS"}
]

tcp = 0
udp = 0
dns = 0

print("--- Network Traffic Analysis ---")

for packet in packets:
    print("Source:", packet["source"])
    print("Destination:", packet["destination"])
    print("Protocol:", packet["protocol"])
    print()

    if packet["protocol"] == "TCP":
        tcp += 1
    elif packet["protocol"] == "UDP":
        udp += 1
    elif packet["protocol"] == "DNS":
        dns += 1

print("Total Packets:", len(packets))
print("TCP Packets:", tcp)
print("UDP Packets:", udp)
print("DNS Packets:", dns)
print("Analysis Completed.")
