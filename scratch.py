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
# access_key = ""
# secret = ""
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
#     consumer_key="",
#     consumer_secret="",
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
# s = "a3b2c1"

# for i in s:
#     # print (type(i))
#     try:
#         int(i)
#         pass
#     except ValueError:
#         for j in s[i:]:



# a= int(input())

# if a%2 ==0 and a>3:
#     print ("YES")
# else :
#     print ("NO")
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
# s = "a3b2c1"
# 
# for i in s:
#     # print (type(i))
#     try:
#         int(i)
#         pass
#     except ValueError:
#         for j in s[i:]:
#     
#    input a1b10c12 op abbbbbbbbbbcccccccccccc
# val = input()
# out_string = ""
# 
# while val:
#     ind = 0
#     for i in range(1,len(val)):
#         if ord(val[i])>=97 and ord(val[i])<=122:
#             ind = i
#             break
#     else:
#         num = int(val[1:])
#         alpha = val[0]
#         out_string +=alpha*num
#         break
#     num = int(val[1:ind])
#     alpha = val[0]
#     out_string += alpha*num
#     val = val[i:]
# print(out_string)
# 
# val = input()
# out_string = ""
# 
# while val:
#     ind = 0
#     for i in range(len(val)):
#         if ord(val[i])>=97 and ord(val[i])<=122:
#             ind = i
#             break
#     num = int(val[:ind])
#     alpha = val[i]
#     out_string += alpha*num
#     val = val[i+1:]
# print(out_string)


# ip: {2,3,2,4,5,12,2,.......}
# op: {freq (1), ascending (2)}
# 
# list_of_integers = list(map(int,input().split(' ')))
# 
# result = sorted(list_of_integers, key = list_of_integers.count, reverse = True)
# 
# print(result)

# 
# first = list(map(int,input().split(' ')))
# 
# # sort
# for i in first :
#     print(str(i))
#     
# 
# 
# # map 
# 
# mapped_value 
# # arrange op




# Input : 1 1 2 5 6 7 8 9 9 4 2 1
# Output :  1 1 1 9 9 2 2 5 6 7 8


# Primary aim : to sort by frequency
# Secondary aim : to sort ascending

#Input
# given = list(map(int,input().split(' ')))
# 
# 
# dict ={}
# 
# #duplicate removal
# given_set = set(given)
# 
# 
# 
# 
# for i in given_set:
#     dict[i] =given.count(i)#key --- number , val--- count
# 
# print(dict) #{2:time, 3 :time}
# temp  = []
# 
# for element in dict:
#     while int(dict[element])> 5:
#         print(element)
#         break
# 
# 
# dict = sorted(dict.items()) #ascend
# dict = sorted(dict,key = lambda items: items[1],reverse=True) #sort by counts
# 
# 
# lst=[]
# for k,v in dict:  #iterating the dict
#     for i in range(v): #to append in lst
#         lst.append(k)
# 
# print (lst)
# 
# 
# import itertools
# a = list(map(int,input().split()))
# lst = []
# for i in range(len(a)-1):
#     if a[i]>a[i+1]:
#         lst.append("D")
#     elif a[i]<a[i+1]:
#         lst.append("I")
#     else:
#         continue
# dict = {"I": "Increasing", "D": "Decreasing"}
# grouped = list(itertools.groupby(lst))
# if len(grouped) == 1:
#     print(dict[grouped[0][0]])  #IIIII    I I I  I D DI
# elif len(grouped) == 2:
#     print(f"Strictly {dict[grouped[0][0]]}")
# else:
#     print("Not applicable")


