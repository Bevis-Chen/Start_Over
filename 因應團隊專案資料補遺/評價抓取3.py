import requests, time, math, threading
import sqlite3, os
import pandas as pd
from datetime import datetime
from bs4 import BeautifulSoup
from queue import Queue
from tools import get_chrome, find_element, get_soup
from fake_useragent import UserAgent
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

def get_chrome(url, chromeDriver= r'C:\webdriver\chromedriver.exe', hide=False):    
    try:        
        service=Service(chromeDriver)
        options=webdriver.ChromeOptions()  
        userAgent = UserAgent().random   # 為了搞定反爬蟲
        # print(userAgent )
        options.add_argument(f'user-agent= {userAgent}')
        if hide:
            options.add_argument('--headless')
        chrome= webdriver.Chrome(service= service, options=options)
        chrome.implicitly_wait(15)
        chrome.get(url)
        return chrome
    except Exception as e:
        print(e, "是出了什麼問題...?")    
    return "Nothing"

def find_element(chrome, xpath):
    try:
        return chrome.find_element(By.XPATH, xpath)
    except Exception as e:
        print(e, "xpath怪怪的@@")
    return "Nothing"

def get_comment_if_one(name):
    #順利版本
    #只有一個
    #評論 : 排序
    time.sleep(.5)
    xpath1 = '/html/body/div[1]/div[3]/div[8]/div[9]/div/div/div[1]/div[2]/div/div[1]/div/div/div[46]/div[2]/button/span'
    element = find_element(chrome, xpath1)
    element.click()
    #最新 排序
    time.sleep(.5)
    xpath2 = "/html/body/div[1]/div[3]/div[3]/div[1]/div[2]"
    element = find_element(chrome, xpath2)
    element.click()
    soup = BeautifulSoup(chrome.page_source, "html.parser")
    comments = soup.find_all(class_ = "jftiEf fontBodyMedium")
    w8nwRe = [one.find(class_ = "w8nwRe") for one in comments if "w8nwRe" in str(one)]
    for i in range(len(w8nwRe)):
        element = chrome.find_element(By.CLASS_NAME, 'w8nwRe')
        element.click()
        time.sleep(0.3)
    soup1 = BeautifulSoup(chrome.page_source, "html.parser")
    comments1 = soup1.find_all(class_ = "jftiEf fontBodyMedium")
    data = []
    for com in comments1:
        temp = []
        if "wiI7pd" in str(com):
            people = "姓名: " + com.find(class_ = "d4r55").text
            comment = "評論 : " + com.find(class_ = "wiI7pd").text
            temp.append([people, comment])
        data.append(temp)
    return data
        
def get_comment_if_more(name):  
    # global name
    # if "m6QErb DxyBCb kA9KIf dS8AEf ecceSd" in str(chrome.page_source):
    #     soup = BeautifulSoup(chrome.page_source, "html.parser")
    #     if name == soup.find(class_ = "qBF1Pd fontHeadlineSmall").text:   
    chrome.refresh()
    time.sleep(.5)
    xpath1 = "/html/body/div[1]/div[3]/div[8]/div[9]/div/div/div[1]/div[2]/div/div[1]/div/div/div[1]/div[1]/div[1]/div/a"
    element = find_element(chrome, xpath1)
    element.click()
    #評論 : 排序
    time.sleep(.5)
    xpath2 = "/html/body/div[1]/div[3]/div[8]/div[9]/div/div/div[1]/div[3]/div/div[1]/div/div/div[2]/div[49]/div[2]/button/span"
    element = find_element(chrome, xpath2)
    element.click()
    #最新 排序
    time.sleep(.5)
    xpath3 = "/html/body/div[1]/div[3]/div[3]/div[1]/div[2]"
    element = find_element(chrome, xpath3)
    element.click()
    soup1 = BeautifulSoup(chrome.page_source, "html.parser")
    comments = soup1.find_all(class_ = "jftiEf fontBodyMedium")
    w8nwRe = [one.find(class_ = "w8nwRe") for one in comments if "w8nwRe" in str(one)]
    for i in range(len(w8nwRe)):
        element = chrome.find_element(By.CLASS_NAME, 'w8nwRe')
        element.click()
    soup2 = BeautifulSoup(chrome.page_source, "html.parser")
    comments2 = soup2.find_all(class_ = "jftiEf fontBodyMedium")
    data = []
    for com in comments2:
        temp = []
        if "wiI7pd" in str(com):            
            people = "姓名: " + com.find(class_ = "d4r55").text
            comment = "評論 : " + com.find(class_ = "wiI7pd").text
            temp.append([people, comment])
        data.append(temp)
    return data

