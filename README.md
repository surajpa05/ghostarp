<img width="1014" height="653" alt="image" src="https://github.com/user-attachments/assets/f7889c4c-8078-4399-bac8-c1d397842a27" />

# GhostARP

> **"Packets lie. We listen."**

An educational Layer 2 networking research tool focused on ARP behavior, Ethernet communication, packet crafting, and local network experimentation using Python and Scapy.

---

## ⚠️ Legal Disclaimer

**FOR EDUCATIONAL AND AUTHORIZED TESTING PURPOSES ONLY**

GhostARP was built to study:
- ARP cache behavior
- Ethernet frame delivery
- Layer 2 trust relationships
- Packet crafting
- Local network communication

Unauthorized interception, disruption, or manipulation of network traffic may violate local laws and regulations.

Only use this project:
- on networks you own
- in lab environments
- or where you have explicit authorization

You are solely responsible for how you use this software.

---

## 📚 Learning Objectives

This project was created to better understand:

- Ethernet frame delivery
- ARP request/reply mechanics
- ARP cache behavior
- Layer 2 vs Layer 3 networking
- Packet crafting with Scapy
- Network discovery techniques
- Protocol trust assumptions
- Local network traffic flow

---

## 🎯 Overview

GhostARP is a Python-based Layer 2 networking tool designed for studying ARP communication and local network behavior.

The project includes:
- ARP-based host discovery
- MAC address vendor identification
- Interactive terminal UI
- Layer 2 packet crafting
- ARP cache manipulation experiments
- Automatic ARP cache restoration

The focus of the project is educational understanding rather than offensive automation.

---

## ✨ Features

### 🔍 Network Discovery
- ARP-based local network scanning
- Automatic subnet detection
- Active host identification
- IP ↔ MAC mapping
- Vendor identification using OUI lookup

### 🧪 ARP Experimentation
- Layer 2 packet crafting with Scapy
- ARP reply generation
- Gateway identification
- ARP cache restoration on exit

### 🎨 Terminal Interface
- Interactive CLI menus
- ASCII art banners
- Colorized output
- Persistent scan result display
- Dynamic terminal sizing

### 🛡️ Safety Features
- Automatic cleanup on Ctrl+C
- Exception handling
- Input validation
- Graceful recovery logic

---

## 🔬 How It Works

### 1. Discovery Phase

GhostARP performs host discovery using ARP broadcasts.

The scanner:
1. Sends ARP requests across the subnet
2. Receives replies from active hosts
3. Maps IP addresses to MAC addresses
4. Resolves vendors using OUI lookup

Example:

```text
Who has 192.168.1.1?
```

Response:

```text
192.168.1.1 is at aa:bb:cc:dd:ee:ff
```

---

### 2. ARP Cache Behavior

Devices maintain temporary ARP caches that store:

```text
IP Address → MAC Address
```

Example:

```text
192.168.1.1 → bc:62:d2:d9:d3:78
```

These mappings allow Ethernet frames to be delivered locally.

---

### 3. Packet Structure

Example ARP reply structure:

```text
Ethernet Frame:
  dst: [Target MAC]

ARP Packet:
  op: 2 (ARP Reply)
  psrc: [Claimed IP]
  hwsrc: [Claimed MAC]
  pdst: [Target IP]
  hwdst: [Target MAC]
```

---

## 🧠 Important Networking Concepts

### Layer Separation

| Layer | Responsibility |
|---|---|
| IP | Logical routing |
| MAC | Local frame delivery |
| ARP | IP ↔ MAC resolution |

---

### Why ARP Matters

ARP acts as the bridge between:

```text
IP Layer → Ethernet Layer
```

Without ARP:
- IP knows where traffic should go
- Ethernet does not know which MAC should receive frames

---

## 📦 Installation

### Requirements

- Linux
- Python 3.12+
- Root privileges
- Scapy

---

### Clone Repository

```bash
git clone https://github.com/yourusername/GhostARP.git
cd GhostARP
```

---

### Install Dependencies

Using uv:

```bash
uv sync
```

Using pip:

```bash
pip install -r requirements.txt
```

---

## 🚀 Usage

Run GhostARP:

```bash
sudo python main.py
```

---

### Workflow

1. Select network interface
2. Scan local subnet
3. Review discovered hosts
4. Select target for experimentation
5. Observe ARP behavior
6. Exit safely with automatic restoration

---

## 📁 Project Structure

```text
GhostARP/
├── main.py
├── Core/
│   ├── ArpForging.py
│   ├── NetworkDetails.py
│   └── utils/
│       ├── Banner.py
│       └── Display.py
├── pyproject.toml
├── uv.lock
└── README.md
```

---

## 🔧 Technical Details

### Core Technologies

| Technology | Purpose |
|---|---|
| Python | Main language |
| Scapy | Packet crafting |
| InquirerPy | Interactive CLI |
| psutil | System information |
| netifaces | Interface enumeration |

---

### ARP Characteristics

ARP has:
- no authentication
- no integrity verification
- temporary cache-based trust

This behavior makes ARP extremely important for understanding local network communication.

---

## ⚠️ Limitations

### Current Limitations

- IPv4 only
- Linux focused
- Single-target experimentation
- No GUI
- No IPv6/NDP support

---

### Educational Focus

GhostARP prioritizes:
- protocol understanding
- packet visibility
- networking fundamentals

over:
- stealth
- automation
- large-scale deployment

---

## 📖 Educational Resources

### Learn More

- RFC 826 — ARP Specification
- Scapy Documentation
- Ethernet Frame Structure
- Linux Neighbor Discovery
- ARP Cache Management

---


## 📄 License

MIT License

---

## 👤 Author

**Suraj P A**  
Cybersecurity & Networking Enthusiastic

---


## Final Note

GhostARP was built as a learning-focused networking project to better understand how local networks actually function beneath the abstraction layers most applications hide.

Understanding packets is understanding the network itself.

---

