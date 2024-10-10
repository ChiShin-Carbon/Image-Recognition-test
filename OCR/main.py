from fastapi import FastAPI
from connect import connect_to_mongo
from fastapi.middleware.cors import CORSMiddleware
from ocrapi import ocrapi

app = FastAPI()


origins = [
    "https://my-nextjs-69tqp1kw2-chengggkks-projects.vercel.app",  # Replace with your actual Vercel domain
    "http://localhost:3000",  # Local development
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



# Connect to MongoDB
connect_to_mongo()

# Include routers
app.include_router(ocrapi)


@app.get("/")
async def read_root():
    return {"message": "Welcome to the FastAPI MongoDB project!"}