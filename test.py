from datetime import datetime, timedelta

current_datetime = datetime.now()
delta = timedelta(days = -5)
need_date = current_datetime + delta
Date = str(need_date.month) + "/" + str(need_date.day)

print(Date)