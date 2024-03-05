import requests, time, math, threading
import sqlite3, os
import pandas as pd
from datetime import datetime
from bs4 import BeautifulSoup
from queue import Queue
from selenium_tools import get_chrome, find_element, get_soup
from fake_useragent import UserAgent
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

url = "https://www.google.com/maps/"
# datas = pd.read_csv("Taipei_to_hots_copy1.csv", encoding = "utf-8-sig")
# datas = pd.read_csv("NewTaipei_to_hots_copy1.csv", encoding = "utf-8-sig")
# print(datas)
files_path = r"D:\More Document\Python\宏碁班\課程講義\練習題\Start_Over\因應團隊專案資料補遺\Taipei_to_hots_copy1.csv"

datas = pd.read_csv(files_path, encoding = "utf-8-sig")

def for_comments(name):
    xpath1 = "/html/body/div[1]/div[3]/div[8]/div[3]/div[1]/div[1]/div/div[2]/form/input"
    element = find_element(chrome, xpath = xpath1)
    element.clear()
    element.click()
    element.send_keys(name + "\n")
    time.sleep(2)
    soup = BeautifulSoup(chrome.page_source, "html.parser")
    if "RZ66Rb" not in str(chrome.page_source):
        url_new = soup.find("a", class_ = "hfpxzc").get("href")            
        chrome.quit()
        chrome = get_chrome(url_new, hide = False)
        time.sleep(0.5)
        #網頁最大化
        chrome.maximize_window()
        chrome.refresh()    
    elif "RZ66Rb" in str(chrome.page_source):
        time.sleep(0.5)
    soup = BeautifulSoup(chrome.page_source, "html.parser") 
    com_list = [name]
    if "Gpq6kf fontTitleSmall" in str(chrome.page_source):
        try:
            try:
                xpath = "/html/body/div[1]/div[3]/div[8]/div[9]/div/div/div[1]/div[2]/div/div[1]/div/div/div[3]/div/div/button[2]"
                element = chrome.find_element(By.XPATH, xpath)
                element.click()                
            except Exception as e:
                xpath = "/html/body/div[1]/div[3]/div[8]/div[9]/div/div/div[1]/div[2]/div/div[1]/div/div/div[3]/div/div/button[3]"
                element = chrome.find_element(By.XPATH, xpath)
                element.click()            
        except Exception as e:
            try:
                xpath = "/html/body/div[2]/div[3]/div[8]/div[9]/div/div/div[1]/div[2]/div/div[1]/div/div/div[3]/div/div/button[2]"
                element = chrome.find_element(By.XPATH, xpath)
                element.click()                
            except Exception as e:
                xpath = "/html/body/div[2]/div[3]/div[8]/div[9]/div/div/div[1]/div[2]/div/div[1]/div/div/div[3]/div/div/button[3]"
                element = chrome.find_element(By.XPATH, xpath)
                element.click()      
        time.sleep(0.5)
        try:
            try: 
                comment_roller = "/html/body/div[1]/div[3]/div[8]/div[9]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]"                
                pane = chrome.find_element(By.XPATH, comment_roller)
                chrome.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", pane)
            except Exception as e:
                comment_roller = "/html/body/div[2]/div[3]/div[8]/div[9]/div/div/div[1]/div[2]/div/div[1]/div/div/div[4]"
                pane = chrome.find_element(By.XPATH, comment_roller)
                chrome.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", pane)                     
        except Exception as e:
            try: 
                comment_roller = "/html/body/div[2]/div[3]/div[8]/div[9]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]"                
                pane = chrome.find_element(By.XPATH, comment_roller)
                chrome.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", pane)
            except Exception as e:
                comment_roller = "/html/body/div[2]/div[3]/div[8]/div[9]/div/div/div[1]/div[2]/div/div[1]/div/div/div[4]"
                pane = chrome.find_element(By.XPATH, comment_roller)
                chrome.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", pane)   
        time.sleep(0.5)
        try:
            try: 
                comment_roller = "/html/body/div[1]/div[3]/div[8]/div[9]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]"                
                pane1 = chrome.find_element(By.XPATH, comment_roller)
                chrome.execute_script("arguments[0].scrollTop = 0", pane1)
            except Exception as e:
                comment_roller = "/html/body/div[2]/div[3]/div[8]/div[9]/div/div/div[1]/div[2]/div/div[1]/div/div/div[4]"
                pane1 = chrome.find_element(By.XPATH, comment_roller)
                chrome.execute_script("arguments[0].scrollTop = 0", pane1)                     
        except Exception as e:
            try: 
                comment_roller = "/html/body/div[2]/div[3]/div[8]/div[9]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]"                
                pane1 = chrome.find_element(By.XPATH, comment_roller)
                chrome.execute_script("arguments[0].scrollTop = 0", pane1)
            except Exception as e:
                comment_roller = "/html/body/div[2]/div[3]/div[8]/div[9]/div/div/div[1]/div[2]/div/div[1]/div/div/div[4]"
                pane1 = chrome.find_element(By.XPATH, comment_roller)
                chrome.execute_script("arguments[0].scrollTop = 0", pane1)  
        time.sleep(0.5)
        soup2 = BeautifulSoup(chrome.page_source, "html.parser")
        comments = soup2.find_all("div", class_ = "jftiEf fontBodyMedium")
        time.sleep(2)
        for i in comments:
            if "w8nwRe" in str(i): 
                element = chrome.find_element(By.CLASS_NAME, 'w8nwRe')
                element.click()
        time.sleep(0.5)
        try:
            try: 
                comment_roller = "/html/body/div[1]/div[3]/div[8]/div[9]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]"                
                pane1 = chrome.find_element(By.XPATH, comment_roller)
                chrome.execute_script("arguments[0].scrollTop = 0", pane1)
            except Exception as e:
                comment_roller = "/html/body/div[2]/div[3]/div[8]/div[9]/div/div/div[1]/div[2]/div/div[1]/div/div/div[4]"
                pane1 = chrome.find_element(By.XPATH, comment_roller)
                chrome.execute_script("arguments[0].scrollTop = 0", pane1)                     
        except Exception as e:
            try: 
                comment_roller = "/html/body/div[2]/div[3]/div[8]/div[9]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]"                
                pane1 = chrome.find_element(By.XPATH, comment_roller)
                chrome.execute_script("arguments[0].scrollTop = 0", pane1)
            except Exception as e:
                comment_roller = "/html/body/div[2]/div[3]/div[8]/div[9]/div/div/div[1]/div[2]/div/div[1]/div/div/div[4]"
                pane1 = chrome.find_element(By.XPATH, comment_roller)
                chrome.execute_script("arguments[0].scrollTop = 0", pane1)
        time.sleep(0.5)
        soup2 = BeautifulSoup(chrome.page_source, "html.parser")
        comments = soup2.find_all("div", class_ = "jftiEf fontBodyMedium")
        chrome.quit()
        print(name + "SuccessFul!")
        for com in comments:
            if "wiI7pd" in str(com):
                com_list.extend(["姓名: " + com.find(class_ = "d4r55").text, "評論: " + com.find("span", class_ = "wiI7pd").text])
            else:
                com_list.extend(["姓名: " + com.find(class_ = "d4r55").text, "評論: " + "很讚"])
    else:
        com_list = [name, "暫無評價"]      
    return com_list


try:
    all_comments = []
    for name in datas["shopName"]:
        while True:
            chrome = get_chrome(url, hide = True)
            if "yZqPAf" in str(chrome.page_source):
                chrome = get_chrome(url, hide = True)
            else:
                break
        chrome.refresh()
        #網頁最大化
        chrome.maximize_window()
        while True:
            try:
                com_list = for_comments(name)
                if com_list[2:] == []:
                    com_list = for_comments(name)
            except Exception as e:
                chrome.quit()
                com_list = for_comments(name)
                if com_list[2:] == []:
                    com_list = for_comments(name)
            else:
                break
        all_comments.append(com_list)
        time.sleep(2)
    print(pd.DataFrame(all_comments))          
except Exception as e:
    print(e)

now_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

df1 = pd.DataFrame(all_comments)
df1.to_csv(f"tapei_comments_{now_time}.csv", encoding = "UTF-8-sig")