import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By
# start the browser
options = Options()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-gpu")
options.add_argument("--window-size=1920,1080")
driver = webdriver.Remote(
   command_executor='http://ec2-3-17-64-190.us-east-2.compute.amazonaws.com:4444/wd/hub',
   desired_capabilities=DesiredCapabilities.CHROME,
   options=options)
print '01'
time.sleep(3)
# Navigate to url
#driver.get("https://www.google.com")
driver.get("https://ito-kodai031.outsystemscloud.com/Bookings/RoomDetail.aspx")
#assert 'Google' in driver.title
print '02'
time.sleep(3)
#driver.get_screenshot_as_file("./1.png")
# Store 'google search' button web element
time.sleep(3)
#nameQ = driver.find_element_by_name("q")
ele = driver.find_element(By.ID, "OutSystemsUIWeb_wt14_block_wtLogin_OutSystemsUIWeb_wt15_block_wtLogin_OutSystemsUIWeb_wt26_block_wtInput_wtUserNameInput")
print '03'
time.sleep(3)
# Performs mouse move action onto the element
ele.send_keys("Selenium WebDriver")
print '04'
time.sleep(3)
#driver.get_screenshot_as_file("./2.png")
time.sleep(3)
webdriver.ActionChains(driver).move_to_element(ele).perform()
time.sleep(3)
driver.get_screenshot_as_file("./3.png")
time.sleep(3)
driver.close()
