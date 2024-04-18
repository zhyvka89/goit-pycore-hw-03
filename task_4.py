from datetime import datetime, timedelta


def get_upcoming_birthdays(users):
    current_date = datetime.today().date()
    list_of_upcoming_bdays = []
    for user in users:
        bday_obj = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        bday_day = bday_obj.day
        bday_month = bday_obj.month
        bday_this_year = datetime(
            year=current_date.year, month=bday_month, day=bday_day).date()
        if (bday_this_year < current_date):
            bday_next_year = datetime(
                year=current_date.year+1, month=bday_month, day=bday_day).date().strftime("%Y.%m.%d")
            user_obj = {
                "name": user["name"],
                "congratulation_date": bday_next_year
            }
            list_of_upcoming_bdays.append(user_obj)
            print(user_obj)
        else:
            # next_week = current_date + timedelta(days=7)
            diff = bday_this_year - current_date
            time_delta = timedelta(7)
            if (diff <= time_delta):
                print("We will celebrate this week!!!")
            # print(diff)
        print(list_of_upcoming_bdays)
        # time_delta = timedelta(7)
        # print(time_delta)


users = [
    {"name": "John Doe", "birthday": "1985.04.20"},
    {"name": "Jane Smith", "birthday": "1990.01.27"}
]


get_upcoming_birthdays(users)


# now = datetime.now()
# future_date = now + timedelta(days=10)  # Додаємо 10 днів до поточної дати
# print(future_date)
