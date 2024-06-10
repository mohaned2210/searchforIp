import requests
from bs4 import BeautifulSoup
import time
import sys

def bing_search(query):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    url = f"https://www.bing.com/search?q={query}"
    response = requests.get(url, headers=headers)
    return response.text

def parse_results(html):
    soup = BeautifulSoup(html, 'html.parser')
    results = []
    for item in soup.find_all('li', class_='b_algo'):
        title = item.find('h2').text
        link = item.find('a')['href']
        description = item.find('p').text if item.find('p') else ''
        results.append({'title': title, 'link': link, 'description': description})
    return results

def read_ips(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file]

def save_results(ip, results):
    if results:
        with open(f"{ip}_results.txt", 'w') as file:
            for result in results:
                file.write(f"Title: {result['title']}\n")
                file.write(f"Link: {result['link']}\n")
                file.write("\n")
        print(f"Find result for IP {ip}")
        return True
    return False

def main(file_path):
    ips = read_ips(file_path)
    found_any_result = False

    for ip in ips:
        query = f'ip:"{ip}"'
        print(f"Searching for {query}...")
        html = bing_search(query)
        results = parse_results(html)
        if save_results(ip, results):
            found_any_result = True
        time.sleep(5)  # Be polite and avoid being blocked by the search engine

    if not found_any_result:
        print("No result found")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 dorkforipBing.py <path_to_ip_file>")
        sys.exit(1)
    
    file_path = sys.argv[1]
    main(file_path)
