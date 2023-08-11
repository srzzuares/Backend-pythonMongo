import { Component } from '@angular/core';
import { AlumnosService } from 'src/app/services/alumnos.service';

@Component({
  selector: 'app-form',
  templateUrl: './form.component.html',
  styleUrls: ['./form.component.css']
})
export class FormComponent {
  constructor(public studentsService:AlumnosService){}
}
