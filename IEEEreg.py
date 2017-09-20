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
    # time.sleep(5)
    # window.execute_script('window.scrollTo(0, 1000)')
    # time.sleep(5)
    #
    
    time.sleep(10)
    try:
        put_tabs(window, 2)
        ActionChains(window).key_down(Keys.ESCAPE).key_up(Keys.ESCAPE).perform()
        # window.find_element_by_id('AttestationInfo').click()
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

def fill_additional_details(window):
    ''' Function to fill in additional details '''
    try:
        put_tabs(window, 7)
        ActionChains(window).key_down(Keys.ENTER).key_up(Keys.ENTER).perform()
        time.sleep(5)
        window.find_element_by_id('mbMCAddMemProdBtn').click()
        window.execute_script('window.scrollTo(0, 2400)')
        time.sleep(12)
        window.find_element_by_id('TechnicallyCurrent').click()
        window.find_element_by_id('CareerOpurtunities').click()
        window.find_element_by_id('ExpandProfessionalNetwork').click()
        window.find_element_by_id('ConnectToLocalActivities').click()
        window.find_element_by_id('HumanitarianPrograms').click()
        window.find_element_by_id('Discounts').click()
        fill_select(window, 'member-referral', "Member referral")
        fill_input(window, 'referring-mem-name', 'Saurabh Sunil Chheda')
        fill_input(window, 'referring-mem-number', '93651909')
        put_tabs(window, 1)
        ActionChains(window).key_down(Keys.ENTER).key_up(Keys.ENTER).perform()
    except NoSuchElementException:
        time.sleep(2)
        fill_additional_details(window)

def logout(window):
    ''' Logs user out '''
    time.sleep(10)
    username = window.find_element_by_id('mn-ieee-username')
    logout_button = window.find_element_by_id('mn-signout-link')
    ActionChains(window).move_to_element(username).click(logout_button).perform()
    time.sleep(10)


def main():
    ''' Initialization function '''

    csv = open("todo.csv", 'r')
    for record in csv:
        window = webdriver.Firefox()
        record = record.split(',')
        email = record[0]
        year_of_grad = record[1]
        window.get("http://www.ieee.org/go/join_student")
        login(window, email)
        fill_contact_information(window)
        fill_educational_information(window, year_of_grad)
        fill_additional_details(window)
        window.close()
    csv.close()

if __name__ == "__main__":
    main()