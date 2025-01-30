while True:
    try:
        attendees = int(input("Enter number of attendees: "))
        break
    except ValueError:
        print("Invalid input. Please enter a number.")

venue = "large hall" if attendees > 100 else "conference room"
print(f"Recommended venue: {venue}")

if attendees > 50:
    audio_system = "professional audio system"
else:
    audio_system = "basic audio system"
print(f"Recommended audio system: {audio_system}")

if attendees > 20:
    projector = "high-definition projector"
else:
    projector = "standard projector"
print(f"Recommended projector: {projector}")

if attendees > 100:
    catering = "full catering service"
elif attendees > 50:
    catering = "light refreshments"
else:
    catering = "no catering"
print(f"Recommended catering: {catering}")

while True:
    food_choice = input("Do you want vegetarian food? (yes/no): ")
    if food_choice.lower() == "yes":
        caterer = "Veggie Delight Caterers"
        break
    elif food_choice.lower() == "no":
        caterer = "Gourmet Meals Caterers"
        break
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")

print(f"Recommended caterer: {caterer}")