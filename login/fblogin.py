
from selenium import webdriver

browser = webdriver.Chrome('chromedriver.exe')  # Optional argument, if not specified will search path.


# Step 2) Navigate to Facebook
browser.get("http://www.facebook.com")
# Step 3) Search & Enter the Email or Phone field & Enter Password
username = browser.find_element_by_id("email")
password = browser.find_element_by_id("pass")
submit   = browser.find_element_by_name("login")
username.send_keys("nidclone@gmail.com")
password.send_keys("Vietthinh2k1")
# Step 4) Click Login
submit.click()
