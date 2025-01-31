import random

# List of moods
moods = ["Happy", "Sad", "Energetic", "Calm"]

# List of days of the week
days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# List of times of the day
times_of_day = ["Morning", "Afternoon", "Evening"]

# Outer loop to iterate over the days of the week
for day in days_of_week:
    # Print the current day
    print(f"Mood Tracker for {day}:")
    
    # Inner loop to iterate over the times of the day
    for time in times_of_day:
        # Randomly select a mood from the list
        mood = random.choice(moods)
        
        # Print the time and the corresponding mood
        print(f"{time}: {mood}")
    
    # Print a blank line to separate the days
    print()