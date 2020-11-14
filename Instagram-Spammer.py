#Install-selenium
#Download-FireFox-WebDriver

from selenium import webdriver
from time import sleep

firefox = webdriver.Firefox(executable_path="./geckodriver")

firefox.get('https://www.instagram.com/')
sleep(1)
#Answer-All-Questions
username = input('Enter Your Username : ')
password = input('Enter Your Password : ')
contact  = input('Enter the name of user or group : ')
message  = input('Enter your message : ')
countmsg = int(input('Enter the count : '))


#Start-To-Login
sleep(1)
username_input = firefox.find_element_by_xpath(
    "//input[@name='username']")
username_input.send_keys(username)
sleep(1)
password_input = firefox.find_element_by_xpath(
    "//input[@name='password']")
password_input.send_keys(password)
submit_btn = firefox.find_element_by_xpath(
    "//button[@type='submit']")
submit_btn.click()
sleep(5)

#Start-Canceling-Ads
try:
    firefox.find_element_by_xpath(
        '//*[@id="react-root"]/section/main/div/div/div/div/button').click()
except:
    pass
firefox.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]').click()
sleep(5)

#Open-Directs
firefox.find_element_by_xpath('//a[@class="xWeGp"]/*[name()="svg"][@aria-label="Direct"]').click()
sleep(2)

#Search-Your-Contact
firefox.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div/button').click()
sleep(2)
firefox.find_element_by_xpath('/html/body/div[4]/div/div/div[2]/div[1]/div/div[2]/input').send_keys(contact)
sleep(2)
firefox.find_element_by_xpath('/html/body/div[4]/div/div/div[2]/div[2]/div[1]/div/div[3]/button/span').click()
sleep(2)

#Open-Contact-Direct
firefox.find_element_by_xpath('/html/body/div[4]/div/div/div[1]/div/div[2]/div/button/div').click()
sleep(2)

#Starting-Spam-:)
for i in range(countmsg):

    firefox.find_element_by_xpath('/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea').send_keys(message)

    firefox.find_element_by_xpath(
    '//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button').click()
    
    
#Completed
#
#Instagram ==> _.hesampv
#Telegram ==> @hesamzs

