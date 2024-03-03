
# WebScanner


WebScan Pro is a powerful penetration testing tool designed for web security assessments. It allows you to gather valuable information about a target website, including server version, PHP version, and performs a thorough nmap scan to unveil potential vulnerabilities.

## Features

- **Server Version Detection:** Identify the server software and version running on the target website.
- **PHP Version Detection:** Discover the PHP version used by the target website for in-depth analysis.
- **Comprehensive Nmap Scan:** Perform a detailed nmap scan to uncover potential security loopholes.

## Usage

```bash
python website_scanner.py -s example.com -sv -p -a
```

## Available Flags

-s or --site: Specify the target website URL.
-sv or --server: Get server version information.
-p or --php: Get PHP version information.
-a or --all: Get all available information, including nmap scan results.

## Installation

1. Clone the repository
```bash
git clone https://github.com/Ga14ctic/scanner
```
2. Install required python libraries
```bash
pip install -r requirements.txt
```
3. Install nmap
```bash
sudo apt-get install nmap
```

## Disclaimer

WebScanner is intended for legal and ethical use only. Unauthorized use of this tool is strictly prohibited. Use it responsibly and only on websites you have explicit permission to test.

## Contributing

We welcome contributions! If you find a bug or have an idea for an improvement, please open an issue or submit a pull request.
