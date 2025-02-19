import json
from datetime import datetime

class ToDoList:
    def __init__(self):
        self.tasks = []
        self.load_tasks()

    def load_tasks(self):
        try:
            with open("tasks.json", "r") as file:
                self.tasks = json.load(file)
        except FileNotFoundError:
            self.tasks = []

    def save_tasks(self):
        with open("tasks.json", "w") as file:
            json.dump(self.tasks, file, indent=4)

    def add_task(self, task, priority="Medium", due_date=None):
        task_data = {
            "task": task,
            "priority": priority,
            "due_date": due_date,
            "completed": False
        }
        self.tasks.append(task_data)
        print(f"Task '{task}' added to the list.")
        self.save_tasks()

    def view_tasks(self, filter_by=None):
        if not self.tasks:
            print("No tasks in the list.")
            return

        print("\nTo-Do List:")
        for index, task in enumerate(self.tasks):
            if filter_by == "completed" and not task["completed"]:
                continue
            if filter_by == "pending" and task["completed"]:
                continue
            if filter_by and filter_by.lower() != task["priority"].lower():
                continue

            status = "Done" if task["completed"] else "Not Done"
            due_date = task["due_date"] if task["due_date"] else "No due date"
            print(f"{index + 1}. {task['task']} - Priority: {task['priority']} - Due: {due_date} - {status}")

    def mark_task_completed(self, task_number):
        if 1 <= task_number <= len(self.tasks):
            self.tasks[task_number - 1]["completed"] = True
            print(f"Task {task_number} marked as completed.")
            self.save_tasks()
        else:
            print("Invalid task number.")

    def delete_task(self, task_number):
        if 1 <= task_number <= len(self.tasks):
            removed_task = self.tasks.pop(task_number - 1)
            print(f"Task '{removed_task['task']}' deleted from the list.")
            self.save_tasks()
        else:
            print("Invalid task number.")

    def edit_task(self, task_number, new_task=None, new_priority=None, new_due_date=None):
        if 1 <= task_number <= len(self.tasks):
            task = self.tasks[task_number - 1]
            if new_task:
                task["task"] = new_task
            if new_priority:
                task["priority"] = new_priority
            if new_due_date:
                task["due_date"] = new_due_date
            print(f"Task {task_number} updated.")
            self.save_tasks()
        else:
            print("Invalid task number.")

def get_priority():
    while True:
        priority = input("Enter priority (High/Medium/Low): ").capitalize()
        if priority in ["High", "Medium", "Low"]:
            return priority
        print("Invalid priority. Please enter High, Medium, or Low.")

def get_due_date():
    while True:
        due_date = input("Enter due date (YYYY-MM-DD, or leave blank): ")
        if not due_date:
            return None
        try:
            datetime.strptime(due_date, "%Y-%m-%d")
            return due_date
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")

def main():
    todo_list = ToDoList()

    while True:
        print("\nTo-Do List Menu:")
        print("1. Add Task")
        print("2. View All Tasks")
        print("3. View Completed Tasks")
        print("4. View Pending Tasks")
        print("5. View Tasks by Priority")
        print("6. Mark Task as Completed")
        print("7. Delete Task")
        print("8. Edit Task")
        print("9. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter the task: ")
            priority = get_priority()
            due_date = get_due_date()
            todo_list.add_task(task, priority, due_date)
        elif choice == "2":
            todo_list.view_tasks()
        elif choice == "3":
            todo_list.view_tasks(filter_by="completed")
        elif choice == "4":
            todo_list.view_tasks(filter_by="pending")
        elif choice == "5":
            priority = get_priority()
            todo_list.view_tasks(filter_by=priority)
        elif choice == "6":
            task_number = int(input("Enter the task number to mark as completed: "))
            todo_list.mark_task_completed(task_number)
        elif choice == "7":
            task_number = int(input("Enter the task number to delete: "))
            todo_list.delete_task(task_number)
        elif choice == "8":
            task_number = int(input("Enter the task number to edit: "))
            new_task = input("Enter new task description (or leave blank to keep current): ")
            new_priority = get_priority() if input("Change priority? (y/n): ").lower() == "y" else None
            new_due_date = get_due_date() if input("Change due date? (y/n): ").lower() == "y" else None
            todo_list.edit_task(task_number, new_task, new_priority, new_due_date)
        elif choice == "9":
            print("Exiting the To-Do List application. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()