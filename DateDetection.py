"""Greetings, all. This is a practice project from the book "Automate The Boring Stuff With Python" by Al Swaigert.
I'll admit the practice projects in this book have been an immense challenge for me; I've had to seek
additional resources to supplement my learning from this book, but thus far I've pushed on and taken my best attempt
at this practice project in this book.
"""

import re
# Decided to make checking for leap year a separate function; trying to bunch this in
# with the other code seemed cluttery. This function checks for a leap year to make sure
# whether or not a date of February 29th is valid.
def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return True
    return False
# Our main function.
def date_detector(text):
    print(f"Checking: {(text)}")  # This will show the exact string being checked

    date_pattern = re.compile(r'(\d{2})/(\d{2})/(\d{4})')  # Easiest pattern I can come up with for MM/DD/YYYY format
    # Please note, this program ONLY detects dates in the above specified MM/DD/YYYY format.
    # Other methods of the date will crash the program, the assignment does not call for setting up
    # the program to accept other date formats should they rise, so I didn't do that.

    date = date_pattern.search(text) # We search for our pattern.

    month = int(date.group(1))  # Here, we store the groups of our pattern into variables. 
    day = int(date.group(2))
    year = int(date.group(3))

    # Next, we will check for validity of the date in the provided string!

    # First we check for valid months, there are 12 months in a year (for those of you whon didn't know LOL)
    if month < 1 or month > 12:
        print("Invalid month!")
        return
    # In the next two blocks of code, we will do validation for days in months with 30 and 31 days.
    if month in (1, 3, 7, 8, 10, 12) and day > 31:
        print(f'Invalid date! {month} only has 31 days!')
        return
    
    elif month in (4, 5, 6, 9, 11) and day > 30:
        print(f'Invalid date! {month} selected has only 30 days!')
        return

    if month == 2:  # Doing our checks for February and for leap years
        if day == 29:
            if not is_leap_year(year):
                print("Invalid! Not a leap year.")
        elif day > 29:
            print("Invalid! Day is above 29 for February.")
            return
    print(f'{dates} Appears to be valid!')
# Down here, we just supply a date to the program and have the program tell us whether or not its valid 
# and then call the function.
dates = "02/21/2012"
date_detector(dates)
