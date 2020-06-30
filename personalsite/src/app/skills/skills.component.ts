import { Component, OnInit } from '@angular/core';
import { TranslationsService } from '../translations.service';

@Component({
  selector: 'app-skills',
  templateUrl: './skills.component.html',
  styleUrls: ['./skills.component.css']
})
export class SkillsComponent implements OnInit {

  skills = {

  }

  constructor(private translations: TranslationsService) { }

  ngOnInit() {
    this.skills = this.getSkills();
  }

  getSkills() {
    return this.translations.getTranslations().skills;
  }
}
