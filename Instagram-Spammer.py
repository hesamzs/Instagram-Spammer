#Install-selenium
#Download-FireFox-WebDriver

from selenium import webdriver
from time import sleep
import time
import cfonts
import colorama

colorama.init()
print(cfonts.render("Instgram Spammer" , colors=["red" , "yellow"]))

print(colorama.Fore.GREEN+'''
🔒 - Use at your own risk, we are not responsible for your actions.
☑️ - Made by  Hesamzs and Mazdak Pakaghideh.
📝 - Notes: follow the instructions below .
'''+colorama.Fore.RESET)
print(colorama.Fore.GREEN+'''
=======
📝 - Instructions:
--------------------------------------------------------
|1-) Type the Instagram account username               |
|                                                      |
|2-) Type the Instagram account password               |
|                                                      |
|3-) Enter the name of user or group                   |                                               
|                                                      |
|4-) Delay beatwean each message                       |
|                                                      |
|5-) Message body                                      |
|                                                      |
|6-) Enter the count of Messgae                        |
|                                                      |   
|                                                      | 
-------------------------------------------------------|
''')



start = str(input("🔥 - Type ENTER to open browser "))
firefox = webdriver.Firefox(executable_path="./geckodriver")

firefox.get('https://www.instagram.com/')
print(colorama.Fore.BLUE+"Enter your username")
username = str(input("=> "))
print( colorama.Fore.BLUE+"Enter your password")
password = str(input("=> "))

print(colorama.Fore.BLUE+"Enter the name of user or group")
contact = str(input("=> "))

print(colorama.Fore.BLUE+"Enter the Delay beatwean each message (from 0.1)")
delay = float(input("=> "))

print(colorama.Fore.BLUE+"Enter your message")
message = str(input("=> "))


print(colorama.Fore.BLUE+"Enter the count (0 for ultimated)")
countmsg = int(input("=> "))



#Start-To-Login
def sendMessage(msg , delay , user , passwd , count , contact_name):
    sleep(1)
    username_input = firefox.find_element_by_xpath(
    "//input[@name='username']")
    username_input.send_keys(user)
    
    password_input = firefox.find_element_by_xpath(
    "//input[@name='password']")
    password_input.send_keys(passwd)
    submit_btn = firefox.find_element_by_xpath(
        "//button[@type='submit']")
    submit_btn.click()
    
    sleep(7)
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
    firefox.find_element_by_xpath('/html/body/div[4]/div/div/div[2]/div[1]/div/div[2]/input').send_keys(contact_name)
    sleep(2)
    firefox.find_element_by_xpath('/html/body/div[4]/div/div/div[2]/div[2]/div[1]/div/div[3]/button/span').click()
    
    sleep(2)
    #Open-Contact-Direct
    firefox.find_element_by_xpath('/html/body/div[4]/div/div/div[1]/div/div[2]/div/button/div').click()
    
    sleep(2)
    #Starting-Spam-:)
    if count == 0:
        while 1:
                firefox.find_element_by_xpath('/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea').send_keys(msg)

                firefox.find_element_by_xpath(
        '//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button').click()
                sleep(delay)
        
    else:
            for i in range(count):

                firefox.find_element_by_xpath('/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea').send_keys(msg)

                firefox.find_element_by_xpath(
        '//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button').click()
                sleep(delay)
        
            
        
sendMessage(message , delay , username  ,password , countmsg , contact)
#Completed
#
#Instagram ==> _.hesampv
#Telegram ==> @hesamzs

