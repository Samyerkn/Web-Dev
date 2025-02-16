import {Component, inject} from '@angular/core';
import {CarService} from './car.service';

@Component({
  selector: 'app-root',
  template: `<p>Car Listing: {{ display }}</p>`,
})
class CarService {
  carService = inject(CarService);
}

export class AppComponent {
  display = '';

  constructor() {
    this.display = this.carService.getCars().join(' ⭐️ ');
  }
}
