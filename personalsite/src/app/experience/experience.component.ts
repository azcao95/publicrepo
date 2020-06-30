import { Component, OnInit } from '@angular/core';
import { TranslationsService } from '../translations.service';

@Component({
  selector: 'app-experience',
  templateUrl: './experience.component.html',
  styleUrls: ['./experience.component.css']
})
export class ExperienceComponent implements OnInit {
  experience = {}

  constructor(private translations: TranslationsService) { }

  ngOnInit() {
    this.experience = this.getExperience();
  }

  getExperience() {
    return this.translations.getTranslations().experience;
  }
}
