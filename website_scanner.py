import requests
import argparse
from bs4 import BeautifulSoup

def get_server_version(url):
    try:
        response = requests.head(url)
        server_version = response.headers.get('Server')
        return server_version
    except Exception as e:
        print(f"Error: {e}")
        return None

def get_additional_info(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        # Add more scraping logic here to extract additional information
        # For example, extracting PHP version or any other details you're interested in
        # Replace the following line with your specific logic
        additional_info = "Additional information not implemented yet"
        return additional_info
    except Exception as e:
        print(f"Error: {e}")
        return None

def main():
    parser = argparse.ArgumentParser(description="Website Scanner")
    parser.add_argument('-s', '--site', help='Website URL', required=True)
    parser.add_argument('-sv', '--server', action='store_true', help='Get server version')
    parser.add_argument('-a', '--all', action='store_true', help='Get all information')

    args = parser.parse_args()

    site_url = args.site

    if args.server or args.all:
        server_version = get_server_version(site_url)
        if server_version:
            print(f"Server Version: {server_version}")

    if args.all:
        additional_info = get_additional_info(site_url)
        if additional_info:
            print(f"Additional Information: {additional_info}")

if __name__ == "__main__":
    main()
