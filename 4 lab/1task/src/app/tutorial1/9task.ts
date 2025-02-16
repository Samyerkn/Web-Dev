import {Component, Output, EventEmitter} from '@angular/core';

@Component({
  selector: 'app-child',
  styles: `.btn { padding: 5px; }`,
  template: `
    <app-child (addItemEvent)="addItem($event)" />
  `,
})
export class ChildComponent {
  @Output() addItemEvent = new EventEmitter<string>();
  addItem() {
  this.addItemEvent.emit('🐢');
  }
}
