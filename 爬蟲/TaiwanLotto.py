import requests
from bs4 import BeautifulSoup

url = "https://www.taiwanlottery.com.tw/3th_Lotto/SuperLotto638/history.aspx"
Headers = {"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"}
my_data = {
    "__EVENTTARGET": "", "__EVENTARGUMENT": "", "__LASTFOCUS": "",
    "__VIEWSTATE":"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",
    "__VIEWSTATEGENERATOR": "EE963908",
    "__EVENTVALIDATION": "aHflKZihoz7y8sPmDlgXQalECYHG1vSzqdr3dxS27HtXEuypESqrIO/fBqnHTyMkvwTejqJFwYLvSl7ngK1dXbODCUdf27+2SQDd65qrmou2L6Hj0WHflcXZNtsUnkwLDhea8Cm8m5QQnE7vposj//QpEF3OHiwH+moJk4zUyYoh5lE6r2TZ+Y5A5at/2Ay5x4EuPxjiV5rDfG+QVMFxKivAjYHm1AuvefLFVq5azgH5lmaaHsTwL+TacDHHnh+bSUQ06NiVWNQXylclDpbQiqkOIdOyQngA1BPbcb0V6xT3oJJH/+eeBDRlsIa/rmdG8hFR/wo/23JVMjD6a8gO7+EQqW9N6jtHqi0kJyVku5l48ugCj/P1yT2ZomwfErvd8e11ShZSefLYzLkXF9t+r21sWXCDl1b72f9nCP8XISidHjoycLuEvFM1pnj6PsoEL0B5k1vCt6MkUDDuKrE35zhx7HSQRvcT2AQI0JBTo6YBj/5zhjCg107I7MtO+51cMVQSo/VUWMAfWC4ATLn+b30ycDp1GlbkYH9c8rvysgQ6Lq5bi45UGz/P80Ivke0dseGdix4aXTgnAt5yggcA/tEalhj2tgTXA+SLrcfKh8gJ+D/ZNLghB5vGVebOLxEMSItQFPo9Nh/OxVjdZB0E8W8tJGWGYgoEl3DMdt160FnWBMzidh9G+Ch6+JJWTgXhZr8pTNdpwAPhRNg1ZtVVnyKfs5I4M7KHSubZQuKyIiX9tkztV64zHmTUqOULq4NRCPjSfRhp4EgsupUAJ31+IX0VMdt5kruOSbz2sg8qTWcLiYbryQjBku/3XacPQX0C0rzZSlrJdeYGjWWnGIXIQo2Yx97eVHLvwt05vnh/SbMd9x7i",
    "SuperLotto638Control_history1$DropDownList1": "0",
    "SuperLotto638Control_history1$chk": "radYM",
    "SuperLotto638Control_history1$dropYear": "102",
    "SuperLotto638Control_history1$dropMonth": "6",
    "SuperLotto638Control_history1$btnSubmit": "查詢",
}

resp = requests.post(url, headers = Headers, data = my_data)

if resp.status_code == 200 :
    # soup = BeautifulSoup(resp.text, "html.parser")
    # __VIEWSTATE = soup.find()
    text = resp.text
    print(text)




