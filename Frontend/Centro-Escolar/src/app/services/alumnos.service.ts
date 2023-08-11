import { HttpClient } from '@angular/common/http'
import { Injectable } from '@angular/core';
import { Alumno, Alumno2 } from '../models/alumno';

@Injectable({
  providedIn: 'root'
})
export class AlumnosService {
  URLWEB = 'http://127.0.0.1:8000/';
  alumnos: Alumno[] = [];

  selectStudent:Alumno2={
    matricula:10000,
    nombre:'',
    apellidos:'',
    cuatrimestre:9,
    promedio:10
  }
  constructor(private http: HttpClient) { }
  getAllStudents() {
    return this.http.get<Alumno[]>(this.URLWEB + 'students')
  }
  addStudent(alumno:Alumno) {
    return this.http.post(this.URLWEB + 'students',alumno)
  }
}
