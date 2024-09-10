from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional
import db_test as mydb


app = FastAPI()


class Task(BaseModel):
    id: Optional[int] = 0 
    title: str
    description: Optional[str] = None
    due_date: Optional[datetime]
    created_at: Optional[datetime] = datetime.now()
    priority: str = None
    completed: bool = False

#welcome function
@app.get("/")
def get_todo():
    
    return{ "Welcome to todo"}


# to get list of todos
@app.get("/todos", response_model=List[Task])
def get_todos():
    data= mydb.get_values()
    temp_todos= []
    for i in data:
        temp_todo= Task(id=i[0], title=i[1], description=i[2], due_date=i[3], created_at=i[4], priority=i[5], completed=i[6])
        temp_todos.append(temp_todo)
    return temp_todos

# to get specific todo
@app.get("/todos/{todo_id}", response_model= Task)
def get_todo_by_id(todo_id: int):
    data = mydb.get_values_by_id(todo_id)

    return Task(id=data[0], title=data[1], description=data[2], due_date=data[3], created_at=data[4], priority=data[5], completed=data[6])
        

   


@app.post("/todos", response_model=Task)
def post_todo(todo: Task):
    titles= todo.title
    descriptions = todo.description
    due_dates= todo.due_date
    prioritys= todo.priority
    completeds=todo.completed

    mydb.add_values(titles, descriptions, due_dates,prioritys, completeds)

    
    data = mydb.get_values()

    '''
    [
        (),
        (),
        ()
    ]
    '''
    tup= data[-1]
    
    return Task(id=tup[0], title=tup[1], description=tup[2], due_date=tup[3], created_at=tup[4], priority=tup[5], completed=tup[6])
        

@app.put("/todos/{todo_id}", response_model= dict)
def update_todo_by_id(todo_id: int, todo: Task):
    title= todo.title if todo.title else None
    description = todo.description if todo.description else None
    due_date= todo.due_date  if todo.due_date else None
    priority= todo.priority if todo.priority else None
    completed=todo.completed if todo.completed is not None else None

    is_updated = mydb.update_value(todo_id, title, description, due_date, priority, completed)

    if is_updated:
        return {"message": f"Todo with id {todo_id} is successfully updated."}
    else:
        raise HTTPException(status_code=404, detail=f"Todo with id {todo_id} not found or couldn't be updated.")
    
    


@app.delete("/todos/{todo_id}", response_model= dict)
def delete_todo_by_id(todo_id: int):
   is_deleted = mydb.delete_value(todo_id)

   if is_deleted:
       return {"message": f"Todo with id {todo_id} is successfully deleted."}
   else:
       raise HTTPException(status_code=404, detail=f"Todo with id {todo_id} not found or couldn't be deleted.")
   




