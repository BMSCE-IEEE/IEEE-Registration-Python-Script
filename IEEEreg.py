''' Module for Automated Script for BMSCE IEEE Registrations '''
# Requires Selenium, Gecko and Mozilla Firefox
# @author: Saurabh Chheda

import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

def put_tabs(window, no_of_tabs):
    ''' Function to put tabs '''
    for i in range(no_of_tabs):
        ActionChains(window).key_down(Keys.TAB).key_up(Keys.TAB).perform()

def select_option(window, option):
    ''' Function to select nth option '''
    for i in range(option):
        ActionChains(window).key_down(Keys.DOWN).key_up(Keys.DOWN).perform()

def fill_input(window, input_id, value):
    ''' Function fills in textboxes with value '''
    continue_link = window.find_element_by_id(input_id)
    continue_link.click()
    continue_link.clear()
    continue_link.send_keys(value)

def fill_select(window, select_id, option_value):
    ''' Function to select an option '''
    select_el = Select(window.find_element_by_id(select_id))
    select_el.select_by_value(option_value)

def fill_after_tabs(window, no_of_tabs, value):
    ''' Function to add tabs and then fill an input '''
    put_tabs(window, no_of_tabs)
    ActionChains(window).send_keys(value).perform()

def login(window, email):
    ''' Function to log in '''
    try:
        fill_input(window, 'username', email)
        fill_input(window, 'password', 'bmsceieee17')
        continue_link = window.find_element_by_id('ppctLoginSubmit')
        continue_link.click()
    except NoSuchElementException:
        time.sleep(2)
        login(window, email)
    except ElementNotInteractableException:
        time.sleep(2)
        login(window, email)

def fill_contact_information(window):
    ''' Function to fill in address '''
    try:
        address_type = window.find_element_by_id("contact-info_customer_addresses_0__addressType_code-3")
        address_type.click()
        fill_select(window, "country", "IN")
        time.sleep(2)
        fill_after_tabs(window, 9, 'B.M.S. College of Engineering')
        fill_after_tabs(window, 1, 'P.O. Box No.: 1908, Bull Temple Road')
        fill_after_tabs(window, 2, 'Bangalore')
        fill_after_tabs(window, 2, '560019')
        put_tabs(window, 8)
        ActionChains(window).key_down(Keys.ENTER).key_up(Keys.ENTER).perform()
    except NoSuchElementException:
        time.sleep(2)
        fill_contact_information(window)

def fill_educational_information(window, year):
    ''' Function to fill educational details '''
    # @debug
    time.sleep(5)
    window.execute_script('window.scrollTo(0, 1000)')
    time.sleep(5)
    #
    try:
        window.find_element_by_id("AttestationInfo").click()
        fill_after_tabs(window, 8, "B.M")
        time.sleep(2)
        put_tabs(window, 3)
        ActionChains(window).key_down(Keys.ENTER).key_up(Keys.ENTER).perform()
        time.sleep(4)
        put_tabs(window, 1)
        ActionChains(window).key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
        put_tabs(window, 1)
        select_option(window, 7)
        put_tabs(window, 1)
        select_option(window, 136)
        put_tabs(window, 1)
        select_option(window, 6)
        put_tabs(window, 1)
        select_option(window, int(year)-2017)
        put_tabs(window, 2)
        select_option(window, 3)
        put_tabs(window, 1)
        select_option(window, 16)
        put_tabs(window, 2)
        ActionChains(window).key_down(Keys.ENTER).key_up(Keys.ENTER).perform()        
    except NoSuchElementException:
        time.sleep(2)
        fill_educational_information(window, year)

def main():
    ''' Initialization function '''
    window = webdriver.Firefox()

    csv = open("todo.csv", 'r')
    '''for record in csv:
        record = record.split(',')
        email = record[0]
        dept = record[1]
        year_of_grad = record[2]'''
    window.get("http://www.ieee.org/go/join_student")
    login(window, 'shrividhiya.te17@bmsce.ac.in')
    #fill_contact_information(window)
    fill_educational_information(window, '2021')
    csv.close()

if __name__ == "__main__":
    main()

