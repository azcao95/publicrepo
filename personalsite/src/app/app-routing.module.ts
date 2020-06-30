import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { BioComponent } from './bio/bio.component';
import { HomeComponent } from './home/home.component';
import { SkillsComponent } from './skills/skills.component';
import { DownloadComponent } from './download/download.component';
import { ExperienceComponent } from './experience/experience.component';

const routes: Routes = [
  {path: '', redirectTo: '/Home', pathMatch: 'full'},
  {path:'Home', component: HomeComponent},
  {path:'Bio', component: BioComponent},
  {path:'Experience', component: ExperienceComponent},
  {path: 'Skills', component: SkillsComponent},
  {path: 'Download', component: DownloadComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
