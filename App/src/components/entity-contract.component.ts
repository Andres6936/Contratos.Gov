import {Component, Input} from "@angular/core";
import type {Contract} from "../app/app.types";

@Component({
  selector: 'app-entity-contract',
  templateUrl: './entity-contract.component.html',
  standalone: true,
})
export class EntityContractComponent {
     @Input({required: true}) public contract!: Contract;
}
