# from datetime import datetime,timedelta
# 
# def seconds_delayer(delay_time_in_seconds):
# 
#   present_time = datetime.now()
#   delay_time = present_time + timedelta(0,int(delay_time_in_seconds))
#   expanded_time = delay_time.strftime('%Y-%m-%dT%H:%M:%S')
#   print(expanded_time)
#   return expanded_time
# seconds_delayer("3600")

# import boto3
# import os
# 
# access_key = "AKIA4LQZTKGPYEUZ5W7X"
# secret = "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"
# 
# client =boto3.client('s3',aws_access_key_id = access_key ,aws_secret_access_key = secret)
# 
# for file in os.listdir():
#   if '.py' in file:
#     bucket ='test-bucket'
#     key = "python/"+str(file)
#     client.upload_file(file, bucket, key)
# 
# from woocommerce import API
# 
# wcapi = API(
#     url="https://ambitious-ladybug.jurassic.ninja/",
#     consumer_key="ck_b29086324c67a1ea3a4ead2db47b851f2610cf21",
#     consumer_secret="cs_1613f48dd4d22513aa9926324aa6646e23ccdfdf",
#     wp_api=True,
#     version="wc/v3"
# )
# 
# data ={
#     "update" : [
#         {
#             "id" :25,
#             "default_attributes" :[
#                 {
#                     "id" :25,
#                     "name" :"stock_quantity",
#                     "option" : 1000
#                 }
#             ]
#         }
#     ]
# }
# 
# print(wcapi.post("products/batch", data).json())
# print(wcapi.get("products").json())
# data = {
#     "regular_price": "24.54"
# }
# 
# print(wcapi.put("products/25", data).json())

# from flask import Flask
# import json
# app = Flask(__name__)
# 
# @app.route("/test",methods=["GET"])
# def test():
# 
#     print("test")
#     return("Abishaik")
#     
# app.run(host='0.0.0.0', port=5000)


# print("hello 1") #stringh
# print(1) #integer
# print(1.5) #float
# print(["abishaik",1,2.3]) #list
# 2
# a= int(input())
# b= int(input())
# print(a+b)
# modules required
# from selenium import webdriver
# import time
# 
# # Creating instance for the chrome browser
# driver = webdriver.Chrome(executable_path='./chromedriver')
# 
# 
# # Variables
# url = 'https://go.vdezi.com/'
# emailPath = '//*[@id="mat-input-0"]'
# passwordPath = '//*[@id="mat-input-1"]'
# checkBoxPath = '//*[@id="vdezi-login-login-1"]/label/div'
# signInButton = '//*[@id="mat-tab-content-0-0"]/div/app-login/div/div[2]/form/button'
# 
# # EMAIL CONFIG
# email = 'abishaik01@gmail.com'
# 
# # script
# driver.get(url)
# print("Automation Started")
# try :
#     driver.find_element_by_xpath(emailPath).send_keys(email)
#     driver.find_element_by_xpath(passwordPath).send_keys('password')
#     driver.find_element_by_xpath(checkBoxPath).click()
#     driver.find_element_by_xpath(signInButton).click()
# 
# except EnvironmentError as e:
#     print(e)
#     print('Error')
# 
# print("Sign Up Automation Completed")
# 
# 
# """
# Aim : to Automate the Sign Up using the selenium 
# """
# 
# # modules required
# from selenium import webdriver
# import time
# import random
# import string
# 
# # Creating instance for the chrome browser
# driver = webdriver.Chrome(executable_path='./chromedriver')
# print("Automation Started")
# 
# # Variables
# url = 'https://go.vdezi.com/'
# signUpPath ='//*[@id="mat-tab-label-0-1"]/div'
# emailPath ='//*[@id="mat-input-7"]'
# passpordPath ='//*[@id="mat-input-8"]'
# confirmPasspordPath = '//*[@id="mat-input-9"]'
# iAgreePath ='//*[@id="vdezi-login-register-1"]/label/div'
# registerPath = '//*[@id="mat-tab-content-1-1"]/div/app-register/div/form/button'
# 
# #email generation
# def random_char(y):
#        return ''.join(random.choice(string.ascii_lowercase) for x in range(y))
#        
# email=str(random_char(7)+"@"+random_char(5)+"."+random_char(3))
# print(email)
# 
# 
# # Script
# driver.get(url)
# 
# try :
#     driver.find_element_by_xpath(signUpPath).click()
#     driver.find_element_by_xpath(emailPath).send_keys(email)
#     driver.find_element_by_xpath(passpordPath).send_keys("password")
#     driver.find_element_by_xpath(confirmPasspordPath).send_keys("password")
#     driver.find_element_by_xpath(iAgreePath).click()
#     driver.find_element_by_xpath(registerPath).click()
# 
# except :
#     print("Error")
# 
# time.sleep(3)
# driver.close()
# time.sleep(1)
# print("Sign Up Automation Completed")

# working
# import pyautogui
# import time
# 
# time.sleep(5)
# i=18
# for k in range (19,98):
# 
# a= "ssmdk"
# print(type(a))
#     i=i+1
#     pyautogui.typewrite(str(k))
#     pyautogui.press('left')
#     pyautogui.press('left')
#     pyautogui.press('down')
s = "a3b2c1"

for i in s:
    # print (type(i))
    try:
        int(i)
        pass
    except ValueError:
        for j in s[i:]:
            
