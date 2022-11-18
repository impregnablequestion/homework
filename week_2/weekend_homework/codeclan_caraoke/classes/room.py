class Room:
    
    def __init__(self, room_id, capacity):
        self.room_id = room_id
        self.capacity = capacity
        self.current_guests = []
        self.songs_available = []
    
    def add_song(self, song):
        self.songs_available.append(song)

    def add_playlist(self, songs):
        self.songs_available.extend(songs)

    def populate_room(self, guests):
        if len(self.current_guests) + len(guests) <= self.capacity:
            self.current_guests.extend(guests)
        else:
            return "Sorry, we're at capacity right now"

    def add_individual(self, guest):
        if len(self.current_guests) < self.capacity:
            self.current_guests.append(guest)   
        else:
            return "Sorry, we're at capacity right now"  

    def empty_room(self):
        self.current_guests.clear()

    def remove_guest(self, guest):
        self.current_guests.remove(guest)
