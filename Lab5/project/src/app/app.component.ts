import { Component } from '@angular/core';
import { Product } from './product';
import { Category } from './category';
import { CommonModule } from '@angular/common';
import { ProductListComponent } from './product-list/product-list.component';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrl: './app.component.css',
  imports: [CommonModule, ProductListComponent],
  standalone: true
})
export class AppComponent {
  categories: Category[] = [
    {
      name: 'Smartphones',
      products: [
        {
          id: 1,
          name: 'Apple iPhone 13',
          image: 'Assets/phone1.jpg',
          description: '128Gb черный IOS 15 4G Lightning',
          rating: 4.9,
          link: 'https://kaspi.kz/shop/p/apple-iphone-13-128gb-chernyi-102298404/?c=750000000',
          likes: 0
        },
        {
          id: 2,
          name: 'Apple iPhone 16 Pro Max',
          image: 'Assets/phone2.jpg',
          description: '256Gb черный IOS 18 4G USB Type-C',
          rating: 5.0,
          link: 'https://kaspi.kz/shop/p/apple-iphone-16-pro-max-256gb-chernyi-123787551/?c=750000000',
          likes: 0
        },
        {
          id: 3,
          name: 'Apple iPhone 16 Pro Max',
          image: 'Assets/phone3.jpg',
          description: '256Gb золотистый IOS 18 4G USB Type-C',
          rating: 4.8,
          link: 'https://kaspi.kz/shop/p/apple-iphone-16-pro-max-256gb-zolotistyi-123890547/?c=750000000',
          likes: 0
        },
        {
          id: 4,
          name: 'Apple iPhone 16 128Gb',
          image: 'Assets/phone4.jpg',
          description: '128Gb черный IOS 18 4G USB Type-C',
          rating: 4.9,
          link: 'https://kaspi.kz/shop/p/apple-iphone-16-128gb-chernyi-123713453/?c=750000000',
          likes: 0
        },
        {
          id: 5,
          name: 'Apple iPhone 16 Pro Max',
          image: 'Assets/phone5.jpg',
          description: '256Gb серебристый IOS 18 4G USB Type-C',
          rating: 5.0,
          link: 'https://kaspi.kz/shop/p/apple-iphone-13-128gb-chernyi-102298404/?c=750000000',
          likes: 0
        }
      ]
    },
    {
      name: 'Laptops',
      products: [
        {
          id: 6,
          name: 'Apple MacBook Air 13',
          image: 'Assets/laptop1.jpg',
          description: '2022 13.6" / 8 Гб / SSD 256 Гб / macOS / MLXW3 / серый',
          rating: 4.7,
          link: 'https://kaspi.kz/shop/p/apple-macbook-air-13-2022-13-6-8-gb-ssd-256-gb-macos-mlxw3-105933794/?c=750000000',
          likes: 0
        },
        {
          id: 7,
          name: 'Apple MacBook Air 13',
          image: 'Assets/laptop2.jpg',
          description: '2022 13.6" / 8 Гб / SSD 256 Гб / macOS / MLY33 / черный',
          rating: 4.9,
          link: 'https://kaspi.kz/shop/p/apple-macbook-air-13-2022-13-6-8-gb-ssd-256-gb-macos-mly33-105933768/?c=750000000',
          likes: 0
        },
        {
          id: 8,
          name: 'Apple MacBook Pro 14',
          image: 'Assets/laptop3.jpg',
          description: '2024 / 24 Гб / SSD 512 Гб / macOS / MX2H3 / черный',
          rating: 5.0,
          link: 'https://kaspi.kz/shop/p/apple-macbook-pro-14-2024-24-gb-ssd-512-gb-macos-mx2h3-132140624/?c=750000000',
          likes: 0
        },
        {
          id: 9,
          name: 'Apple MacBook Air 13',
          image: 'Assets/laptop4.jpg',
          description: '2022 13.6" / 8 Гб / SSD 256 Гб / macOS / MLY13 / золотистый',
          rating: 5.0,
          link: 'https://kaspi.kz/shop/p/apple-macbook-air-13-2022-13-6-8-gb-ssd-256-gb-macos-mly13-105933751/?c=750000000',
          likes: 0
        },
        {
          id: 10,
          name: 'Apple MacBook Air 13',
          image: 'Assets/laptop5.jpg',
          description: '2020 13.3" / 8 Гб / SSD 256 Гб / macOS / MGND3 / золотистый',
          rating: 5.0,
          link: 'https://kaspi.kz/shop/p/apple-macbook-air-13-2020-13-3-8-gb-ssd-256-gb-macos-mgnd3-100797576/?c=750000000',
          likes: 0
        }
      ]
    },
    {
      name: 'Television',
      products: [
        {
          id: 11,
          name: 'LG 50UQ76003LD',
          image: 'Assets/tv1.jpg',
          description: '127 см черный Smart Wi-Fi Россия 50.0 дюйм',
          rating: 4.9,
          link: 'https://kaspi.kz/shop/p/lg-50uq76003ld-127-sm-chernyi-105054596/?c=750000000',
          likes: 0
        },
        {
          id: 12,
          name: 'LG 43UN71006LB',
          image: 'Assets/tv2.jpg',
          description: '109 см черный Smart Wi-Fi 43.0 дюйм',
          rating: 4.7,
          link: 'https://kaspi.kz/shop/p/lg-43un71006lb-109-sm-chernyi-100331551/?c=750000000',
          likes: 0
        },
        {
          id: 13,
          name: 'Samsung UE43T5300AUXCE',
          image: 'Assets/tv3.jpg',
          description: '109 см черный Smart Wi-Fi 43.0 дюйм',
          rating: 4.8,
          link: 'https://kaspi.kz/shop/p/samsung-ue43t5300auxce-109-sm-chernyi-100182013/?c=750000000',
          likes: 0
        },
        {
          id: 14,
          name: 'Samsung UE65AU7100UXCE',
          image: 'Assets/tv4.jpg',
          description: '165 см черный Smart Wi-Fi 65.0  дюйм',
          rating: 4.6,
          link: 'https://kaspi.kz/shop/p/samsung-ue65au7100uxce-165-sm-chernyi-101475922/?c=750000000',
          likes: 0
        },
        {
          id: 15,
          name: 'LG 50UQ80006LB',
          image: 'Assets/tv5.jpg',
          description: '127 см черный Smart Wi-Fi Индонезия 50.0 дюйм',
          rating: 4.9,
          link: 'https://kaspi.kz/shop/p/lg-50uq76003ld-127-sm-chernyi-105054596/?c=750000000',
          likes: 0
        }
      ]
    },
    {
      name: 'Headphones',
      products: [
        {
          id: 16,
          name: 'Apple AirPods 3',
          image: 'Assets/air1.jpg',
          description: 'Lightning Charging Case белый беспроводное',
          rating: 4.9,
          link: 'https://kaspi.kz/shop/p/apple-airpods-3-with-lightning-charging-case-belyi-106667987/?c=750000000',
          likes: 0
        },
        {
          id: 17,
          name: 'Apple AirPods Pro 2',
          image: 'Assets/air1.jpg',
          description: 'Type-C/Wireless Charging белый регулятор громкости',
          rating: 5.0,
          link: 'https://kaspi.kz/shop/p/apple-airpods-pro-2-with-type-c-wireless-charging-belyi-113677582/?c=750000000',
          likes: 0
        },
        {
          id: 18,
          name: 'Apple AirPods 4 ',
          image: 'Assets/air3.jpg',
          description: 'Active Noise Cancellation белый USB Type-C',
          rating: 4.7,
          link: 'https://kaspi.kz/shop/p/apple-airpods-4-active-noise-cancellation-belyi-124333921/?c=750000000',
          likes: 0
        },
        {
          id: 19,
          name: 'Apple AirPods 4',
          image: 'Assets/air4.jpg',
          description: 'Active Noise Cancellation белый USB Type-C',
          rating: 4.9,
          link: 'https://kaspi.kz/shop/p/apple-airpods-4-belyi-124333372/?c=750000000',
          likes: 0
        },
        {
          id: 20,
          name: 'Apple AirPods 3',
          image: 'Assets/air5.jpg',
          description: 'Lightning/Wireless Charging белый',
          rating: 4.7,
          link: 'https://kaspi.kz/shop/p/apple-airpods-3-with-lightning-wireless-charging-belyi-102667744/?c=750000000',
          likes: 0
        }
      ]
    }
  ];

  selectedCategory: Category | null = null;

  selectCategory(category: Category) {
    this.selectedCategory = category;
  }
}
