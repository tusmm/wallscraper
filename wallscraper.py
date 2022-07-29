"""
Author: Ryan Ong
        rto9185@rit.edu
File: wallscraper.py
language: python3
Description: scrapes images off of wallhaven.cc
"""

import requests 
from bs4 import BeautifulSoup 
import os

'''
Downloads a wall of wallpaper images from a search category
from wallhaven.cc, into a folder in the parent directory of this file
:param url: the: The url of the page
:folder: The name of the folder/the name of the category
'''
def imageDown(url, folder):
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

        if image is None: 
            continue
        else:
            image = image.get('src')
        
        with open(folder + str(fileCounter) + '.jpg', 'wb') as f:
            im = requests.get(image)
            f.write((im.content))

        if fileCounter % 3 == 0:
            print("Downloading images...")

        fileCounter += 1

    print("Finished downloading!")

'''
Gets the url of the wallhaven.cc website to be scraped
:param category: The search category
:return: returns the completed url of the category
'''
def getUrl(category):
    url = 'https://wallhaven.cc/search?q=' + category
    return url

'''
Prints a help menu with valid commands
'''
def help():
    print("Available commands:")
    print("\tsearch <category>")
    print("\thelp")
    print("\tquit")

'''
Performs the search with the url and inputted category
:param category: The category of the search
'''
def search(category):
    category = category.replace(" ", '+')
    url = getUrl(category)
    imageDown(url, category)

if __name__ == "__main__":
    print("Search for wallpapers on wallhaven.cc")
    help()

    while True:
        splitInput = input("> ").split(" ", 1)
        
        if splitInput[0] == "quit":
            print("Terminating program.")
            exit()

        elif splitInput[0] == "search":
            search(splitInput[1])
            print("Search for more wallpapers or enter 'quit' to quit")
        elif splitInput[0] == "help":
            help()

        else:
            print("Invalid command.")
            help()
            continue
        
