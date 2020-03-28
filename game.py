# STRUCTURE

# Player is an object, but only to have inventory & progression through the story

class Player:
    def __init__(self, name, prog, inv):
        self.name = name
        self.prog = prog
        self.inv = inv

player = Player('', 0, [])
name = player.name

# Progression attribute will increment as you go on, and this will dictate what's shown as a prompt

class Section: 
    def __init__(self, desc, opt):
        self.desc = desc
        self.opt = opt

parts = {
    0: Section('Please enter your name (or Q to quit).', []),
    1: Section(f'Hello, {player.name}', ['1) Start your journey']),
    2: Section('You are in the dusty stacks of your favorite record store.', [1, 2, 3])
}



while True:
    
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
        else: 
            player.name = str(cmd)
            player.prog = 1
            
    elif current == 1:
        if cmd == "q" or cmd == "Q":
            break
        elif cmd == parts[current].opt[0][0]:
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