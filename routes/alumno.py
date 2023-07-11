from fastapi import APIRouter
from config.db import conn
from models.alumno import alumnos
from schemas.alumno import UserModel
router = APIRouter()


#get all students

@router.get("/students")
async def get_students():
    result = conn.execute(alumnos.select()).fetchall()
    print(result)
    resultado = conn.execute(alumnos.select()).fetchall()
    response=[]
    for student in resultado:
        alumno={
            "matricula":student[0],
            "nombre":student[1],
            "apellidos":student[2],
            "cuatrimestre":student[3],
            "promedio":student[4]
        }
        response.append(alumno)
    return response

#create a student

@router.post("/students")
async def create_student(alumno:UserModel):
    conn.execute(alumnos.insert().values(dict(alumno)))
    conn.commit()
    res={'message': "Student successfully"}
    return res


""" @app.get("/")
async def root():
    return {"message": "Hello World"}


#get a student by id        

@app.get("/students/{student_id}")
async def get_student(student_id: int):
    return {"message": "Hello World"}


#update a student

@app.put("/students/{student_id}")
async def update_student():
    return {"message": "Hello World"}

#delete a student

@app.delete("/students/{student_id}")
async def delete_student():
    return {"message": "Hello World"} """