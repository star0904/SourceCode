from datetime import datetime


def get_first_days_of_month(start_year):
    dates = []
    current_date = datetime(start_year, 1, 1)
    end_date = datetime.now()

    while current_date <= end_date:
        # 将当前日期转换为日期格式
        date_str = current_date.strftime("%Y-%m-01")
        dates.append(date_str)

        # 移动到下一个月的第一天
        if current_date.month == 12:
            current_date = datetime(current_date.year + 1, 1, 1)
        else:
            current_date = datetime(current_date.year, current_date.month + 1, 1)

    return dates


# 示例：获取2008年到现在每年每月一号的日期格式
dates = get_first_days_of_month(2008)

# 打印日期格式
for date in dates:
    print(date)
