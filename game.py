# STRUCTURE

# Player is an object, but only to have inventory & progression through the story

# Progression attribute will increment as you go on, and this will dictate what's shown as a prompt

class Player:
    def __init__(self, prog):
        self.prog = 0