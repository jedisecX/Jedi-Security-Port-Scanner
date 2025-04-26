# Jedi-Security-Port-Scanner
Basic Port Scanner


Network Security Scanner

A Python-based tool for scanning open ports, detecting weak security configurations, and identifying vulnerabilities across networks. This scanner is designed for security professionals and network administrators to assess the security posture of their networks and identify potential risks.

Features

Port Scanning: Detect open ports and services running on a target system or subnet.

Vulnerability Detection: Match open ports/services with known CVEs (Common Vulnerabilities and Exposures).

Offline Mode: Scan with a local CVE database, enabling offline vulnerability detection.

Multi-Target Scanning: Scan entire subnets or multiple IP addresses simultaneously.

Advanced Scan Modes: Includes stealth and SYN scan options to avoid detection.

Dynamic Reporting: Generate exportable PDF and HTML reports containing scan results, vulnerabilities, and recommendations.

Interactive Web Dashboard: Visualize scan results in an interactive web-based dashboard.


Requirements

Python 3.6+

Required libraries:

nmap or scapy for service detection

requests for fetching data from online databases

License

This project is licensed under the MIT License - see the LICENSE file for details.
