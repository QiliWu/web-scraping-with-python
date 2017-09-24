from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains

driver = webdriver.PhantomJS(executable_path=r'D:\03-CS\plantomJS\phantomjs-2.1.1-windows\bin\phantomjs')
driver.get("http://pythonscraping.com/pages/files/form.html")

firstnameField = driver.find_element_by_name('firstname')
lastnameField = driver.find_element_by_name('lastname')
submitField = driver.find_element_by_id('submit')

#--method one--
firstnameField.send_keys('Qili')
lastnameField.send_keys('Wu')
submitField.click()


#--method two--
actions = ActionChains(driver).click(firstnameField).send_keys('Qili').click(lastnameField).send_keys('Wu').send_keys(Keys.RETURN)
actions.perform()
#------


print(driver.find_element_by_tag_name('body').text)
driver.close()