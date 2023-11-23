from util import get_day_of_week
 

month, day, year = map(int, input().split())
day_of_week = get_day_of_week(month, day, year)
print(day_of_week)
 


