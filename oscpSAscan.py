####################################################################################################
####################################################################################################
####################################################################################################
##############PJ!^^:^^!JP#######P?~^::^!YB######GY7~^::^!?P#####Y!!!~~!!7YG#########################
############5~  .~!7!~.  ^Y###B!  :7??~  .5###B7.  ^!77~:  ^5###7  .!!!~.  !B#####BPPB##############
###########J  .JB#####B5:  7##P  .G&&&&57!J##B^  !G######Y.  P##7  ~&###B~  7####&Y  Y&#############
##########B.  Y&#######&P   P#B!  :!7??YP#&##J  :B########GPPG##7  ~&###B^  7#GPPP7  ?PPPB##########
##########B.  P#########B.  5###P?!^^::  .7B#?  ^###############7  :!!!~.  !B#J....  ....Y##########
###########7  ^G#######B!  ~B#5YYB&####B^  ?&G.  J########7::?##7  .!!!!7YG###BBBBJ  JBBBB##########
############?.  !J5P5Y7.  !B##?  :YPGGPJ.  5##P:  ^J5P55?^  ~B##7  ~&#############Y..5##############
#############G?~.     .^?P#####5!:  .. .:7P####BY!:     .:75####?..!##############BBBB##############
################BGPPPGB##########BGPPPGB##########BGGPPGB#######BBBB################################
####################################################################################################
####################################################################################################
####################################################################################################

# This script was created by Yehonatan Sion / J4c0b_1337


#!/usr/bin/env python3

import subprocess
import argparse
import sys

def get_args():
    parser = argparse.ArgumentParser(
        description="Run full TCP and UDP nmap scans for OSCP-style enumeration.",
        epilog="Examples:\n  python3 oscpSAscan.py -ip 192.168.1.10 -SA SA-Target\n  python3 oscpSAscan.py",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument("-ip", "--ip", type=str, help="Target IP address")
    parser.add_argument("-SA", "--sa", type=str, help="SA name for output file")

    args = parser.parse_args()

    if not args.ip or not args.sa:
        print("[*] No full CLI input provided. Switching to interactive mode.")
        args.ip = input("Enter target IP address: ").strip()
        args.sa = input("Enter machine name: ").strip()

    return args

def run_command(cmd, sudo=False):
    if sudo:
        print("[!] This command requires sudo privileges.")
    subprocess.run(cmd, shell=True, executable="/bin/bash")

def read_ports_from_file(file_path):
    try:
        with open(file_path, "r") as f:
            ports_line = f.read().strip()
            if ports_line:
                return set(ports_line.split(","))
            return set()
    except FileNotFoundError:
        print(f"[!] File not found: {file_path}")
        return set()

def main():
    print("""
####################################################################################################
####################################################################################################
####################################################################################################
##############PJ!^^:^^!JP#######P?~^::^!YB######GY7~^::^!?P#####Y!!!~~!!7YG#########################
############5~  .~!7!~.  ^Y###B!  :7??~  .5###B7.  ^!77~:  ^5###7  .!!!~.  !B#####BPPB##############
###########J  .JB#####B5:  7##P  .G&&&&57!J##B^  !G######Y.  P##7  ~&###B~  7####&Y  Y&#############
##########B.  Y&#######&P   P#B!  :!7??YP#&##J  :B########GPPG##7  ~&###B^  7#GPPP7  ?PPPB##########
##########B.  P#########B.  5###P?!^^::  .7B#?  ^###############7  :!!!~.  !B#J....  ....Y##########
###########7  ^G#######B!  ~B#5YYB&####B^  ?&G.  J########7::?##7  .!!!!7YG###BBBBJ  JBBBB##########
############?.  !J5P5Y7.  !B##?  :YPGGPJ.  5##P:  ^J5P55?^  ~B##7  ~&#############Y..5##############
#############G?~.     .^?P#####5!:  .. .:7P####BY!:     .:75####?..!##############BBBB##############
################BGPPPGB##########BGPPPGB##########BGGPPGB#######BBBB################################
####################################################################################################
####################################################################################################
####################################################################################################
""")
    print("[*] This script was created by Yehonatan Sion / J4c0b_1337\n")
    args = get_args()
    ip = args.ip
    machine_name = args.sa

    print(f"\n[+] Running first scan on {ip} (without sudo)...")
    nmap_cmd1 = f"nmap -v -p- -Pn -n --min-rate 5000 {ip} --open | awk '/^[0-9]+/ {{split($1, a, \"/\"); print a[1]}}' | paste -sd, - > open_ports.txt"
    run_command(nmap_cmd1)

    print(f"[+] Running second scan on {ip} (with sudo)...")
    nmap_cmd2 = f"sudo nmap -v -p- -Pn -n --min-rate 5000 {ip} --open | awk '/^[0-9]+/ {{split($1, a, \"/\"); print a[1]}}' | paste -sd, - > open_ports2.txt"
    run_command(nmap_cmd2, sudo=True)

    print("[*] Merging ports from open_ports.txt and open_ports2.txt...")
    ports1 = read_ports_from_file("open_ports.txt")
    ports2 = read_ports_from_file("open_ports2.txt")
    combined_ports = sorted(ports1.union(ports2), key=lambda x: int(x))

    with open("open_ports3.txt", "w") as f:
        f.write(",".join(combined_ports))

    print("[+] Combined ports saved to open_ports3.txt\n")

    ports_str = ",".join(combined_ports)

    print(f"[+] Running third scan on merged TCP ports...")
    nmap_cmd3 = f"sudo nmap -p {ports_str} -sS -sC -sV -n -Pn {ip} -oN {machine_name}"
    run_command(nmap_cmd3, sudo=True)

    print(f"[✓] Third scan completed. Output saved to: {machine_name}")

    print(f"\n[+] Running UDP top 100 ports scan on {ip}...")
    nmap_cmd4 = f"sudo nmap -Pn -n {ip} -sU --top-ports=100 --reason -oN udpports.txt"
    run_command(nmap_cmd4, sudo=True)

    print(f"[✓] UDP scan completed. Output saved to: udpports.txt\n")

if __name__ == "__main__":
    main()