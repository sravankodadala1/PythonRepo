import calendar

def get_day_of_week(m, d, y):

    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    day_index = calendar.weekday(y, m, d)
    return days[day_index]
