contacts = {}

while True:
    print("\n1. Add Contact")
    print("2. View Comtacts")
    print("3. Exit")
    
    choice = input("Enter your choice (1/2/3): ")
    
    if choice == '1':
        name = input("Enter name: ")
        number = input("Enter phone number: ")
        contacts[name] = number
        print("contact saved.")
        
    elif choice == '2':
        if not contacts:
            print("No contacts found.")
        else:
            print("\ncontact list:")
            for name , number in contacts.items():
                print(f"{name} → {number}")
    elif choice == '3':
        print("Exiting contact book.")
        
    else:
        print("invalid choice.")