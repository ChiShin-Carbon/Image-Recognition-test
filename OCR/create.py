from fastapi import APIRouter, HTTPException, status
from connect import collection
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from test_schema import test_serial, list_serial
from test_model import TestModel


create = APIRouter()

class User(BaseModel):
    name: str
    age: int

@create.post("/create-test", status_code=status.HTTP_201_CREATED)
async def create_test(test: TestModel):
    result = collection.insert_one(test.dict())
    if not result.acknowledged:
        raise HTTPException(status_code=500, detail="Failed to insert data")
    return test_serial(collection.find_one({"_id": result.inserted_id}))