from psycopg2 import connect, sql


def create_tasks_table():
    create_table_query = '''
    CREATE TABLE IF NOT EXISTS tasks (
        id SERIAL PRIMARY KEY,
        title VARCHAR(255) NOT NULL,
        completed BOOLEAN DEFAULT FALSE
    )
    '''

def get_db_connection():
    conn = connect(
        dbname='python_class',
        user='postgres',
        password='password',
        host='localhost',
        port='5432'
    )
    return conn

def main():
    # Connect to the database
    conn = get_db_connection()
    cursor = conn.cursor()

    # Main loop for user interaction
    while True:
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Remove Task")
        print("4. Update Task")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            title = input("Enter task title: ")
            cursor.execute("INSERT INTO tasks (title, completed) VALUES (%s, %s)", (title, False))
            conn.commit()
            print("Task added.")

        elif choice == '2':
            cursor.execute("SELECT * FROM tasks")
            tasks = cursor.fetchall()
            for task in tasks:
                print(f"{task[0]}: {task[1]} - {'Completed' if task[2] else 'Not Completed'}")

        elif choice == '3':
            task_id = input("Enter task ID to remove: ")
            cursor.execute("DELETE FROM tasks WHERE id = %s", (task_id,))
            conn.commit()
            print("Task removed.")
        
        elif choice == '4':
            task_id = input("Enter task ID to update: ")
            completed = input("Have you completed the task (True/False): ")
            cursor.execute("UPDATE tasks SET completed = %s WHERE id = %s", (completed, task_id))
            conn.commit()
            print("Task updated.")

        elif choice == '5':
            break

        else:
            print("Invalid option. Please try again.")

    cursor.close()
    conn.close()

if __name__ == "__main__":
    main()