import unittest

from classes.song import Song

class TestSong(unittest.TestCase):
    
    def setUp(self):
        self.song1 = Song("Crazy", "Patsy Cline")
        self.song2 = Song("Crazy", "Gnarls Barkley")
        self.song3 = Song("The Fear", "Lily Allen")
        self.song4 = Song("Smile", "Lily Allen")

    def test_song_has_name(self):
        self.assertEqual(self.song1.name, "Crazy")

    def test_song_has_artist(self):
        self.assertEqual(self.song2.artist, "Gnarls Barkley")