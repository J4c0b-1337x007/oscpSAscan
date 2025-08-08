# oscpSAscan.py

A focused and effective Nmap automation tool for OSCP-style enumeration.

## 🔥 Why this script?

This script was created by **Yehonatan Sion / J4c0b_1337** to help automate service enumeration for **Service-Assisted (SA)** machines during OSCP training and the exam.

It's designed to be:
- ✅ Not too bloated
- ✅ Not too shallow
- ✅ Just right for scanning and enumerating SA boxes

It merges speed and completeness, giving you exactly what you need to start exploiting quickly — without wasting time or missing services.

---

## ⚙️ Features

- Full TCP port scan (top speed)
- Merges open ports from **non-sudo** and **sudo** scans
- Service detection on discovered ports
- UDP top 100 port scan
- Flexible: use via CLI or interactively
- Clean and readable output files
- ASCII banner (hell yeah 😎)

---

## 🚀 Usage

### 1. 📥 Add `nmap` to `/etc/sudoers` (no password required)

You must allow `nmap` to be run via sudo without being prompted for a password.

**Run this:**
```bash
echo "kali ALL=(ALL) NOPASSWD: /usr/bin/nmap" | sudo tee /etc/sudoers.d/nmap
sudo chmod 440 /etc/sudoers.d/nmap
```

---

### 2. 🧠 Run the script in one of two ways:

#### ✅ Method 1: With CLI arguments

```bash
python3 oscpSAscan.py -ip <target IP> -SA <output name>
```

Example:
```bash
python3 oscpSAscan.py -ip 192.168.170.122 -SA Hutch
```

#### ✅ Method 2: Interactive mode

Just run:
```bash
python3 oscpSAscan.py
```

And it will prompt:
```
Enter target IP address:
Enter machine name:
```

---

## 📂 Output Files

- `open_ports.txt` (non-sudo fast TCP scan)
- `open_ports2.txt` (sudo fast TCP scan)
- `open_ports3.txt` (merged and sorted ports)
- `<SA name>` (service detection scan)
- `udpports.txt` (UDP top 100 scan)

---

## 💀 Disclaimer

This tool was made for training and authorized penetration testing (like the OSCP exam). Do not use it on targets you don’t have permission to scan.

---

## 🧠 Tip

Pair this with:
- `gobuster`
- `nikto`
- `smbclient`, `enum4linux`, etc.

And you’ll be OSCP-ready as hell.

---

Made with blood, sweat, and reverse shells.
