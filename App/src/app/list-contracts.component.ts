import {Component, inject, OnInit} from "@angular/core";
import {DatesContractComponent} from "../components/contracts/dates-contract.component";
import {EntityContractComponent} from "../components/contracts/entity-contract.component";
import {ExternalResourcesContractComponent} from "../components/contracts/external-resources-contract.component";
import {InvestmentContractComponent} from "../components/contracts/investment-contract.component";
import {LegalRepresentativeContractComponent} from "../components/contracts/legal-representative-contract.component";
import {LocationContractComponent} from "../components/contracts/location-contract.component";
import {TypeContractComponent} from "../components/contracts/type-contract.component";
import {ValueContractComponent} from "../components/contracts/value-contract.component";
import type {Contract} from "./app.types";
import {AppService} from "./app.service";

@Component({
  selector: 'app-list-contracts',
  templateUrl: './list-contracts.component.html',
  standalone: true,
  imports: [
    DatesContractComponent,
    EntityContractComponent,
    ExternalResourcesContractComponent,
    InvestmentContractComponent,
    LegalRepresentativeContractComponent,
    LocationContractComponent,
    TypeContractComponent,
    ValueContractComponent
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
