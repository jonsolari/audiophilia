# STRUCTURE

# Player is an object, but only to have inventory & progression through the story

class Player:
    def __init__(self, prog, inv):
        self.prog = 0
        self.inv = []

# Progression attribute will increment as you go on, and this will dictate what's shown as a prompt

class Section: 
    def __init__(self, id, desc, opt):
        self.id = id
        self.desc = desc
        self.opt = []

while True:
    print("Welcome! Press Q to quit.")

    cmd = input("--->")

    if cmd == "q":
        break