import re
import pandas as pd

# 09{1}\d{8}   >>  手機電話
# \D\w+@{1}\w+\.com$    >>  email 驗證 (開頭不能是0~9數字))
# [A-Z]{1}[1-2]{1}\d{8}    >> 身分證

s = ["yulin@gmail.com", "dspring1995@gmail.com"]

for i in s:
    result = re.findall("\D\w+@\w+.com$", i)
    print(result)