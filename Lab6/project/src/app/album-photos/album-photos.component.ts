import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { AlbumsService } from '../albums.service';
import { Photo } from '../photo';

@Component({
  selector: 'app-album-photos',
  imports: [],
  templateUrl: './album-photos.component.html',
  styleUrl: './album-photos.component.css'
})
export class AlbumPhotosComponent implements OnInit{
  photos: any[] = [];
  albumId: number | undefined;

  constructor(
    private route: ActivatedRoute,
    private albumService: AlbumsService,
    private router: Router
  ) {}

  ngOnInit() {
    this.route.paramMap.subscribe(params => {
      this.albumId = Number(params.get('id'));
      this.getPhotos(this.albumId);
    })
  }

  getPhotos(id: number) {
    this.albumService.getAlbumPhotos(id).subscribe(photos => {
      this.photos = photos;
    });
  }

  goBack() {
    this.router.navigate(['/albums', this.albumId]);
  }
}
