import {Component, Input} from "@angular/core";
import type {Contract} from "../app/app.types";


@Component({
  selector: 'app-investment-contract',
  templateUrl: './investment-contract.component.html',
  standalone: true,
})
export class InvestmentContractComponent {
   @Input({required: true}) public contract!: Contract;
}
