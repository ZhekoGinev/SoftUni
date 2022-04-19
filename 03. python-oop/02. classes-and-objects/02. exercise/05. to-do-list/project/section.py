from project.task import Task


class Section:
    def __init__(self, name: str) -> None:
        self.name = name
        self.tasks = []

    def add_task(self, new_task: Task):
        if new_task not in self.tasks:
            self.tasks.append(new_task)
            return f"Task {new_task.details()} is added to the section"
        else:
            return f"Task is already in the section {self.name}"

    def complete_task(self, task_name: str):
        task: Task
        for task in self.tasks:
            if task.name == task_name:
                task.completed = True
            return f"Completed task {task_name}"
        return f"Could not find task with the name {task_name}"

    def clean_section(self):
        removed = 0
        task: Task
        for task in self.tasks:
            if task.completed == True:
                self.tasks.remove(task)
                removed += 1
        return f"Cleared {removed} tasks."

    def view_section(self):
        section_details = "\n".join([t.details() for t in self.tasks])
        return f"Section {self.name}:\n{section_details}"
