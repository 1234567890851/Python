import datetime

mood_log = {}

while True:
    print("\n1. Log today's mood")
    print("2. view mood history")
    print("3.exit")
    
    choice = input("Enter your choice (1/2/3): ")
    
    if choice == '1':
        today = datetime.date.today().isoformat()
        mood = input("how are you feeling today? ")
        mood_log[today] = mood
        print("mood logged.")
        
    elif choice == '2':
        if not mood_log:
            print("No mood data found.")
        else:
            print("\n mood history:")
            for date, mood in mood_log.items():
                print(f"{date}: {mood}")
    elif choice == '3':
        print("Goodbye! Take care of yourself.")
        break
    else:
        print("Invalid choice.")
        
        
        
        