import unittest

from classes.room import Room
from classes.song import Song
from classes.guest import Guest

class TestRoom(unittest.TestCase):
    
    def setUp(self):
        self.room1 = Room("Room 1", 6)
        self.room2 = Room("Room 2", 8)
        self.guest1 = Guest("Barney")
        self.guest2 = Guest("Craig")
        self.guest3 = Guest("Steve")
        self.guest_list = [(self.guest1), (self.guest2), (self.guest3)]

    def test_room_has_room_id(self):
        self.assertEqual(self.room1.room_id, "Room 1")

    def test_room_has_capacity(self):
        self.assertEqual(self.room2.capacity, 8)

    def test_room_has_list_of_current_guests(self):
        self.assertEqual(self.room2.current_guests, [])

    def test_room_has_list_of_songs_available(self):
        self.assertEqual(self.room1.songs_available, [])

    def test_can_add_songs_to_songs_available(self):
        song1 = Song("Replay", "Iyaz")
        self.room2.add_songs(song1)
        self.assertEqual(self.room2.songs_available, [song1])

    def test_can_populate_room(self):
        self.room1.populate_room(self.guest_list)
        self.assertEqual(self.room1.current_guests, [self.guest_list])

    def test_can_empty_room(self):
        self.room1.populate_room(self.guest_list)
        self.room1.empty_room()
        self.assertEqual(self.room1.current_guests, [])

    def test_check_out_individual_guest(self):
        self.room1.populate_room(self.guest_list)
        self.room1.remove_guest(self.guest2)
        self.assertEqual(self.room1.current_guests, [(self.guest1), (self.guest3)])
