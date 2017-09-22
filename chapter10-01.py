from selenium import webdriver
import time

driver = webdriver.PhantomJS(executable_path=r'D:\03-CS\plantomJS\phantomjs-2.1.1-windows\bin\phantomjs')
driver.get('http://pythonscraping.com/pages/javascript/ajaxDemo.html')
time.sleep(5)
print(driver.find_element_by_id('content').text)
driver.close()