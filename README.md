# testing_the_browsers
Here we will test whether or not we can open the browsers and google some random word. All done in selenium 3.4.3 and 3.5.0 with python bindings

Browsers that will be tested are: Firefox, Chrome, Edge, Opera, IE...sorry Safari users

IE

for IE driver there is an issue related to "unknown capabilities named platform" error if it is run on selenium 3.4.3.
When starting ie driver wrongly named capabilities were passed to it ("platform" instead "platformName", 
plus "platform" took allcaps strings while "plafromName" took only small caps ("WINDOWS" was passed instead of "windows"); 
the same was happening with "version" key as well)
there are several worarounds for this issue:
  
  1. delete "platform" and "version" keys from "capabilities" dictionary like this:
  capabilities.pop("platform", None)
  capabilities.pop("version", None)
  this solution was provided here: 
  https://stackoverflow.com/questions/45827046/cant-open-ie-using-selenium-in-python/46001825#46001825
  
  
  2. as pointe by Grimlek here: 
  https://github.com/SeleniumHQ/selenium/issues/3808
  delete the line '"capabilities": w3c_caps', from the following piece of code:
  parameters = {"capabilities": w3c_caps,
                     "desiredCapabilities": capabilities}
  this code is located in start_session function located in
  C:\ProgramData\Anaconda3\Lib\site-packages\selenium\webdriver\remote\webdriver.py (exact path may vary)
  
  
  3. update to selenium 3.5.0 where it seems that this issue is no longer occurring

Also there is an issue again related to the IE driver with 64bit version of the driver low typing speed (1 character every 5 seconds). This was explained in great detail here: http://jimevansmusic.blogspot.rs/2014/09/screenshots-sendkeys-and-sixty-four.html
it seems that the only solution for this is using 32bit version of driver


Edge

this must seem by now as some microsoft bashing but it isn't. With Edge zoom level of the browser needs to be set at 100% otherwise click() method will not work. 
Also worth to mention is the issue reported here: https://connect.microsoft.com/IE/feedback/details/1883692 Edge does not fire input events on certain inputs (like radio or checkbox). This issue might break some tests when conducted on Edge.


Chrome

for chrome to work without annoying infobars that are saying that it's being controlled by a robot use the following:
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--disable-infobars")
driver = webdriver.Chrome("C:\\folded\\browsdrv\\krom\\chromedriver.exe", chrome_options=chrome_options)


Firefox

with autoamted test that require often to login and logout of certain websites test may break because of warnings that Firefox is issuing. To disable these warnings consider following:

profajl = webdriver.FirefoxProfile()
profajl.accept_untrusted_certs = True
profajl.set_preference("security.insecure_field_warning.contextual.enabled", False)
driver = webdriver.Firefox(firefox_profile=profajl, executable_path=r"C:\\folded\\browsdrv\\gecko\\geckodriver.exe")

this created firefox profile and then within that profile accepted untrusted certificates and disabled contextual warning about insecure fields.


Opera

for selenium 3.4.3 following configuration worked:

webdriver_service = service.Service("C:\\folded\\browsdrv\\opera\\operadriver.exe")
webdriver_service.start()
driver = webdriver.Remote(webdriver_service.service_url, webdriver.DesiredCapabilities.OPERA)
