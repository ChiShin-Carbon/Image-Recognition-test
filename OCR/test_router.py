from fastapi import APIRouter, HTTPException
from connect import collection
from test_schema import test_serial, list_serial
from test_model import TestModel

test_router = APIRouter()

@test_router.post("/test", response_model=dict)
async def create_test(test: TestModel):
    result = collection.insert_one(test.dict())
    if not result.acknowledged:
        raise HTTPException(status_code=500, detail="Failed to insert data")
    return test_serial(collection.find_one({"_id": result.inserted_id}))

@test_router.get("/test", response_model=list)
async def get_all_tests():
    tests = list(collection.find())
    return list_serial(tests)

@test_router.get("/test/{test_id}", response_model=dict)
async def get_test(test_id: str):
    test = collection.find_one({"_id": test_id})
    if not test:
        raise HTTPException(status_code=404, detail="Test not found")
    return test_serial(test)

@test_router.delete("/test/{test_id}", response_model=dict)
async def delete_test(test_id: str):
    result = collection.delete_one({"_id": test_id})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Test not found")
    return {"message": "Test deleted successfully"}