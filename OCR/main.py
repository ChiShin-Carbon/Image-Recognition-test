from fastapi import FastAPI
from test_router import test_router
from connect import connect_to_mongo
from create import create
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Connect to MongoDB
connect_to_mongo()

# Include routers
app.include_router(create)

@app.get("/")
async def read_root():
    return {"message": "Welcome to the FastAPI MongoDB project!"}