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


def executeBot():
    #this is were you add the link you want to open
    browser.get('https://shop.funko.com/collections/funko-shop-exclusives')
    #here are the values for each input and here is where you can replace them
    input_sq = "star wars"
    input_mail = "tortugarara@gmail.com"
    input_name = "Letinsky"
    input_last = "Molinisky"
    address = "lalaland 29"
    apartment = "123"
    city = "saltadilla"
    zipcode = "89909"




    #each "method" has the same structure, reaches an element-> stores it as a button -> clicks it
    browser.find_element_by_xpath('/html/body/div[1]/header/div[2]/div/div[1]/div[4]/div/label')
    sqbutton = browser.find_element_by_xpath('/html/body/div[1]/header/div[2]/div/div[1]/div[4]/div/label')
    sqbutton.get_attribute('href')
    sqbutton.click()

    #in this case it is stored as a text field -> sends keys that are the parameters stated before
    browser.find_element_by_xpath('/html/body/div[1]/header/div[3]/div/form/div/div[1]/input')
    sqtextfield = browser.find_element_by_xpath('/html/body/div[1]/header/div[3]/div/form/div/div[1]/input')
    sqtextfield.send_keys(input_sq)
    searchbutton = browser.find_element_by_xpath('/html/body/div[1]/header/div[3]/div/form/div/div[2]/button')
    searchbutton.click()

    #it takes the first element on the list to the cart
    addtocartbutton = browser.find_element_by_xpath('/html/body/div[2]/main/div/div/div[1]/a/form/button/span')
    addtocartbutton.click()

   #Here is a bit of hardcoding since only one click was not enough for it to work each time
    checkoutbutton = browser.find_element_by_xpath('/html/body/div[2]/main/div[1]/div/div/form/div/div/div[2]/div/button[2]')
    checkoutbutton.click()
    checkoutbutton.click()

    mailfield = browser.find_element_by_xpath('/html/body/div[2]/div/div[1]/div[2]/div/form/div[1]/div[1]/div[2]/div[1]/div/div/input')
    mailfield.send_keys(input_mail)

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
executeBot()
