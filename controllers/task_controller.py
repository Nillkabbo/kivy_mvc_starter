from models.task_model import TaskModel
from models.user_model import UserModel

class TaskController:
    def __init__(self):
        self.models = {}
        self.user_model = UserModel()
    
    def add_model(self, model_name):
        self.models[model_name] = TaskModel(model_name)
    
    def add_task(self, model_name, user_id, title):
        self.models[model_name].add_task(user_id, title)
    
    def get_tasks(self, model_name, user_id):
        return self.models[model_name].get_tasks(user_id)
    
    def delete_task(self, model_name, task_id):
        self.models[model_name].delete_task(task_id)
    
    def add_user(self, username, password):
        self.user_model.add_user(username, password)
    
    def get_user(self, username, password):
        return self.user_model.get_user(username, password)
