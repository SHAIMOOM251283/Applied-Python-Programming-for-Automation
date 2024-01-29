import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def get_links(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        links = [urljoin(url, a.get('href')) for a in soup.find_all('a', href=True)]
        return links
    else:
        print(f"Failed to retrieve links from {url}. Status code: {response.status_code}")
        return []

def check_links(links):
    broken_links = []
    for link in links:
        response = requests.get(link)
        if response.status_code == 404:
            broken_links.append(link)
            print(f"Broken link: {link}")
    return broken_links

def main():
    url = input("Enter the URL of the web page: ")
    links = get_links(url)
    
    if links:
        print(f"\nChecking {len(links)} links...\n")
        broken_links = check_links(links)

        if not broken_links:
            print("All links are working.")
    else:
        print("No links found on the given page.")

if __name__ == "__main__":
    main()
