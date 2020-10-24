from selenium import webdriver                           # Allows to connect browser
from selenium.webdriver.common.keys import Keys          # Allows us to access common keys like enter and esc
import time
import json 

# Showing the path to the webdrive location
PATH = 'C:\Program Files (x86)\chromedriver.exe'

# Creating a driver object containing the browser selection and linking it to the webdrive executable  
driver = webdriver.Chrome(PATH)


def scrap():
    search_results = []

    for i in range(6, 6+10, 1):
        cc = driver.find_elements_by_xpath("//ul[@class='lemon--ul__09f24__1_cxs undefined list__09f24__17TsU']/li[{}]".format(i))
        search_results.append(cc[0].text.split("\n"))

    data = clean(search_results)
    return data


def clean(unclean_result):
    data = {}
    for j in range(len(unclean_result)):
        store_name = unclean_result[j][0]
    
        data[store_name[3:]] = {
            "# of ratings": unclean_result[j][1],
            "key words": unclean_result[j][2:-1],
            "review": unclean_result[j][-1]
        }
    return data


def dict_merg(d1,d2,d3,d4,d5):
    d1.update(d2)
    d1.update(d3)
    d1.update(d4)
    d1.update(d5)
    return d1
    

if __name__ == '__main__':
    # Getting the targetted website
    driver.get("https://www.yelp.ca/ottawa")

    search = driver.find_element_by_id("find_desc")
    search.send_keys("poutine")
    search.send_keys(Keys.RETURN)
    
    data1 = scrap()

    link = driver.find_element_by_link_text("2")
    link.click()
    data2 = scrap()

    link = driver.find_element_by_link_text("3")
    link.click()
    data3 = scrap()

    link = driver.find_element_by_link_text("4")
    link.click()
    data4 = scrap()

    link = driver.find_element_by_link_text("5")
    link.click()
    data5 = scrap()

    time.sleep(5)
    driver.quit()

    final_json = dict_merg(data1,data3,data4,data5)

    json_object = json.dumps(data1, indent=4)
    with open('Scraped_yelp_poutine.json', 'w') as outfile:
        outfile.write(json_object)
