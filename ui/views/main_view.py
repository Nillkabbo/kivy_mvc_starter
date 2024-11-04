from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.properties import ObjectProperty

class MainView(BoxLayout):
    task_input = ObjectProperty(None)
    task_list = ObjectProperty(None)
    user_spinner = ObjectProperty(None)
    
    def __init__(self, controller, **kwargs):
        super().__init__(**kwargs)
        self.controller = controller
        self.model_name = 'Model1'  # Default model name
        self.user_id = 'User1'      # Default user id
        self.refresh_user_spinner()
        self.refresh_tasks(self.model_name, self.user_id)
    
    def add_task(self, model_name, user_id):
        task_text = self.task_input.text.strip()
        if task_text:
            self.controller.add_task(model_name, user_id, task_text)
            self.task_input.text = ''
            self.refresh_tasks(model_name, user_id)
    
    def refresh_tasks(self, model_name, user_id):
        self.task_list.clear_widgets()
        tasks = self.controller.get_tasks(model_name, user_id)
        for task in tasks:
            self.task_list.add_widget(
                TaskItemView(task, model_name, self.controller, lambda: self.refresh_tasks(model_name, user_id))
            )
    
    def set_user(self, user):
        self.user_id = user[0]  # Assuming user[0] is the user_id
        self.refresh_tasks(self.model_name, self.user_id)
    
    def refresh_user_spinner(self):
        users = self.controller.user_model.get_all_users()
        self.user_spinner.values = [user[1] for user in users]  # Assuming user[1] is the username

class TaskItemView(BoxLayout):
    def __init__(self, task, model_name, controller, refresh_callback, **kwargs):
        super().__init__(**kwargs)
        self.task = task
        self.model_name = model_name
        self.controller = controller
        self.refresh_callback = refresh_callback
        self.size_hint_y = None
        self.height = 40
        
        self.orientation = 'horizontal'
        self.spacing = 5
        
        # Add task text
        self.add_widget(
            Label(text=task[1], size_hint_x=0.7)
        )
        
        # Add delete button
        delete_btn = Button(
            text='Delete',
            size_hint_x=0.3
        )
        delete_btn.bind(on_press=self.delete_task)
        self.add_widget(delete_btn)
    
    def delete_task(self, instance):
        self.controller.delete_task(self.model_name, self.task[0])  # Pass model_name and task_id
        self.refresh_callback()
