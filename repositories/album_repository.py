from db.run_sql import run_sql

from models.album import Album
from repositories import artist_repository

def select(id):
    album = None
    sql = "SELECT * FROM albums WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    if result is not None:
        album = Album(result['artist'], result['title'], result['genre'], result['id'])
    return album


def select_all():
    albums = []
    sql = "SELECT * FROM albums"
    results = run_sql(sql)

    for row in results:
        artist_id = artist_repository.select(row['id'])
        album = Album(artist_id.name, row['title'], row['genre'], row['id'])
        albums.append(album)

    return albums

def save(album):
    sql = "INSERT INTO albums (artist, title, genre, artist_id) VALUES (%s, %s, %s, %s) RETURNING *"
    values = [album.artist.name, album.title, album.genre, album.artist.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    album.id = id
    return album

def delete_all():
    sql = "DELETE FROM albums"
    run_sql(sql)