import calendar
from datetime import datetime

# 当前年月
now = datetime.now()
current_month = now.month
current_year = now.year

# 当前月份的日历
cal = calendar.month(current_year, current_month)

# 打印
print(cal)