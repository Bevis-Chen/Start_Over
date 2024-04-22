from datetime import datetime

current_datetime = datetime.now()

print(current_datetime.day - 1)
print(str(current_datetime.month) + "/" + str(current_datetime.day))