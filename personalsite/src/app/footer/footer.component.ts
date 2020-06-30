import { Component, OnInit } from '@angular/core';
import { TranslationsService } from '../translations.service';

@Component({
  selector: 'app-footer',
  templateUrl: './footer.component.html',
  styleUrls: ['./footer.component.css']
})
export class FooterComponent implements OnInit {
  footer = {
  }

  constructor(private translations: TranslationsService) { }

  ngOnInit() {
    this.footer = this.getFooter();
  }

  getFooter(){
    return this.translations.getTranslations().footer;
  }
}
