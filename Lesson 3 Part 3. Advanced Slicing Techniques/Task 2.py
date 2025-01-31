# Given list of temperatures
temperatures = [72, 75, 78, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106]

# Extract the temperatures for the second week (7 days) of the month
# Note: Python's list slicing is exclusive of the end index, so we use 14 to include temperatures up to index 13
second_week_temperatures = temperatures[7:14]

# Print the extracted temperatures
print(second_week_temperatures)
# Given list of temperatures
temperatures = [72, 75, 78, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106]

# Extract the temperatures above 100
temperatures_above_100 = [temp for temp in temperatures if temp > 100]

# Print the extracted temperatures
print(temperatures_above_100)