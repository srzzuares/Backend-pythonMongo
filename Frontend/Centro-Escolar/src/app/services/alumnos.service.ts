import { HttpClient } from '@angular/common/http'
import { Injectable } from '@angular/core';
import { Alumno } from '../models/alumno';

@Injectable({
  providedIn: 'root'
})
export class AlumnosService {
  alumnos: Alumno[] = [];
  constructor(private http: HttpClient) { }
}
