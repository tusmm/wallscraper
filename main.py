"""
get top wallpapers from websites
"""

from fileinput import filename
import requests 
from bs4 import BeautifulSoup 
import os

url = 'https://wallhaven.cc/search?q=id:37&sorting=random&ref=fp'

r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')

#prints the tite of the site
print(soup.title.text)

# figures = soup.find_all('figure')
# links = []
# for figure in figures:
#     links.append(figure.get('href'))

# gets the thumbnails
images = soup.find_all('img')

fileNameCounter = 0
for image in images:
    link = image.get('data-src')
    if fileNameCounter == 0:
        fileNameCounter += 1
    else:
        with open(str(fileNameCounter) + '.jpg', 'wb') as f:
            im = requests.get(link)
            f.write(im.content)
        fileNameCounter += 1
