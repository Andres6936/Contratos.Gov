import {Component, Input} from "@angular/core";
import type {Contract} from "../../app/app.types";

@Component({
  selector: 'app-location-contract',
  templateUrl: './location-contract.component.html',
  standalone: true,
})
export class LocationContractComponent {
    @Input({required: true}) public contract!: Contract;
}
