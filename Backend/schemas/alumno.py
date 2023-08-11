from pydantic import BaseModel


class UserModel(BaseModel):
    matricula: int = 2005
    nombre: str = 'Crystian'
    apellidos: str = 'Suarez'
    cuatrimestre: int = 9
    promedio: float = 10
