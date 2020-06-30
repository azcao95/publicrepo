import { Component, OnInit } from '@angular/core';
import { TranslationsService} from '../translations.service';

@Component({
  selector: 'app-navigation',
  templateUrl: './navigation.component.html',
  styleUrls: ['./navigation.component.css']
})
export class NavigationComponent implements OnInit {

  navbar = {
  }

  constructor(private translations: TranslationsService) { }

  ngOnInit() {
    this.navbar = this.getNavBar();
  }

  getNavBar() {
    return this.translations.getTranslations().navigation;
  }

}
