import { Component, Input, Output, EventEmitter } from '@angular/core';
import { Product } from '../product';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-product-item',
  imports: [CommonModule],
  templateUrl: './product-item.component.html',
  styleUrl: './product-item.component.css',
  standalone: true
})
export class ProductItemComponent {
  @Input() product!: Product;
  @Output() remove: EventEmitter<number> = new EventEmitter<number>();

  likeProduct() {
    this.product.likes++;
  }

  shareOnWhatsApp() {
    const whatsappUrl = `https://wa.me/?text=${encodeURIComponent(this.product.link)}`;
    window.open(whatsappUrl, '_blank');
  }

  shareOnTelegram() {
    const telegramUrl = `https://t.me/share/url?url=${encodeURIComponent(this.product.link)}`;
    window.open(telegramUrl, '_blank');
  }

  removeProduct() {
    this.remove.emit(this.product.id);
  }
}
