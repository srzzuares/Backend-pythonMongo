from fastapi import FastAPI
app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

#get all students

@app.get("/students")
async def get_students():
    return {"message": "Hello World"}

#get a student by id        

@app.get("/students/{student_id}")
async def get_student(student_id: int):
    return {"message": "Hello World"}


#create a student

@app.post("/students")
async def create_student():
    return {"message": "Hello World"}

#update a student

@app.put("/students/{student_id}")
async def update_student():
    return {"message": "Hello World"}

#delete a student

@app.delete("/students/{student_id}")
async def delete_student():
    return {"message": "Hello World"}

