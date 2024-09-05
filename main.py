from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional
import db_test as mydb


app = FastAPI()

todos =[]

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
    print(mydb.hello_from_db())
    return{ "Welcome to todo"}

# to get list of todos
@app.get("/todos", response_model=List[Task])
def get_todos():
    return todos

# to get specific todo
@app.get("/todos/{todo_id}", response_model= Task)
def get_todo_by_id(todo_id: int):
    todo = next((todo for todo in todos if todo.id == todo_id), None)

    if todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")

    return todo


@app.post("/todos", response_model=Task)
def post_todo(todo: Task):
    
    temp_todo= Task(id=len(todos)+1, title=todo.title, description=todo.description, due_date=todo.due_date, created_at=datetime.now(), priority=todo.priority, completed=todo.completed)
    todos.append(temp_todo)
    return temp_todo


@app.delete("/todos/{todo_id}", response_model= dict)
def delete_todo_by_id(todo_id: int):
    global todos
    todo = [todo for todo in todos if todo.id != todo_id]
    return {"detail": "Todo Deleted"}





