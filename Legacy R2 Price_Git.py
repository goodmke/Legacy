from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
options = webdriver.ChromeOptions()
#command about closing gui?
options.add_argument("--headless")

# gets the website
driver = webdriver.Chrome("C:\Program Files (x86)\chromedriver.exe" , chrome_options=options)
driver.get("https://www.legacyhomesal.com/pennington-freedom-series-richmond-ii")

# finds the Base Price header
price = driver.find_element_by_xpath("//h3[@class='ng-binding']")
print(price.text)

# converts the string to integer
p = price.text[12::]
r = int(p.replace(',', ''))
driver.close()
if r <= 278900:
    print("No price change. Your equity is: ", r - INPUT_INITIAL_INVESTMENT)
    #print("No price change. Your equity is: ", int(userQuantityPurchased) + int(userPrice))

    PATH = "C:\Program Files (x86)\chromedriver.exe"
    driver = webdriver.Chrome(PATH)

    # gets the google login website
    driver.get("https://accounts.google.com/o/oauth2/v2/auth/oauthchooseaccount?redirect_uri=https%3A%2F%2Fdevelopers"
               ".google.com%2Foauthplayground&prompt=consent&response_type=code&client_id=407408718192.apps"
               ".googleusercontent.com&scope=email&access_type=offline&flowName=GeneralOAuthFlow")

    # clicks on the sign in field, clears contents and writes username and password
    driver.find_element_by_id("identifierId").click()
    driver.find_element_by_id("identifierId").clear()
    driver.find_element_by_id("identifierId").send_keys("INPUT GOOGLE USERNAME")
    driver.find_element_by_class_name("VfPpkd-RLmnJb").click()
    time.sleep(3)
    driver.find_element_by_xpath('//*/div[1]/div/div[1]/input').send_keys('INPUT GOOGLE PASSWORD')
    driver.find_element_by_class_name('VfPpkd-RLmnJb').click()

    # gets google voice
    driver.get("https://voice.google.com/u/0/messages")
    time.sleep(2)
    driver.find_element_by_xpath('//*/div[2]/a[2]').click()
    time.sleep(2)
    driver.get('https://voice.google.com/u/0/messages')
    time.sleep(3)

    # Sends New Message, types in the mdn, clicks on the correct contact, types the message, sends
    driver.find_element_by_xpath('//*[@id="messaging-view"]/div/md-content/div/div/div/div[2]').click()
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="input_1"]').send_keys('INPUT YOUR PHONE NUMBER')
    driver.find_element_by_xpath('//*[@id="input_1"]').send_keys(Keys.RETURN)
    driver.find_element_by_xpath('//*[@id="input_1"]').send_keys('INPUT ANY OTHER PHONE NUMBER YOU WANT SMS TO GO TO')
    driver.find_element_by_xpath('//*[@id="input_1"]').send_keys(Keys.RETURN)
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="input_2"]').send_keys('No price change on the Richmond II. Your equity is: $', r - INPUT_INITIAL_INVESTMENT)
    driver.find_element_by_xpath('//*[@id="input_2"]').send_keys(Keys.RETURN)
    time.sleep(2)
    driver.close()
else:
    print("The price has increased!! Your equity is: ", r- INPUT_INITIAL_INVESTMENT)

    PATH = "C:\Program Files (x86)\chromedriver.exe"
    driver = webdriver.Chrome(PATH)

    # gets the google login website
    driver.get("https://accounts.google.com/o/oauth2/v2/auth/oauthchooseaccount?redirect_uri=https%3A%2F%2Fdevelopers"
               ".google.com%2Foauthplayground&prompt=consent&response_type=code&client_id=407408718192.apps"
               ".googleusercontent.com&scope=email&access_type=offline&flowName=GeneralOAuthFlow")

    # clicks on the sign in field, clears contents and writes username and password
    driver.find_element_by_id("identifierId").click()
    driver.find_element_by_id("identifierId").clear()
    driver.find_element_by_id("identifierId").send_keys("INPUT GOOGLE USERNAME")
    driver.find_element_by_class_name("VfPpkd-RLmnJb").click()
    time.sleep(3)
    driver.find_element_by_xpath('//*/div[1]/div/div[1]/input').send_keys('INPUT GOOGLE PASSWORD')
    driver.find_element_by_class_name('VfPpkd-RLmnJb').click()

    # gets google voice
    driver.get("https://voice.google.com/u/0/messages")
    time.sleep(2)
    driver.find_element_by_xpath('//*/div[2]/a[2]').click()
    time.sleep(2)
    driver.get('https://voice.google.com/u/0/messages')
    time.sleep(3)
    # Sends New Message, types in the mdn, clicks on the correct contact, types the message, sends
    driver.find_element_by_xpath('//*[@id="messaging-view"]/div/md-content/div/div/div/div[2]').click()
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="input_1"]').send_keys('INPUT YOUR PHONE NUMBER')
    driver.find_element_by_xpath('//*[@id="input_1"]').send_keys(Keys.RETURN)
    driver.find_element_by_xpath('//*[@id="input_1"]').send_keys('INPUT ANY OTHER PHONE NUMBER YOU WANT SMS TO GO TO')
    driver.find_element_by_xpath('//*[@id="input_1"]').send_keys(Keys.RETURN)
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="input_2"]').send_keys('The Richmond II price has gone up! '
                                                                 'https://www.legacyhomesal.com/pennington-freedom'
                                                                 '-series-richmond-ii', 'Your equity is: $', r- INPUT INITIAL INVESTMENT)
    driver.find_element_by_xpath('//*[@id="input_2"]').send_keys(Keys.RETURN)
    time.sleep(2)
    driver.quit()
# next is to create a scheduled task which will run this script every day.
