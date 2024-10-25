#Baselise-app/app/src/main.py

from fastapi import FastAPI
from src.db import create_table, insert_item, get_items
import uvicorn 

app = FastAPI()

@app.get('/')
async def read():
    """
    Reads items using the get_items function asynchronously.
    
    Returns:
        items: A list of items.
    """
    return await get_items()

@app.post('/create')
async def create():
    """
    Asynchronously creates a table and returns the result.
    
    Returns:
        dict: A dictionary containing the result of creating the table.
    """
    result = await create_table()
    
    return {'result': result}

@app.post('/')
async def write():
    """
    Asynchronously writes an item and its description using the `insert_item` function.
    
    Returns:
        dict: A dictionary containing the result of the write operation.
    """
    result = await insert_item('item', 'description')
    
    return {'result': result}

if __name__ == "__main__":
    uvicorn.run("main:app", port=5000, log_level="info")