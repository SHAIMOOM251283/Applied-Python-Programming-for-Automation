import requests
import os
import bs4
from urllib.parse import urljoin
import threading

def download_comic(url):
    while not url.endswith('#'):
        # Download the page.
        print('Downloading page %s...' % url)
        res = requests.get(url)
        res.raise_for_status()
        soup = bs4.BeautifulSoup(res.text, 'html.parser')

        # Find the URL of the comic image.
        comicElem = soup.select('#comic img')

        if comicElem:
            comicUrl = comicElem[0].get('src')

            # Handle relative URLs
            comicUrl = urljoin(url, comicUrl)

            # Download the image.
            print('Downloading image %s...' % (comicUrl))
            res = requests.get(comicUrl)
            res.raise_for_status()

            # Save the image to ./xkcd.
            imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')

            for chunk in res.iter_content(100000):
                imageFile.write(chunk)

            imageFile.close()
        else:
            print('Could not find comic image.')

        # Get the Prev button's url.
        prevLink = soup.select('a[rel="prev"]')[0]
        url = 'https://xkcd.com' + prevLink.get('href')

def main():
    url = 'https://xkcd.com'  # starting url
    os.makedirs('xkcd', exist_ok=True)  # store comics in ./xkcd

    # Number of threads for downloading comics
    num_download_threads = 14  # or any other number suitable for your use case

    # Create a list to hold thread objects
    download_threads = []

    # Create download threads
    for i in range(0, 1400, 100):
        download_thread = threading.Thread(target=download_comic, args=(f'https://xkcd.com/{i}',))
        download_threads.append(download_thread)
        download_thread.start()

    # Wait for all download threads to finish
    for download_thread in download_threads:
        download_thread.join()

    print('Done.')

if __name__ == "__main__":
    main()
