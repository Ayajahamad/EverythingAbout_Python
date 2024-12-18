import os
from datetime import datetime

class TodoItem:
    def __init__(self, task):
        self.task = task
        self.completed = False
        self.completion_date = None

    def mark_completed(self):
        if not self.completed:  # Ensure the task isn't already completed
            self.completed = True
            self.completion_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Store the completion date

    def __str__(self):
        status = "✔️" if self.completed else "❌"
        if self.completed:
            return f"{status} {self.task} (Completed on: {self.completion_date})"
        return f"{status} {self.task}"

class TodoList:
    def __init__(self):
        self.items = []

    def add_task(self, task):
        if not task.strip():
            print("\033[91mError: Task cannot be empty.\033[0m")  # Red error message
            return
        self.items.append(TodoItem(task))
        print(f"\033[92mAdded task: {task}\033[0m")  # Green success message

    def remove_task(self, index):
        if index < 0 or index >= len(self.items):
            print("\033[91mError: Invalid task number.\033[0m")
            return
        removed_task = self.items.pop(index)
        print(f"\033[93mRemoved task: {removed_task.task}\033[0m")  # Yellow message

    def complete_task(self, index):
        if index < 0 or index >= len(self.items):
            print("\033[91mError: Invalid task number.\033[0m")
            return
        if self.items[index].completed:
            print("\033[91mError: Task is already completed.\033[0m")
            return
        self.items[index].mark_completed()
        print(f"\033[92mCompleted task: {self.items[index].task}\033[0m")

    def show_tasks(self):
        if not self.items:
            print("\033[94mNo tasks available.\033[0m")  # Blue message
            return
        print("\n\033[1mTodo List:\033[0m")  # Bold title
        for idx, item in enumerate(self.items):
            print(f"{idx + 1}. {item}")

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    todo_list = TodoList()

    while True:
        clear_screen()
        print("\n\033[1m--- Todo List Menu ---\033[0m")  # Bold menu title
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Complete Task")
        print("4. Show Tasks")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == '1':
            task = input("Enter the task: ")
            todo_list.add_task(task)
        elif choice == '2':
            todo_list.show_tasks()
            try:
                index = int(input("Enter the task number to remove: ")) - 1
                todo_list.remove_task(index)
            except ValueError:
                print("\033[91mError: Please enter a valid number.\033[0m")
        elif choice == '3':
            todo_list.show_tasks()
            try:
                index = int(input("Enter the task number to complete: ")) - 1
                todo_list.complete_task(index)
            except ValueError:
                print("\033[91mError: Please enter a valid number.\033[0m")
        elif choice == '4':
            todo_list.show_tasks()
        elif choice == '5':
            print("\033[92mExiting the program. Goodbye!\033[0m")
            break
        else:
            print("\033[91mError: Invalid choice. Please select a number between 1 and 5.\033[0m")

if __name__ == "__main__":
    main()
