from classes.guest import Guest
from classes.song import Song

class Room:
    
    def __init__(self, room_id, capacity):
        self.room_id = room_id
        self.capacity = capacity
        self.current_guests = []
        self.songs_available = []
        self.entry_fee = 11.00

    def check_favourite_song(self):
        for guest in self.current_guests:
            if guest.favourite_song in self.songs_available:
                return guest.cheer()
    
    def add_song(self, song):
        self.songs_available.append(song)

    def add_playlist(self, songs):
        self.songs_available.extend(songs)

    def populate_room(self, guests):
        total_wallet = 0

        for guest in guests:
            total_wallet += guest.wallet

        group_entry_fee = (len(guests)*self.entry_fee)
        if total_wallet < group_entry_fee:
            return f'Sorry, you need {group_entry_fee - total_wallet} to come in'

        if len(self.current_guests) + len(guests) <= self.capacity:
            self.current_guests.extend(guests)
            return self.check_favourite_song()
        else:
            return "Sorry, we're at capacity right now"

    def add_individual(self, guest):
        if guest.wallet < self.entry_fee:
            return "Sorry, the entry fee is ELEVEN pounds"
        if len(self.current_guests) < self.capacity:
            self.current_guests.append(guest) 
            guest.wallet -= self.entry_fee
            return self.check_favourite_song()  
        else:
            return "Sorry, we're at capacity right now"  

    def empty_room(self):
        self.current_guests.clear()

    def remove_guest(self, guest):
        self.current_guests.remove(guest)




