import json

# Dummy login credentials
VALID_EMAIL = "pythondeveloper@gmail.com"
VALID_PASSWORD = "@taskdone25"


##Defining Task structure

class Task:
    def __init__(self, task_id, title):
        self.id = task_id
        self.title = title
        self.completed = False

    def __str__(self):
        status = "Completed" if self.completed else "Pending"
        return f"[{self.id}] {self.title} - {status}"

##Implementing task managing functions

tasks = []
task_id_counter = 1

def add_task(title):
    global task_id_counter
    task = Task(task_id_counter, title)
    tasks.append(task)
    task_id_counter += 1
    print(f"Task '{title}' added with ID {task.id}.")

def view_tasks():
    if not tasks:
        print("No tasks found.")
    else:
        for task in tasks:
            print(task)

def delete_task(task_id):
    global tasks
    tasks = [task for task in tasks if task.id != task_id]
    print(f"Task with ID {task_id} deleted.")


def mark_task_complete(task_id):
    for task in tasks:
        if task.id == task_id:
            task.completed = True
            print(f"Task with ID {task_id} marked as complete.")
            return
    print(f"Task with ID {task_id} not found.")

##File handling

def save_tasks():
    with open("tasks.json", "w") as file:
        task_list = [{"id": task.id, "title": task.title, "completed": task.completed} for task in tasks]
        json.dump(task_list, file)
    print("Tasks saved to tasks.json.")

def load_tasks():
    global tasks, task_id_counter
    try:
        with open("tasks.json", "r") as file:
            task_list = json.load(file)
            tasks = [Task(task["id"], task["title"]) for task in task_list]
            task_id_counter = max(task.id for task in tasks) + 1 if tasks else 1
        print("Tasks loaded from tasks.json.")
    except FileNotFoundError:
        print("No tasks file found. Starting with an empty task list.")

##Authentication

def login():
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    if email == VALID_EMAIL and password == VALID_PASSWORD:
        print("Login successful!")
        return True
    else:
        print("Invalid credentials. Please try again.")
        return False

def main():
    if not login():
        return

##Creating a CommandLine Interface

    load_tasks()
    while True:
        print("\nTask Manager CLI")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Mark Task as Complete")
        print("5. Save and Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter task title: ")
            add_task(title)
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            task_id = int(input("Enter task ID to delete: "))
            delete_task(task_id)
        elif choice == "4":
            task_id = int(input("Enter task ID to mark as complete: "))
            mark_task_complete(task_id)
        elif choice == "5":
            save_tasks()
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()