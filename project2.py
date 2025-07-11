tasks = []

while True:
    print("\n1. Add Task")
    print("2. View Tasks")
    print("3. Exit")

    choice = input("Enter your choice (1/2/3): ")

    if choice == '1':
        task = input("Enter task: ")
        tasks.append(task)
        print("✅ Task added.")
    elif choice == '2':
        print("\n📝 Your Tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
    elif choice == '3':
        print("👋 Exiting...")
        break
    else:
        print("❌ Invalid choice. Try again.")
