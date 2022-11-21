from classes.guest import Guest
from classes.room import Room
from classes.song import Song

room1 = Room("Room 1", 10)

guest1 = Guest("Barney", 100.00, Song("Believe", "Cher"))
guest2 = Guest("Craig", 200.00, Song("Wichita Lineman", "Glen Campbell"))
guest3 = Guest("Steve", 175.00, Song("Seasons(Waiting on You", "Future Islands"))
guest_list = [guest1, guest2, guest3]

print(room1.current_guests)

room1.populate_room(guest_list)

for guest in room1.current_guests:
    print(guest.__str__())

