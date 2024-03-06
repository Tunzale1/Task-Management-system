from uuid import uuid4
import argparse
class Task:
    
    def __init__(self, title, description, completed=False):
        self.id = str(uuid4())
        self.title = title
        self.description = description
        self.completed = completed

    def mark_as_completed(self):
        self.completed = True
    
    def __str__(self):
        return f"Task: {self.title} ID: {self.id} Description: {self.description} Completed: {self.completed}"

class TaskManager:

    def __init__(self):
        self.tasks = {}

    def add_task(self, title, description):
        new_task = Task(title, description)
        self.tasks[new_task.id] = new_task
    
    def remove_task(self, id):
        if id in self.tasks:
            del self.tasks[id]

    def mark_task_completed(self, id):
        if id in self.tasks:
            self.tasks[id].mark_as_completed()

    def list_tasks(self):
        for task_id, task in self.tasks.items():
            print(f"Task ID: {task_id}")
            print(f"Title: {task.title}")
            print(f"Description: {task.description}")
            print(f"Completed: {task.completed}")

    def find_task(self, id):
        if id in self.tasks:
            return self.tasks[id]
        else:
            return None     



def main():
    parser = argparse.ArgumentParser(description="Task Manager CLI")
    parser.add_argument("action", choices=["add", "remove", "complete", "list", "find", "exit"], help="Action to perform on tasks")

    task_manager = TaskManager()

    while True:
        args = parser.parse_args(input("Enter command: ").strip().split())

        if args.action == "add":
            title = input("Enter title: ")
            description = input("Enter description: ")
            task_manager.add_task(title, description)
        elif args.action == "remove":
            task_id = input("Enter task ID to remove: ")
            task_manager.remove_task(task_id)
        elif args.action == "complete":
            task_id = input("Enter task ID to mark as completed: ")
            task_manager.mark_task_completed(task_id)
        elif args.action == "list":
            task_manager.list_tasks()
        elif args.action == "find":
            task_id = input("Enter task ID to find: ")
            print(task_manager.find_task(task_id))
        elif args.action == "exit":
            print("Exiting...")
            break

if __name__ == "__main__":
    main()


