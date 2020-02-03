from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import NoSuchElementException

browser = webdriver.Chrome('/Users/stevemint/Downloads/chromedriver')



browser.get('https://shop.funko.com/collections/funko-shop-exclusives')
input_sq = "star wars"
input_mail = "leetymolina@gmail.com"
input_name = "Letinsky"
input_last = "Molinisky"
address = "lalaland 29"
apartment = "123"
city = "saltadilla"
zipcode = "10300"



browser.find_element_by_xpath('/html/body/div[1]/header/div[2]/div/div[1]/div[4]/div/label')
sqbutton = browser.find_element_by_xpath('/html/body/div[1]/header/div[2]/div/div[1]/div[4]/div/label')
sqbutton.get_attribute('href')
sqbutton.click()

browser.find_element_by_xpath('/html/body/div[1]/header/div[3]/div/form/div/div[1]/input')
sqtextfield = browser.find_element_by_xpath('/html/body/div[1]/header/div[3]/div/form/div/div[1]/input')
sqtextfield.send_keys(input_sq)
searchbutton = browser.find_element_by_xpath('/html/body/div[1]/header/div[3]/div/form/div/div[2]/button')
searchbutton.click()

addtocartbutton = browser.find_element_by_xpath('/html/body/div[2]/main/div/div/div[1]/a/form/button/span')
addtocartbutton.click()

checkoutbutton = browser.find_element_by_xpath('/html/body/div[2]/main/div[1]/div/div/form/div/div/div[2]/div/button[2]')
checkoutbutton.click()
checkoutbutton.click()

namefield = browser.find_element_by_xpath('/html/body/div[2]/div/div[1]/div[2]/div/form/div[1]/div[2]/div[2]/div/div[1]/div/input')
namefield.send_keys(input_name)

lastfield = browser.find_element_by_xpath('/html/body/div[2]/div/div[1]/div[2]/div/form/div[1]/div[2]/div[2]/div/div[2]/div/input')
lastfield.send_keys(input_last)

addressfield = browser.find_element_by_xpath('/html/body/div[2]/div/div[1]/div[2]/div/form/div[1]/div[2]/div[2]/div/div[4]/div/input')
addressfield.send_keys(address)

apartmentfield = browser.find_element_by_xpath('/html/body/div[2]/div/div[1]/div[2]/div/form/div[1]/div[2]/div[2]/div/div[5]/div/input')
apartmentfield.send_keys(apartment)

cityfield = browser.find_element_by_xpath('/html/body/div[2]/div/div[1]/div[2]/div/form/div[1]/div[2]/div[2]/div/div[6]/div/input')
cityfield.send_keys(city)

zipfield =  browser.find_element_by_xpath("/html/body/div[2]/div/div[1]/div[2]/div/form/div[1]/div[2]/div[2]/div/div[9]/div/input")
zipfield.send_keys(zipcode)

