
# oscpSAscan.py

A focused and effective Nmap automation tool for OSCP-style enumeration.

---

## 🔥 Why this script?

Created by **Yehonatan Sion / J4c0b_1337** to automate enumeration on **Service-Assisted (SA)** OSCP machines.  
Fast, thorough, and gets you exactly what you need — nothing יותר, כלום פחות.

---

## ⚠️ Important Note on `sudo` Permissions

> **Don’t add `nmap` ל-sudoers.**  
זה מפתה, אבל פותח חור לאבטחה. עדיף להכניס את הסיסמה בעצמך, תמיד.

---

## ⚙️ Features

- Full TCP port scan (fast)
- Merges open ports from sudo/non-sudo scans
- Service detection on found ports
- UDP top 100 port scan
- CLI *or* interactive usage
- Clean output, auto-deletes זמני
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

All results in a folder called <SA name>:

```text
<SA name>/
├── TCPopenports.txt   # Merged/sorted open TCP ports (comma-separated)
├── <SA name>         # Full nmap service scan output
├── ip                # The target IP address (single line)
└── UDPopenports.txt  # UDP top 100 scan (nmap format)
```
*כל קבצי ביניים נמחקים אוטומטית.*

---

## 💀 Disclaimer

מיועד אך ורק ל*בדיקות מורשות* (OSCP, לקוח שאישר וכו').  
אם תסרוק משהו בלי רשות — בעיה שלך.

---

## 🧠 Tip

השתמש עם:
```bash
gobuster
nikto
smbclient
enum4linux
```
ותהיה מוכן לאוסי-אס-פי, בלי שטויות.

---

Made with blood, sweat, and reverse shells.
