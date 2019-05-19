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
        url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
        browser.visit(url)
        # Find and click the 'search' button
        full_image_button = browser.find_by_xpath('//*[@id="full_image"]')
        # Interact with elements
        full_image_button.click()
        if browser.is_element_not_present_by_xpath('//*[@id="fancybox-lock"]/div/div[2]/div/div[1]/a[2]'):
            sleep(2)
        more_button = browser.find_by_xpath('//*[@id="fancybox-lock"]/div/div[2]/div/div[1]/a[2]')
        more_button.click()
        sleep(1)
        featured_image = browser.find_by_xpath('//*[@id="page"]/section[1]/div/article/figure/a')['href']

    wallpaper = urllib.request.urlretrieve(featured_image, "image/nasaImage.png")[0]
    SPI_SETDESKWALLPAPER = 0x14     #which command (20)

    SPIF_UPDATEINIFILE   = 0x2 #forces instant update
    src = r"{}/{}".format(os.path.dirname(__file__),wallpaper) #full file location
    #in python 3.4 you have to add 'r' before "path\img.jpg"

    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, src, SPIF_UPDATEINIFILE)
    #SystemParametersInfoW instead of SystemParametersInfoA (W instead of A)

if __name__ == '__main__':
    main()