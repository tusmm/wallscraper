"""
get wallpapers from websites
"""

import requests 
from bs4 import BeautifulSoup 
import os

def getUserInput():
    search = input('Please enter the category of your search: ').replace(" ", '+')
    url = 'https://wallhaven.cc/search?q=' + search
    return url, search

def imagedown(url, folder):
    path = os.getcwd()
    parentDir = os.path.abspath(os.path.join(path, os.pardir))
    try:
        os.mkdir(os.path.join(parentDir, folder))
    except:
        print("Error making directory")

    os.chdir(os.path.join(parentDir, folder))
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    
    print("Beginning image download...")
    # prints the tite of the site
    print(soup.title.text)

    figures = soup.find_all('figure')
    href = []
    for figure in figures:
        h = figure.find('a').get('href')
        href.append(h)

    fileCounter = 0
    for h in href:
        r = requests.get(str(h))
        soup = BeautifulSoup(r.text, 'html.parser')
        image = soup.find('img', id="wallpaper")
        if image is None: # fixme: if an image is a png
            continue
        else:
            image = image.get('src')
        
        with open(search + str(fileCounter) + '.jpg', 'wb') as f:
            im = requests.get(image)
            f.write((im.content))

        if fileCounter % 3 == 0:
            print("Downloading images...")

        fileCounter += 1
    print("Finished downloading!")

if __name__ == "__main__":
    url, search = getUserInput()
    imagedown(url, search)
