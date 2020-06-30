import { Injectable } from "@angular/core";
import { HttpClient } from "@angular/common/http";
import { Observable, throwError } from "rxjs";
import { catchError, retry } from "rxjs/operators";

@Injectable({
  providedIn: "root",
})
export class RpsService {
  constructor(private http: HttpClient) {}

  url = "http://localhost:3000/api/match";

  getResponse(myChoice: String) {
    return this.http.post(
      `${this.url}`,
      { choice: myChoice },
      { observe: "response" }
    );
  }
}
