import { Injectable } from '@angular/core';
import { translations } from './translations'

@Injectable({
  providedIn: 'root'
})

export class TranslationsService {

  tlns = translations;

  constructor() { }

  getTranslations() {
    return this.tlns;
  }
}
