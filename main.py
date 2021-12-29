from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
from datetime import *
import uuid

app = FastAPI()

class ToDo(BaseModel):
    id: Optional[str] = ''
    todo_name: str
    date_start: Optional[str] = date.today()
    date_finish: Optional[str] = date.today()
    status: Optional[bool] = False
    
todo_array = []

@app.get('/')
def read_root():
    return {'hello' : 'world'}

@app.get('/items/{id}')
def read_item(id: int, q: Optional[str] = None):
    return {
        'code': 200,
        'status': 'OK',
        'message': 'OK',
        'data': {
            'id': id,
            'q': q
        }
    }
    
@app.post('/items')
def add_todo(todo: ToDo):
    data_push = {
        'id': uuid.uuid4(),
        'todo_name': todo.todo_name
    }
    todo_array.append(data_push)
    return {
        'code': 200,
        'status': 'OK',
        'message': 'OK',
        'data': todo_array
    } 