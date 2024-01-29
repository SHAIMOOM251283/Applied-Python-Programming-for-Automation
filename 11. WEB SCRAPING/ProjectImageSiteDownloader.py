import requests
import os
import bs4
from urllib.parse import urljoin

url = 'https://imgur.com/search?q=fireworks'  # starting url for fireworks search
os.makedirs('imgur_fireworks', exist_ok=True)  # store fireworks images in ./imgur_fireworks
max_images_to_download = 5
image_count = 0

while not url.endswith('#') and image_count < max_images_to_download:
    # Download the page.
    print('Downloading page %s...' % url)
    res = requests.get(url)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'html.parser')

    # Find the URLs of the images.
    image_elems = soup.select('.image-list-link img')

    for image_elem in image_elems:
        image_url = image_elem.get('src')

        # Handle relative URLs
        image_url = urljoin(url, image_url)

        # Download the image.
        print('Downloading image %s...' % (image_url))
        res = requests.get(image_url)
        res.raise_for_status()

        # Save the image to ./imgur_fireworks.
        image_file = open(os.path.join('imgur_fireworks', os.path.basename(image_url)), 'wb')

        for chunk in res.iter_content(100000):
            image_file.write(chunk)

        image_file.close()

        image_count += 1

        if image_count >= max_images_to_download:
            break

    # Get the next page's url.
    next_page_elem = soup.select('a.paginationNext')

    if next_page_elem:
        url = 'https://imgur.com' + next_page_elem[0].get('href')
    else:
        print('No more pages available.')
        break

print('Done.')


