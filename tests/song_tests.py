import unittest
from src.song import Song


class SongTest(unittest.TestCase):
    def setUp(self):
        self.temp = Song()

    def test_verse_1(self):
        self.assertEqual(self.temp.get_verse(1), "On the first day of Christmas my true love gave to me: a Partridge in a Pear Tree.")


    def tearDown(self):
        self.temp = None