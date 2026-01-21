import room
import event

weapon = 0
keys = []
fuel = 0

running = True

while running:
    dir = room.enter(room_name)
    room_name = room.move(room_name, room.rooms[room_name], dir)