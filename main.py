from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/posts")
async def get_posts():
    return {"message": "Get all posts"}

@app.post("/posts")
async def create_post():
    return {"message": "Create a new post"}

