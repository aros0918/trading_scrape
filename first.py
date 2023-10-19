from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time
import csv
# file_path = './file.csv'
# driver = webdriver.Chrome()
# scroll_interval = 1
# total_scroll_time = 60000
# total_scrolls = int(total_scroll_time/scroll_interval)
# driver.get("https://www.medica-tradefair.com/vis/v1/en/search?oid=80396&lang=2&_query=&f_type=contact")
# for _ in range(total_scrolls):
#     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
# time.sleep(10)
# searchItems = driver.find_elements(By.CLASS_NAME, "searchresult-item   ")

# links = []
# for searchItem in searchItems:
#     mainItem = searchItem.find_element(By.CLASS_NAME, "media__body__txt ")
#     link = mainItem.find_element(By.TAG_NAME, "a").get_attribute("href")
#     links.append(link)
# print(len(links))
# set_links = {"https://www.medica-tradefair.com/vis/v1/en/exhprofiles/rZEgsEwMQoCs3h8uUi8O6A?oid=80396&lang=2&_query=&f_type=contact",}
# for _ in links:
#     set_links.add(_)
# real_links = [['url'],]
# for _ in set_links:
#     real_links.append([_])
# print(len(real_links))
# with open(file_path, 'w', newline='', encoding='utf-8') as file:
#     writer = csv.writer(file) 
#     for row in real_links:
#         writer.writerow(row)
# driver.quit()


driver = webdriver.Chrome()
file_path = "./complete.csv"
data = ['url', 'fname', 'lname', 'title', 'email', 'company name' ]

with open(file_path, 'a', newline='', encoding='utf-8') as file:
    writer = csv.writer(file) 
    writer.writerow(data)
    with open('1.txt', 'r') as file1:
        content = file1.read()
        splited_data = content.splitlines()
        for url in splited_data:
            driver.get(url)
            time.sleep(1)
            try:  
                
                profiles = driver.find_elements(By.CLASS_NAME, "contact-person-stand")
            except NoSuchElementException:
                profiles = driver.find_elements(By.CLASS_NAME, "contact-person-profile")
            try: 
                companyName = driver.find_element(By.CLASS_NAME, "profile__name").text
            except NoSuchElementException:
                companyName = ""
            print(len(profiles))
            for profile in profiles:
                profile.click()
                time.sleep(4)
                try:
                    detail = driver.find_element(By.CLASS_NAME, "contact-person-details-content")
                except NoSuchElementException:
                    continue
                try:
                    name = detail.find_element(By.TAG_NAME, "h1").text
                    names = name.split(' ')
                    fname = names[0]
                    lname = names[-1]
                except NoSuchElementException:
                    fname = ""
                    lname = ""
                position = ""
                try:
                    position = detail.find_element(By.CLASS_NAME, "contact-person-details-content__position").text
                except NoSuchElementException:
                    position = ""
                try:
                    element = driver.find_element(By.CLASS_NAME, "contact-person-details-content__department")
                    position = element.text
                except NoSuchElementException:
                    print("no such element")
                
                try:
                    email = detail.find_element(By.CLASS_NAME, "contact-person-contact").text
                except NoSuchElementException:
                    email = ""
                
                writer.writerow([url, fname, lname, position, email, companyName])
                button = driver.find_element(By.CLASS_NAME, "content-modal__close-button")
                button.click()
                time.sleep(1)
        
driver.quit()



# import requests

# url = 'https://www.medica-tradefair.com/vis-api/vis/v1/en/search/slice?oid=80396&lang=2&_query=&f_type=contact&_start=0&_rows=4000'
# headers = {
#     'X-Vis-Domain': 'https://www.medica-tradefair.com'
# }
# resp = requests.get(url, headers=headers)
# print(resp.text)