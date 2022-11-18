class Room:
    
    def __init__(self, room_id, capacity):
        self.room_id = room_id
        self.capacity = capacity
        self.current_guests = []
        self.songs_available = []
    
    def add_songs(self, song):
        self.songs_available.append(song)

    def populate_room(self, guest):
        self.current_guests.append(guest)

    def empty_room(self):
        self.current_guests.clear()

    def remove_guest(self, guest):
        self.current_guests.remove(guest)

