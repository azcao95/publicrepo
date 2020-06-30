import { Component, OnInit } from '@angular/core';
import { TranslationsService } from '../translations.service';

@Component({
  selector: 'app-bio',
  templateUrl: './bio.component.html',
  styleUrls: ['./bio.component.css']
})
export class BioComponent implements OnInit {
  bio = {}
  
  constructor(private translations: TranslationsService) { }

  ngOnInit() {
    this.bio = this.getBio();
  }

  getBio() {
    return this.translations.getTranslations().bio;
  }
}
