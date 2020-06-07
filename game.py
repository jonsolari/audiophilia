import time
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame

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
    0: Section('You are in the dusty stacks of your favorite record store. TK description of the store. sun-faded promo posters they refuse to sell, a bunch of issues of old zines & record review books, a weird amount of 90s porno mags in with all that', ['1) Dig in some crates'], [1]),
    1: Section('You\'ve narrowed it down to three titles. TK Warning about your choice here heavily influencing your future! or something. TBD if this will be true', ['1) ' + '\033[31m' + 'Aja by Steely Dan'+'\033[0m', '2) ' + '\033[32m'+'Moving Pictures by Rush' + '\033[0m', '3) ' + '\033[34m'+'The Lamb Lies Down on Broadway by Genesis'+'\033[0m',], [2, 3, 4]),
    2: Section('Nice, a classic. What pressing is it?', ['1) Let\'s check!'], [5]),
    3: Section('Nice, a classic. What pressing is it?', ['1) Let\'s check!'], [6]),
    4: Section('Nice, a classic. What pressing is it?', ['1) Let\'s check!'], [7]),
    5: Section('There\'s a thread on the Steve Hoffman forums with over \n650 posts in it, but you\'re not about to traipse through \nall that bullshit in full, on your smartphone, here at \nthe store. People seem pretty over the moon about an \noriginal pressing with \033[31mAB-1006\033[0m carved into the deadwax.', ['1) Check the deadwax.'], [8]),
    6: Section('\'The Rush Vinyl Pressing Thread\' on the Steve Hoffman \nforums says to check the deadwax to see if both sides \nhave an \033[32m\'RL\'\033[0m (for \033[32mRobert Ludwig\033[0m). A lot of people are \narguing for various CD masterings too but you\'re not \nabout the digital life anymore, not since dropping well \nover $600 on a turntable cartridge alone.', ['1) Check the deadwax.'], [9]),
    7: Section('You discreetly (you think) pull out your phone and see \nwhat people are saying about it on the Steve Hoffman \nforums. They all seem to be fawning over the \033[34m200g \nClassic Records reissue\033[0m from 2001. Weird time for vinyl, \nyou almost never see stuff from that era in stores. \n\nCould this be..?', ['1) Could it?'], [10]),
    8: Section('Hell yeah, there it is! \033[31mAB-1006\033[0m!', ['1) Inspect the rest of the disc.'], [11]),
    9: Section('Clear as day on both sides, \033[32m\'RL\'\033[0m! Dutch pressing, apparently.', ['1) Inspect the rest of the disc.'], [11]),
    10: Section('It could! \033[34m\'Manufactured and Distributed under \nexclusive license to Classic Records\'\033[0m is there \non both the center labels and the back cover, \notherwise it looks like an Atco original. \n\nHell yeah!', ['1) Inspect the discs.'], [12]),
    11: Section('Looks real clean! Aged for sure, but no big scuffs or \nscratches that you can see.', ['1) Take this bad boy up to the counter!'], [13]),
    12: Section('They look good! The Near Mint grading on the price sticker isn\'t far off.', ['1) Take this bad boy up to the counter!'], [13]),
    13: Section('You walk up to the counter with some excitement but also \nconsiderable dread that the clerk is going to want to \ntalk to you, a lot.', ['1) Who\'s working?'], [14]),
    14: Section('Phil is working the register today. An old hand for sure, \na hi-fi wizard with waist-length grey hair tied back in an \nintricate braid. He\'s friendly enough, but does not value \nanyone\'s time particularly highly.', ['1) "Hey man! How\'s it going?"', '2) Approach in silence.', '3) Mutter to yourself angrily in the hopes he\'ll be too scared to engage.'], [15, 16, 17]),
    15: Section('"Hey, brotherman. How\'s it hangin\'. Balmy day out there, \nman. Balmy. Have people been using that word a lot more \nlately? I feel like I\'m hearing that shit all day \neveryday man. We don\'t have THAT many balmy days, but I \ngotta hand it to \'em today, it\'s a balmy one. \n\nWhatcha got there?"', ['1) Put your purchase on the counter.'], [18, 19, 20]),
    16: Section('"Hello! What did ya find today?"', ['1) Put your purchase on the counter.'], [18, 19, 20]),
    17: Section('"I can take who\'s next."', ['1) Put your purchase on the counter.'], [18, 19, 20]),
    18: Section('"Aja. Nice, man. Classic. Did you know they didn\'t want \nPurdie to do a shuffle on \'Home At Last\' but he managed \nto sneak it in anyway?? That guy was a trip, man. He\'d \nset up little signs next to his kit that said shit like \n"YOU DID IT, YOU HIRED THE HITMAKER." I love that shit \nman. Have you read \'Reeling in the Years\'? \'Major Dudes\' \nis okay but it\'s mostly old Rolling Stone reviews and \nshit. \'Eminent Hipsters\' is fun if you dig Fagen \nrambling on about jazz and being a crabby old bastard. \nThat 33 1/3 book is fine too but I\'d skip it and just \nwatch the \'Classic Albums\' documentary. It\'s on YouTube \nwith Japanese subtitles for some reason, but it hasn\'t \nbeen copyright flagged yet."', ['1) "Oh really? Nice. That\'s cool man."', '2) "Yes. I know all this."', '3) Silence. Stonewall him until he runs out of gas.'], [21, 22, 23]),
    19: Section('Moving Pictures, unimpeachable man, truly unimpeachable. \nHow do you get two songs like Tom Sawyer and Limelight \non the same record? It\'s almost unfair. I got so into \nthis band and then I\'m reading along with the lyrics on \n2112 and they thank Ayn Rand...? The GENIUS of Ayn \nRand....!?!? Broke my heart, man. How can ya be so \nprogressive musically and so back-asswards in the \npolitical realm.', ['1) "I dunno, man. That\'s rough."', '2) "Yeah."', '3) Silence. Stonewall him until he runs out of gas.'], [21, 22, 24]),
    20: Section('"And the Laaaaaaaamb.... Lies Dowwwwwwwn.... on \nBroo-OO-ooadway!! Hell yeah man. Gabriel\'s last stand. \nCarpet Crawlers is a stone classic, man. You ever see the \nlive show they did where he tells that trippy story before \ngoing into Supper\'s Ready? Is that on here (*looks at \nsleeve*) ah shit, that\'s right it\'s on Foxtrot. Another \nheavy one. Did you know Eno worked on this one? Makes sense \nif you look at the hair they were both sporting at the time."', ['1) "Oh really? Nice. That\'s cool man."', '2) "Yes. I know all this."', '3) Silence. Stonewall him until he runs out of gas.'], [21, 22, 25]),
    21: Section('TK one more screen of rambling and then he gives you the total', ['1) Pay the man.'], [29]),
    22: Section('TK shopkeep looks a bit stung and gives you the total', ['1) Pay the man.'], [29]),
    23: Section('TK another screen about aja', ['1) ...'], [26]),
    24: Section('TK another screen about rush', ['1) ...'], [27]),
    25: Section('TK another screen about genesis', ['1) ...'], [28]),
    26: Section('TK final screen about aja, and the total', ['1) Pay the man.'], [29]),
    27: Section('TK final screen about rush, and the total', ['1) Pay the man.'], [29]),
    28: Section('TK final screen about genesis, and the total', ['1) Pay the man.'], [29]),
    29: Section('TK shopkeep bids you farewell!', ['1) Leave the shop.'], [30]),
    30: Section('TK description of your sad car, what you\'re thinking about on the ride home. you\'re on main street and your cat is almost out of food', ['1) Drive to the pet store.'], [31, 32, 33]),
    31: Section('TK you go in and get the cat food. You have \'Limelight\' stuck in your head though-- you probably should have bought Moving Pictures instead.',['1) Goddamnit.'],[34]),
    32: Section('TK you go in and get the cat food. You have \'Carpet Crawlers\' stuck in your head though-- you probably should have bought The Lamb Lies Down on Broadway instead.',['1) Goddamnit.'],[34]),
    33: Section('TK you go in and get the cat food. You have \'Peg\' stuck in your head though-- you probably should have bought Aja instead.',['1) Goddamnit.'],[34]),
    34: Section('TK you drive the rest of the way home.',['1) Pull into your parking spot.'],[35]),
    35: Section('TK your neighbor Chip accosts you as you\'re about to put the key in the lock', ['1) engage pleasantly', '2) nod, mumble something, and go inside', '3) kind of in a hurry right now', '4) fuck off, Chip'], [36, 37, 38, 39]),
    36: Section('TK nice chip', ['1) Ask about his kids', '2) Ask about his wife', '3) Wrap things up and go inside.'], [40, 41, 42]),
    37: Section('TK chip calls after you', ['1) Close the door and lock it.'], [42]),
    38: Section('TK chip seems sad', ['1) Close the door and lock it.'], [42]),
    39: Section('What did you just say to me you piece of shit? Nobody LIKES you here. Did you know that? I\'m glad I slept with your wife last year. Go the fuck inside and listen to your jazz fusion whatever-the-fuck. If I hear that shit through the walls again I\'m gonna knock down this door and break your goddamn legs. FUCK you', ['1) Go inside.'], [42]),
    40: Section('TK chips tells you about his kids at length', ['1) Wrap it up here and go inside.'], [42]),
    41: Section('TK chips tells you about his wife, makes some uncomfortable comments', ['1) Wrap it up here and go inside'], [42]),
    42: Section('TK description of your deeply sad apartment', ['1) Feed your cat, Miles'], [43]),
    43: Section('TK description of your cat and why you named him that', ['1) Move to the listening room.', '2) Have a nice snack first.'], [45, 44]),
    44: Section('TK very sad bachelor snack', ['1) Now you\'re ready to listen, to appreciate.'], [45]),
    45: Section('TK description of listening room', ['1) Turn everything on and let it warm up for a good half hour. Lot of tubes in there, lot of voltage that needs stabilizing.'], [46]),
    46: Section('TK this will be a while', ['1) Sit in silence.'], [47]),
    47: Section('TK a half hour passes while you think about things.', ['1) Think about your hi-fi setup.', '2) Think about your ex-wife.', '3) Check tomorrow\'s weather.'], [48, 49, 50]),
    48: Section('TK describe setup at length, whine about things you don\'t yet have', ['1) Everything should be warmed up by now.'], [56]),
    49: Section('TK wax nostalgic about your wife', ['1) How did you two meet again?'], [51]),
    50: Section('TK check your smartphone before remembering it might be adding unwanted electrical interference to your otherwise sealed-off listening room. (the weather will be fine tomorrow)', ['1) Put your phone in the other room.'], [54]),
    51: Section('TK how you met your wife through friends and it was awkward at first but you fought through that and got to know each other quite intimately', ['1) Remember last summer at Cape Cod?'], [52]),
    52: Section('TK last summer at cape cod', ['1) Where did it all go wrong?'], [53]),
    53: Section('TK where it all went wrong. you stopped listening, dove into your interests too much, became a kind of shadow of yourself', ['1) Tubes are probably warm by now. Let\'s hear this new disc.'], [56]),
    54: Section('TK put your phone down on the coffee table, airplane mode just to be extra safe.', ['1) Pet Miles'], [55]),
    55: Section('TK you pet Miles. he\'ll always be there for you.', ['1) Head back in and listen to your new record!'], [56]),
    56: Section('TK careful unsheathing of the LP', ['1) '], []),
}

