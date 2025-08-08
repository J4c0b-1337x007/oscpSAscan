
# oscpSAscan.py

A focused and effective Nmap automation tool for OSCP-style enumeration.

---

## 🔥 Why this script?

Created by **Yehonatan Sion / J4c0b_1337** to automate service enumeration for **Service-Assisted (SA)** OSCP machines.  
It’s fast, thorough, and gives you exactly what you need to start exploiting quickly.

---

## ⚠️ Important Note on `sudo` Permissions

> **Don’t add `nmap` to your sudoers file.**  
It’s tempting, but you’re just opening yourself up to unnecessary risk.  
Enter your sudo password manually, and keep your box safe.

---

## ⚙️ Features

- Full fast TCP port scan
- Merges open ports from sudo/non-sudo scans
- Service detection on discovered ports
- UDP top 100 port scan
- Flexible CLI and interactive usage
- Clean and organized output
- Auto-cleans temp files
- ASCII banner

---

## 🚀 Usage

```bash
# Run with CLI arguments
python3 oscpSAscan.py -ip <target IP> -SA <output name>
# Example
python3 oscpSAscan.py -ip 192.168.170.122 -SA Hutch

# Run in interactive mode (will prompt you)
python3 oscpSAscan.py
# Prompts:
# Enter target IP address:
# Enter machine name:
```

---

## 📂 Output

All results are saved in a folder named after the value you provide to -SA (the machine name):

```text
<SA name>/
├── TCPopenports.txt   # Merged/sorted open TCP ports (comma-separated)
├── <SA name>         # Full nmap service scan output
├── ip                # The target IP address (single line)
└── UDPopenports.txt  # UDP top 100 scan (nmap format)
```
*Temporary files are auto-deleted.*

---

## 💀 Disclaimer

This tool is for authorized testing and training only (like the OSCP exam).  
Do **not** use it on targets you don’t have permission to scan.

---

## 🧠 Tip

Pair this script with:
```bash
gobuster
nikto
smbclient
enum4linux
```
And you’ll be OSCP-ready.

---

Made with blood, sweat, and reverse shells.
