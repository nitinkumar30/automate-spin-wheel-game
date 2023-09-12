import pyperclip as pyperclip
import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import csv

URL = "https://wordwall.net/create/editcontent?guid=a7818eace12248abad19a059e5d8a564"

#########################################################################################
# TEXT INPUTS
#########################################################################################
username = "himetih398@horsgit.com"
password = "cG/8W?7KxF9,Pa2"
title_input = "AJU MCA 2021 spin wheel"
desc = "AJU MCA 2021 batch spin wheel"

#########################################################################################
# XPATHS
#########################################################################################
email = "//input[@id='Email']"
pswd = "//input[@id='Password']"
login = "//button[@class='default-btn js-btn-load account-submit-btn medium text-input']"
title = "//input[@class='js-activity-title']"
description = "//input[@class='js-instruction-input']"
add_option = "//div[@class='editor-add-item js-editor-add-item no-select ']"
done = "//button[@class='default-btn large js-done-button']"
share = "//a[@class='default-btn white share-button js-share-button  js-share-button-private']"
res_title = "//input[@class='formfield-input formfield-title js-resource-title']"
publish = "//a[@class='default-btn large js-next-publish cta-spacer']"
copy_link = "//a[@class='default-btn js-share-link-copy']"

#########################################################################################
# CSV FILE READ
#########################################################################################

file_path = "names.csv"
lines = []
n = num = 1
with open(file_path, mode='r', newline='') as file:
    csv_reader = csv.reader(file)

    for row in csv_reader:
        lines.append(row[0])


opt = webdriver.ChromeOptions()
opt.add_argument("--start-maximized")
chromedriver_autoinstaller.install()
browser = webdriver.Chrome(options=opt)


#########################################################################################
# FUNCTIONS
#########################################################################################

def ss():
    global num
    time.sleep(1)
    browser.save_screenshot('screenshots/' + str(num) + '.png')
    num += 1


def click(xpath):
    browser.find_element(By.XPATH, xpath).click()
    ss()
    time.sleep(1)
    print("Element clicked")


def input(xpath, text):
    ele = browser.find_element(By.XPATH, xpath)
    ele.clear()
    ele.send_keys(text)
    ss()
    time.sleep(1)
    print("Text inserted in the element")


#########################################################################################
# STEPS
#########################################################################################

browser.get(URL)
print('URL navigated')

# Put email & password
input(email, username)
input(pswd, password)
click(login)
time.sleep(2)
ss()


# Put title
input(title, title_input)
time.sleep(2)
ss()

# Put description
input(description, desc)
time.sleep(2)
ss()


# Type option

for name in lines:
    option = "//*[@id='editor_component_0']/div/div/div[" + str(n) + "]/div[3]/div[5]/div/span"
    print("XPATH -", option, "NAME -", name)

    input(option, name)
    print(name, "NAME ADDED")
    if n < 40:
        click(add_option)
        print("OPTION ADDED")
    n += 1
    # time.sleep(10)

# Then apply loop
click(done)
print("SPIN WHEEL DARE CREATED.")

click(share)
input(res_title, title_input)
click(publish)
click(copy_link)
time.sleep(2)
ss()

# Reads text from clipboard & displays it
link = pyperclip.paste()
print("LINK TO THE DARE -", link)

time.sleep(5)
