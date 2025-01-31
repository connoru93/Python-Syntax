import random

# List of moods
moods = ["Happy", "Sad", "Energetic", "Calm"]

# List of days of the week
days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# Loop through each day of the week using the range() function
for i in range(7):
    # Randomly select a mood from the list
    mood = random.choice(moods)
    
    # Print the day and the corresponding mood
    print(f"On {days_of_week[i]}, you were feeling {mood}.")