# a = list(map(int,input().split()))
# inc = 0
# dec = 0
# last = 0
# initial = a[0]
# flag = True
# for i in range(1,len(a)):
#     if last=="i" or last==0:
#         if a[i]>initial:
#             if inc == 0 and dec == 0:
#                 inc+=1
#                 last = "i"
#             elif inc == 1 and dec == 0:
#                 last = "i"
#                 initial = a[i]
#                 continue
#             elif inc == 0 and dec == 1:
#                 last = "i"
#                 inc+=1
#             else:
#                 break
#         elif a[i]<initial:
#             if inc == 0 and dec == 0:
#                 dec+=1
#                 last = "d"
#             elif inc == 1 and dec == 0:
#                 dec+=1
#                 last = "d"
#             elif inc == 0 and dec == 1:
#                 last = "d"
#                 initial = a[i]
#                 continue
#             else:
#                 break
#         else:
#             continue
#     elif last == "d" or last == 0:
#         if a[i]>initial:
#             if inc == 0 and dec == 0:
#                 inc+=1
#                 last = "i"
#             elif inc == 1 and dec == 0:
#                 last = "i"
#                 initial = a[i]
#                 continue
#             elif inc == 0 and dec == 1:
#                 last = "i"
#                 inc+=1
#             else:
#                 break
#         elif a[i]<initial:
#             if inc == 0 and dec == 0:
#                 dec+=1
#                 last = "d"
#             elif inc == 1 and dec == 0:
#                 dec+=1
#                 last = "d"
#             elif inc == 0 and dec == 1:
#                 last = "d"
#                 initial = a[i]
#                 continue
#             else:
#                 break
#         else:
#             initial = a[i]
#             continue
#     initial = a[i]
# 
# else:
#     flag = False
#     if last == "d" and inc == 0:
#         print("Decreasing")
#     elif last == "d" and inc == 1:
#         print("Stricting Increasing")
#     elif last == "i" and dec == 0:
#         print("Increasing")
#     elif last == "i" and dec == 1:
#         print("Stricting Decreasing")
# 
# if flag == True:
#     print("Undefined")
# 
# 
# class Student:
#     def __init__(self, name, age,address):
#         self.name = name
#         self.age = age
#         self.address = address
# 
# lst=[]
# 
# for i in range(3):
#     name , age , address = list(input().split())
#     Student.name = name
#     Student.age = age
#     Student.address = address
# 
#     dic = {
#         "name" :
#     }
#     
# 
# num=int(input()) 
# 
# for i in lst:
#     print ()
# 
# print(list(i for i in lst))
# 
# class Student:
#     def __init__(self, name,age, address):
#         self.name = name
#         self.age = age
#         self.address = address
# 
# class Address:
#     def __init__(self,state,city):
#         self.state = state
#         self.city = city
# lst =[]
# 
# for i in range(3):
#     
#     a,b,c,d = list(input().split(" "))
#     address = Address(c,d)
#     s=Student(a,b,address)
#     lst.append(s)
# 
# for i in lst:
#     print(i.name)
#     print(i.age)
#     print(i.address.city)
#     print(i.address.state)
# 
#     print("********************************")
# 
# 
# class Human :
#     def __init__(self, name,age,sex):
#         self.name = name
#         self.age = age
#         self.sex = sex
# 
# 
# class Student(Human):
#     def __init__(self,college,major,name,age,sex):
#         super(name,age,sex)
#         self.college =college
#         self.major = major
# 
# class Professional(Human):
#     def __init__(self,organization,experience):
#         self.organization = organization
#         self.experience = experience
# 
# Abishaik = Professional("Eunimart","1year")
# 


# print(Abishaik)

# a= "1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31"
# lst = list(a.split(" "))
# print(lst)
# positive=[]
# negative=[]
# for i in lst:
#     if int(i) >= 0 :
#         positive.append(i)
#     else:
#         negative.append(i)
# output=[]
# print(positive)
# print(negative)
# if len(positive)>len(negative):
#     ran = negative
#     big=positive
#     
# else:
#     ran = positive
#     big = negative
# 
# for i in range(len(ran)):
#     output.append(negative[i])
#     output.append(positive[i])
# 
# for i in range (len(ran),len(big)):
#     output.append(big[i])
#     
# 
# print(output)


#!/bin/python3
# 
# import math
# import os
# import random
# import re
# import sys
# 
# 
# 
# if __name__ == '__main__':
#     n = int(input().strip())
# 
# if n%2 !=0 and n!=0:
#     print("Weird")
# 
# else:
#     if n == 2 or n==5 or n>20:
#         print("Not Weird")
#     else:
#         print("Weird")
#         

# a= "abishaik"
# b= "aibshaik"
# sa=sorted(a)
# sb=sorted(b)
# count=0
# if len(a) != len(b):
#     print("Not a Anagram")
# 
# else:
#     for i in range(0,len(a)):
#         if sa[i] ==sb[i]:
#             count+=1
#         else:
#             break
# 
#     if count == len(a):
#         print("Anagram")  
#     
#     else:
#         print("Not")
# 
#Push
# a="abisjakjs"
# 
# lis=["a","e","i","o","u"]
# 
# va =[]
# 
# for i in a :
#     if i in lis:
#         va.append(ord(i))
# 
# for i in range len(va-1):
#     t = a[]
# a=9
# b=6
# c=2
# d=1
# 
# if c<=a :
#     if c<=b :
#         if a%c ==0:
#             if b%c ==0:
#                 d=c
#                 c=c+1
#             else:
#                 c=c+1
#         else :
#             c= c+1 
#             
#     else :
#         print (d)    
# 
# else :
#     print (d)
# print(6%1)
# a=10
# b=1
# 
# def sol(a,b):
#     if a<=5:
#         print(b)
#     else :
#         b=b+a
#         a=a-1
#         sol(a,b)
# sol(a,b)

