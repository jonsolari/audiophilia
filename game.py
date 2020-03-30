# STRUCTURE

# Player is an object, but only to have inventory & progression through the story

class Player:
    def __init__(self, name, prog, inv):
        self.name = name
        self.prog = prog
        self.inv = inv

    def __str__(self):
        return f'{self.name}, {self.prog}, {self.inv}'

player = Player('', 0, [])
name = player.name

# Progression attribute will increment as you go on, and this will dictate what's shown as a prompt

class Section: 
    def __init__(self, desc, opt):
        self.desc = desc
        self.opt = opt

parts = {
    0: Section('You are in the dusty stacks of your favorite record store.', ['1) Dig in some crates']),
    1: Section('You\'ve narrowed it down to three titles.', ['1) Aja by Steely Dan', '2) Moving Pictures by Rush', '3) Bitches Brew by Miles Davis'])
}

# PUT SOME STUFF OUT HERE

welcome = 'Welcome to AUDIOPHILIA, the game of hi-fi perfection. Please enter your name, or LOAD to load an existing game.'

print(welcome)

intro = input('-->')

while player.name == '':
    if intro == "LOAD":
        print('Feature TK')
        print()
        print(welcome)
        intro = input('-->')
    else:
        player.name = intro

print(f'Welcome, {player.name}!')

while True:
    
    # MAKE SOME OF THIS FUNCTIONS

    current = player.prog
    
    print()
    
    print(parts[current].desc)
    
    print()
    
    for i in parts[current].opt:
        print(i)
    
    print()

    cmd = input("-->")

    if current == 0:
        if cmd == "q" or cmd == "Q":
            break
        elif cmd == parts[current].opt[0][0]:
            player.prog = 1
        else: 
            print('I didn\'t understand that.')
            
    elif current == 1:
        if cmd == "q" or cmd == "Q":
            break
        
            player.prog = 2
        else:
            print('I didn\'t understand that.')
    
    elif current == 2:
        if cmd == "q" or cmd == "Q":
            break
        else:
            print('Yo')
        


    # if cmd == "q" or cmd == "Q":
    #     break
    # else: 
    #     print("I didn't understand that.")
    #     print()