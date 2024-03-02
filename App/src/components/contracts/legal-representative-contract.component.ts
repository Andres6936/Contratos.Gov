import {Component, Input} from "@angular/core";
import type {Contract} from "../../app/app.types";

@Component({
  selector: 'app-legal-representative-contract',
  templateUrl: './legal-representative-contract.component.html',
  standalone: true,
})
export class LegalRepresentativeContractComponent {
    @Input({required: true}) public contract!: Contract;
}
