import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Album } from './album';
import { Photo } from './photo';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})

export class AlbumsService {

  constructor(private client: HttpClient) {

  }

  getAlbums(): Observable<Album[]> {
    return this.client.get<Album[]>('https://jsonplaceholder.typicode.com/albums');
  }

  getAlbum(id: number): Observable<Album> {
    return this.client.get<Album>(`https://jsonplaceholder.typicode.com/albums/${id}`);
  }

  updateAlbum(id: number, title: string): Observable<Album> {
    return this.client.put<Album>(`https://jsonplaceholder.typicode.com/albums/${id}`, {title})
  }

  addAlbum(album: Album): Observable<Album> {
    return this.client.post<Album>('https://jsonplaceholder.typicode.com/albums/add', album);
  }

  deleteAlbum(id: number): Observable<void> {
    return this.client.delete<void>(`https://jsonplaceholder.typicode.com/albums/${id}`);
  }

  getAlbumPhotos(id: number): Observable<Photo[]> {
    return this.client.get<Photo[]>(`https://jsonplaceholder.typicode.com/albums/${id}/photos`);
  }
}
