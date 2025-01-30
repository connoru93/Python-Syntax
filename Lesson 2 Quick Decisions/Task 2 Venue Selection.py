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