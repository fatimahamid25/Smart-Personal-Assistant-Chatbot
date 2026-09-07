tasks = []

def add_task(task):
   tasks.append(task)
   return "Task added."

def get_tasks():
    return tasks

def delete_task(index):
    if 0 <= index < len(tasks):
     tasks.pop(index)
    return "Task deleted."
    return "Invalid task."
