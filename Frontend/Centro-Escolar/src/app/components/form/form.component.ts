import { Component } from '@angular/core';
import { NgForm } from '@angular/forms';
import { AlumnosService } from 'src/app/services/alumnos.service';

@Component({
  selector: 'app-form',
  templateUrl: './form.component.html',
  styleUrls: ['./form.component.css']
})
export class FormComponent {
  constructor(public studentsService:AlumnosService){}
  addStundents(form:NgForm){
    this.studentsService.addStudent(form.value).subscribe(
      res=>{
        this.studentsService.getAllStudents().subscribe(
          res => {
            this.studentsService.alumnos = res;
            console.log(res)
          },
          err => console.error(err)
        )
      },
      err=> console.error(err)
    )
  }
}
