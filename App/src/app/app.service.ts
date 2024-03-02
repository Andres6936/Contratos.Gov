import {Injectable} from "@angular/core";
import {createTRPCClient, httpBatchLink} from '@trpc/client';
import {AppRouter} from "xserver";


@Injectable({
  providedIn: 'root'
})
export class AppService {
  private readonly trcp;

  constructor() {
    this.trcp = createTRPCClient<AppRouter>({
      links: [
        httpBatchLink({
          url: 'http://127.0.0.1:8000',
        })
      ]
    });
  }


  public async getContracts(pageCount:number, pageSize: number) {
    return await this.trcp.contractList.query({
      PageSize: pageSize,
      PageCount: pageCount,
    });
  }
}

