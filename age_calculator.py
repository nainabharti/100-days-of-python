from datetime import date
import calendar
try:
    date_of_birth = date.strptime(input("Enter date of birth (YYYY-MM-DD): "),"%Y-%m-%d")
    today = date.today()
    if date_of_birth > today:
        print("Invalid date of birth! Please enter a valid date.")
    else:
        years = today.year - date_of_birth.year
        months = today.month - date_of_birth.month
        days = today.day - date_of_birth.day
        if days < 0:
            previous_month = today.month - 1
            previous_year = today.year
            if previous_month == 0:
                previous_month = 12
                previous_year -= 1

            days_in_previous_month = calendar.monthrange(previous_year, previous_month)[1]
            days += days_in_previous_month
            months -= 1
        if months < 0:
            months += 12
            years -= 1
        print(f"Your age is {years} years, {months} months and {days} days.")
except ValueError:
    print("Invalid date format! Please enter the date as YYYY-MM-DD.")