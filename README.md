# Universal Log Scanner (Python)

Universal Log Scanner is a Python-based security automation tool that scans
`.log`, `.txt`, and `.csv` files to detect suspicious activities such as
failed logins, unauthorized access, errors, and brute-force attempts.
It also extracts attacker IP addresses and generates a scan report.

This tool is inspired by basic SIEM / SOC log analysis concepts (like Splunk).

---

## Features

- Supports `.log`, `.txt`, and `.csv` files
- Works with Windows Server exported CSV logs
- Keyword-based suspicious activity detection
- IP address extraction and counting
- Automatic scan report generation
- Simple and beginner-friendly

---

## How This Tool Works

1. The tool reads log files line by line  
2. Each log entry is checked against predefined suspicious keywords  
3. If a match is found, it is marked as an alert  
4. IP addresses are extracted using regex  
5. A summary report is generated showing:
   - Total lines scanned
   - Total alerts found
   - IP address activity

---

## Supported Keywords (Default Rules)

- failed login
- unauthorized
- error
- brute force
- multiple failed

You can add or remove keywords in the code as needed.

---

## Requirements

- Python 3.8 or higher
- Works on Windows, Linux, and macOS

Check Python installation:
```bash
python --version


## How to Run the Tool

### Step 1: Open Terminal / PowerShell
- Windows: Press `Win + R` → type `cmd` or `powershell` → Enter
- Linux / macOS: Open Terminal

---

### Step 2: Go to the Project Folder
Use the `cd` command to navigate to the folder where the project is extracted.

Example (Windows):
```bash
cd F:\universal-log-scanner


# Example (Linux / macOS):
cd /home/user/universal-log-scanner


# Run the Script
# Execute the Python file using the following command:
python log_scanner.py


#Check the Results
#Alerts will appear in the terminal
#A report file named scan_report.txt will be created in the same folder
#Example Output

[ALERT] Failed login attempt from IP 192.168.1.10
Scan Completed
Total lines scanned: 120
Total alerts found: 5


View the Report

Open scan_report.txt in any text editor to see the full scan summary.


---

## 🧠 One-line explanation (simple)
> Download → Extract → Open terminal → `cd` into folder → `python log_scanner.py`

---

## ✅ Ab README me ye cover ho gaya:
- ✔ Run command  
- ✔ Folder navigation  
- ✔ Windows / Linux / macOS  
- ✔ Output location  

