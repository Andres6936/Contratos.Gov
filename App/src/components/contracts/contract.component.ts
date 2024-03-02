import {Component, Input} from "@angular/core";
import type {Contract} from "../../app/app.types";
import {EntityContractComponent} from "./widgets/entity-contract.component";
import {LocationContractComponent} from "./widgets/location-contract.component";
import {InvestmentContractComponent} from "./widgets/investment-contract.component";
import {DatesContractComponent} from "./widgets/dates-contract.component";
import {TypeContractComponent} from "./widgets/type-contract.component";
import {ValueContractComponent} from "./widgets/value-contract.component";
import {LegalRepresentativeContractComponent} from "./widgets/legal-representative-contract.component";
import {ExternalResourcesContractComponent} from "./widgets/external-resources-contract.component";
import {ProviderContractComponent} from "./widgets/provider-contract.component";

@Component({
  selector: 'app-contract',
  templateUrl: './contract.component.html',
  standalone: true,
  imports: [
    EntityContractComponent,
    LocationContractComponent,
    InvestmentContractComponent,
    DatesContractComponent,
    TypeContractComponent,
    ValueContractComponent,
    LegalRepresentativeContractComponent,
    ExternalResourcesContractComponent,
    ProviderContractComponent
  ]
})
export class ContractComponent {
   @Input({required: true}) public contract!: Contract;
}
