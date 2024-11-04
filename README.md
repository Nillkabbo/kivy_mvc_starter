## Application Overview

This application is a Kivy-based MVC (Model-View-Controller) starter template that includes user registration, login, and task management features.

### Main Application Entry Point

#### [main_app.py](file:///Users/md.rakibulhasan/Downloads/nmr_structured_mvc/main_app.py)

1. **Imports and Logging Configuration:**
   - The necessary modules and classes are imported.
   - Logging is configured to capture and display log messages.

2. **Loading the KV File:**
   - The KV file (`main.kv`) is loaded using `Builder.load_file`.

3. **TaskApp Class:**
   - The `TaskApp` class inherits from `App`.
   - The `build` method is overridden to set up the application.

4. **Setting Up the ScreenManager:**
   - A `ScreenManager` instance (`sm`) is created to manage different screens.
   - Two screens are added to the `ScreenManager`: `user_screen` and `main_screen`.
   - The `UserView` and `MainView` instances are added to their respective screens.
   - The initial screen is set to `user`.

5. **Running the Application:**
   - The `TaskApp` instance is created and run.
   - If an exception occurs, it is logged, and the application exits.

### Models

#### [user_model.py](file:///Users/md.rakibulhasan/Downloads/nmr_structured_mvc/models/user_model.py)

1. **UserModel Class:**
   - Manages user data using SQLite.
   - Connects to the `users.db` database and creates a `users` table if it doesn't exist.

2. **Methods:**
   - `add_user`: Adds a new user to the database.
   - `get_user`: Retrieves a user from the database based on username and password.
   - `get_all_users`: Retrieves all users from the database.
   - `__del__`: Closes the database connection when the instance is deleted.

#### [task_model.py](file:///Users/md.rakibulhasan/Downloads/nmr_structured_mvc/models/task_model.py)

1. **TaskModel Class:**
   - Manages task data using SQLite.
   - Connects to a database specific to the model name (e.g., `Model1_tasks.db`) and creates a `tasks` table if it doesn't exist.

2. **Methods:**
   - `add_task`: Adds a new task to the database.
   - `get_tasks`: Retrieves tasks from the database for a specific user.
   - `delete_task`: Deletes a task from the database based on task ID.
   - `__del__`: Closes the database connection when the instance is deleted.

### Controller

#### [task_controller.py](file:///Users/md.rakibulhasan/Downloads/nmr_structured_mvc/controllers/task_controller.py)

1. **TaskController Class:**
   - Manages interactions between the models and the views.

2. **Initialization:**
   - Initializes an empty dictionary (`models`) to store `TaskModel` instances.
   - Creates an instance of `UserModel`.

3. **Methods:**
   - `add_model`: Adds a new `TaskModel` instance to the `models` dictionary.
   - `add_task`: Adds a task to the specified model for a specific user.
   - `get_tasks`: Retrieves tasks from the specified model for a specific user.
   - `delete_task`: Deletes a task from the specified model.
   - `add_user`: Adds a new user using the `UserModel`.
   - `get_user`: Retrieves a user using the `UserModel`.

### Views

#### [user_view.py](file:///Users/md.rakibulhasan/Downloads/nmr_structured_mvc/ui/views/user_view.py)

1. **UserView Class:**
   - Manages user registration and login.

2. **Initialization:**
   - Initializes the `controller` attribute with the provided controller instance.

3. **Methods:**
   - `register_user`: Registers a new user and refreshes the user spinner in the `MainView`.
   - `login_user`: Logs in a user and switches to the `MainView`.
   - `refresh_user_spinner`: Refreshes the user spinner in the `MainView`.
   - `get_all_usernames`: Retrieves all usernames from the `UserModel`.

#### [main_view.py](file:///Users/md.rakibulhasan/Downloads/nmr_structured_mvc/ui/views/main_view.py)

1. **MainView Class:**
   - Manages task input and display.

2. **Initialization:**
   - Initializes the `controller`, `model_name`, and `user_id` attributes.
   - Refreshes the user spinner and tasks.

3. **Methods:**
   - `add_task`: Adds a new task for the specified model and user.
   - `refresh_tasks`: Refreshes the task list for the specified model and user.
   - `set_user`: Sets the current user and refreshes tasks.
   - `refresh_user_spinner`: Refreshes the user spinner with all usernames.

4. **TaskItemView Class:**
   - Represents a single task item in the task list.
   - Initializes the task item with task details, delete button, and delete functionality.

### KV File

#### [main.kv](file:///Users/md.rakibulhasan/Downloads/nmr_structured_mvc/ui/kvs/views/main.kv)

1. **UserView Layout:**
   - Defines the layout for user registration and login.
   - Includes text inputs for username and password, and buttons for registration and login.

2. **MainView Layout:**
   - Defines the layout for task input and display.
   - Includes spinners for selecting model and user, a text input for task entry, and a button for adding tasks.
   - Includes a scrollable grid layout for displaying tasks.

### Application Flow

1. **Startup:**
   - The application starts with the `TaskApp` class, which sets up the `ScreenManager` with `UserView` and `MainView`.

2. **User Registration/Login:**
   - The user registers or logs in using the `UserView`.
   - Upon successful login, the application switches to the `MainView`.

3. **Task Management:**
   - In the `MainView`, the user can select a model and user, add tasks, and view tasks.
   - Tasks are managed by the `TaskController`, which interacts with the `TaskModel` and `UserModel`.

4. **Dynamic Updates:**
   - The user spinner in the `MainView` is dynamically updated when a new user is registered.
   - Tasks are dynamically updated based on the selected model and user.

### Steps to Run the Application

1. **Ensure Dependencies:**
   - Make sure you have Python and Kivy installed.

2. **Set Up the Project Structure:**
   - Organize your project files as follows:
     ```
     nmr_structured_mvc/
     ├── controllers/
     │   └── task_controller.py
     ├── models/
     │   ├── task_model.py
     │   └── user_model.py
     ├── ui/
     │   ├── kvs/
     │   │   └── views/
     │   │       └── main.kv
     │   └── views/
     │       ├── main_view.py
     │       └── user_view.py
     └── main_app.py
     ```

3. **Run the Application:**
   - Navigate to the project directory and run the `main_app.py` file:
     ```sh
     python main_app.py
     ```

4. **Register and Log In:**
   - Use the `UserView` to register a new user.
   - Log in with the registered user to switch to the `MainView`.

5. **Manage Tasks:**
   - In the `MainView`, select a model and user, add tasks, and view tasks.

This detailed explanation covers the entire application flow, from the main application entry point to each screen, view, model, and controller, along with the steps to run the application.