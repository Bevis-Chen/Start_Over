import requests, time, math, threading
import sqlite3, os
import pandas as pd
from queue import Queue
from datetime import datetime
from bs4 import BeautifulSoup
from selenium_tools import get_chrome, find_element
from fake_useragent import UserAgent
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By


url = "https://www.google.com/maps/"
datas = pd.read_csv(r"因應團隊專案資料補遺\Taipei_to_hots_copy1.csv", encoding = "utf-8-sig")
# print(datas)

try:
    while True:
        chrome = get_chrome(url, hide = False)
        if "yZqPAf" in str(chrome.page_source):
            chrome = get_chrome(url, hide = False)
        else:
            break
    chrome.refresh()
    #網頁最大化
    chrome.maximize_window()
    time.sleep(0.5)
    xpath1 = "/html/body/div[1]/div[3]/div[8]/div[3]/div[1]/div[1]/div/div[2]/form/input"
    element = find_element(chrome, xpath = xpath1)
    element.clear()
    element.click()
    element.send_keys(datas["shopName"][1] + "\n")    

    if "Nv2PK Q2HXcd THOPZb" in str(chrome.page_source):
            soup = BeautifulSoup(chrome.page_source, "html.parser")
            num = -1
            for number in soup.find_all("div", class_ = "Nv2PK Q2HXcd THOPZb"):
                number_text = eval(number.find("span", class_ = "UY7F9").text)
                if number_text > num:
                    num = number_text
                    url_new = number.find("a", class_ = "hfpxzc").get("href")
            chrome.quit()
            chrome = get_chrome(url_new, hide = False)
            time.sleep(0.5)
            #網頁最大化
            chrome.maximize_window()
            chrome.refresh()    
    elif "RZ66Rb" in str(chrome.page_source):
        time.sleep(0.5)   
    
    # 解決評論位置(暴力)
    soup = BeautifulSoup(chrome.page_source, "html.parser")
    comment_locate = len(soup.find_all("div", class_ = "Gpq6kf fontTitleSmall"))
    time.sleep(0.5)
    if comment_locate == 3:
        xpath = "/html/body/div[2]/div[3]/div[8]/div[9]/div/div/div[1]/div[2]/div/div[1]/div/div/div[3]/div/div/button[2]/div[2]/div[2]"
        element = chrome.find_element(By.XPATH, xpath)
        element.click()   
    elif comment_locate == 4:
        xpath = "/html/body/div[2]/div[3]/div[8]/div[9]/div/div/div[1]/div[2]/div/div[1]/div/div/div[3]/div/div/button[3]/div[2]/div[2]"
        element = chrome.find_element(By.XPATH, xpath)
        element.click()
    time.sleep(0.5)
    comment_roller = "/html/body/div[2]/div[3]/div[8]/div[9]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]"
    pane = chrome.find_element(By.XPATH, comment_roller)
    chrome.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", pane)
    time.sleep(0.5)
    # 不一定要有這個
    comment_roller = "/html/body/div[2]/div[3]/div[8]/div[9]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]"
    pane1 = chrome.find_element(By.XPATH, comment_roller)
    chrome.execute_script("arguments[0].scrollTop = 0", pane1)
    time.sleep(0.5)
    soup2 = BeautifulSoup(chrome.page_source, "html.parser")
    comments = soup2.find_all("div", class_ = "jftiEf fontBodyMedium")
    print(len(comments))
    # print(comments)
    time.sleep(2)
    # numbers_w8nwRe = [one.find(class_ = "w8nwRe") for one in comments if "w8nwRe" in str(one)]
    for i in comments:
        if "w8nwRe" in str(i): 
            element = chrome.find_element(By.CLASS_NAME, 'w8nwRe')
            element.click()
    time.sleep(0.5)
    comment_roller = "/html/body/div[2]/div[3]/div[8]/div[9]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]"
    pane1 = chrome.find_element(By.XPATH, comment_roller)
    chrome.execute_script("arguments[0].scrollTop = 0", pane1)
    time.sleep(0.5)
    soup2 = BeautifulSoup(chrome.page_source, "html.parser")
    comments = soup2.find_all("div", class_ = "jftiEf fontBodyMedium")
    print(len(comments))
    print(comments)










except Exception as e:
    print(e)




