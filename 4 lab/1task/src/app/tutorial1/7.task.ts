import {Component} from '@angular/core';

@Component({
  selector: 'app-root',
  template: `
    <section (mouseover)="onMouseOver()">
  `,
})
export class AppComponent {
  message = '';

  onMouseOver() {
    this.message = 'Way to go 🚀';
  }
}
