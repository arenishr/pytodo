import json

class ToDoList:
    def __init__(self):
        self.tasks = self.load_tasks()

    def add_task(self, description):
        task = {'description': description, 'completed': False}
        self.tasks.append(task)
        self.save_tasks()

    def view_tasks(self):
        for i, task in enumerate(self.tasks):
            status = 'Completed' if task['completed'] else 'Pending'
            print(f"{i + 1}. {task['description']} - {status}")

    def mark_complete(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index]['completed'] = True
            self.save_tasks()

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            del self.tasks[index]
            self.save_tasks()

    def save_tasks(self):
        with open('tasks.json', 'w') as file:
            json.dump(self.tasks, file)

    def load_tasks(self):
        try:
            with open('tasks.json', 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return []

if __name__ == "__main__":
    todo_list = ToDoList()
    while True:
        print("\n1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task Complete")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("Enter choice: ")
        if choice == '1':
            description = input("Enter task description: ")
            todo_list.add_task(description)
        elif choice == '2':
            todo_list.view_tasks()
        elif choice == '3':
            index = int(input("Enter task number to mark as complete: ")) - 1
            todo_list.mark_complete(index)
        elif choice == '4':
            index = int(input("Enter task number to delete: ")) - 1
            todo_list.delete_task(index)
        elif choice == '5':
            break
        else:
            print("Invalid choice.")
