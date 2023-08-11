from fastapi import APIRouter
from config.db import conn
from models.alumno import alumnos
from schemas.alumno import UserModel
router = APIRouter()


# get all students

@router.get("/students")
def get_students():
    result = conn.execute(alumnos.select()).fetchall()
    resultado = conn.execute(alumnos.select()).fetchall()
    response = []
    for student in resultado:
        alumno = {
            "ID": student[0],
            "matricula": student[1],
            "nombre": student[2],
            "apellidos": student[3],
            "cuatrimestre": student[4],
            "promedio": student[5]
        }
        response.append(alumno)
    return response

# create a student


@router.post("/students")
def create_student(alumno: UserModel):
    conn.execute(alumnos.insert().values(dict(alumno)))
    conn.commit()
    res = {'message': "Student successfully"}
    return res


@router.get('/getOne/{code}')
def getOne(code):
    student = conn.execute(alumnos.select().where(
        alumnos.c.ID == code)).first()
    if student != None:
        student_dict = {
            "ID": student[0],
            "matricula": student[1],
            "nombre": student[2],
            "apellidos": student[3],
            "cuatrimestre": student[4],
            "promedio": student[5]
        }
        return student_dict
    else:
        res = {
            "status": "No existe el alumno"
        }
        return res


@router.put('/updateOne/{code}')
def actualizarAlumno(alumno: UserModel, code):
    res = getOne(code)
    if res.get("status") == "No existe el alumno":
        return res
    else:
        result = conn.execute(alumnos.update().values(
            dict(alumno)).where(alumnos.c.ID == code))
        conn.commit()
    return result.last_updated_params()


@router.delete('/delete/{code}')
def eliminarAlumno(code):
    res = getOne(code)
    if res.get("status") == "No existe el alumno":
        return res
    else:
        result = conn.execute(alumnos.delete().where(alumnos.c.ID == code))
        conn.commit()
        res1 = {
            "status": "Alumno eliminado con éxito"
        }
        return res1
