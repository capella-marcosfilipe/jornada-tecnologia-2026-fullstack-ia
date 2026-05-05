import { Routes } from '@angular/router';
import { DashboardComponent } from './components/dashboard/dashboard';
import { UploadComponent } from './components/upload-button/upload-button';

export const routes: Routes = [
  // Redireciona a raiz direto para o dashboard
  { path: '', redirectTo: 'dashboard', pathMatch: 'full' },
  { path: 'dashboard', component: DashboardComponent },
  { path: 'upload', component: UploadComponent },
];
