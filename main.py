from splinter import Browser
from time import sleep
import urllib
import ctypes
import os


def main():
    """ Scrape Nasa's website for the featured image of the day and set it as the desktop image """

    executable_path = {'executable_path':f'{os.path.dirname(__file__)}/chromedriver.exe'}
    with Browser('chrome', **executable_path) as browser:
        # Visit URL
        url = "https://www.jpl.nasa.gov/images/earth"
        browser.visit(url)
        sleep(1)
        img = browser.find_by_xpath('//*[@id="65603"]')['src']
        print(img)
    wallpaper = urllib.request.urlretrieve(img, f"{os.path.dirname(__file__)}/image/nasaImage.png")[0]
    SPI_SETDESKWALLPAPER = 0x14     #which command (20)
    SPIF_UPDATEINIFILE   = 0x2 #forces instant update
    src = r"{}".format(wallpaper) #full file location
    #in python 3.4 you have to add 'r' before "path\img.jpg"

    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, src, SPIF_UPDATEINIFILE)
    #SystemParametersInfoW instead of SystemParametersInfoA (W instead of A)

if __name__ == '__main__':
    main()