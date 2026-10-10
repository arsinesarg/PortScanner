# PortScanner

A lightweight, multi-threaded TCP port scanner built in Python. Designed for speed and efficiency, it allows quick infrastructure reconnaissance and service detection across custom port ranges.

## Features

* **Multi-threaded Scanning:** Utilizes Python's ThreadPoolExecutor for concurrent and fast port checking.
* **Service Detection:** Automatically attempts to identify running services on open ports.
* **Flexible Configuration:** Easily adjustable target specification, custom port ranges, and thread count limits.
* **Clean Output:** Clear, structured status reports with execution timestamps.

## Requirements

* Python 3.x (no external third-party libraries required).

## Usage

Run the script from the command line by passing the target IP address or domain:

python scanner.py <target_ip_or_domain>

### Options

* `-p`, `--ports`: Specify a port range (default: 1-1024).
* `-t`, `--threads`: Set the number of concurrent threads (default: 100).

### Examples

Scan default ports (1-1024) on a local machine:
python scanner.py 127.0.0.1

Scan a custom port range with 50 threads:
python scanner.py scanme.nmap.org -p 1-500 -t 50
