import os
import genius
import poet

g = genius.Genius()
artists = ['Bob Dylan', 'Tim Buckley', 'The Beatles']
text = g.get_artists_lyrics(artists, songs_per_artist=15)

p = poet.Poet()
p.train_on(text, n_epochs=30)
poem = p.generate(u'Hey ', n_gen_chars=2000)
print(poem)