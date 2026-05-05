import { Injectable, signal } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Informativo } from '../models/informativo';

@Injectable({ providedIn: 'root' })
export class AnaliseService {
  private apiUrl = 'http://localhost:8000';
  
  // Usaremos Signals para que o Dashboard atualize automaticamente
  listaInformativos = signal<Informativo[]>([]);

  constructor(private http: HttpClient) {}

  // MÉTODO PARA IMPLEMENTAR COM O ALUNO:
  // enviarArquivo(file: File) { ... }
}