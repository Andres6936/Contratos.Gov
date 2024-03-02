import {Component, Input} from "@angular/core";
import type {Contract} from "../../app/app.types";
import {CurrencyPipe} from "@angular/common";

@Component({
  selector: 'app-external-resources-contract',
  templateUrl: './external-resources-contract.component.html',
  standalone: true,
  imports: [
    CurrencyPipe
  ]
})
export class ExternalResourcesContractComponent {
  @Input({required: true}) public contract!: Contract;
}
