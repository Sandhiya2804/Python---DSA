class Task:
    def __init__(self, task_name):
        self.task_name = task_name
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def add_task(self, task_name):
        new_task = Task(task_name)
        if not self.head:
            self.head = new_task
            self.tail = new_task
        else:
            self.tail.next = new_task
            self.tail = new_task
        self.length += 1

    def remove_task(self):
        if not self.head:
            print("No tasks to remove.")
            return None
        task = self.head
        self.head = self.head.next
        self.length -= 1
        return task

    def display_tasks(self):
        if not self.head:
            print("No tasks available.")
            return
        current_task = self.head
        while current_task:
            print(current_task.task_name)
            current_task = current_task.next

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.stack:
            print("Nothing to undo.")
            return None
        return self.stack.pop()

class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if not self.queue:
            print("No tasks in queue.")
            return None
        return self.queue.pop(0)


def task_manager():
    linked_list = LinkedList()
    undo_stack = Stack()
    priority_queue = Queue()

    while True:
        print("\nTask Manager Menu:")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Undo Remove")
        print("4. Show All Tasks")
        print("5. Show Tasks by Priority")
        print("6. Exit")

        choice = int(input("Choose an option: "))

        if choice == 1:
            task_name = input("Enter task name: ")
            linked_list.add_task(task_name)
            priority_queue.enqueue(task_name)
            print(f"Task '{task_name}' added.")

        elif choice == 2:
            removed_task = linked_list.remove_task()
            if removed_task:
                undo_stack.push(removed_task.task_name)
                print(f"Task '{removed_task.task_name}' removed.")

        elif choice == 3:
            undone_task = undo_stack.pop()
            if undone_task:
                linked_list.add_task(undone_task)
                priority_queue.enqueue(undone_task)
                print(f"Undo complete. Task '{undone_task}' restored.")

        elif choice == 4:
            print("Pending Tasks:")
            linked_list.display_tasks()

        elif choice == 5:
            print("Tasks by Priority (FIFO):")
            while priority_queue.queue:
                print(priority_queue.dequeue())

        elif choice == 6:
            print("Exiting Task Manager.")
            break

        else:
            print("Invalid choice. Please try again.")


task_manager()
