from django.test import TestCase
from app.models import Music


# Create your tests here.
class TestGame_test_cases(TestCase):
    def test_song_maker(self):
        music = Music.make_song("9 to 5", "Dolly Parton")
        
        self.assertEqual(music.name, "9 to 5" ,"Dolly Parton")

    def test_read_all_games(self):
        music = Music.make_song("9 to 5", "Dolly Parton")

        musics = Music.read_all_songs()
        name = [Music.name for m in musics]
        self.assertEqual(len(name), 1)

    def test_delete_music(self):
        music = Music.make_song("9 to 5", "Dolly Parton")
        musics = Music.delete_music(music)
        self.assertEqual(len(musics), 0)

    def test_update_game(self):
        music = Music.make_song("9 to 5", "Dolly Parton")
        music = Music.update_song("9 to 5", "Took her to the O", "Dolly Parton", "King Von")

        self.assertEqual(music.name, "Took her to the O", "King Von")

    def test_read_by_title(self):
        music = Music.make_song("9 to 5", "Dolly Parton")
        musics= Music.read_by_title(music.name)
        self.assertEqual(musics.name, "9 to 5")

    def test_filtered_search(self):
        music = Music.make_song("9 to 5", "Dolly Parton")
        musics=Music.read_filter(music.artist)
        self.assertEqual(musics[0].artist, "Dolly Parton")
