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

        sleep(1)

        find_all_h3  = browser.find_elements(By.TAG_NAME, 'h3')

        _dic = { }
        for __ in find_all_h3:

            h3_text =  __.get_attribute('innerText')

            # dic[h1_text] = {

            # } 
            try: 
                if __.find_element(By.TAG_NAME, 'fa-icon'): 

                    __.find_element(By.TAG_NAME, 'fa-icon').click()

                print('\t'+ h3_text)

                sleep(1)

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

                if __.find_element(By.TAG_NAME, 'fa-icon'): 

                    __.find_element(By.TAG_NAME, 'fa-icon').click()

            except: 
                pass

            
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



def getAll():
    res = get("https://api.production.standardsmap.sustainable-trade.org/api/standards?client=NO%20AFFILIATION").json()

    return res





data = ['1080',  '1090', '11', '112', '118', '119', '120', '120934', '124', '127', '128', '129', '13', '131', '136', '138', '139', '14', '140', '141', '142', '142369', '142370', '142371', '143', '144', '145', '145236', '146', '148', '150', '152', '153', '154', '155', '156', '15658', '15684', '15687', '15689', '157', '158', '159', '16', '160', '161', '163', '164', '165', '166', '16690', '167', '169', '170', '172', '173', '174', '175', '176', '177', '178', '179', '18', '181', '182', '184', '186', '187', '189', '19', '191919', '193', '194', '195', '196', '197', '2', '200', '200397', '200398', '201354', '202', '2020', '202720', '204', '2050', '206', '2099', '21', '211000', '21100101', '211005', '211006', '211007', '213', '214', '215', '234', '234568', '235', '236', '237', '239', '24', '241', '242', '243', '244', '245', '248', '249', '250', '254', '255', '256', '26', '260', '261', '263', '265', '267', '271118', '276', '278', '279', '282', '283', '284', '285', '287', '288', '291', '293', '294', '295', '297', '298', '299', '30', '301', '302', '31', '311', '314', '33', '331', '333', '338', '34', '340', '341', '342', '343', '344', '345', '347', '348', '3490', '3491', '35', '36', '364758', '365', '366', '37', '370', '379', '38', '380', '381', '384', '385', '386', '390', '391', '396', '40', '401', '4011', '402', '403', '405', '407', '408', '41', '4117', '416', '420', '422', '423', '425', '427', '428', '429', '4317', '434', '435', '436', '437', '438', '441', '4417', '442', '443', '444', '448', '45', '451', '45346', '459', '4596', '46', '462', '463', '464', '467', '468', '47', '470', '475987', '481', '482', '484', '485', '488', '49', '490', '494', '495', '496', '497', '498', '499', '5', '501', '503', '504', '510', '511', '512', '513', '516546', '519', '526', '527', '53', '535', '538', '539', '54', '547', '553', '555', '556', '558', '559', '56', '561', '562', '563', '564', '566', '567', '5673', '5697', '56972', '57', '58', '583', '59', '6', '60', '600', '61', '64', '647', '65', '67', '674', '677', '680', '685', '698', '7', '700', '701', '702', '707', '712', '7281', '7282', '7283', '729', '73', '730', '731', '732', '733', '734', '76', '767902', '777777', '78651', '789', '8013', '803', '8041', '8042', '8043', '8047', '8048', '8052', '859', '863', '868686', '870', '891', '897952', '898989', '9', '903', '905', '906', '907', '908', '91', '93268', '9367', '98379', '98731', '98759']



for id in data:

    wb =  Workbook()
    wa = wb.active



    print(id)

    overview =  overView(id)
    print("pass get overview")



    howtocomply =  howToComply(id)
    print("pass get howtoComply")
   
    requirement =  requirements(id)
    print("pass get requirement")
    _governance =  governance(id)
    print("pass get governance")
    _resources =  resources(id)
    print("pass get resources")



    
    print("overview start")

    wa.append(overview)

    print("overview end")


    wa.append([""])
    wa.append([""])
    wa.append([""])
    wa.append(["requirement"])
    wa.append([""])
    wa.append([""])
    wa.append([""])


    print("requirement start")

    for _ in requirement:

        wa.append([_])

        for __ in requirement[_]:

            wa.append(["", __])

            for ___ in requirement[_][__]:

                wa.append(["", ""] + ___)

    print("requirement end")
    

    wa.append([""])
    wa.append([""])
    wa.append([""])
    wa.append(["How to Comply"])
    wa.append([""])
    wa.append([""])
    wa.append([""])


    print('howtocomply start ')

    for _ in howtocomply:
    
        wa.append([_])
      
        if 'str' in  str(type(howtocomply[_])):

            wa.append(["" ,  howtocomply[_]])
        else: 
            wa.append([" ", _  ])

            for __ in howtocomply[_]:
                wa.append( [" ",  " "] + __)

    print('howtocomply end ')
    
    wa.append([""])
    wa.append([""])
    wa.append([""])
    wa.append(["Governance"])
    wa.append([""])
    wa.append([""])
    wa.append([""])

    print('governance start')
    for _ in _governance:

        wa.append([_])

        if 'list' in str(type(_governance[_])):

            wa.append([""] + _governance[_])

        else:
            for __ in _governance[_]:
                
                wa.append(["",  __, _governance[_][__]])

    print('governance end')

    wa.append([""])
    wa.append([""])
    wa.append([""])
    wa.append(["Resources"])
    wa.append([""])
    wa.append([""])
    wa.append([""])

    print("resources start")
    for _ in _resources:

        wa.append(_)

    print("resources end    ")
    

    wb.save(f'{id}.xlsx')

