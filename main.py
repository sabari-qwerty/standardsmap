# selenium
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService

#  selenium selecter

from selenium.webdriver.common.by import By

# scrape
from requests import get
from bs4 import BeautifulSoup

# oter
from time import sleep

from openpyxl import Workbook


def geographical_scope_soup(html):

    soup = BeautifulSoup(
        html, 'html.parser'
    ).find_all('span', class_="maxlinestwo")

    return ", ".join([text.text for text in soup])


def getText(html):

    soup = BeautifulSoup(
        html, 'html.parser'
    ).text

    return str(soup).strip()


def requirements(id):

    # browser = webdriver.Firefox(
    #     service=FirefoxService(
    #         GeckoDriverManager().install()
    #     )
    # )

    browser = webdriver.Chrome(
        service=ChromeService(
            ChromeDriverManager().install()
        )
    )
    browser.implicitly_wait(5)

    browser.get(f"https://standardsmap.org/en/factsheet/{id}/requirements")

    sleep(25)

    find_all_h1 = browser.find_elements(
        By.TAG_NAME, 'h1'
    )[3:]

    for _ in find_all_h1:
        h1_text = _.get_attribute("innerText")
        _.find_element(By.TAG_NAME, 'fa-icon').click()

        sleep(4)

        find_all_h3 = browser.find_elements(By.TAG_NAME, 'h3')

        for __ in find_all_h3:

            # print(__.get_attribute("innerText"))

            __.find_element(By.TAG_NAME, 'fa-icon').click()

            print("\t" + __.get_attribute('innerText'))

            all_column = browser.find_elements(
                By.CSS_SELECTOR, ".d-flex.flex-nowrap.ng-star-inserted"
            )

            for column in all_column:

                find_all_a = column.find_elements(
                    By.TAG_NAME, 'a'
                )

                index = [num
                         for num in range(len(find_all_a)) if "more info" in str(find_all_a[num].get_attribute("innerText")).lower().strip()][0]

                find_all_a[index].click()
                sleep(2)

                single_colum = str(
                    column.get_attribute("innerText")).split('\n')

                first_4 = single_colum[:4]
                with_out_4 = "\n".join([_ for _ in single_colum[4:] if _][:-1])

                # print("\t\t", first_4 + [with_out_4])

                sleep(2)

            sleep(2)

            __.find_element(By.TAG_NAME, 'fa-icon').click()

        _.find_element(By.TAG_NAME, 'fa-icon').click()


