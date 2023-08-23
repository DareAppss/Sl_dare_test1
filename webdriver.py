from aiogram.types import Update
from selenium import webdriver


def get_website_title(url):
    # Create a new instance of the Chrome web driver
    driver = webdriver.Chrome()

    try:
        # Open the specified webpage
        driver.get(url)

        # Get and return the page title
        title = driver.title
        return title
    finally:
        # Make sure to always quit the driver to close the browser window
        driver.quit()