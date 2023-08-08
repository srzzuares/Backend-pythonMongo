import { Component } from '@angular/core';
import { AlumnosService } from 'src/app/services/alumnos.service';

@Component({
  selector: 'app-table',
  templateUrl: './table.component.html',
  styleUrls: ['./table.component.css']
})
export class TableComponent {
  constructor(public alumnoService: AlumnosService) { }
  ngOnInit() {
    this.getAllStudents();
  }
  getAllStudents() {
    this.alumnoService.getAllStudents().subscribe(
      res => {
        this.alumnoService.alumnos = res;
        console.log(res)
      },
      err => console.error(err)
    )
  }
}
