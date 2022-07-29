<<<<<<< HEAD
"""
get top wallpapers from websites
"""

from fileinput import filename
import requests 
from bs4 import BeautifulSoup 
import os

search = input('Please enter the category of your search: ').replace(" ", '+')
url = 'https://wallhaven.cc/search?q=' + search

r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')

#prints the tite of the site
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
    if image is None:
        continue
    else:
        image = image.get('src')
    
    with open(search + str(fileCounter) + '.jpg', 'wb') as f:
        im = requests.get(image)
        f.write((im.content))

    fileCounter += 1
=======
"""
get wallpapers from websites
"""

from fileinput import filename
import requests 
from bs4 import BeautifulSoup 
import os

search = input('Please enter the category of your search: ').replace(" ", '+')
url = 'https://wallhaven.cc/search?q=' + search

def imagedown(url, folder):
    try:
        os.mkdir(os.path.join(os.getcwd(), folder))
    except:
        print("Error making directory")

    os.chdir(os.path.join(os.getcwd(),folder))
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')

    #prints the tite of the site
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
        if image is None:
            continue
        else:
            image = image.get('src')
        
        with open(search + str(fileCounter) + '.jpg', 'wb') as f:
            im = requests.get(image)
            f.write((im.content))

        fileCounter += 1

imagedown(url, search)
>>>>>>> 7024d081e19811054239c87b1a64aba5c46462b8
