import requests
from bs4 import BeautifulSoup
import time
import sys
import random
import argparse

def bing_search(query):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/547.36 (KHTML, like Gecko) Chrome/53.0.3029.110 Safari/547.3'}
    url = f"https://www.bing.com/search?q={query}"
    response = requests.get(url, headers=headers)
    return response.text, url

def parse_results(html):
    soup = BeautifulSoup(html, 'html.parser')
    results = []
    for item in soup.find_all('li', class_='b_algo'):
        title = item.find('h2').text
        link = item.find('a')['href']
        description = item.find('p').text if item.find('p') else ''
        results.append({'title': title, 'link': link, 'description': description})
    return results

def read_file(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file]

def save_results(target, results, search_url):
    if results:
        #print(f"Found results for {target}")
        print(f"Search URL: {search_url}")
        return True
    return False

def main(file_path, mode):
    targets = read_file(file_path)
    found_any_result = False
    for target in targets:
        if mode == 'ip':
            query = f'ip:"{target}"'
        elif mode == 'subdomain':
            query = f'site:{target}'
        else:
            print(f"Invalid mode: {mode}")
            return

        print(f"Searching for {query}...")
        html, search_url = bing_search(query)
        results = parse_results(html)
        if save_results(target, results, search_url):
            found_any_result = True
        time.sleep(random.randrange(2, 4))  # Be polite and avoid being blocked by the search engine

    if not found_any_result:
        print("No results found")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Search for IP addresses or subdomains using Bing.")
    parser.add_argument("-u", "--file", required=True, help="Path to the file containing IPs or subdomains")
    parser.add_argument("-m", "--mode", choices=['ip', 'subdomain'], required=True, help="Search mode: 'ip' or 'subdomain'")
    args = parser.parse_args()

    main(args.file, args.mode)
