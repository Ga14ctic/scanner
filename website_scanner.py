import requests
import argparse
from bs4 import BeautifulSoup
import subprocess

def get_server_version(url):
    try:
        response = requests.head(url)
        server_version = response.headers.get('Server')
        return server_version
    except Exception as e:
        print(f"Error: {e}")
        return None

def get_php_version(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        # Replace the following line with your specific logic to extract PHP version
        # This is just an example, and you might need to adjust it based on the website's structure
        php_version = soup.find('meta', {'name': 'generator'}).get('content')
        return php_version
    except Exception as e:
        print(f"Error: {e}")
        return None

def nmap_scan(url):
    try:
        result = subprocess.run(['nmap', '-F', url], capture_output=True, text=True)
        if "Nmap done" in result.stderr:
            # No open ports found
            return "No open ports found."
        else:
            return result.stdout
    except Exception as e:
        print(f"Error: {e}")
        return None

def main():
    parser = argparse.ArgumentParser(description="Website Scanner")
    parser.add_argument('-s', '--site', help='Website URL', required=True)
    parser.add_argument('-sv', '--server', action='store_true', help='Get server version')
    parser.add_argument('-p', '--php', action='store_true', help='Get PHP version')
    parser.add_argument('-a', '--all', action='store_true', help='Get all information')

    args = parser.parse_args()

    site_url = args.site

    if args.server or args.all:
        server_version = get_server_version(site_url)
        if server_version:
            print(f"Server Version: {server_version}")

    if args.php or args.all:
        php_version = get_php_version(site_url)
        if php_version:
            print(f"PHP Version: {php_version}")

    if args.all:
        nmap_result = nmap_scan(site_url)
        if nmap_result:
            print(f"Nmap Scan Results:\n{nmap_result}")

if __name__ == "__main__":
    main()
