# Python-Port-Scanner
# Simple Python Port Scanner

A lightweight, multithreaded port scanner written in Python for cybersecurity professionals, students, and network engineers. This script scans a target IP address or hostname to identify open TCP ports.

## Features

- Fast multithreaded scanning
- Scans ports 1 through 100 (customizable)
  Clean output with thread-safe console printing
- Easily extensible for larger port ranges or logging

## Example Usage

```bash
python simple_port_scanner.py
You can change the target and range in the script:

python
Copy
Edit
TARGET = "scanme.nmap.org"  # Safe test target from Nmap
PORT_RANGE = 100            # Number of ports to scan
THREADS = 100               # Number of concurrent threads
Disclaimer
This script is for educational and authorized use only. Do not scan devices or networks without explicit permission. Unauthorized scanning may violate local laws and network policies.
