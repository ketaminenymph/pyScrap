import whatismyip
import requests
import random
from bs4 import BeautifulSoup

ip = whatismyip.whatismyipv4()
url = 'https://iknowwhatyoudownload.com/en/peer/?ip=' + ip
A = ("Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36",
       "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.1 Safari/537.36",
       "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36",
       )

Agent = A[random.randrange(len(A))]
headers = {'user-agent': Agent}
r = requests.get(url, headers=headers)

soup = BeautifulSoup(r.content, 'html.parser')
mydiv = soup.find_all("thead", class_='header-torrents')
nameTag = soup.find_all("div", class_='torrent_files')


if __name__ == "__main__":
    print("\nPeer IP: " + ip)
    print('\nTorrent Filenames: ')
    for div in nameTag:
        print(div.a.contents[0])
        break
    else:
        print("No public IP torrents found")




