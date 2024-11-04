from models.user_model import UserModel

class UserController:
    def __init__(self, db_name='tasks.db'):
        self.user_model = UserModel(db_name)
    
    def add_user(self, username, password):
        self.user_model.add_user(username, password)
    
    def get_user(self, username, password):
        return self.user_model.get_user(username, password)
    
    def get_all_users(self):
        return self.user_model.get_all_users()
