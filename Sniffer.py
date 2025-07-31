import scapy.all as scapy
import re


def load_blocked_websites(file_path):
    with open(file_path, 'r') as file:
        blocked_websites = [line.strip() for line in file]
    return blocked_websites


def is_blocked(url, blocked_websites):
    for blocked_site in blocked_websites:
        if re.search(blocked_site, url):
            return True
    return False


def analyze_packet(packet, blocked_websites):
    url = None
    try:
        if packet.haslayer(scapy.Raw):
            load = packet[scapy.Raw].load.decode(errors="ignore")
            if "HTTP" in load:
                url_match = re.search(r'Host: (.*?)\r\n', load)
                if url_match:
                    url = url_match.group(1)
                    if is_blocked(url, blocked_websites):
                        print("[ALERT] Suspicious website access detected:", url)
                        return
        if url:
            print("[+] HTTP Request to:", url)
    except Exception as e:
        print("Error:", e)


def start_packet_capture(interface, blocked_websites):
    scapy.sniff(iface=interface, prn=lambda x: analyze_packet(x, blocked_websites), filter="tcp port 80")


def main():
    blocked_websites = load_blocked_websites("blocked_websites.txt")
    interface = "eth0"  # Change this to your network interface
    start_packet_capture(interface, blocked_websites)

if __name__ == "__main__":
    main()
