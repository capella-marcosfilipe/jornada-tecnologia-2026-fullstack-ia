import { Component, inject, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
// import { AnaliseService } from '../../services/analise.service'; // A ser implementado com o T3

@Component({
  selector: 'app-dashboard',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './dashboard.html',
  styleUrl: './dashboard.css',
})
export class DashboardComponent implements OnInit {
  // Injetando o serviço (Padrão moderno Angular 21)
  // public service = inject(AnaliseService); // A ser implementado com o T3

  ngOnInit() {
    // Aqui chamaremos o método que você vai criar com os alunos
    // this.service.buscarInformativos(); // A ser implementado com o T3
  }
}
