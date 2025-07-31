# 🛡️ Network Sniffer & Website Blocker

A Python-based tool to monitor and detect HTTP requests to suspicious or blocked domains using live packet sniffing. Built using Scapy, this project simulates a lightweight intrusion detection mechanism.

---

## 🔍 Features

- 📡 Live packet capture on specified network interface
- 🌐 HTTP request extraction and domain analysis
- 🚫 URL filtering based on a user-defined blocked list
- 🧠 Regex-based pattern matching for flexible domain filtering
- ⚙️ Terminal output of detected threats and normal traffic

---

## 🧰 Technologies Used

- Python
- [Scapy](https://scapy.net/)
- Regular Expressions (re module)

---
   ```bash
## 📁 File Structure

.
├── main.py # Packet sniffer and analyzer
├── blocked_websites.txt # List of domains to block (one per line)
└── README.md # Project documentation

yaml
Copy
Edit
```
---

## ▶️ How to Run

1. **Install Scapy:**
   ```bash
   pip install scapy
Update the blocked websites list:
Add one domain per line in blocked_websites.txt, e.g.

   ```bash
facebook.com
youtube.com
```
---
Run the script:

Replace eth0 with your actual network interface (e.g., wlan0 or Wi-Fi)

```bash
Copy
Edit
sudo python main.py
