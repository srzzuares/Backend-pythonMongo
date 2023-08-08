from fastapi import APIRouter
from config.db import conn
from models.alumno import alumnos
from schemas.alumno import UserModel
router = APIRouter()


#get all students

@router.get("/students")
def get_students():
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
def create_student(alumno:UserModel):
    conn.execute(alumnos.insert().values(dict(alumno)))
    conn.commit()
    res={'message': "Student successfully"}
    return res


@router.get('/getOne/{code}')
def getOne(code):
    student=conn.execute(alumnos.select().where(alumnos.c.matricula==code)).first()
    if student != None:
        student_dict={
            "matricula":student[0],
            "nombre":student[1],
            "apellidos":student[2],
            "cuatrimestre":student[3],
            "promedio":student[4]
        }
        return student_dict
    else:
        res={
            "status":"No existe el alumno"
        }
        return res
    
    
@router.put('/updateOne/{code}')
def actualizarAlumno(alumno:UserModel, code):
    res=getOne(code)
    print(res)
    if res.get("status")=="No existe el alumno":
       return res
    else:
        result=conn.execute(alumnos.update().values(dict(alumno)).where(alumnos.c.matricula==code))
        conn.commit()
    return result.last_updated_params()  

        
@router.delete('/delete/{code}')
def eliminarAlumno(code):
    res=getOne(code)
    if res.get("status")=="No existe el alumno":
       return res
    else:
        result=conn.execute(alumnos.delete().where(alumnos.c.matricula==code))
        conn.commit()
        res1={
            "status":"Alumno eliminado con éxito"
        }
        return res1