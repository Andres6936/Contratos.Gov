import {Component, inject, OnInit} from '@angular/core';
import {CommonModule} from '@angular/common';
import {RouterOutlet} from '@angular/router';
import {AppService} from "./app.service";

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [CommonModule, RouterOutlet],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})
export class AppComponent implements OnInit  {
  private readonly appService = inject(AppService);
  public readonly  title = 'App';

  ngOnInit(): void {
    this.appService.getContracts().subscribe({
      next:( result) => {
        console.log(result)
      }
    })
  }
}
