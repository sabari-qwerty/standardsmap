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

    browser = webdriver.Chrome(
        service=ChromeService(
            ChromeDriverManager().install()
        )
    )

    browser.implicitly_wait(5)

    browser.get(f"https://standardsmap.org/en/factsheet/{id}/requirements")

    sleep(10)

    find_all_h1 = browser.find_elements(
        By.TAG_NAME, 'h1'
    )[3:]


    dic = {
        
    }

    for _ in find_all_h1:

        h1_text = _.get_attribute('innerText')


        _.find_element(By.TAG_NAME, 'fa-icon').click()

        sleep(4)

        find_all_h3  = browser.find_elements(By.TAG_NAME, 'h3')

        _dic = { }
        for __ in find_all_h3:

            h3_text =  __.get_attribute('innerText')

            # dic[h1_text] = {

            # } 

            __.find_element(By.TAG_NAME, 'fa-icon').click()

            print('\t'+ h3_text)

            sleep(5)

            select_data = browser.find_elements(By.CSS_SELECTOR, '.d-flex.flex-nowrap.ng-star-inserted')

            fin_list = []
            for _num_ in range(len(select_data)):
            


                # sleep(1)

                select_one  =  select_data[_num_].get_attribute("innerText").split('\n')
                

                select_list = []
                if select_one: 
                    single_colum =  [ data for data in select_one if data ][:-1]

                    first_4 = single_colum[:4]
                    with_out_4 = "\n".join(single_colum[4:])

                    select_list = first_4 + [with_out_4]
                

                fin_list.append(select_list)

                sleep(1)
            __.find_element(By.TAG_NAME, 'fa-icon').click()

            
            _dic[h3_text] = fin_list
        dic[h1_text] = _dic
        _.find_element(By.TAG_NAME, 'fa-icon').click()

    return dic





def resources(id):

    browser = webdriver.Chrome(
        service=ChromeService(
            ChromeDriverManager().install()
        )
    )

    browser.implicitly_wait(5)

    browser.get(f'https://standardsmap.org/en/factsheet/{id}/resources')

    sleep(10)

    container = browser.find_element(
        By.CSS_SELECTOR, ".container"
    )
    select_row  = container.find_elements(
        By.CSS_SELECTOR, ".row"
    )

    list_data = [
        ["Resources"]
    ]

    for row in select_row:

        html = row.get_attribute('innerHTML')

        if "<h1 " in html:

            list_data.append(["" , row.find_element(By.TAG_NAME,  'h1').get_attribute('innerText')])

        else: 

            list_data.append(["", "", row.get_attribute("innerText")])

    return list_data

def governance(id): 

    browser = webdriver.Chrome(
        service=ChromeService(
            ChromeDriverManager().install()
        )
    )

    browser.implicitly_wait(5)

    browser.get(f"https://standardsmap.org/en/factsheet/{id}/governance")

    sleep(10)

    overView_first_div = browser.find_element(
        By.XPATH, "/html/body/app-root/div/div/app-factsheet/app-governance/div[1]/div[2]/div[1]"
    )

    

    overView_seocund_div = browser.find_element(
        By.XPATH, "/html/body/app-root/div/div/app-factsheet/app-governance/div[1]/div[2]/div[2]"
    )

    
    overView_text =  overView_first_div.get_attribute("innerText")
    
    overView_secound_text = overView_seocund_div.get_attribute("innerText")
    

    select_all_details = browser.find_elements(
        By.CSS_SELECTOR, ".d-flex.flex-nowrap.mb-3.pt-3.pb-3.background-color-teal"
    )

    select_all_expand_details = browser.find_elements(
        By.CSS_SELECTOR, ".row.background-color-white.collapse"
    )

    _dic = {}

    _dic["overview"] = [overView_text, overView_secound_text]
    for _ in range(len(select_all_details)):

        text = select_all_details[_].find_element(By.TAG_NAME, 'h2').get_attribute('innerText')

        select_container =  select_all_expand_details[_].find_element(By.CSS_SELECTOR, '.container')

        select_all_row = select_container.find_elements(By.CSS_SELECTOR, ".row.pb-3.col-12.justify-content-between.ng-star-inserted")
        __dic = {}
        for row in select_all_row:



            value = row.get_attribute('innerText')

            key = None
            if "<fa-icon " in row.get_attribute('innerHTML'):
                class_ =  row.find_element(By.TAG_NAME, "svg").get_attribute('class')

                key =  'fa-check' in str(class_)

                __dic[value] =  key

        _dic[text] = __dic

    return _dic


    
def howToComply(id):
    browser = webdriver.Chrome(
        service=ChromeService(
            ChromeDriverManager().install()
        )
    )
    browser.implicitly_wait(5)

    browser.get(f"https://standardsmap.org/en/factsheet/{id}/how-to-comply")

    sleep(10)

    overview = browser.find_element(
        By.XPATH, "/html/body/app-root/div/div/app-factsheet/app-how-to-comply/div/div[2]/div")

    overview_text = overview.get_attribute("innerText")



    select_all_details = browser.find_elements(
        By.CSS_SELECTOR, ".d-flex.flex-nowrap.mb-3.pt-3.pb-3.background-color-teal")

    select_container = browser.find_elements(
        By.CSS_SELECTOR, ".container"
    )[1:5]

    dic = {}

    dic["overview"] = overview_text 
    # [...document.querySelectorAll('.container')].slice(1, 5)
    for _num in range(len(select_all_details)):


        text = select_all_details[_num].find_element(By.TAG_NAME, 'h2').get_attribute("innerText")
        print(text)
        
        container_child =  select_container[_num].find_elements(
            By.TAG_NAME, ".row.pb-3.col-12.ng-star-inserted")

        select_table = select_container[_num].get_attribute("innerHTML")

        soup_single_div_data = BeautifulSoup(str(select_table),  'html.parser').find_all('div', class_="row pb-3 col-12 ng-star-inserted")

        _list = []
        for _ in soup_single_div_data:
            _list.append([_.find('div').text, _.find_all('div')[-1].text])


        dic[text] = _list

    return dic


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

    origin_text = geographical_scope_soup(origin)

    destination = browser.find_element(
        By.XPATH, "/html/body/app-root/div/div/app-factsheet/standard-overview/div/div/div[1]/div[3]/div/div[2]"
    ).get_attribute("innerHTML")

    description_text = geographical_scope_soup(destination)

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

    return [heading_text, img_url, description_text, sector_text, product_text, origin_text,
            description_text, value_chain_text, lastest_highlights, interesting_facts, year_of_found]
    browser.close()

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





# print(overView(496))
# requirements(496)
# howToComply(496)
# print(governance(496))
print(resources(1000))