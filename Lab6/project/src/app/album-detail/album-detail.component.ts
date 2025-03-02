import { Component } from '@angular/core';
import { AlbumsService } from '../albums.service';
import {ActivatedRoute, Router} from "@angular/router";
import { Album } from '../album';
import { ALBUMS } from '../db';

@Component({
  selector: 'app-album-detail',
  imports: [],
  templateUrl: './album-detail.component.html',
  styleUrl: './album-detail.component.css'
})
export class AlbumDetailComponent {
  album: Album | undefined;

  constructor(private albumService: AlbumsService,
    private route: ActivatedRoute,
    private router: Router) {}

  ngOnInit() {
    this.route.paramMap.subscribe((params) => {
      let id = Number(params.get('id'));
      this.getAlbum(id);
    })
  }

  getAlbum(id: number) {
    this.albumService.getAlbum(id).subscribe((album) => {
      this.album = album;
    })
  }

  saveAlbum() {
    if(this.album) {
      this.albumService.updateAlbum(this.album.id, this.album.title).subscribe();
    }
  }

  goToPhotos() {
    if(this.album) {
      this.router.navigate([`/albums/${this.album.id}/photos`]);
    }
  }

  goBack() {
    this.router.navigate(['/albums']);
  }
}
