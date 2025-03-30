from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_browser = webdriver.Chrome()

chrome_browser.maximize_window()
chrome_browser.get('https://omayo.blogspot.com/') # notice the URL has changed from the video to the new demo site!

print('omayo (QAFox.com)' in chrome_browser.title) # this should return True
print('Python Easy Demo' in chrome_browser.title) # this should return False

assert 'omayo (QAFox.com)' in chrome_browser.title # this should not raise an exception
# assert 'Python Easy Demo' in chrome_browser.title # this should raise an exception

# assert 'omayo (QAFox.com)' in chrome_browser.body # this should not raise an exception
# assert 'Python Easy Demo' in chrome_browser.body # this should not raise an exception

# find the element by class name
# button = chrome_browser.find_element(By.CLASS_NAME, 'widget-content') # this should return a single element
button = chrome_browser.find_element(By.ID, "but2") # this should return a single element
# print(button)
print(button.get_attribute('innerHTML')) # this should return the innerHTML of the element

# i want selenium not to close the browser after the script is done
input("press enter to close the browser...")
chrome_browser.quit()

