# Bloodshot Guardians - DDoS Simulator

**Bloodshot Guardians** is an advanced, educational DDoS simulation tool designed for ethical penetration testing, network stress testing, and learning purposes only.

## ⚠️ IMPORTANT LEGAL DISCLAIMER

**This tool is provided STRICTLY FOR EDUCATIONAL AND ETHICAL PURPOSES ONLY.**

- It is intended **exclusively** for authorized testing on systems you own or have **explicit written permission** to test.
- Any use against third-party servers, networks, or services **without consent** is **illegal** and strictly prohibited.
- The authors, contributors, and maintainers of this project are **NOT RESPONSIBLE** for any misuse, damage, legal consequences, or violations resulting from the use of this tool.
- Always comply with local and international laws, including but not limited to the **Computer Fraud and Abuse Act (CFAA)**, **GDPR**, and all applicable cybercrime legislation.

**Use responsibly. Protect, don't destroy.**

## Features

- Multi-mode packet flooding simulation (specific port / random ports)
- Live statistics dashboard with real-time monitoring
- Target down detection with approximate downtime calculation
- Progress bar & detailed attack analytics
- Intensity level, botnet size simulation, power level, bandwidth usage & more
- Clean CTRL+C handling & safe exit

## Installation

```bash
apt update -y && apt upgrade -y
pkg install git
pkg install python3 -y
https://github.com/mdnurnobirazz/BloodshotGuardiansDDoS.git
cd BloodshotGuardiansDDoS
pip install tqdm
python3 RDDoS.py
```

## Usage
Select target (domain or IP)
Choose port mode
Start simulation
Monitor live stats
Press CTRL+C to safely stop
