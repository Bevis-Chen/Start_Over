import re

# 09{1}\d{8}   >>  手機電話
# \D\w+@{1}\w+\.com$    >>  email 驗證 (開頭不能是0~9數字))
# [A-Z]{1}[1-2]{1}\d{8}    >> 身分證

# 身分證
num = input()
result = re.findall(r"[A-Z]{1}[1-2]{1}\d{8}", num)
if result != []:
    print("身分證: ", result[0])
else:
    print("號碼有誤!")


# 手機電話
phone = input()
result = re.findall(r"09{1}\d{8}", phone)
if result != []:
    print("手機電話: ", result[0])
else:
    print("號碼有誤!")

# email 驗證 (開頭不能是0~9數字))
email = input()
result = re.findall(r"\D\w+@{1}\w+\.com$", email)
if result != []:
    print("Email: ", result[0])
else:
    print("號碼有誤!")