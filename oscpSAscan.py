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
import os

def get_args():
    parser = argparse.ArgumentParser(
        description="Run full TCP and UDP nmap scans for OSCP-style enumeration.",
        epilog="Examples:\n  python3 oscpSAscan.py -ip 192.168.1.10 -SA SA-Target\n  python3 oscpSAscan.py",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument("-ip", "--ip", type=str, help="Target IP address")
    parser.add_argument("-SA", "--sa", type=str, help="SA name for output file (will be folder name!)")
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

    outdir = machine_name
    if not os.path.exists(outdir):
        os.makedirs(outdir)

    # 1. First scan - non-sudo, output not saved permanently
    nmap_cmd1 = "nmap -v -p- -Pn -n --min-rate 5000 {} --open | awk '/^[0-9]+/ {{split($1, a, \"/\"); print a[1]}}' | paste -sd, - > .open_ports_tmp1.txt".format(ip)
    run_command(nmap_cmd1)

    # 2. Second scan - sudo, output not saved permanently
    nmap_cmd2 = "sudo nmap -v -p- -Pn -n --min-rate 5000 {} --open | awk '/^[0-9]+/ {{split($1, a, \"/\"); print a[1]}}' | paste -sd, - > .open_ports_tmp2.txt".format(ip)
    run_command(nmap_cmd2, sudo=True)

    # 3. Merge and sort (output only merged file)
    ports1 = read_ports_from_file(".open_ports_tmp1.txt")
    ports2 = read_ports_from_file(".open_ports_tmp2.txt")
    combined_ports = sorted(ports1.union(ports2), key=lambda x: int(x))

    # write merged ports to correct file in the new directory
    tcp_ports_path = os.path.join(outdir, "TCPopenports.txt")
    with open(tcp_ports_path, "w") as f:
        f.write(",".join(combined_ports))

    # cleanup temp files
    if os.path.exists(".open_ports_tmp1.txt"):
        os.remove(".open_ports_tmp1.txt")
    if os.path.exists(".open_ports_tmp2.txt"):
        os.remove(".open_ports_tmp2.txt")

    ports_str = ",".join(combined_ports)

    # 4. Full service scan, output file is <dir>/<machine_name>
    nmap_cmd3 = f"sudo nmap -p {ports_str} -sS -sC -sV -n -Pn {ip} -oN {os.path.join(outdir, machine_name)}"
    run_command(nmap_cmd3, sudo=True)

    # 5. Write IP file
    ip_path = os.path.join(outdir, "ip")
    with open(ip_path, "w") as f:
        f.write(ip + "\n")

    # 6. UDP scan, output is <dir>/UDPopenports.txt
    udp_path = os.path.join(outdir, "UDPopenports.txt")
    nmap_cmd4 = f"sudo nmap -Pn -n {ip} -sU --top-ports=100 --reason -oN {udp_path}"
    run_command(nmap_cmd4, sudo=True)

    print(f"\n[✓] All scans complete. Output saved to directory: {outdir}")
    print(f"  ├── TCPopenports.txt")
    print(f"  ├── {machine_name}")
    print(f"  ├── ip")
    print(f"  └── UDPopenports.txt\n")

if __name__ == "__main__":
    main()
