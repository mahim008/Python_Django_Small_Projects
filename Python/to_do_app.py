def add_task(task_list):
    task = input("Enter a new task: ")
    task_list.append({"task": task, "completed": False})
    print("Task saved successfully!")
    
def display_tasks(task_list):
    if len(task_list) == 0:
        print("No tasks found.")
    else:
        print("Your current saved tasks are : ")
        for index, task in enumerate(task_list):
            status = "complete" if task["completed"] else "imcomplete"
            print(f"\n[{status}] --- {index}. {task['task']}\n")
            
def mark_completed(task_list):
    display_tasks(task_list)
    task_index = int(input("Enter the index of the task to mark as completed: "))
    if 0 <= task_index < len(task_list):
        task_list[task_index]["completed"] = True
        print("Task marked as completed!")
    else:
        print("Invalid task index, check again!")

print("\nWelcome to Mahim's world best task manager!")
tasks = []
mahim_loves_python = True

while mahim_loves_python:
    print("The task menu for you is:\n\t1. Add a task\n\t2. Mark task as completed\n\t3. See existing tasks\n\t4. Exit the app")
    choice = input("Enter your choice (1-4): ")
    if choice == "1":
        add_task(tasks)
    elif choice == "2":
        mark_completed(tasks)
    elif choice == "3":
        display_tasks(tasks)
    elif choice == "4":
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")


