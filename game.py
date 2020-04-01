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
    def __init__(self, desc, opt, path):
        self.desc = desc
        self.opt = opt
        self.path = path

parts = {
    0: Section('You are in the dusty stacks of your favorite record store.', ['1) Dig in some crates'], [1]),
    1: Section('You\'ve narrowed it down to three titles.', ['1) ' + '\033[31m' + 'Aja by Steely Dan'+'\033[0m', '2) ' + '\033[32m'+'Moving Pictures by Rush' + '\033[0m', '3) ' + '\033[34m'+'Bitches Brew by Miles Davis'+'\033[0m',], [2, 3, 4]),
    2: Section('Nice, a classic. What pressing is it?', ['1) Let\'s check!'], [5]),
    3: Section('Nice, a classic. What pressing is it?', ['1) Let\'s check!'], [6]),
    4: Section('Nice, a classic. What pressing is it?', ['1) Let\'s check!'], [7]),
    5: Section('There\'s a thread on the Steve Hoffman forums with over \n650 posts in it, but you\'re not about to traipse through \nall that bullshit in full, on your smartphone, here at \nthe store. People seem pretty over the moon about an \noriginal pressing with \033[31mAB-1006\033[0m carved into the deadwax.', ['1) Check the deadwax.'], []),
    6: Section('\'The Rush Vinyl Pressing Thread\' on the Steve Hoffman \nforums says to check the deadwax to see if both sides \nhave an \'RL\' for Robert Ludwig. A lot of people are \narguing for various CD masterings too but you\'re not \nabout the digital life anymore, not since dropping well \nover $600 on a turntable cartridge alone.', ['1) Check the deadwax.'], [8]),
}

# PUT SOME STUFF OUT HERE

welcome = 'Welcome to AUDIOPHILIA, the game of hi-fi perfection. Please enter your name, or LOAD to load an existing game.'

print()
print()
print()
print()
print()
print()
print()
print()
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

print()
print(f'Welcome, {player.name}!')

while True:
    
    # MAKE SOME OF THIS FUNCTIONS

    current = player.prog
    
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    
    print(parts[current].desc)
    
    print()
    
    for i in parts[current].opt:
        print(i)
    
    print()

    cmd = input("-->")

    def choicehandler(choice):
        adjust = int(choice) -1
        optnum = len(parts[current].opt)
        if int(choice) <= optnum:
            if cmd == parts[current].opt[adjust][0]:
                player.prog = parts[current].path[adjust]
        else: 
            print(f'Please choose a selection between 1 and {optnum}.')

    if cmd == "q" or cmd == "Q":
        break

    choicehandler(cmd)

    # if player.prog == 1:
    #     if cmd == 1:
    #         player.prog = 2
    #     elif cmd == 2: 
    #         player.prog = 3
    #     elif cmd == 3:
    #         player.prog = 4
    # else:
    #     choicehandler(cmd)

    def choicehandler(choice):
        adjust = int(choice) -1
        if cmd == parts[current].opt[adjust][0]:
            player.prog = parts[current].path[adjust]
        else: 
            print('I didn\'t understand that.')

    




    # if current == 0:
    #     if cmd == "q" or cmd == "Q":
    #         break
    #     elif cmd == parts[current].opt[0][0]:
    #         player.prog = 1
    #     else: 
    #         print('I didn\'t understand that.')
            
    # elif current == 1:
    #     if cmd == "q" or cmd == "Q":
    #         break
        
    #         player.prog = 2
    #     else:
    #         print('I didn\'t understand that.')
    
    # elif current == 2:
    #     if cmd == "q" or cmd == "Q":
    #         break
    #     else:
    #         print('Yo')
        


    # if cmd == "q" or cmd == "Q":
    #     break
    # else: 
    #     print("I didn't understand that.")
    #     print()