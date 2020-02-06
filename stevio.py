
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import NoSuchElementException
browser = webdriver.Chrome('/Users/stevemint/Downloads/chromedriver 2')

def executeBot():

    #this is were you add the link you want to open
    browser.get('https://shop.funko.com/collections/funko-shop-exclusives')
    #here are the values for each input and here is where you can replace them
    input_sq = "cthulu"
    input_mail = "tortugarara@gmail.com"
    input_name = "Lety"
    input_last = "Molinisky"
    address = "9807 NF"
    apartment = "123"
    city = "Austin"
    zipcode = "78726"
    state = "Texas"



    #each "method" has the same structure, reaches an element-> stores it as a button -> clicks it
    browser.find_element_by_xpath('//*[@id="SiteNavSearchCart"]/label')
    sqbutton = browser.find_element_by_xpath('//*[@id="SiteNavSearchCart"]/label')
    sqbutton.get_attribute('href')
    sqbutton.click()

    #in this case it is stored as a text field -> sends keys that are the parameters stated before

    sqtextfield = browser.find_element_by_xpath('//*[@id="SearchDrawer"]')
    sqtextfield.send_keys(input_sq)
    searchbutton = browser.find_element_by_xpath('//*[@id="shopify-section-header"]/header/div[2]/div/form/div/div[2]/button')
    searchbutton.click()

    #it takes the first element on the list to the cart
    addtocartbutton = browser.find_element_by_xpath('//*[@id="MainContent"]/div/div/div/a/form/button/span')
    addtocartbutton.click()

    #added a sleep so the page can load properly
    sleep(1)

    #Here is a bit of hardcoding since only one click was not enough for it to work each time
    checkoutbutton = browser.find_element_by_xpath('//*[@id="shopify-section-cart-template"]/div/div/form/div/div/div[2]/div/button[2]')
    checkoutbutton.click()



    #wait = WebDriverWait(browser, 2)
    #element = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="checkout_email"]')))
    sleep(1)
    mailfield = browser.find_element_by_xpath('//*[@id="checkout_email"]')
    mailfield.send_keys(input_mail)

    namefield = browser.find_element_by_xpath('//*[@id="checkout_shipping_address_first_name"]')
    namefield.send_keys(input_name)

    lastfield = browser.find_element_by_xpath('//*[@id="checkout_shipping_address_last_name"]')
    lastfield.send_keys(input_last)

    addressfield = browser.find_element_by_xpath('//*[@id="checkout_shipping_address_address1"]')
    addressfield.send_keys(address)

    apartmentfield = browser.find_element_by_xpath('//*[@id="checkout_shipping_address_address2"]')
    apartmentfield.send_keys(apartment)

    cityfield = browser.find_element_by_xpath('//*[@id="checkout_shipping_address_city"]')
    cityfield.send_keys(city)

    stateSelect = browser.find_element_by_xpath('//*[@id="checkout_shipping_address_province"]')
    selected = stateSelect.find_element_by_xpath('//*[@id="checkout_shipping_address_province"]/option[52]')
    selected.click()

    zipfield = browser.find_element_by_xpath('//*[@id="checkout_shipping_address_zip"]')
    zipfield.send_keys(zipcode)
    sleep(1)
    zipfield.send_keys(Keys.ENTER)


executeBot()

