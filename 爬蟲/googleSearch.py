import pandas as pd
import requests
from bs4 import BeautifulSoup

url = r"https://www.google.com/search?q=android&sca_esv=100a8d72724cfbcd&ei=mvT-Zf6jC77d1e8P68Gq2A4&ved=0ahUKEwj-2Nb-2IqFAxW-bvUHHeugCusQ4dUDCBA&oq=andorid&gs_lp=Egxnd3Mtd2l6LXNlcnAiB2FuZG9yaWQyBBAAGEcyBBAAGEcyBBAAGEcyBBAAGEcyBBAAGEcyBBAAGEcyBBAAGEcyBBAAGEcyBBAAGEcyBBAAGEdIwglQAFgAcAB4ApABAJgBAKABAKoBALgBDMgBAJgCAaACBZgDAOIDBRIBMSBAiAYBkAYKkgcBMaAHAA&sclient=gws-wiz-serp"

resp = requests.get(url)

if resp.status_code == 200:
    # print(resp.text)
    soup = BeautifulSoup(resp.text, "html.parser")
    print(soup.find(class_ = "LC20lb"))

