import {Component, Input} from "@angular/core";
import type {Contract} from "../../../app/app.types";

@Component({
  selector: 'app-dates-contract',
  templateUrl: './dates-contract.component.html',
  standalone: true,
})
export class DatesContractComponent {
      @Input({required: true}) public contract!: Contract;
}
