# selenium
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService

#  selenium selecter

from selenium.webdriver.common.by import By

# scrape
from requests import get
from bs4 import BeautifulSoup

# oter
from time import sleep


def chrome(id):

    browser = webdriver.Chrome(
        service=ChromeService(
            ChromeDriverManager().install()
        )
    )

    browser.implicitly_wait(5)

    browser.get(f"https://standardsmap.org/en/factsheet/{id}/overview")

    sleep(10)

    loaded = browser.find_element(
        By.CSS_SELECTOR, '.loaded-content'
    )

    select_all_nav_tag = browser.find_elements(
        By.CSS_SELECTOR, 'a.nav-link'
    )[2:]

    heading = browser.find_element(By.TAG_NAME, 'h1')
    heading_text = heading.text

    img = loaded.find_element(By.XPATH, "//img[@alt='Standard Logo']")
    img_url = img.get_attribute('src')

    description = loaded.find_element(By.CSS_SELECTOR, ".standard-description")
    description_text = description.text

    see_more_tag = browser.find_elements(By.TAG_NAME, "see-more")

    #  Sector

    if '<a ' in see_more_tag[0].get_attribute("innerHTML"):
        see_more_tag[0].find_element(By.TAG_NAME, 'a').click()
        sleep(2)
        dialog_content = browser.find_element(
            By.CLASS_NAME, "p-dialog-content")
        select_content = dialog_content.get_attribute("innerText")
        print(str(select_content).split('\n'))

        browser.find_element(
            By.CLASS_NAME, "p-dialog-header-close-icon").click()

        sleep(1)

        # browser.find_element(
        #     By.CLASS_NAME, "p-dialog-header-close-icon").click()

        # sleep(1)

    else:
        sector_text = see_more_tag[0].get_attribute('innerText')
        print(', '.join(sector_text.split("\n")))

    # Product(s)
    if '<a ' in see_more_tag[1].get_attribute("innerHTML"):
        see_more_tag[1].find_element(By.TAG_NAME, 'a').click()
        sleep(2)
        dialog_content = browser.find_element(
            By.CLASS_NAME, "p-dialog-content")
        select_content = dialog_content.get_attribute("innerText")
        print(str(select_content).split('\n'))

        browser.find_element(
            By.CLASS_NAME, "p-dialog-header-close-icon").click()

        sleep(1)

    else:
        product_text = see_more_tag[1].get_attribute('innerText')

        print(", ".join(product_text.split('\n')))

    # scope

    origin = browser.find_element(
        By.XPATH, "/html/body/app-root/div/div/app-factsheet/standard-overview/div/div/div[1]/div[3]/div/div[1]").get_attribute("innerHTML")

    print(origin)

    destination = browser.find_element(
        By.XPATH, "/html/body/app-root/div/div/app-factsheet/standard-overview/div/div/div[1]/div[3]/div/div[2]"
    ).get_attribute("innerHTML")

    print(destination)


chrome(496)
