import { Component, OnInit } from '@angular/core';
import { TranslationsService } from '../translations.service';

@Component({
  selector: 'app-download',
  templateUrl: './download.component.html',
  styleUrls: ['./download.component.css']
})
export class DownloadComponent implements OnInit {

  download = {
  }

  constructor(private translations: TranslationsService) { }

  ngOnInit() {
    this.download = this.getDownload();
  }

  getDownload() {
    return this.translations.getTranslations().download;
  }
}
