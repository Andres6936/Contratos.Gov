import {Component} from "@angular/core";
import {ArrowLeftIcon} from "../icons/arrow-left.icon";
import {ArrowRightIcon} from "../icons/arrow-right.icon";

@Component({
  selector: 'app-pagination',
  templateUrl: './pagination.component.html',
  imports: [
    ArrowLeftIcon,
    ArrowRightIcon
  ],
  standalone: true
})
export class PaginationComponent {

}
