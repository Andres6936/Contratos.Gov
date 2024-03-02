import {Component, Input} from "@angular/core";
import type {Contract} from "../../app/app.types";

@Component({
  selector: 'app-type-contract',
  templateUrl: 'type-contract.component.html',
  standalone: true
})
export class TypeContractComponent {
    @Input({required: true}) public contract!: Contract;
}
