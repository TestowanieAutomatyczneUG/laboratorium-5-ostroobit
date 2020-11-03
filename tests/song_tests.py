import unittest
from src.song import Song

class SongTest(unittest.TestCase):
    def test_verse_1(self):
        self.assertEqual(Song.get_verse(1), "On the first day of Christmas my true love gave to me: a Partridge in a Pear Tree.")

    