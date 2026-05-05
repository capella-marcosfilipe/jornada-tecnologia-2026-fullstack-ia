import { Component, signal, inject } from '@angular/core';
// import { AnaliseService } from '../../services/analise'; // Implementar com o T3

@Component({
  selector: 'app-upload-button',
  standalone: true,
  templateUrl: './upload-button.html',
  styleUrl: './upload-button.css',
})
export class UploadComponent {
  // private analiseService = inject(AnaliseService); // Implementar com o T3
  imagePreview = signal<string | null>(null);

  onFileSelected(event: any) {
    const file: File = event.target.files[0];
    if (file) {
      const reader = new FileReader();
      reader.onload = () => this.imagePreview.set(reader.result as string);
      reader.readAsDataURL(file);

      // TODO: Implementar a chamada ao serviço com o Tutor 3
      // this.analiseService.enviar(file).subscribe(...)
    }
  }
}
