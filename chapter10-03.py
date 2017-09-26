from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import StaleElementReferenceException
import time

def waitForLoad(driver):
    elem = driver.find_element_by_tag_name('html')
    print(elem.text)
    count = 0
    while True:
        count += 1
        if count > 10:
            print ('Timing out after 10 seconds and returning')
            return
        time.sleep(0.5)
        #elem ==driver.find_element_by_tag_name('html') will just return True or False,
        #but will never raise a StaleElementReferenceException.

        #It will only raise a StaleElementReferenceException when using elem to do something
        # while it is not the original one due to the page changing.
        try:
            elem.text == driver.find_element_by_tag_name('html').text
        except StaleElementReferenceException:
            return


driver = webdriver.PhantomJS(executable_path=r'D:\03-CS\plantomJS\phantomjs-2.1.1-windows\bin\phantomjs')
driver.get('http://pythonscraping.com/pages/javascript/redirectDemo1.html')
waitForLoad(driver)
print(driver.page_source)