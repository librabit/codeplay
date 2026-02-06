import event

rooms = {'room01':[1,0,0,0,0], 'room02':[1,1,0,0],
         'room03':[0,1,1,0,0],'room04':[1,0,0,1],
         'room05':[1,1,0,0],'room06':[1,1,1,1],
         'room07':[0,0,0,1],'room08':[0,0,1,1],
         'room09':[0,0,1,1],'room10':[0,1,1,0],
         'room11':[1,1,0,0],'room12':[0,1,0,0],
         'room13':[1,1,0,0],'room14':[0,1,0,1],
         'room15':[1,0,1,0],'room16':[1,1,0,1],
         'room17':[0,0,1,0],'room18':[0,0,0,0]}

room_name = "room01"
dir = 0
running = True

def enter(room_name):
    print(f"현재 위치 : {room_name}")
    print("어디로 가시겠습니까?")
    print("1. 오른쪽\n2. 왼쪽\n3. 뒤쪽\n4. 앞쪽")
    direction = int(input())

    return direction

def notice(txt):
    print(txt)

def move(room_name, walls, direction):
    nextRoom = room_name
    t = ""
    if room_name == "room01":
        if walls[direction - 1] == 1:
            nextRoom = 'room02'
            t = f"{nextRoom} 방으로 이동!"
        else:
            t = "이쪽은 막혀있다!"
             
    if room_name == "room02":
        if walls[direction - 1] == 1:
            if direction - 1 == 0:
                nextRoom = 'room03'
            elif direction - 1 == 1:
                nextRoom = 'room01'
            t = f"{nextRoom} 방으로 이동!"
        else:
            t = "이쪽은 막혀있다!"
    
    if room_name == "room03":
        if walls[direction - 1] == 1:
            if direction - 1 == 0:
                nextRoom = 'room02'
                t = f"{nextRoom} 방으로 이동!"
            elif direction - 1 == 2:
                nextRoom = 'room04'
                t = f"{nextRoom} 방으로 이동!"
        else:
            t = "이쪽은 막혀있다!"
    
    if room_name == "room04":
        if walls[direction - 1] == 1:
            if direction - 1 == 0:
                nextRoom = 'room05'

            elif direction - 1 == 3:
                nextRoom = 'room03'
            t = f"{nextRoom} 방으로 이동!"
        else:
            t = "이쪽은 막혀있다!"

    if room_name == "room05":
        if walls[direction - 1] == 1:
            if direction - 1 == 0:
                nextRoom = 'room06'
            elif direction - 1 == 1:
                nextRoom = 'room04'
            t = f"{nextRoom} 방으로 이동!"
        else:
            t = "이쪽은 막혀있다!"

    if room_name == "room06":
        if walls[direction - 1] == 1:
            if direction - 1 == 0:
                nextRoom = 'room13'
            elif direction - 1 == 1:
                nextRoom = 'room05'
            elif direction - 1 == 2:
                nextRoom = 'room07'
            elif direction - 1 == 3:
                nextRoom = 'room08'
            t = f"{nextRoom} 방으로 이동!"
        else:
            t = "이쪽은 막혀있다!"

    if room_name == "room07":
        if walls[direction - 1] == 1:
            nextRoom = 'room06'
            t = f"{nextRoom} 방으로 이동!"
        else:
            t = "이쪽은 막혀있다!"

    if room_name == "room08":
        if walls[direction - 1] == 1:
            if direction - 1 == 3:
                nextRoom = 'room09'
            elif direction - 1 == 2:
                nextRoom = 'room07'
            t = f"{nextRoom} 방으로 이동!"
        else:
            t = "이쪽은 막혀있다!"

    if room_name == "room09":
        if walls[direction - 1] == 1:
            if direction - 1 == 3:
                nextRoom = 'room10'
            elif direction - 1 == 2:
                nextRoom = 'room08'
            t = f"{nextRoom} 방으로 이동!"
        else:
            t = "이쪽은 막혀있다!"

    if room_name == "room10":
        if walls[direction - 1] == 1:
            if direction - 1 == 1:
                nextRoom = 'room11'
                t = f"{nextRoom} 방으로 이동!"
            elif direction - 1 == 2:
                nextRoom = 'room09'
                t = f"{nextRoom} 방으로 이동!"
        else:
            t = "이쪽은 막혀있다!"

    if room_name == "room11":
        if walls[direction - 1] == 1:
            if direction - 1 == 0:
                nextRoom = 'room10'
            elif direction - 1 == 1:
                nextRoom = 'room12'
            t = f"{nextRoom} 방으로 이동!"
        else:
            t = "이쪽은 막혀있다!"

    if room_name == "room12":
        if walls[direction - 1] == 1:
            nextRoom = 'room11'
            t = f"{nextRoom} 방으로 이동!"
        else:
            t = "이쪽은 막혀있다!"

    if room_name == "room13":
        if walls[direction - 1] == 1:
            if direction - 1 == 0:
                nextRoom = 'room14'
            elif direction - 1 == 1:
                nextRoom = 'room06'
            t = f"{nextRoom} 방으로 이동!"
        else:
            t = "이쪽은 막혀있다!"

    if room_name == "room14":
        if walls[direction - 1] == 1:
            if direction - 1 == 3:
                nextRoom = 'room15'
            elif direction - 1 == 1:
                nextRoom = 'room13'
            t = f"{nextRoom} 방으로 이동!"
        else:
            t = "이쪽은 막혀있다!"

    if room_name == "room15":
        if walls[direction - 1] == 1:
            if direction - 1 == 0:
                nextRoom = 'room16'
            elif direction - 1 == 2:
                nextRoom = 'room14'
            t = f"{nextRoom} 방으로 이동!"
        else:
            t = "이쪽은 막혀있다!"

    if room_name == "room16":
        if walls[direction - 1] == 1:
            if direction - 1 == 0:
                nextRoom = 'room18'
            elif direction - 1 == 1:
                nextRoom = 'room15'
            elif direction - 1 == 3:
                nextRoom = 'room17'
            t = f"{nextRoom} 방으로 이동!"
        else:
            t = "이쪽은 막혀있다!"

    if room_name == "room17":
        if walls[direction - 1] == 1:
            nextRoom = 'room16'
            t = f"{nextRoom} 방으로 이동!"
        else:
            t = "이쪽은 막혀있다!"

    if room_name == "room18":
        if walls[direction - 1] == 1:
            nextRoom = 'room17'
            t = f"{nextRoom} 방으로 이동!"
        else:
            t = "이쪽은 막혀있다!"

    notice(t)
    
    return nextRoom

# while running:
#     dir = enter(room_name)
#     room_name = move(room_name, rooms[room_name], dir)