def add_item():
    item = input("Enter any item to add: ")
    shopping_list.append(item)
    print(f"{item} added to the list.")

def remove_item():
    item = input("Enter the item to remove: ")
    if item in shopping_list:
        shopping_list.remove(item)
        print(f"{item} removed from the list.")
    else:
        print(f"{item} is not in the list.")

def display_list():
    print("Shopping List:")
    for item in shopping_list:
        print(f"--- {item}")

shopping_list = []
print("\nWelcome to Mahim's world best Grocery Shopping!")

mahim_loves_python = True
while mahim_loves_python:
    print("\nAvilable Options :")
    print("1. Add a item")
    print("2. Remove a item")
    print("3. Display whole list")
    print("4. Exit the app")

    choice = input("\nEnter your choice (1-4): ")
    if choice == "1":
        add_item()
    elif choice == "2":
        remove_item()
    elif choice == "3":
        display_list()
    elif choice == "4":
        print("Thank you for using Mahim's world best Grocery Shopping List. Have a great day!")
        break
    else:
        print("Invalid choice. Please try again.")


