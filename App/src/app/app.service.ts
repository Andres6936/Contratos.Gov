import {inject, Injectable} from "@angular/core";
import {HttpClient} from "@angular/common/http";
import {Contract} from "./app.types";
import {Observable} from "rxjs";

@Injectable({
  providedIn: 'root'
})
export class AppService {
  private readonly httpService = inject(HttpClient)

  public getContracts(pageCount:number, pageSize: number): Observable<Contract[]> {
    return this.httpService.get<Contract[]>('http://127.0.0.1:8000/contracts', {
      params: {
        skip: pageCount,
        limit: pageSize,
      }
    })
  }
}

