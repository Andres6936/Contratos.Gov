import {Component, Input} from "@angular/core";
import type {Contract} from "../app/app.types";

@Component({
  selector: 'app-value-contract',
  standalone: true,
  templateUrl: './value-contract.component.html'
})
export class ValueContractComponent {
  @Input({required: true}) public contract!: Contract;
}
