from selenium import webdriver ##Imports the selenium web driver
import time
driver = webdriver.Firefox() ##Create a Firefox Webdriver
driver.get("https://www.ieee.org/membership-application/public/login/mymembershiplogin.html")

print "Enter First Name"
fnme = raw_input()

print "Enter Second Name"
lnme = raw_input()

print "Enter Email" #Taking only once although to be filled twice
email = raw_input()

print "Enter Password"
pword = raw_input()

print "Place od Birth?"
pob = raw_input()

print "Address?"
add = raw_input()

print "City?"
city = raw_input()

print "Postal Code?"
pcode = raw_input()

print "Month of Grad?"
gradMnth = raw_input()

print "Year of Grad?"
gradYear = raw_input()

continue_link = driver.find_element_by_xpath("//input[@id='registerModalWindowBtn']") 
continue_link.click()

time.sleep(5)


continue_link = driver.find_element_by_xpath("//input[@id='firstName']")
continue_link.click()
continue_link.clear()
continue_link.send_keys(fnme)

continue_link = driver.find_element_by_xpath("//input[@id='lastName']")
continue_link.click()
continue_link.clear()
continue_link.send_keys(lnme)

continue_link = driver.find_element_by_xpath("//input[@id='emailId']")
continue_link.click()
continue_link.clear()
continue_link.send_keys(email)

continue_link = driver.find_element_by_xpath("//input[@id='confirmEmailId']")
continue_link.click()
continue_link.clear()
continue_link.send_keys(email)

continue_link = driver.find_element_by_xpath("//input[@id='accountRegStep2Password']")
continue_link.click()
continue_link.clear()
continue_link.send_keys(pword)

continue_link = driver.find_element_by_xpath("//input[@id='confirmPassword']")
continue_link.click()
continue_link.clear()
continue_link.send_keys(pword)

el = driver.find_element_by_id('securityQuestion1')
for option in el.find_elements_by_tag_name('option'):
    if option.text == 'Who was your first employer?':
        option.click() # select() in earlier versions of webdriver
        break

continue_link = driver.find_element_by_xpath("//input[@id='securityQuestionAnswer1']")
continue_link.click()
continue_link.clear()
continue_link.send_keys("IEEE")

el = driver.find_element_by_id('securityQuestion2')
for option in el.find_elements_by_tag_name('option'):
    if option.text == 'What city were you born in?':
        option.click() # select() in earlier versions of webdriver
        break

continue_link = driver.find_element_by_xpath("//input[@id='securityQuestionAnswer2']")
continue_link.click()
continue_link.clear()
continue_link.send_keys(pob)



continue_link = driver.find_element_by_xpath("//input[@id='modalWindowRegisterStep1CreateAcctBtn']") 
continue_link.click()

time.sleep(15)

continue_link = driver.find_element_by_xpath("//div[@id='mpanel-ContactInfo-body']") 
continue_link.click()
time.sleep(5)
continue_link = driver.find_element_by_xpath("//input[@id='contact-info_customer_addresses_0__addressType_code-1']") 
continue_link.click()

continue_link = driver.find_element_by_xpath("//input[@id='address-line1']")
continue_link.click()
continue_link.clear()
continue_link.send_keys(add)

continue_link = driver.find_element_by_xpath("//input[@id='city']")
continue_link.click()
continue_link.clear()
continue_link.send_keys(city)

continue_link = driver.find_element_by_xpath("//input[@id='postal-code']")
continue_link.click()
continue_link.clear()
continue_link.send_keys(pcode)

continue_link = driver.find_element_by_xpath("//input[@id='save']") 
continue_link.click()

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


