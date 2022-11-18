import unittest

from classes.room import Room
from classes.song import Song
from classes.guest import Guest

class TestRoom(unittest.TestCase):
    
    def setUp(self):
        self.room1 = Room("Room 1", 6)
        self.room2 = Room("Room 2", 8)
        self.room3 = Room("Room 3", 3)
        self.room4 = Room("Room 4", 4)
        self.guest1 = Guest("Barney")
        self.guest2 = Guest("Craig")
        self.guest3 = Guest("Steve")
        self.guest4 = Guest("Chris")
        self.guest5 = Guest("Natasha")
        self.guest6 = Guest("Mia")
        self.guest_list = [self.guest1, self.guest2, self.guest3]
        self.guest_list2 = [self.guest4, self.guest5, self.guest6]
        self.song1 = Song("Crazy", "Patsy Cline")
        self.song2 = Song("Song 2", "Blur")
        self.song3 = Song("The Fear", "Lily Allen")
        self.playlist = [self.song1, self.song2, self.song3]


    def test_room_has_room_id(self):
        self.assertEqual(self.room1.room_id, "Room 1")

    def test_room_has_capacity(self):
        self.assertEqual(self.room2.capacity, 8)

    def test_room_has_list_of_current_guests(self):
        self.assertEqual(self.room2.current_guests, [])

    def test_room_has_list_of_songs_available(self):
        self.assertEqual(self.room1.songs_available, [])

    def test_can_add_song_to_songs_available(self):
        song1 = Song("Replay", "Iyaz")
        self.room2.add_song(song1)
        self.assertEqual(self.room2.songs_available, [song1])

    def test_can_add_playlist_to_songs_available(self):
        input = len(self.playlist)
        self.room1.add_playlist(self.playlist)
        output = len(self.room1.songs_available)
        self.assertEqual(input, output)

    def test_can_populate_room(self):
        self.room1.populate_room(self.guest_list)
        self.assertEqual(self.room1.current_guests, [self.guest1, self.guest2, self.guest3])

    def test_can_add_individual_guest_to_room(self):
        self.room1.add_individual(self.guest2)
        self.assertEqual(self.room1.current_guests, [self.guest2])

    def test_can_empty_room(self):
        self.room1.populate_room(self.guest_list)
        self.room1.empty_room()
        self.assertEqual(self.room1.current_guests, [])

    def test_check_out_individual_guest(self):
        self.room1.populate_room(self.guest_list)
        self.room1.remove_guest(self.guest2)
        self.assertEqual(self.room1.current_guests, [self.guest1, self.guest3])

    def test_add_individual_when_room_at_capacity(self):
        self.room3.populate_room(self.guest_list)
        self.guest4 = Guest("Willie")
        output = self.room3.add_individual(self.guest4)
        self.assertEqual(output, "Sorry, we're at capacity right now")

    def test_add_group_when_no_available_capacity(self):
        self.room4.populate_room(self.guest_list)
        output = self.room4.populate_room(self.guest_list2)
        self.assertEqual(output, "Sorry, we're at capacity right now")

    def test_add_group_when_available_capacity(self):
        self.room2.populate_room(self.guest_list)
        self.room2.populate_room(self.guest_list2)
        self.assertEqual(self.room2.current_guests, 
        [self.guest1, self.guest2, self.guest3, self.guest4, self.guest5, self.guest6])

    
        



    

    
