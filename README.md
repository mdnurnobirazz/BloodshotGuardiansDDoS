# Bloodshot Guardians - DDoS Simulator

**Bloodshot Guardians** is an educational and ethical penetration testing tool designed for simulating DDoS attacks in a controlled environment.

## ⚠️ IMPORTANT DISCLAIMER
- This tool is provided **FOR EDUCATIONAL PURPOSES ONLY**.
- It is strictly for **authorized ethical testing** on systems you own or have explicit permission to test.
- Any illegal use, including attacking third-party servers without consent, is **strictly prohibited**.
- The author and contributors are **NOT RESPONSIBLE** for any misuse or damage caused by this tool.
- Use this tool responsibly and in compliance with all applicable laws.

## Features
- Advanced packet flooding simulation
- Live statistics dashboard
- Target down detection
- Multi-port / random port modes
- Progress bar and detailed analytics

## Installation
```bash
apt update -y && apt upgrade -y
pkg install git
pkg install python3 -y
https://github.com/mdnurnobirazz/BloodshotGuardiansDDoS.git
cd BloodshotGuardiansDDoS
pip install tqdm
python3 RDDoS.py
