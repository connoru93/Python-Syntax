# Function to check if a year is a leap year
def is_leap_year(year):
    # Check if the year is divisible by 4
    if year % 4 == 0:
        # Check if the year is a centurial year
        if year % 100 == 0:
            # If it is a centurial year, check if it is divisible by 400
            if year % 400 == 0:
                return True  # It is a leap year
            else:
                return False  # It is not a leap year
        else:
            return True  # It is a leap year
    else:
        return False  # It is not a leap year

# Prompt the user to input a year
year_input = int(input("Enter a year: "))

# Check if the year is a leap year
if is_leap_year(year_input):
    print(f"The year {year_input} is a leap year.")
else:
    print(f"The year {year_input} is not a leap year.")