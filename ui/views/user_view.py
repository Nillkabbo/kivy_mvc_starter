from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.properties import ObjectProperty

class UserView(BoxLayout):
    username_input = ObjectProperty(None)
    password_input = ObjectProperty(None)
    
    def __init__(self, controller, **kwargs):
        super().__init__(**kwargs)
        self.controller = controller
    
    def register_user(self):
        username = self.username_input.text.strip()
        password = self.password_input.text.strip()
        if username and password:
            self.controller.add_user(username, password)
            self.username_input.text = ''
            self.password_input.text = ''
            self.refresh_user_spinner()
    
    def login_user(self):
        username = self.username_input.text.strip()
        password = self.password_input.text.strip()
        if username and password:
            user = self.controller.get_user(username, password)
            if user:
                # Proceed to main view
                screen_manager = self.parent.parent
                main_screen = screen_manager.get_screen('main')
                main_view = main_screen.children[0]  # Get the MainView instance
                main_view.set_user(user)
                screen_manager.current = 'main'
    
    def refresh_user_spinner(self):
        screen_manager = self.parent.parent
        main_screen = screen_manager.get_screen('main')
        main_view = main_screen.children[0]  # Get the MainView instance
        main_view.refresh_user_spinner()
    
    def get_all_usernames(self):
        users = self.controller.get_all_users()
        return [user[1] for user in users]  # Assuming user[1] is the username
