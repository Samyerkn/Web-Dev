import { Component, Input } from '@angular/core';
import { Product } from '../product';
import { CommonModule } from '@angular/common';
import { ProductItemComponent } from '../product-item/product-item.component';

@Component({
  selector: 'app-product-list',
  templateUrl: './product-list.component.html',
  styleUrl: './product-list.component.css',
  standalone: true,
  imports: [CommonModule, ProductItemComponent]
})
export class ProductListComponent {
  @Input() products: Product[] = [];

  onRemoveProduct(productId: number) {
    this.products = this.products.filter(product => product.id !== productId);
  }
}
