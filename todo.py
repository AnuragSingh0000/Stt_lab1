"""Code for TO DO"""

def display_menu():
    """Function to display the possible tasks"""
    print("\n--- To-Do List Menu ---")
    print("1. Add a task")
    print("2. Remove a task")
    print("3. Mark task as done")
    print("4. View all tasks")
    print("5. Exit")

def add_task(tasks):
    """Function to add tasks"""
    task = input("Enter a new task: ").strip()
    if task:
        tasks.append({"task": task, "done": False})
        print(f"Added task: '{task}'")
    else:
        print("Task cannot be empty.")

def remove_task(tasks):
    """Function to remove tasks"""
    view_tasks(tasks)
    if not tasks:
        return
    try:
        index = int(input("Enter task number to remove: ")) - 1
        if 0 <= index < len(tasks):
            removed = tasks.pop(index)
            print(f"Removed task: '{removed['task']}'")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def mark_done(tasks):
    """Function to mark completed tasks"""
    view_tasks(tasks)
    if not tasks:
        return
    try:
        index = int(input("Enter task number to mark as done: ")) - 1
        if 0 <= index < len(tasks):
            tasks[index]["done"] = True
            print(f"Marked task '{tasks[index]['task']}' as done.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def view_tasks(tasks):
    """Function to view all the tasks"""
    if not tasks:
        print("No tasks in your to-do list.")
        return
    print("\nYour Tasks:")
    for i, task in enumerate(tasks, 1):
        status = "✓" if task["done"] else "✗"
        print(f"{i}. [{status}] {task['task']}")

def main():
    """Main function"""
    tasks = []
    while True:
        display_menu()
        choice = input("Choose an option (1-5): ").strip()
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            remove_task(tasks)
        elif choice == "3":
            mark_done(tasks)
        elif choice == "4":
            view_tasks(tasks)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