anomalies = [15, 16, 17, 30]

welcome = 'Welcome to AUDIOPHILIA, the game of hi-fi perfection. Please enter your name, or LOAD to load an existing game.'

# print()
# print()
# print()
# print()
# print()
# print()
# print()
# print()
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

    current = player.prog
    
    # print()
    # print()
    # print()
    # print()
    # print()
    # print()
    # print()
    # print()
    
    print(parts[current].desc)
    
    print()
    
    # FOR MIDI PLAYER + CHOICE DELAY
    # if player.prog == 5(TK):
    #     time.sleep(5)

    for i in parts[current].opt:
        print(i)
    
    print()

    # print("inventory: ", player.inv)

    cmd = input("-->")


    def choicehandler(choice):
        adjust = int(choice) -1
        optnum = len(parts[current].opt)

        if player.prog == 2:
            player.inv = 'aja'
            # THIS WORKS for playing a MIDI in the fucking command line, which, lol
            # pygame.mixer.init()
            # pygame.mixer.music.load('multimedia/cow.mid')
            # pygame.mixer.music.play()
            
        if player.prog == 3:
            player.inv = 'rush'
            
        if player.prog == 4:
            player.inv = 'lamb'

        if int(choice) <= optnum and player.prog in anomalies:
            if 'aja' in player.inv and int(choice) == 1:
                player.prog = parts[current].path[0]
            elif 'rush' in player.inv and int(choice) == 1:
                player.prog = parts[current].path[1]
            elif 'lamb' in player.inv and int(choice) == 1:
                player.prog = parts[current].path[2]
        elif int(choice) <= optnum and player.prog not in anomalies:
            if cmd == parts[current].opt[adjust][0]:
                player.prog = parts[current].path[adjust]
        else: 
            print(f'Please choose from the available selections.')

    if cmd == "q" or cmd == "Q":
        break

    
    choicehandler(cmd)
    


