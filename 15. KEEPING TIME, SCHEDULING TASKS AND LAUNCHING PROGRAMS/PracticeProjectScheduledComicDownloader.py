import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# Function to download an image
def download_image(url, folder_path):
    response = requests.get(url)
    if response.status_code == 200:
        image_name = url.split("/")[-1]
        file_path = os.path.join(folder_path, image_name)
        with open(file_path, 'wb') as f:
            f.write(response.content)
        print(f"Downloaded: {image_name}")
    else:
        print(f"Failed to download image from {url}")

# Function to check and download updated comics
def check_and_download_comics(url, folder_path, last_visit_info):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        comic_image = soup.find('img')

        if comic_image:
            comic_url = urljoin(url, comic_image['src'])
            comic_date = comic_image['alt']

            if comic_date != last_visit_info.get(url, ''):
                download_image(comic_url, folder_path)
                last_visit_info[url] = comic_date
                print(f"Updated comic found on {url}")
            else:
                print(f"No updated comics on {url}")
        else:
            print(f"No comic image found on {url}")
    else:
        print(f"Failed to access {url}")

# Main function
def main():
    base_folder = 'downloadedcomics'
    if not os.path.exists(base_folder):
        os.makedirs(base_folder)

    # Dictionary to store last visit information for each website
    last_visit_info = {}

    websites = [
        #"https://www.buttersafe.com/",
        "https://www.savagechickens.com/"
    ]

    for website in websites:
        check_and_download_comics(website, base_folder, last_visit_info)

    # Save last visit information to a file for future use
    with open('last_visit_info.txt', 'w') as f:
        for url, date in last_visit_info.items():
            f.write(f"{url} {date}\n")

if __name__ == "__main__":
    main()