'''
continue_link = driver.find_element_by_xpath("//input[@id='student-id']") 
continue_link.click()

continue_link = driver.find_element_by_xpath("//input[@id='stud-university']")
continue_link.click()
continue_link.clear()
continue_link.send_keys("B.M")

time.sleep(2)

continue_link = driver.find_element_by_xpath("//a[@title='Select B. M. Sreenivasalah College of Engineering']") 
continue_link.click()


continue_link = driver.find_element_by_xpath("//input[@id='educational-info_currentSchool_degreeType_codeUndergraduate Student']") 
continue_link.click()

el = driver.find_element_by_id('stud-degree-pursued')
for option in el.find_elements_by_tag_name('option'):
    if option.text == 'Bachelor of Engineering':
        option.click() # select() in earlier versions of webdriver
        break

el = driver.find_element_by_id('stud-degree-pursued')
for option in el.find_elements_by_tag_name('option'):
    if option.text == 'Bachelor of Engineering':
        option.click() # select() in earlier versions of webdriver
        break

###################################################################
#########		Below code is temperory 	  #########
###################################################################
###				 ACAD  				###
el = driver.find_element_by_id('stud-degree-pursued')
for option in el.find_elements_by_tag_name('option'):
    if option.text == 'Bachelor of Engineering':
        option.click() # select() in earlier versions of webdriver
        break
###				PROGRAM				###
###################################################################
#########		Above code is temperory 	  #########
###################################################################


el = driver.find_element_by_id('estimated-grad-month')
for option in el.find_elements_by_tag_name('option'):
    if option.text == gradMnth:
        option.click() # select() in earlier versions of webdriver
        break
el = driver.find_element_by_id('estimated-grad-year')
for option in el.find_elements_by_tag_name('option'):
    if option.text == gradYear:
        option.click() # select() in earlier versions of webdriver
        break
el = driver.find_element_by_id('stud-current-study')
for option in el.find_elements_by_tag_name('option'):
    if option.text == "Engineering":
        option.click() # select() in earlier versions of webdriver
        break
el = driver.find_element_by_id('stud-technical-focus')
for option in el.find_elements_by_tag_name('option'):
    if option.text == "Engineering Profession":
        option.click() # select() in earlier versions of webdriver
        break

continue_link = driver.find_element_by_xpath("//input[@id='save-educational-info']") 
continue_link.click()

time.sleep(3)

continue_link = driver.find_element_by_xpath("//input[@id='TechnicallyCurrent']") 
continue_link.click()

continue_link = driver.find_element_by_xpath("//input[@id='CareerOpurtunities']") 
continue_link.click()

continue_link = driver.find_element_by_xpath("//input[@id='ExpandProfessionalNetwork']") 
continue_link.click()

continue_link = driver.find_element_by_xpath("//input[@id='ConnectToLocalActivities']") 
continue_link.click()

el = driver.find_element_by_id('member-referral')
for option in el.find_elements_by_tag_name('option'):
    if option.text == "Member referral":
        option.click() # select() in earlier versions of webdriver
        break


continue_link = driver.find_element_by_xpath("//input[@id='referring-mem-name']")
continue_link.click()
continue_link.clear()
continue_link.send_keys("Tarun Verma")

continue_link = driver.find_element_by_xpath("//input[@id='referring-mem-number']")
continue_link.click()
continue_link.clear()
continue_link.send_keys("93151099")

continue_link = driver.find_element_by_name("proceed-checkout-button") 
continue_link.click()

continue_link = driver.find_element_by_xpath("//a[@id='open-challan-link']") 
continue_link.click()

continue_link = driver.find_element_by_xpath("//input[@id='mobile-telephone-number']")
continue_link.click()
continue_link.clear()
continue_link.send_keys("+919431908524")

continue_link = driver.find_element_by_xpath("//input[@id='challan-membership-terms-conditions']") 
continue_link.click()

continue_link = driver.find_element_by_xpath("//input[@id='challan-terms-conditions']") 
continue_link.click()

time.sleep(2)

continue_link = driver.find_element_by_xpath("//input[@id='saveMobilePhoneId']") 
continue_link.click()
'''

