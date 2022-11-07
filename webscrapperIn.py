# Import libraries and packages for the project 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from time import sleep
import time
import csv

# Creating a webdriver instance
driver = webdriver.Chrome("C:/Users/Alejandro/Desktop/acceptgo/chromedriver.exe")
# This instance will be used to log into LinkedIn
  
# Opening linkedIn's login page
driver.get("https://linkedin.com/uas/login")
  
# waiting for the page to load
sleep(5)
  
# entering username
username = driver.find_element("id", "username")
  
# In case of an error, try changing the element
# tag used here.
  
# Enter Your Email Address
username.send_keys("")  
  
# entering password
pword = driver.find_element('id','password')
# In case of an error, try changing the element 
# tag used here.
  
# Enter Your Password
pword.send_keys("")        
  
# Clicking on the log in button
# Format (syntax) of writing XPath --> 
# //tagname[@attribute='value']
#driver.find_element_by_xpath("//button[@type='submit']").click()
driver.find_element('xpath',"//button[@type='submit']").click()
# In case of an error, try changing the
# XPath used here.


with open('output.csv', 'w',  newline = '') as file_output:
    headers = ['Name', 'Job Title', 'Location', 'URL']
    writer = csv.DictWriter(file_output, delimiter=',', lineterminator='\n',fieldnames=headers)
    writer.writeheader()
    linkedin_URL = 'https://www.linkedin.com/in/jonathan-capra-jgcc/'
    driver.get(linkedin_URL)
    print('- Accessing profile: ', linkedin_URL)
    sleep(3)
    
    start = time.time()
 
    # will be used in the while loop

    initialScroll = 0

    finalScroll = 1000
 

    while True:

        driver.execute_script(f"window.scrollTo({initialScroll},{finalScroll}) ")

    # this command scrolls the window starting from

    # the pixel value stored in the initialScroll 

    # variable to the pixel value stored at the

    # finalScroll variable

        initialScroll = finalScroll

        finalScroll += 1000
 

    # we will stop the script for 3 seconds so that 

    # the data can load

        sleep(3)

    # You can change it as per your needs and internet speed
 

        end = time.time()
 

    # We will scroll for 20 seconds.

    # You can change it as per your needs and internet speed

        if round(end - start) > 20:
            break

    page_source = BeautifulSoup(driver.page_source, 'lxml')
    info_div = page_source.find('div',{'class':'ph5'})
    info_work = page_source.find("div", {"id": "experience"})
    ##page_source.find('div',{'id':'experience'})
    ##soup.find("section", {"id": "experience-section"}).find('ul')
   ## print(info_work)

    try:
        name = info_div.find('h1', class_='text-heading-xlarge inline t-24 v-align-middle break-words').get_text().strip() #Remove unnecessary characters 
        print('--- Profile name is: ', name)
        skills = info_div.find('div', class_='text-body-medium break-words').get_text().strip() #Remove unnecessary characters 
        print('--- Headline/Skills ||: ', skills)
        home = info_div.find('span', class_='text-body-small inline t-black--light break-words').get_text().strip()
        print('--- Profile home is: ', home)
        
        
        cargo = info_work.find('div', class_='display-flex align-items-center').get_text().strip() #Remove unnecessary characters 
        print('--- universidad: ', cargo)
        empresa = info_work.find('span', class_='t-14 t-normal').get_text().strip() #Remove unnecessary characters 
        print('--- maestria en: ', empresa)
        writer.writerow({headers[0]:name, headers[1]:skills, headers[2]:home, headers[3]:linkedin_URL})
        print('\n')
    except:
        print('hola')
        pass

