import { Component, inject, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterModule } from '@angular/router';
import { AnaliseService } from '../../services/analise';

@Component({
  selector: 'app-dashboard',
  standalone: true,
  imports: [CommonModule, RouterModule],
  templateUrl: './dashboard.html',
  styleUrl: './dashboard.css',
})
export class DashboardComponent implements OnInit {
  // Tornamos público para o HTML conseguir ler os dados
  public service = inject(AnaliseService);

  ngOnInit() {
    // Ao abrir a tela, busca o data.json via FastAPI
    this.service.buscarTodos();
  }
}
