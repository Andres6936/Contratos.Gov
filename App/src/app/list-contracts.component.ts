import {Component, inject, OnInit} from "@angular/core";
import type {Contract} from "./app.types";
import {AppService} from "./app.service";
import {ContractComponent} from "../components/contracts/contract.component";
import {ArrowLeftIcon} from "../components/icons/arrow-left.icon";

@Component({
  selector: 'app-list-contracts',
  templateUrl: './list-contracts.component.html',
  standalone: true,
  imports: [
    ContractComponent,
    ArrowLeftIcon
  ]
})
export class ListContractsComponent implements OnInit {
  private readonly appService = inject(AppService);

  private pageCount = 0;
  private pageSize = 10;
  public contracts: Contract[] = []

  ngOnInit(): void {
    this.appService.getContracts(this.pageCount, this.pageSize).then((items) => {
      this.contracts = items as Contract[]
    }).catch(error => {
      console.error(error)
    })
  }
}
