from selenium import webdriver
import time
import re
import os


#Getting browser current page URL
driver = webdriver.Chrome(executable_path = "C:\\Users\\adarb\\Documents\\devops\\gitprojects\\FinalProject\\chromedriver.exe")
driver.get("http://192.168.99.100:5000")
driver.implicitly_wait(10)
driver.maximize_window()

el = driver.find_element_by_tag_name("body").text

print(el)