# STRUCTURE

# Player is an object, but only to have inventory & progression through the story

class Player:
    def __init__(self, name, prog, inv):
        self.name = name
        self.prog = 0
        self.inv = []

player = Player("", 0, [])

# Progression attribute will increment as you go on, and this will dictate what's shown as a prompt

class Section: 
    def __init__(self, id, desc, opt):
        self.id = id
        self.desc = desc
        self.opt = []

parts = {
    0: Section(0, "Please enter your name (or Q to quit).", []),
    1: Section(1, f"Hello, {player.name}!", [])
}



while True:
    current = player.prog
    
    print(parts[current].desc)

    cmd = input("-->")

    if current == 0:
        if cmd == "q" or cmd == "Q":
            break
        else: 
            player.name = cmd
            # print(player.name)
            player.prog = 1
            # print(player.prog)
    elif current == 1:
        if cmd == "q" or cmd == "Q":
            break


    # if cmd == "q" or cmd == "Q":
    #     break
    # else: 
    #     print("I didn't understand that.")
    #     print()