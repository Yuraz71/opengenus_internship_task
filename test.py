import requests
from bs4 import BeautifulSoup
import re


def check_for_wrong_domain(link, url):
    # Function: is current link contains another domain (True) or domain in URL (False) ?
    # Parameters: BS4 obect with link, str - URL
    domain_url = url.split('/')[2]
    if re.search(domain_url, str(link)):
        return False
    return True


def open_connect(url):
    # Function for open connect and get session object
    # Parameter: string - URL
    session = requests.Session()
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit 537.36 (KHTML, like Gecko) Chrome",
        "Accept": "text/html,application/xhtml+xml,application/xml; q=0.9,image/webp,*/*;q=0.8"}
    session_response = session.get(url, headers=headers)
    return session_response


def count_bytes(session_response):
    # Function for counting Size of the webpage in bytes
    # Parameter: Session object
    len_page = len(session_response.text)
    return len_page


def count_links(session_response, url):
    # Function for counting Number of links in that page pointing to same domain (find <a> tags)
    # Parameters: Session object, string - URL
    bsObj = BeautifulSoup(session_response.text, 'lxml')
    all_a = bsObj.find_all('a')
    wrong_domain = 0
    for link in all_a:
        # Function: is current link contains another domain (True) or domain in URL (False) ?
        # Parameters: BS4 obect with link, str - URL
        if check_for_wrong_domain(link, url):
            wrong_domain += 1
    count_a = len(all_a) - wrong_domain
    return count_a


if __name__ == '__main__':
    # Input URL for counting
    url = input('Please, enter URL for proceed: ')
    # Function for open connect and get session object
    # Parameter: string - URL
    session_response = open_connect(url.strip())
    # Function for counting Size of the webpage in bytes
    # Parameter: Session object
    len_page = count_bytes(session_response)
    # Function for counting Number of links in that page pointing to same domain (find <a> tags)
    # Parameters: Session object, string - URL
    number_of_links = count_links(session_response, url)
    # Output of results
    print('Size of the webpage is', str(len_page).strip(), 'bytes')
    print('Number of links on that page pointing to same domain is', str(number_of_links).strip())
