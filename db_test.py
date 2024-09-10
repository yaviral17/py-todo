import psycopg2


db_connection= psycopg2.connect(
    dbname='todo',
    user='root',
    password='test1234',
    host='localhost',
    port=6789
)
print("Hello from cursor")

if db_connection:
    
    print("Connected to the database")
cursor =db_connection.cursor()




def create_table():
    global cursor
    create_table= "CREATE TABLE IF NOT EXISTS \"Todo\" (id SERIAL PRIMARY KEY, title VARCHAR(255) NOT NULL, description TEXT, due_date DATE, created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, priority VARCHAR(255), completed BOOLEAN);"
    cursor.execute(create_table)
    db_connection.commit()
    print("Hello from create_table")
    return "Table created"

create_table()
print("Todo table created")


def get_values():
    global cursor
    query= "SELECT * FROM \"Todo\";"
    cursor.execute(query)
    
    print("Hello from get_values")
    data = cursor.fetchall()
    #this is returning list of tuples...
    return data

def get_values_by_id(id):
    global cursor
    query= "SELECT * FROM \"Todo\" Where id= %s;"
    id_value= (id,)
    cursor.execute(query, id_value)

    print("Hello from get values by id")
    data = cursor.fetchone()
    return data
    

def add_values(title, description, due_date, priority, completed):
    global cursor
    
    insert_record = "INSERT INTO \"Todo\" (title, description, due_date, priority, completed) VALUES (%s, %s, %s, %s, %s);"
    insert_value = (title, description, due_date, priority, completed)
    cursor.execute(insert_record, insert_value)
  
    
    print("Hello from add_values")
    try:
        db_connection.commit()        
        return True
    except Exception as e:
        print(e)
        
    
        return False
    
def delete_value(id):
    global cursor

    query = f"DELETE FROM \"Todo\" WHERE id={id};"
    try:
        cursor.execute(query)
        db_connection.commit()
        return True
    except Exception as e:
        print(e)
        return False
     

def update_value(id, title, description, due_date, priority, completed):
    global cursor

    update_record= "UPDATE \"Todo\" SET title=%s, description=%s, due_date=%s, priority=%s, completed=%s WHERE id=%s;"

    update_value= (title, description, due_date, priority, completed, id)
    cursor.execute(update_record, update_value)
    print("Hello from update_value")
    try:
        db_connection.commit()
        return True
    except Exception as e:
        print(e)
        return False

    


if __name__ == "__main__":
    print(add_values( "bhukha", "bhuka hu mie", "2022-12-12", "high", "false"))
    # print(get_values())
    
    pass
    # print(hello_from_db