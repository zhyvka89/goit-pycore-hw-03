from datetime import datetime

def get_days_from_today(date):
  current_date = datetime.now()
  date_obj = datetime.strptime(date, "%Y-%m-%d")
  diff = current_date - date_obj
  return diff.days

result = get_days_from_today("2024-10-09")
print(result)