import {Component, inject, OnInit} from '@angular/core';
import {CommonModule} from '@angular/common';
import {RouterOutlet} from '@angular/router';
import {AppService} from "./app.service";
import type {Contract} from "./app.types";
import {ValueContractComponent} from "../components/value-contract.component";
import {TypeContractComponent} from "../components/type-contract.component";
import {DatesContractComponent} from "../components/dates-contract.component";
import {ExternalResourcesContractComponent} from "../components/external-resources-contract.component";
import {LegalRepresentativeContractComponent} from "../components/legal-representative-contract.component";

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [CommonModule, RouterOutlet, ValueContractComponent, TypeContractComponent, DatesContractComponent, ExternalResourcesContractComponent, LegalRepresentativeContractComponent],
  templateUrl: './app.component.html',
})
export class AppComponent implements OnInit {
  private readonly appService = inject(AppService);
  public readonly title = 'App';

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
