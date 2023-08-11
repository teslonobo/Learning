# A Date in Python is not a datatype but we can import datetime module
import datetime

# Display current date
x = datetime.datetime.now()
print(x)
# The date contains year, month, day, 
# hour, minute, second, and microsecond.

# Return year
print(x.year)

# Return month and day
print(x.month,x.day)

# Create a date object
y = datetime.datetime(2020, 4, 20)
print(y)

# Use strftime() method 
a = y.strftime("%B") #Month name, Full
b = y.strftime("%A") #Weekday, Full
print(f"{a} {b} the {y.day}th")
