import { Component, OnInit } from '@angular/core';
import { TranslationsService} from '../translations.service';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit {

  home = {
  }

  constructor(private translations: TranslationsService) { }

  ngOnInit() {
    this.home = this.getHome();
  }

  getHome() {
    return this.translations.getTranslations().home;
  }
}
