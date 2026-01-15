# ==========================================
# Universal Log Scanner (.log, .txt, .csv)
# ==========================================

import os
import csv
import re
import datetime

# Files to scan (add/remove as needed)
FILES_TO_SCAN = [
    "sample.log",
    "sample.txt",
    "sample.csv"  # replace with your real CSV filename
]

# Output report
REPORT_FILE = "scan_report.txt"

# Suspicious keywords (rules)
KEYWORDS = [
    "failed login",
    "unauthorized",
    "error",
    "brute force",
    "multiple failed"
]

# Regex for IP address detection
IP_REGEX = r"\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b"

start_time = datetime.datetime.now()

print("🔍 Log Scan Started")
print("=" * 40)

total_lines = 0
total_alerts = 0
ip_counter = {}

with open(REPORT_FILE, "w", encoding="utf-8") as report:
    report.write(f"Universal Log Scan Report\n")
    report.write(f"Scan Time: {start_time}\n")
    report.write("=" * 50 + "\n\n")

    for file in FILES_TO_SCAN:
        if not os.path.exists(file):
            print(f"❌ File not found: {file}")
            continue

        print(f"\n📂 Scanning file: {file}")
        report.write(f"\nScanning file: {file}\n")
        report.write("-" * 40 + "\n")

        # -------- CSV FILE --------
        if file.endswith(".csv"):
            with open(file, newline='', encoding="utf-8-sig") as csvfile:
                reader = csv.reader(csvfile, delimiter=',')  # Change to ';' if your CSV uses semicolon
                headers = next(reader, None)  # skip header row

                for row in reader:
                    # Assuming Message column is 3rd column (index 2)
                    if len(row) >= 3:
                        line = row[2]
                    else:
                        line = " ".join(row)

                    total_lines += 1
                    line_lower = line.lower()

                    # Check keywords
                    for keyword in KEYWORDS:
                        if keyword in line_lower:
                            total_alerts += 1
                            report.write(f"[ALERT] {line}\n")
                            print(f"[ALERT] {line}")

                    # IP extraction
                    ips = re.findall(IP_REGEX, line)
                    for ip in ips:
                        ip_counter[ip] = ip_counter.get(ip, 0) + 1

        # -------- LOG / TXT FILE --------
        else:
            with open(file, "r", encoding="utf-8-sig", errors="ignore") as f:
                for line in f:
                    total_lines += 1
                    line_lower = line.lower()

                    for keyword in KEYWORDS:
                        if keyword in line_lower:
                            total_alerts += 1
                            report.write(f"[ALERT] {line}")
                            print(f"[ALERT] {line.strip()}")

                    # IP extraction
                    ips = re.findall(IP_REGEX, line)
                    for ip in ips:
                        ip_counter[ip] = ip_counter.get(ip, 0) + 1

    # -------- SUMMARY --------
    report.write("\n" + "=" * 50 + "\n")
    report.write("Scan Summary\n")
    report.write(f"Total lines scanned: {total_lines}\n")
    report.write(f"Total alerts found: {total_alerts}\n\n")

    report.write("IP Address Activity:\n")
    for ip, count in ip_counter.items():
        report.write(f"{ip} -> {count} times\n")

end_time = datetime.datetime.now()

print("\n✅ Scan Completed")
print(f"📄 Total lines scanned: {total_lines}")
print(f"🚨 Total alerts found: {total_alerts}")
print("🌐 IP activity detected:")
for ip, count in ip_counter.items():
    print(f"   {ip} -> {count} times")

print(f"\n📝 Report saved as: {REPORT_FILE}")
print(f"⏰ Scan duration: {end_time - start_time}")
