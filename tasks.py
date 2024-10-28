import os 
import json


class Task:
    def __init__(self, description, due_date=None, priority=1, completed = False):
        self.description = description
        self.due_date = due_date
        self.priority = priority
        self.completed = completed

    def to_dict(self):
        return {
            'description': self.description,
            'due_date': self.due_date,
            'priority': self.priority,
            'completed': self.completed
        }

class TodoList :
    def __init__(self, filename = 'tasks.json') :
        self.tasks = []
        self.filename = filename
        self.load_tasks()

    def add_task (self , description , due_date =None , priority = 1):
        task = Task(description, due_date , priority)
        self.tasks.append(task)
        self.save_tasks()
    
    def remove_task(self , index ):
        if self.view_tasks :
            del self.tasks[index]
            self.save_tasks()
        else : 
            print("invalid Task id")
    
    def mark_complete (self , index):
        if self.view_tasks :
            self.tasks[index].completed= True
            self.save_tasks()
        else : 
            print("invalid Task id")
    
    def change_priority (self , index, priority):
        if self.view_tasks :
            self.tasks[index].priority = priority
            self.save_tasks()
        else :
            print("invalid Task id")
    
    def view_tasks (self):
        if not self.tasks:
            print ("no task avaidable")
            return False
        for i, task in enumerate(self.tasks, start = 1) :
            status = "✓" if task.completed else "✗"
            print (f"{i}. [{status}] {task.description} Due : {task.due_date} priority : {task.priority}")
    
    def save_tasks(self):
        with open (self.filename , 'w') as f :
            json.dump([task.to_dict() for task in self.tasks], f)
    
    def load_tasks(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as f:
                tasks_data = json.load(f)
                self.tasks = [Task(**task) for task in tasks_data]
