import logging
import sys
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

from controllers.task_controller import TaskController
from models.task_model import TaskModel
from ui.views.main_view import MainView
from ui.views.user_view import UserView  # Import UserView

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load the kv file
Builder.load_file('ui/kvs/views/main.kv')

class TaskApp(App):
    def build(self):
        controller = TaskController()
        controller.add_model('Model1')
        controller.add_model('Model2')
        
        sm = ScreenManager()
        user_screen = Screen(name='user')
        user_screen.add_widget(UserView(controller))
        sm.add_widget(user_screen)
        
        main_screen = Screen(name='main')
        main_screen.add_widget(MainView(controller))
        sm.add_widget(main_screen)
        
        sm.current = 'user'  # Start with the user screen
        
        return sm

if __name__ == '__main__':
    try:
        TaskApp().run()
    except Exception as e:
        logger.error("An error occurred", exc_info=True)
        sys.exit(1)