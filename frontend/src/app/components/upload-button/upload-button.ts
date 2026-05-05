import { Component, signal, inject } from '@angular/core';
import { AnaliseService } from '../../services/analise';
import { Router } from '@angular/router';

@Component({
  selector: 'app-upload',
  standalone: true,
  templateUrl: './upload-button.html',
  styleUrl: './upload-button.css',
})
export class UploadComponent {
  private analiseService = inject(AnaliseService);
  private router = inject(Router);

  isLoading = signal(false);
  imagePreview = signal<string | null>(null);

  onFileSelected(event: any) {
    const file: File = event.target.files[0];
    if (file) {
      this.isLoading.set(true);

      // Preview visual para o aluno
      const reader = new FileReader();
      reader.onload = () => this.imagePreview.set(reader.result as string);
      reader.readAsDataURL(file);

      // Chamada real para o Backend (T1 + T2)
      this.analiseService.enviar(file).subscribe({
        next: () => {
          this.isLoading.set(false);
          this.router.navigate(['/dashboard']); // Volta para o mural após sucesso
        },
        error: () => this.isLoading.set(false),
      });
    }
  }
}
