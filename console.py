import pdb
from models.album import Album
from models.artist import Artist
import repositories.artist_repository as artist_repository
import repositories.album_repository as album_repository

album_repository.delete_all()
artist_repository.delete_all()

artist_1 = Artist("Dir en Grey")
artist_repository.add_artist(artist_1)
artist_2 = Artist("Suede")
artist_repository.add_artist(artist_2)
artist_3 = Artist("Prince")
artist_repository.add_artist(artist_3)
artist_4 = Artist("Malice Mizer")
artist_repository.add_artist(artist_4)

artists = artist_repository.select_all()

for artist in artists:
    print(artist.__dict__)

# artist_3.rebrand('The Artist Formerly Known As Prince')
# artist_repository.update(artist_3)

# result_2 = artist_repository.select(3)

# print(result_2.__dict__)

album_1 = Album(artist_1, "Uroboros", "Metal",)
album_repository.save(album_1)
album_2 = Album(artist_3, "Purple Rain", "Funky Mother",)
album_repository.save(album_2)
album_3 = Album(artist_2, "Dog Man Star", "Rock",)
album_repository.save(album_3)
# album_4 = Album(artist_2, "Coming Up", "Rock",)
# album_repository.save(album_4)
# album_5 = Album(artist_2, "Head Music", "Rock",)
# album_repository.save(album_5)
# album_6 = Album(artist_2, "The Blue Hour", "Rock",)
# album_repository.save(album_6)
# album_7 = Album(artist_1, "Gauze", "Rock",)
# album_repository.save(album_7)
# album_8 = Album(artist_1, "The Insulated World", "Rock",)
# album_repository.save(album_8)
# album_9 = Album(artist_1, "Dum Spiro Spero", "Rock",)
# album_repository.save(album_9)
album_10 = Album(artist_4, "Bara no Seidou", "Metal",)
album_repository.save(album_10)


albums = album_repository.select_all()

for album in albums:
    print(album.__dict__)

album_repository.delete_all()
artist_repository.delete_all()

updated_artist = artist_repository.select_all()
updated_album = album_repository.select_all()

for artist in updated_artist:
    print(artist.__dict__)

for album in updated_album:
    print(album.__dict__)

pdb.set_trace()
