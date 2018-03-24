from bs4 import BeautifulSoup
import requests
def extract_title(content):
    tag = set()
    soup = BeautifulSoup(content)
    tag = soup.find("title", text=True)
    
    if tag:
        return tag.string.strip()
    return None

def extract_text(content):
    links = set()
    soup = BeautifulSoup(content)
    
    for tag in soup.find_all('a', href=True):
        if tag['href'].startswith('http'):
            links.add(tag['href'])
    return links

def crawl(start_url):
    seen_urls = set([start_url])
    available_urls = set([start_url])

    while available_urls:
        url = available_urls.pop()

        try:
            content = requests.get(url, timeout=3).text
        except Exception:
            continue
        title = extract_title(content)
        if title:
            print(title)
            print(url + '\n\n')

        for link in extract_text(content):
            if link not in seen_urls:
                seen_urls.add(link)
                available_urls.add(link)

try:
    crawl('https://towardsdatascience.com/')
except KeyboardInterrupt:
    print('\n\nBye')