from models.task_model import TaskModel

class TaskController:
    def __init__(self, db_name='tasks.db'):
        self.task_model = TaskModel(db_name)
    
    def add_task(self, user_id, title):
        self.task_model.add_task(user_id, title)
    
    def get_tasks(self, user_id):
        return self.task_model.get_tasks(user_id)
    
    def delete_task(self, task_id):
        self.task_model.delete_task(task_id)
