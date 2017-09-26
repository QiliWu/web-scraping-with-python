#coding=utf-8
from selenium import webdriver

driver = webdriver.PhantomJS(executable_path=r'D:\03-CS\plantomJS\phantomjs-2.1.1-windows\bin\phantomjs')
driver.get("http://pythonscraping.com")
driver.implicitly_wait(3)
print('-'*40)
print(driver.get_cookies())

savedcookies = driver.get_cookies()

driver2 = webdriver.PhantomJS(executable_path=r'D:\03-CS\plantomJS\phantomjs-2.1.1-windows\bin\phantomjs')
driver2.get("http://pythonscraping.com")
driver2.implicitly_wait(3)
print('-'*40)
print(driver2.get_cookies())
driver2.delete_all_cookies()

#driver2.get("http://pythonscraping.com")
#driver2.implicitly_wait(3)
#print('-'*40)
#print(driver2.get_cookies())

for cookie in savedcookies:
    driver2.add_cookie(cookie)

driver2.get("http://pythonscraping.com")
driver2.implicitly_wait(3)
print('-'*40)
print(driver2.get_cookies())