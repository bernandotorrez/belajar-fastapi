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
        'todo_name': todo.todo_name,
        'date_start': todo.date_start,
        'date_finish': todo.date_finish,
        'status': False
    }
    todo_array.append(data_push)
    return {
        'code': 200,
        'status': 'OK',
        'message': 'OK',
        'data': data_push
    } 
    
@app.get('/items')
def get_todo():
    if(len(todo_array) == 0):
        return {
            'code': 404,
            'status': 'OK',
            'message': 'DATA IS EMPTY',
            'data': []
        }
    else:
        return {
            'code': 200,
            'status': 'OK',
            'message': 'OK',
            'data': todo_array
        }