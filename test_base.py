import pytest
from selenium import webdriver
import requests
import time
from selenium.webdriver import ActionChains
import os



@pytest.mark.usefixtures("init__driver")
class BaseTest:
    pass

class Testdemo(BaseTest):

    def test1_broken_links(self):
        self.driver.get("http://the-internet.herokuapp.com/broken_images")
        links = self.driver.find_elements_by_tag_name("a")
        for link in links:
            r = requests.head(link)
            if r.status_code != 404:
                self.driver.get(link)
            else:
                print(str(link) + " isn't available.")

    def test2_forgot_passwd(self):
        self.driver.get("http://the-internet.herokuapp.com/forgot_password")
        print("third test")
        self.driver.find_element_by_xpath("//input[@id='email']").send_keys("test@yopmail.com")
        time.sleep(3)
        self.driver.find_element_by_xpath("//i[@class='icon-2x icon-signin']").click()
        time.sleep(3)
        a = self.driver.find_element_by_xpath("//h1[contains(text(),'Internal Server Error')]").text
        assert a=='Internal Server Error'
        print("second test is success")
        print(a)
        print("current working directory is "+os.getcwd())
        folder = os.getcwd() + "//forgot.png"
        self.driver.get_screenshot_as_file(folder)
       # webdriver.Firefox.find_element_by_xpath("//h1[contains(text(),'Internal Server Error')]").text

    def test3_form_valid(self):
        self.driver.get("http://the-internet.herokuapp.com/login")
        print("third test")
        self.driver.find_element_by_xpath("//input[@id='username']").send_keys("tomsmith")
        time.sleep(3)
        self.driver.find_element_by_xpath("//input[@id='password']").send_keys("SuperSecretPassword!")
        time.sleep(3)
        self.driver.find_element_by_xpath("//i[@class='fa fa-2x fa-sign-in']").click()
        time.sleep(3)
        a=self.driver.find_element_by_xpath("//a[contains(text(),'Elemental Selenium')]").text
        time.sleep(3)
        assert a=="Elemental Selenium"
        print("third test is sucess")
        print(a)
        folder = os.getcwd() + "//formval.png"
        self.driver.get_screenshot_as_file(folder)
        #webdriver.Firefox.find_element_by_xpath("//h1[contains(text(),'Internal Server Error')]").is_displayed()

    def test4_alphaform_valid(self):
        self.driver.get("http://the-internet.herokuapp.com/inputs")
        print("fourth test")
        self.driver.find_element_by_xpath("//input[@type='number']").send_keys("abcd")
        time.sleep(3)
        folder = os.getcwd() + "//screenalpha.png"
        self.driver.get_screenshot_as_file(folder)

    def test5_sorttables_valid(self):
        self.driver.get("http://the-internet.herokuapp.com/tables")
        print("fifth test")
        time.sleep(3)
        self.driver.find_element_by_xpath("//a[contains(text(),'edit')]").click()
        time.sleep(3)
        self.driver.find_element_by_xpath("//table[@id='table1']//span[contains(text(),'Due')]").click()
        print("sorting tables")
        time.sleep(3)
        el=  self.driver.find_element_by_xpath("//table[@id='table1']//span[contains(text(),'Due')]")
        action = ActionChains(self.driver)
        time.sleep(3)
        action.click(el)
        time.sleep(3)
        action.click(el)
        print("sorting tables")
        folder = os.getcwd()+"//tables.png"
        self.driver.get_screenshot_as_file(folder)

    def test6_notif_msg_rend(self):
        time.sleep(2)
       # self.driver.get("http://the-internet.herokuapp.com/notification_message_rendered")
       # e2= self.driver.find_element_by_xpath("//a[normalize-space()='Click here']")
        print("sixth test")
        for x in range(6):
            time.sleep(3)
            print(x)
            self.driver.get("http://the-internet.herokuapp.com/notification_message_rendered")
            e2 = self.driver.find_element_by_xpath("//a[normalize-space()='Click here']")
          #  action1 = ActionChains(self.driver)
          #  action1.click(e2)
            e2.click()
            time.sleep(2)
            a3='Action successful'
            time.sleep(4)
           # a4=self.driver.find_element_by_xpath("//div[contains(text(),'Action successful')]")
            if a3==self.driver.find_element_by_xpath("//div[contains(text(),'Action successful')]").text:
                print(a3)
                assert a3==self.driver.find_element_by_xpath("//div[contains(text(),'Action successful')]").text
                print("sixth test is passing")
            else:
                print("testing123")
                folder =os.getcwd()+"//notif.png"
                self.driver.get_screenshot_as_file(folder)














