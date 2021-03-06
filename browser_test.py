'''
Testing browsers configuration in selenium python
'''
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome import service
from time import sleep

def choosebrowser(browser):
    '''
    configurations for different browsers
    '''
    if browser=="chrome":
        # for chrome
        # set the path to chromedriver AND 
        # remove the annoying infobar telling me that Chrome is being controlled by automated software
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--disable-infobars")
        driver = webdriver.Chrome("C:\\folded\\browsdrv\\krom\\chromedriver.exe", chrome_options=chrome_options)
        return driver
    elif browser=="firefox":
        # setup the firefox profile that disables tab that opens "insecure password warning"(accept_untrusted_certs) 
        # and disables contextual warning as well 
        #(by setting firefox preferences security.insecure_field_warning.contextual.enabled)
        profajl = webdriver.FirefoxProfile()
        profajl.accept_untrusted_certs = True
        profajl.set_preference("security.insecure_field_warning.contextual.enabled", False)
        driver = webdriver.Firefox(firefox_profile=profajl, executable_path=r"C:\\folded\\browsdrv\\gecko\\geckodriver.exe")
        return driver
    elif browser=="opera":
        # for opera on selenium 3.4.3 uncomment three following lines
        
        #webdriver_service = service.Service("C:\\folded\\browsdrv\\opera\\operadriver.exe")
        #webdriver_service.start()
        #driver = webdriver.Remote(webdriver_service.service_url, webdriver.DesiredCapabilities.OPERA)

        # for opera on selenium 3.5.0 use the following 
        driver = webdriver.Opera(executable_path="C:\\folded\\browsdrv\\opera\\operadriver.exe")
        return driver
    elif browser=="edge":
        # for edge zoom MUST be set at 100% or else click() is not working 
        driver = webdriver.Edge("C:\\folded\\browsdrv\\edge\\MicrosoftWebDriver.exe")
        return driver
    elif browser=="ie":
        # for IE let's first set capabilities
        capabilities = DesiredCapabilities.INTERNETEXPLORER
        # on selenium 3.4.3 you need to get sort out platform and version keys in capabilities dictionary
        # you can do that like this (see more info in README.md):
        
        #capabilities.pop("platform", None)
        #capabilities.pop("version", None)
        
        # then initialize the driver
        driver = webdriver.Ie(executable_path="C:\\folded\\browsdrv\\ied\\IEDriverServer32.exe", capabilities=capabilities)
        return driver
    else:
        print("Wrong value. Please enter one of the following: chrome, firefox, opera, edge, ie")

        
        
'''
====================================
open chosen browser,
go to google,
enter "python"
and go to python website
====================================
'''
# choose which browser you want to start: ie, chrome, firefox, opera or edge
driver=choosebrowser("ie")
# go to google or wherever
driver.get("https://www.google.rs/")
WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.NAME, "q")))
print("we're here")
# enter "python"
driver.find_element_by_name("q").send_keys("python")
driver.find_element_by_name("q").send_keys(Keys.ENTER)
print("typed it in and searched")
# wait until results show up then click the first result with the link test "Welcome to Python.org"
sleep(1)
WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.LINK_TEXT, "Welcome to Python.org")))
driver.find_element_by_link_text("Welcome to Python.org").click()
print("link clicked")
# wait until python logo shows up
WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CLASS_NAME, "python-logo")))
print("and we're there! yaaay")