try:
    url = "https://www.google.com/maps/@25.149628,121.586901,11.25z?entry=ttu"
    datas = pd.read_csv("Taipei_to_hots_copy1.csv", encoding = "utf-8-sig")
    all_comments = []
    count = 0
    for name in datas["shopName"]:
        count += 1
        print(count, name)
        # if count % 5 == 0:
        # time.sleep(3)
        chrome = get_chrome(url, hide = True)
        #網頁最大化
        chrome.maximize_window()
        time.sleep(1)
        if "mL3xi" in str(chrome.page_source):           
            # 輸入框
            xpath1 = "/html/body/div[1]/div[3]/div[8]/div[3]/div[1]/div[1]/div/div[2]/form/input"
            element= find_element(chrome, xpath1)
            element.clear()
            element.click()
            time.sleep(.5)    
            element.send_keys(name + "\n")
            time.sleep(6)
            # chrome.refresh()
            if "aoRNLd kn2E5e NMjTrf lvtCsd" in str(chrome.page_source):
                soup = BeautifulSoup(chrome.page_source, "html.parser")
                comments = soup.find_all(class_ = "jftiEf fontBodyMedium")
                w8nwRe = [one.find(class_ = "w8nwRe") for one in comments if "w8nwRe" in str(one)]
                # time.sleep(1)
                for i in range(len(w8nwRe)):
                    element = chrome.find_element(By.CLASS_NAME, 'w8nwRe')
                    element.click()
                    time.sleep(0.3)
                # time.sleep(1)
                soup1 = BeautifulSoup(chrome.page_source, "html.parser")
                comments1 = soup1.find_all(class_ = "jftiEf fontBodyMedium")
                data = []
                for com in comments1:
                    temp = []
                    if "wiI7pd" in str(com):
                        people = "姓名: " + com.find(class_ = "d4r55").text
                        comment = "評論 : " + com.find(class_ = "wiI7pd").text
                        temp.extend([people, comment])
                    data.extend(temp)
                chrome.quit()
                all_comments.append([name, data])
            else:
                if "aoRNLd kn2E5e NMjTrf lvtCsd" not in str(chrome.page_source):
                    soup = BeautifulSoup(chrome.page_source, "html.parser") 
                    # if name == soup.find(class_ = "qBF1Pd fontHeadlineSmall").text: 
                    time.sleep(.5)
                    # xpath1 = "/html/body/div[1]/div[3]/div[8]/div[9]/div/div/div[1]/div[2]/div/div[1]/div/div/div[1]/div[1]/div[1]/div/a"         
                    # element = find_element(chrome, xpath1)
                    element = chrome.find_element(By.CSS_SELECTOR, "a.hfpxzc")
                    element.click()
                    time.sleep(1)
                    soup1 = BeautifulSoup(chrome.page_source, "html.parser")
                    comments = soup1.find_all(class_ = "jftiEf fontBodyMedium")
                    w8nwRe = [one.find(class_ = "w8nwRe") for one in comments if "w8nwRe" in str(one)]
                    # time.sleep(1)
                    for i in range(len(w8nwRe)):
                        element = chrome.find_element(By.CLASS_NAME, 'w8nwRe')
                        element.click()
                    # time.sleep(1)
                    soup2 = BeautifulSoup(chrome.page_source, "html.parser")
                    comments2 = soup2.find_all(class_ = "jftiEf fontBodyMedium")
                    data = []
                    for com in comments2:
                        temp = []
                        if "wiI7pd" in str(com):            
                            people = "姓名: " + com.find(class_ = "d4r55").text
                            comment = "評論 : " + com.find(class_ = "wiI7pd").text
                            temp.extend([people, comment])
                        data.extend(temp)
                    chrome.quit()
                    all_comments.append([name, data])
        else:
            if "mL3xi" not in str(chrome.page_source):
                chrome.quit()
    print("Finished!")
    df = pd.DataFrame(all_comments)
except Exception as e:
    print("8逼Q了~")
    print(name)
    print(e)


