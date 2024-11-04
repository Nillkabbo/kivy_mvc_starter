import sqlite3

class TaskModel:
    def __init__(self, model_name):
        self.model_name = model_name
        self.conn = sqlite3.connect(f'{model_name}_tasks.db')
        self.create_table()
    
    def create_table(self):
        cursor = self.conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id TEXT NOT NULL,
                title TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        self.conn.commit()
    
    def add_task(self, user_id, title):
        cursor = self.conn.cursor()
        cursor.execute('INSERT INTO tasks (user_id, title) VALUES (?, ?)', (user_id, title))
        self.conn.commit()
    
    def get_tasks(self, user_id):
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM tasks WHERE user_id = ? ORDER BY created_at DESC', (user_id,))
        return cursor.fetchall()
    
    def delete_task(self, task_id):
        cursor = self.conn.cursor()
        cursor.execute('DELETE FROM tasks WHERE id = ?', (task_id,))
        self.conn.commit()
    
    def __del__(self):
        self.conn.close()