# question 1 


#IP: 
# 6
# 2,3,7,9,4,1

# a = int(input("Enter Array Size :"))
# var = []
# for inps in range (0,a):
#     element = int(input("Enter Array element : "))
#     var.append(element)    
# 
# num1, num2 = 0,0 
# 
# for i in range(len(var)-1):
#     for j in range (i+1,len(var)):
#         total = var[i]+var[j]
#         if total>num1:
#             num2 = num1
#             num1 = total
# 
#         elif total>num2:
#             num2 = total
# print(num2)

# # working


# 
# 
# l=list(input().split())
# print((sorted(l,ket=str)))
# print(9//2)
# question 1 


#IP: 
# 6
# 2,3,7,9,4,1

# a = int(input("Enter Array Size :"))
# var = []
# for inps in range (0,a):
#     element = int(input("Enter Array element : "))
#     var.append(element)    
# 
# num1, num2 = 0,0 
# 
# for i in range(len(var)-1):
#     for j in range (i+1,len(var)):
#         total = var[i]+var[j]
#         if total>num1:
#             num2 = num1
#             num1 = total
# 
#         elif total>num2:
#             num2 = total
# print(num2)

# # working


# 
# 
# l=list(input().split())
# print((sorted(l,ket=str)))
# 
# i= 1
# j=0
# val=0
# n=int(input())
# def sol(i,j,n):
#     if i<=n:
#         if i%2==1 :
#             
#             j=j+i
#             i=i+1
#             sol(i,j,n) 
#         else :
#             i=i+1 
#             sol(i,j,n)
#     else :
#         print(j)
# 
# sol(i,j,n)
# a=7358
# b=21 
# def sol(a,b):
#     if b == 0:
#         print (a)
#     else :
#         c= a%100
#         c= c*100 
#         d= a/100 
#         a= c+d 
#         b= b-1
#         sol(a,b)
# 
# sol(a,b)
# 
# email=input("Name")
# passwords=input("Passwords")
# case = int(input("Case"))
# def Test(email,passwords):
#     #code
#     if (case==1): 
#         OnlyName(email,passwords)
# 
#     elif (case==2):
#         wrongPassword(email,passwords)
# 
#     elif (case==3):
#         Time(email,passwords)
#     
#     elif (case==4):
#         OnlyName(email,passwords)
#         wrongPassword(email,passwords)
#         Time(email,passwords)
# 
# def OnlyName(email,passwords):
#     print("Opening Browser")
#     print("URL--------- Email")
#     print("Report")
# 
# 
# def wrongPassword(email,password):
#     print("Opening Browser")
#     print("URL--------- Email, Wrong password")
#     print("Report")
# 
# 
# def Time(email,password):
#     print("Opening Browser")
#     print("URL--------- Email, correct passwords--------Time")
#     print("Report")
# 
# 

# Prurusothaman ########################################################3
# Test(email,passwords)
# print("Hai"+input() )

# print((int(input())+" is positive" if a>0  else "is zero"  )

# 
# def fun():
#     a= int(input())
#     if a==10:
#         print("Correct !")
#     else: 
#         return fun()
# fun()
#Swathika ############################################
# keys_lists = ['pogmcnf dafc', 'pavmchf dafc']
# words = [
#          ('pogmcnf dafc is the most valuable no in the banking domain', 'pogmcnf dafc'),
#          ('the most valuable number in the insurance domain is the pogmcnf dafc', 'pogmcnf dafc'),
#          ('every insurance individual has an account number', 'account number'),
#          ('I have my own account number which is important to find the insurance', 'account number'),
#          ]
# a = ["abi","john","akash"]
# b =  [("sjadkajasshaik","shaik"),("ssbshaikasd","shaik"),("snjsjsamuelnd","samuel"),("sjhsamuel","samuel"),("sajkjslove","love"),("ksakaxmnaruto","naruto")]
# newlst = []
# for i in range(0,len(b),2):
#     tup1,tup2 = b[i][0],b[i][1]
#     tup3,tup4 = b[i+1][0],b[i+1][1]
#     tup1 = tup1.replace(tup2,a[i//2])
#     tup2 = tup2.replace(tup2,a[i//2])
#     tup3 = tup3.replace(tup4,a[i//2])
#     tup4 = tup4.replace(tup4,a[i//2])
#     newlst.append((tup1,tup2))
#     newlst.append((tup3,tup4))
# print(newlst)

