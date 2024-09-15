import os
import psycopg2
import psycopg2.pool


# Get database connection details from environment variables
DB_NAME = os.getenv('POSTGRES_DB', 'todo')
DB_USER = os.getenv('POSTGRES_USER', 'root')
DB_PASSWORD = os.getenv('POSTGRES_PASSWORD', 'test1234')
DB_HOST = os.getenv('POSTGRES_HOST', '127.0.0.1')
DB_PORT = os.getenv('POSTGRES_PORT', '5432')


# Create a connection pool
connection_pool = psycopg2.pool.SimpleConnectionPool(
    1, 20,
    dbname=DB_NAME,
    user=DB_USER,
    password=DB_PASSWORD,
    host=DB_HOST,
    port=DB_PORT
)

def get_connection():
    return connection_pool.getconn()

def release_connection(con):
    connection_pool.putconn(con)


def create_table():
    con = get_connection()

    try:
        with con.cursor() as cursor:
            create_table= "CREATE TABLE IF NOT EXISTS \"Todo\" (id SERIAL PRIMARY KEY, title VARCHAR(255) NOT NULL, description TEXT, due_date DATE, created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, priority VARCHAR(255), completed BOOLEAN);"
            cursor.execute(create_table)
        con.commit()
        print("Hello from create_table")
    except Exception as e:
           print(f"Error creating table: {e}")
    finally:
        release_connection(con)

create_table()

def get_values():
    con = get_connection()
    try:
        with con.cursor() as cursor:
            query= "SELECT * FROM \"Todo\";"
            cursor.execute(query)
            
            print("Hello from get_values")
            data = cursor.fetchall()
            #this is returning list of tuples...
            return data
    finally:
        release_connection(con)
    

def get_values_by_id(id):
    con = get_connection()
    try:
        with con.cursor() as cursor:
            query= "SELECT * FROM \"Todo\" Where id= %s;"
            id_value= (id,)
            cursor.execute(query, id_value)

            print("Hello from get values by id")
            data = cursor.fetchone()
            return data
    finally:
        release_connection(con)


def add_values(title, description, due_date, priority, completed):
    con = get_connection()
    try:
        with con.cursor() as cursor:
            insert_record = "INSERT INTO \"Todo\" (title, description, due_date, priority, completed) VALUES (%s, %s, %s, %s, %s);"
            insert_value = (title, description, due_date, priority, completed)
            cursor.execute(insert_record, insert_value)
        con.commit()
        return True
    except Exception as e:
        print(f"Error adding values: {e}")
        return False
    finally:
        release_connection(con)
        
           
    
def delete_value(id):
    con = get_connection()
    try:
        with con.cursor() as cursor:
            query = f"DELETE FROM \"Todo\" WHERE id={id};"
            
            cursor.execute(query)
        con.commit()
        return True
    except Exception as e:
        print(f"Error deleting value: {e}")
        return False
    finally:
        release_connection(con)

       
     

def update_value(id, title, description, due_date, priority, completed):
    con = get_connection()
    try:
        with con.cursor() as cursor:
            update_record= "UPDATE \"Todo\" SET title=%s, description=%s, due_date=%s, priority=%s, completed=%s WHERE id=%s;"
            update_value= (title, description, due_date, priority, completed, id)
            cursor.execute(update_record, update_value)
            print("Hello from update_value")
        con.commit()
        return True
    except Exception as e:
        print(f"Error Updating value: {e}")
        return False
    finally: 
        release_connection(con)

if __name__ == "__main__":
    create_table()

    print(add_values("Example Task", "This is an example task", "2023-12-31", "medium", False))
    print(get_values())
