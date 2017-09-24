from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver import ActionChains
import unittest

class TestAddition(unittest.TestCase):
    driver = None
    def setUp(self):
        global driver
        driver = webdriver.PhantomJS(executable_path=r'D:\03-CS\plantomJS\phantomjs-2.1.1-windows\bin\phantomjs')
        driver.get('http://pythonscraping.com/pages/javascript/draggableDemo.html')

    def tearDown(self):
        print("Tearing down the test")

    def test_drag(self):
        global driver
        element = driver.find_element_by_id("draggable")
        target = driver.find_element_by_id('div2')
        actions = ActionChains(driver)
        actions.drag_and_drop(element, target).perform()

        self.assertEqual("You are definitely not a bot!", driver.find_element_by_id("message").text)


if __name__ == '__main__':
    unittest.main()