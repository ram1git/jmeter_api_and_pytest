from selenium import webdriver
import time
from selenium.webdriver.common.by import By
#import repconfig
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import pytest
import os


@pytest.fixture(params=["firefox"],scope='class')
def init__driver(request):
    if request.param == "chrome":
        web_driver = webdriver.Chrome(executable_path="C:\\Users\Admin\\Downloads\\chromedriver_win32new\\chromedriver.exe")
    if request.param == "firefox":
        web_driver = webdriver.Firefox(executable_path=os.getcwd()+"\\geckodriver.exe")
    request.cls.driver = web_driver
    yield
    web_driver.close()