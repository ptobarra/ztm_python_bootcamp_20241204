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
print(button.get_attribute('innerHTML')) # this should return the innerHTML of the element: 'Button2'

# button = chrome_browser.find_element(By.ID, "prompt") # this should return a single element
# print(button)
# print(button.get_attribute('innerHTML')) # this should return the innerHTML of the element

# Locate the button by its ID
button = chrome_browser.find_element(By.ID, "prompt")

# Get the text of the button from its 'value' attribute
button_text = button.get_attribute('value')
print(f"The text of the button is: {button_text}")

# Ensure the text is as expected
assert button_text == "GetPrompt", "Button text does not match!"

assert 'GetPrompt' in chrome_browser.page_source # this should not raise an exception

# Locate the textarea element by its tag name
textarea_element = chrome_browser.find_element(By.TAG_NAME, "textarea")
# Clear the textarea if needed
textarea_element.clear()
# Send some text to the textarea
textarea_element.send_keys("I AM EXTRA COOOOL")

# Locate the textarea element by its ID
textarea_element_written = chrome_browser.find_element(By.ID, "ta1")

# Grab the text written in the textarea
textarea_text_written = textarea_element_written.get_attribute('value')
print(f"The text inside the textarea is: {textarea_text_written}")

# Ensure the text is as expected
assert textarea_text_written == "I AM EXTRA COOOOL", "Textarea text does not match!"

# Locate the timerButton by its ID
timerButton = chrome_browser.find_element(By.ID, "timerButton")

# Simulate a click on the timerButton
timerButton.click()

# Locate the input element using a CSS selector
login_button = chrome_browser.find_element(By.CSS_SELECTOR, 'input[onclick="check(this.form)"]')

# Simulate a click on the button
login_button.click()

# Print confirmation
print("Login button was clicked!")

# To grab all the buttons inside the <form> element using Selenium, you can use the find_elements method with a CSS selector that targets all <input> elements of type button or reset within the form.

# Locate the form element by its name
form_element = chrome_browser.find_element(By.NAME, "login")

# Grab all buttons inside the form
buttons = form_element.find_elements(By.CSS_SELECTOR, 'input[type="button"], input[type="reset"]')

# Print the text or value of each button
for button in buttons:
    button_value = button.get_attribute('value')
    print(f"Button found with value: {button_value}")


# Prevent the browser from closing immediately
input("press enter to close the browser...")
chrome_browser.quit()

