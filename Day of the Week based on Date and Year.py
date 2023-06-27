import datetime

# get user input for date
user_date = input("Enter a date (MM/DD): ")

# get current year
current_year = datetime.datetime.now().year

# combine user input with current year to create datetime object
user_date = datetime.datetime.strptime(f"{user_date}/{current_year}", "%m/%d/%Y")

# get day of the week
day_of_week = user_date.strftime("%A")

# display result
print(f"The day of the week for {user_date.strftime('%m/%d/%Y')} is {day_of_week}.")
