

import datetime

def days_in_month(year, month):
    """
    Inputs:
      year  - an integer between datetime.MINYEAR and datetime.MAXYEAR
              representing the year
      month - an integer between 1 and 12 representing the month

    Returns:
      The number of days in the input month.
    """
    if type(year) is not int:
        raise Exception("Sorry the year should be an integer")
    if month == 12:
        days_per_month = 31
    else:
        days_per_month = (datetime.date(year, month + 1, 1) - datetime.date(year, month, 1)).days
    return days_per_month

def is_valid_date(year, month, day):
    """
    Inputs:
      year  - an integer representing the year
      month - an integer representing the month
      day   - an integer representing the day

    Returns:
      True if year-month-day is a valid date and
      False otherwise
    """
    if type(year) is not int:

        raise Exception("Sorry the year should be an integer")

    try:
        datetime.date(year, month, day)
        return True
    except ValueError:
        print("The dates values are presented in inappropriate form")
        return False

def days_between(year1, month1, day1, year2, month2, day2):
    """
    Inputs:
      year1  - an integer representing the year of the first date
      month1 - an integer representing the month of the first date
      day1   - an integer representing the day of the first date
      year2  - an integer representing the year of the second date
      month2 - an integer representing the month of the second date
      day2   - an integer representing the day of the second date

    Returns:
      The number of days from the first date to the second date.
      Returns 0 if either date is invalid or the second date is
      before the first date.
    """
    if type(year) is not int:
        print("")
        raise Exception("Sorry the year should be an integer")

    if not is_valid_date(year1, month1, day1) or not is_valid_date(year2, month2, day2):
        return 0
    date1 = datetime.date(year1, month1, day1)
    date2 = datetime.date(year2, month2, day2)
    if date1 > date2:
        return 0
    else:
        return (date2 - date1).days

def age_in_days(year, month, day):
    """
    Inputs:
      year  - an integer representing the birthday year
      month - an integer representing the birthday month
      day   - an integer representing the birthday day

    Returns:
      The age of a person with the input birthday as of today.
      Returns 0 if the input date is invalid or if the input
      date is in the future.
    """
    if type(year) is not int:
        raise Exception("Sorry the year should be an integer")
    if not is_valid_date(year, month, day):
        return 0
    today = datetime.date.today()
    birthday = datetime.date(year, month, day)
    if birthday > today:
        return 0
    else:
        return (today - birthday).days

#Unit Test:
year="1975"
month=2
day=3

year2=2023
month2=12
day2=31

print(is_valid_date(year,month,day))
print(days_in_month(year,month))
print(days_between(year,month,day,year2,month2,day2))
print("")
print(age_in_days(year,month,day))