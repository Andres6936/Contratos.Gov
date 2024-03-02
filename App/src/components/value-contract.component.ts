import {Component, Input} from "@angular/core";
import type {Contract} from "../app/app.types";
import {CurrencyPipe} from "@angular/common";

@Component({
  selector: 'app-value-contract',
  standalone: true,
  imports: [
    CurrencyPipe
  ],
  templateUrl: './value-contract.component.html'
})
export class ValueContractComponent {
  @Input({required: true}) public contract!: Contract;
}
