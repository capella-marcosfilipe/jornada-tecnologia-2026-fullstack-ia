import { Component } from '@angular/core';
import { RouterModule } from '@angular/router';
import { UploadComponent } from './components/upload-button/upload-button';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterModule, UploadComponent],
  templateUrl: './app.html',
  styleUrl: './app.css',
})
export class App {
  // Lógica do componente principal
}
