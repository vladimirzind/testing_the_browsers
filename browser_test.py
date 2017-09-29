'''
Testing browsers configuration in selenium python
'''
from selenium import webdriver
from selenium.webdriver import Ie
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome import service
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.opera.webdriver import WebDriver
from selenium.webdriver.ie.webdriver import WebDriver as IE
from time import time
from time import sleep
