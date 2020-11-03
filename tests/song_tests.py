import unittest
from src.song import Song


class SongTest(unittest.TestCase):

    def setUp(self):
        self.temp = Song()

    def test_verse_1(self):
        self.assertEqual(self.temp.get_verse(1), "On the first day of Christmas my true love gave to me: a Partridge in a Pear Tree.")

    def test_verse_2(self):
        self.assertEqual(self.temp.get_verse(2), "On the second day of Christmas my true love gave to me: two Turtle Doves, and a Partridge in a Pear Tree.")

    def test_verse_3(self):
        self.assertEqual(self.temp.get_verse(3), "On the third day of Christmas my true love gave to me: three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.")

    def test_verse_4(self):
        self.assertEqual(self.temp.get_verse(4), "On the fourth day of Christmas my true love gave to me: four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.")

    def test_verses_1_to_6(self):
        self.assertEqual(self.temp.get_verses(1, 6), [
            "On the first day of Christmas my true love gave to me: a Partridge in a Pear Tree.",
            "On the second day of Christmas my true love gave to me: two Turtle Doves, and a Partridge in a Pear Tree.",
            "On the third day of Christmas my true love gave to me: three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.",
            "On the fourth day of Christmas my true love gave to me: four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.",
            "On the fifth day of Christmas my true love gave to me: five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.",
            "On the sixth day of Christmas my true love gave to me: six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree."
        ])

    def tearDown(self):
        self.temp = None