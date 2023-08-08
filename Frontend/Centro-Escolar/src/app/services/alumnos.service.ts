import { HttpClient } from '@angular/common/http'
import { Injectable } from '@angular/core';
import { Alumno } from '../models/alumno';

@Injectable({
  providedIn: 'root'
})
export class AlumnosService {
  URLWEB = 'http://127.0.0.1:8000/';
  alumnos: Alumno[] = [];
  constructor(private http: HttpClient) { }
  getAllStudents() {
    return this.http.get<Alumno[]>(this.URLWEB + 'students')
  }
}
