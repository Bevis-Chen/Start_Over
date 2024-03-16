import requests, re, time
import pandas as pd
from datetime import datetime
from bs4 import BeautifulSoup
from alive_progress import alive_bar

url = "https://www.taiwanlottery.com.tw/3th_Lotto/SuperLotto638/history.aspx"
Headers = {"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"}

def get_SuperLotto_numbers(year, month):
    # global year, month
    r = requests.get('https://www.taiwanlottery.com.tw/3th_Lotto/superlotto638/history.aspx', headers = Headers)
    soup = BeautifulSoup(r.text, 'html.parser')
    __VIEWSTATE = soup.find('input',id='__VIEWSTATE').get('value')
    __VIEWSTATEGENERATOR = soup.find('input',id='__VIEWSTATEGENERATOR').get('value')
    __EVENTVALIDATION = soup.find('input',id='__EVENTVALIDATION').get('value')
    my_data = {
        "__EVENTTARGET": "", "__EVENTARGUMENT": "", "__LASTFOCUS": "",
        "__VIEWSTATE": __VIEWSTATE,
        "__VIEWSTATEGENERATOR": __VIEWSTATEGENERATOR,
        "__EVENTVALIDATION": __EVENTVALIDATION,
        "SuperLotto638Control_history1$DropDownList1": "1",
        "SuperLotto638Control_history1$chk": "radYM",
        "SuperLotto638Control_history1$dropYear": year,
        "SuperLotto638Control_history1$dropMonth": month,
        "SuperLotto638Control_history1$btnSubmit": "查詢",
    }

    resp = requests.post(url, headers = Headers, data = my_data)

    if resp.status_code == 200 :
        soup = BeautifulSoup(resp.text, "html.parser")
        tables= soup.find_all("td", style = "width: 1063px")
        all = []
        for table in tables:
            number_list = []
            order = table.find("span", id = re.compile("SuperLotto638Control_history1_dlQuery_DrawTerm_\d")).text
            number = table.find_all("span", id = re.compile("SuperLotto638Control_history1_dlQuery_SNo\d_\d"))
            print("期別號碼: ", order)
            number_list.append(order)
            print("獎號(含特別號): ", end = " ")
            for num in number:
                print(num.text, end = " ")
                number_list.append(num.text)
            all.append(number_list)                     
            print()
    return all

if __name__ == "__main__":
    all = []
    for i in range(103, 113):
        for k in range(1, 13):
            year = str(i)
            month = str(k)
            one_month = get_SuperLotto_numbers(year, month)
            all.extend(one_month)
            # time.sleep(0.01)
    df = pd.DataFrame(all, columns= ["期別號碼", "獎號(含特別號)"])
    # print(df.to_csv("威力彩所有號碼.csv", encoding = "UTF-8-sig"))