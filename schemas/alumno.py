from pydantic import BaseModel
class UserModel(BaseModel):
    matricula : int
    nombre : str
    apellidos : str
    cuatrimestre : int
    promedio : float