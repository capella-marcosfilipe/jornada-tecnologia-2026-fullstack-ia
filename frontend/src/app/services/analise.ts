import { Injectable, signal, inject } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Informativo } from '../models/informativo';
import { tap } from 'rxjs';

@Injectable({ providedIn: 'root' })
export class AnaliseService {
  private http = inject(HttpClient);
  private apiUrl = 'http://localhost:8000';

  // Signal: A "fonte da verdade" para o Dashboard
  public informativos = signal<Informativo[]>([]);

  // Busca os dados iniciais do data.json
  buscarTodos() {
    this.http.get<Informativo[]>(`${this.apiUrl}/informativos`)
      .subscribe(dados => this.informativos.set(dados));
  }

  // Envia a foto para o LangGraph e atualiza a lista ao receber a resposta
  enviar(arquivo: File) {
    const formData = new FormData();
    formData.append('file', arquivo);

    return this.http.post<Informativo>(`${this.apiUrl}/analisar`, formData).pipe(
      tap(novo => {
        // Atualiza o Signal adicionando o novo item no topo da lista
        this.informativos.update(lista => [novo, ...lista]);
      })
    );
  }
}