def overView(id):

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

    sector_text = ""

    if '<a ' in see_more_tag[0].get_attribute("innerHTML"):
        see_more_tag[0].find_element(By.TAG_NAME, 'a').click()
        sleep(2)
        dialog_content = browser.find_element(
            By.CLASS_NAME, "p-dialog-content")
        select_content = dialog_content.get_attribute("innerText")
        sector_text = ", ".join(str(select_content).split('\n'))

        browser.find_element(
            By.CLASS_NAME, "p-dialog-header-close-icon").click()

        sleep(1)

    else:
        sector_text = see_more_tag[0].get_attribute('innerText')
        ', '.join(sector_text.split("\n"))

    # Product(s)

    product_text = ""
    if '<a ' in see_more_tag[1].get_attribute("innerHTML"):
        see_more_tag[1].find_element(By.TAG_NAME, 'a').click()
        sleep(2)
        dialog_content = browser.find_element(
            By.CLASS_NAME, "p-dialog-content")
        select_content = dialog_content.get_attribute("innerText")
        product_text = ", ".join(str(select_content).split('\n'))

        browser.find_element(
            By.CLASS_NAME, "p-dialog-header-close-icon").click()

        sleep(1)

    else:
        product_text = see_more_tag[1].get_attribute('innerText')

        ", ".join(product_text.split('\n'))

    # scope

    origin = browser.find_element(
        By.XPATH, "/html/body/app-root/div/div/app-factsheet/standard-overview/div/div/div[1]/div[3]/div/div[1]").get_attribute("innerHTML")

    geographical_scope_soup(origin)

    destination = browser.find_element(
        By.XPATH, "/html/body/app-root/div/div/app-factsheet/standard-overview/div/div/div[1]/div[3]/div/div[2]"
    ).get_attribute("innerHTML")

    geographical_scope_soup(destination)

    value_chain_list = []

    production = browser.find_element(
        By.XPATH, "/html/body/app-root/div/div/app-factsheet/standard-overview/div/div/div[1]/div[4]/div[1]"
    ).get_attribute("innerHTML")
    if '<fa-icon ' in production:
        value_chain_list.append(getText(production))

    manufacturing = browser.find_element(
        By.XPATH, "/html/body/app-root/div/div/app-factsheet/standard-overview/div/div/div[1]/div[4]/div[2]"
    ).get_attribute('innerHTML')

    if '<fa-icon ' in manufacturing:
        value_chain_list.append(getText(manufacturing))

    distribution = browser.find_element(
        By.XPATH, "/html/body/app-root/div/div/app-factsheet/standard-overview/div/div/div[1]/div[4]/div[3]"
    ).get_attribute('innerHTML')

    if '<fa-icon ' in distribution:

        value_chain_list.append(getText(distribution))

    consumption = browser.find_element(
        By.XPATH, "/html/body/app-root/div/div/app-factsheet/standard-overview/div/div/div[1]/div[4]/div[4]"
    ).get_attribute('innerHTML')

    if '<fa-icon ' in consumption:

        value_chain_list.append(
            getText(consumption)
        )

    value_chain_text = ", ".join(value_chain_list)

    lastest_highlights = browser.find_element(
        By.XPATH, "/html/body/app-root/div/div/app-factsheet/standard-overview/section[1]/div/div/div[2]/p"
    ).get_attribute('innerText')

    interesting_facts = browser.find_element(
        By.XPATH, "/html/body/app-root/div/div/app-factsheet/standard-overview/section[1]/div/div/div[3]/p"
    ).get_attribute('innerText')

    year_of_found = browser.find_element(
        By.XPATH, "/html/body/app-root/div/div/app-factsheet/standard-overview/section[1]/div/div/div[3]/div"
    ).get_attribute('innerText')

    sleep(1)

    browser.close()

    return [heading_text, img_url, description_text, sector_text, product_text, origin,
            description, value_chain_text, lastest_highlights, interesting_facts, year_of_found]

    select_all_nav_tag[0].click()
    sleep(10)

    find_all = browser.find_elements(
        By.TAG_NAME, 'h1'

    )[3:]

    for _ in find_all:
        print(_.get_attribute("innerText"))
        _.find_element(By.TAG_NAME, 'fa-icon').click()

        sleep(4)

        all_h3 = browser.find_elements(By.TAG_NAME, 'h3')

        for __ in all_h3:
            __.find_element(By.TAG_NAME, 'fa-icon').click()

            print("\t" + __.get_attribute('innerText'))

            select_each_column = browser.find_elements(
                By.CSS_SELECTOR, ".d-flex.flex-nowrap.ng-star-inserted")

            for column in select_each_column:

                find_all_a = column.find_elements(
                    By.TAG_NAME, "a")
                find_all_a[-1].click()
                sleep(2)

                single_colum = column.get_attribute("innerText").split("\n")

                print(single_colum)

                first_4 = single_colum[:4]
                with_out_4 = "\n".join([_ for _ in single_colum[4:] if _][:-1])

                print(first_4)
                print(with_out_4)

                sleep(2)
            # print("\t\t" +  str(len(select_data)))

            sleep(4)

            __.find_element(By.TAG_NAME, 'fa-icon').click()

        _.find_element(By.TAG_NAME, 'fa-icon').click()

        # print(_.get_attribute("innerText"))

    # for _ in find_all:
    #     _.find_element(By.TAG_NAME, 'fa-icon').click()
    #     sleep(4)
    #     all_h3 =  browser.find_elements(By.TAG_NAME, 'h3')

    #     for __ in all_h3:

    #         __.find_element(By.TAG_NAME, "fa-icon").click()
    #         sleep(2)

    # sleep(10)


# print(overView(496))

requirements(496)
