import datetime

date_input = input("Enter a date in the format MM/DD: ")

current_year = datetime.datetime.now().year

date_string = f"{date_input}/{current_year}"
date_object = datetime.datetime.strptime(date_string, "%m/%d/%Y")

day_of_week = date_object.strftime("%A")

print(f"The day of the week for {date_input}/{current_year} is {day_of_week}.")
