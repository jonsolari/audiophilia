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
    1: Section('You\'ve narrowed it down to three titles.', ['1) ' + '\033[31m' + 'Aja by Steely Dan'+'\033[0m', '2) ' + '\033[32m'+'Moving Pictures by Rush' + '\033[0m', '3) ' + '\033[34m'+'The Lamb Lies Down on Broadway by Genesis'+'\033[0m',], [2, 3, 4]),
    2: Section('Nice, a classic. What pressing is it?', ['1) Let\'s check!'], [5]),
    3: Section('Nice, a classic. What pressing is it?', ['1) Let\'s check!'], [6]),
    4: Section('Nice, a classic. What pressing is it?', ['1) Let\'s check!'], [7]),
    5: Section('There\'s a thread on the Steve Hoffman forums with over \n650 posts in it, but you\'re not about to traipse through \nall that bullshit in full, on your smartphone, here at \nthe store. People seem pretty over the moon about an \noriginal pressing with \033[31mAB-1006\033[0m carved into the deadwax.', ['1) Check the deadwax.'], [8]),
    6: Section('\'The Rush Vinyl Pressing Thread\' on the Steve Hoffman \nforums says to check the deadwax to see if both sides \nhave an \033[32m\'RL\'\033[0m (for \033[32mRobert Ludwig\033[0m). A lot of people are \narguing for various CD masterings too but you\'re not \nabout the digital life anymore, not since dropping well \nover $600 on a turntable cartridge alone.', ['1) Check the deadwax.'], [9]),
    7: Section('You discreetly (you think) pull out your phone and see \nwhat people are saying about it on the Steve Hoffman \nforums. They all seem to be fawning over the \033[34m200g \nClassic Records reissue\033[0m from 2001. Weird time for vinyl, \nyou almost never see stuff from that era in stores. \n\nCould this be..?', ['1) Could it?'], [10]),
    8: Section('Hell yeah, there it is! \033[31mAB-1006\033[0m!', ['1) Inspect the rest of the disc.'], [11]),
    9: Section('Clear as day on both sides, \033[32m\'RL\'\033[0m! Dutch pressing, apparently.', ['1) Inspect the rest of the disc.'], [11]),
    10: Section('It could! \033[34m\'Manufactured and Distributed under \nexclusive license to Classic Records\'\033[0m is there \non both the center labels and the back cover, \notherwise it looks like an Atco original. \n\nHell yeah!', ['1) Inspect the discs.'], [12]),
    11: Section('Looks real clean! Aged for sure, but no big scuffs or scratches that you can see.', ['1) Take this bad boy up to the counter!'], [13]),
    12: Section('They look good! The Near Mint grading on the price sticker isn\'t far off.', ['1) Take this bad boy up to the counter!'], [13]),
    13: Section('You walk up to the counter with some excitement but also \nconsiderable dread that the clerk is going to want to \ntalk to you, a lot.', ['1) Who\'s working?'], [14]),
    14: Section('Phil is working the register today. An old hand for sure, \na hi-fi wizard with waist-length grey hair tied back in an \nintricate braid. He\'s friendly enough, but does not value \nanyone\'s time particularly highly.', ['1) "Hey man! How\'s it going?"', '2) Approach in silence.', '3) Mutter to yourself angrily in the hopes he\'ll be too scared to engage.'], [15, 16, 17])
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
            print(f'Please choose from the available selections.')

    if cmd == "q" or cmd == "Q":
        break

    choicehandler(cmd)

    def choicehandler(choice):
        adjust = int(choice) -1
        if cmd == parts[current].opt[adjust][0]:
            player.prog = parts[current].path[adjust]
        else: 
            print('I didn\'t understand that.')

