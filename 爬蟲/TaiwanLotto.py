import requests, re
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.taiwanlottery.com.tw/3th_Lotto/SuperLotto638/history.aspx"
Headers = {"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"}


def get_SuperLotto_numbers(year, month):
    # global year, month
    my_data = {
        "__EVENTTARGET": "", "__EVENTARGUMENT": "", "__LASTFOCUS": "",
        "__VIEWSTATE": "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",
        "__VIEWSTATEGENERATOR": "EE963908",
        "__EVENTVALIDATION": "E8uIlYokm7bLP9oN/osdHl21a9YZV/6c9zx3yFDxNggPx9re3JMdgBQiqiTeUE8LgePJlEs6iboFVPg/eQYOE9cq+04FbXZzg1uBXzI5UQsKMIGj+ZQUPsW6k/0NHaQCzx23kMpsaxZ23fyLYoZgoLeIrpeZ56JjS0BE5gZEvUxK7w2rGKF9gk/+IpWOiYJlv5feIWf5drwBrb+eFPW4MkKVGMtq4ZLd6pveQQr5SdiVYv6XDU+/ioVLQj4qKQKV6QhLzhkbp6x0AhkQfLKTBRaXJOvCQP1P3ZQYI9BWaNgpvjeyCDTsY8lTukYAWraZGbSkFOYoUVrvjfcV2IcjzGZg+HZvchPL/YcbBuFc3eOkeJQNJ9LcVw5om9FA96IOW8DIDIbm4VWEbaZI0oKzPoxZIglglhAbVA1NcJh7OpgFFWEqZmLd3WHc8XlsZsPUqnUmg7o3yLNaFN/+O2+3CPMr/XDsSCePtN+8n+7MVmIIgskLuBmKM1QPQ1pdsysnUUY+hrCF5qOFWiPSLFI3n7RcTNf1x0vhxyO/vCRQUmFg7Z03cFBtXzvTllZRhczMqSfZdRtSOBFAQVPqOwWnJcfQNNHIcNtj1HkIlPZR/YhWwvT1WV2uefnHKrrJLhOlb5lIgKX1HrWZDLv7mg9n64jYwiE7ySsHcpmDErfFmc3ZEglbkyRxhE04pHrG4YjamOUFcxWuAYjGgFez24FDFOkSbZpzmo5MIW29Ygt3ptd0fCpU/FoHGi6+YNezNbEfSUWDcncO8+Zk69B2UEcS9zoS/2QpBeMOb/n+tvZsEEx173Z5A3tOF8LPj8qUNvt4Dbw4ADpL7S4mHM21rlEbFpC93fGPTtR6WWhXRexjNb3fApDE",  
        "SuperLotto638Control_history1$DropDownList1": "1",
        "SuperLotto638Control_history1$chk": "radYM",
        "SuperLotto638Control_history1$dropYear": year,
        "SuperLotto638Control_history1$dropMonth": month,
        "SuperLotto638Control_history1$btnSubmit": "查詢",
    }

    resp = requests.post(url, headers = Headers, data = my_data)

    if resp.status_code == 200 :
        soup = BeautifulSoup(resp.text, "html.parser")
        count = 0
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
    # print(all)
    return all

if __name__ == "__main__":
    

    # all = []
    # for i in range((113-97)):
    #     if i == (113 - 97):
    #         for k in range(2):
    #             year = str(i + 97)
    #             month = str(k + 1)
    #             one_month = get_SuperLotto_numbers(year, month)
    #             all.extend(one_month)
    #     else:
    #         for k in range(12):
    #             year = str(i + 97)
    #             month = str(k + 1)
    #             one_month = get_SuperLotto_numbers(year, month)
    #             all.extend(one_month)
    # df = pd.DataFrame(all, columns= ["期別號碼", "獎號(含特別號)"])
    # print(df.to_csv("威力彩所有號碼.csv", encoding = "UTF-8-sig"))