from datetime import datetime

def get_days_from_today(date):
  try:
    current_date = datetime.now()
    date_obj = datetime.strptime(date, "%Y-%m-%d")
    diff = current_date - date_obj
    return diff.days
  except ValueError:
    print("Wrong date format")
  

result = get_days_from_today("10.09.2023")
print(result)