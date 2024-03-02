import {Component, Input} from "@angular/core";
import type {Contract} from "../../../app/app.types";

@Component({
  selector: 'app-provider-contract',
  templateUrl: './provider-contract.component.html',
  standalone: true
})
export class ProviderContractComponent {
      @Input({required: true}) public contract!: Contract;
}
