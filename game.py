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
    11: Section('Looks real clean! Aged for sure, but no big scuffs or \nscratches that you can see.', ['1) Take this bad boy up to the counter!'], [13]),
    12: Section('They look good! The Near Mint grading on the price sticker isn\'t far off.', ['1) Take this bad boy up to the counter!'], [13]),
    13: Section('You walk up to the counter with some excitement but also \nconsiderable dread that the clerk is going to want to \ntalk to you, a lot.', ['1) Who\'s working?'], [14]),
    14: Section('Phil is working the register today. An old hand for sure, \na hi-fi wizard with waist-length grey hair tied back in an \nintricate braid. He\'s friendly enough, but does not value \nanyone\'s time particularly highly.', ['1) "Hey man! How\'s it going?"', '2) Approach in silence.', '3) Mutter to yourself angrily in the hopes he\'ll be too scared to engage.'], [15, 16, 17]),
    15: Section('"Hey, brotherman. How\'s it hangin\'. Balmy day out there, \nman. Balmy. Have people been using that word a lot more \nlately? I feel like I\'m hearing that shit all day \neveryday man. We don\'t have THAT many balmy days, but I \ngotta hand it to \'em today, it\'s a balmy one. \n\nWhatcha got there?"', ['1) Put your purchase on the counter.'], [18, 19, 20]),
    16: Section('"Hello! What did ya find today?"', ['1) Put your purchase on the counter.'], [18, 19, 20]),
    17: Section('"I can take who\'s next."', ['1) Put your purchase on the counter.'], [18, 19, 20]),
    18: Section('"Aja. Nice, man. Classic. Did you know they didn\'t want \nPurdie to do a shuffle on \'Home At Last\' but he managed \nto sneak it in anyway?? That guy was a trip, man. He\'d \nset up little signs next to his kit that said shit like \n"YOU DID IT, YOU HIRED THE HITMAKER." I love that shit \nman. Have you read \'Reeling in the Years\'? \'Major Dudes\' \nis okay but it\'s mostly old Rolling Stone reviews and \nshit. \'Eminent Hipsters\' is fun if you dig Fagen \nrambling on about jazz and being a crabby old bastard. \nThat 33 1/3 book is fine too but I\'d skip it and just \nwatch the \'Classic Albums\' documentary. It\'s on YouTube \nwith Japanese subtitles for some reason, but it hasn\'t \nbeen copyright flagged yet."', ['1) "Oh really? Nice. That\'s cool man."', '2) "Yes. I know all this."', '3) Silence. Stonewall him until he runs out of gas.'], [21, 22, 23]),
    19: Section('Moving Pictures, unimpeachable man, truly unimpeachable. \nHow do you get two songs like Tom Sawyer and Limelight \non the same record? It\'s almost unfair. I got so into \nthis band and then I\'m reading along with the lyrics on \n2112 and they thank Ayn Rand...? The GENIUS of Ayn \nRand....!?!? Broke my heart, man. How can ya be so \nprogressive musically and so back-asswards in the \npolitical realm.', ['1) "I dunno, man. That\'s rough."', '2) "Yeah."', '3) Silence. Stonewall him until he runs out of gas.'], [21, 22, 23]),
    20: Section('"And the Laaaaaaaamb.... Lies Dowwwwwwwn.... on \nBroo-OO-ooadway!! Hell yeah man. Gabriel\'s last stand. \nCarpet Crawlers is a stone classic, man. You ever see the \nlive show they did where he tells that trippy story before \ngoing into Supper\'s Ready? Is that on here (*looks at \nsleeve*) ah shit, that\'s right it\'s on Foxtrot. Another \nheavy one. Did you know Eno worked on this one? Makes sense \nif you look at the hair they were both sporting at the time."', ['1) "Oh really? Nice. That\'s cool man."', '2) "Yes. I know all this."', '3) Silence. Stonewall him until he runs out of gas.'], [21, 22, 23]),
    21: Section('', [''], []),
    22: Section('', [''], []),
    23: Section('...\n\nOkay after tax, that\'ll be $34.98.', ['1) Pay the man.'], []),
}

anomalies = [15, 16, 17]

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

    # print("inventory: ", player.inv)

    cmd = input("-->")

    def anomalyhandler(choice):
        if player.prog in anomalies:
            if 'aja' in player.inv and choice == 1:
                 player.prog = parts[current].path[0]
            elif 'rush' in player.inv and choice == 1:
                 player.prog = parts[current].path[1]
            elif 'lamb' in player.inv and choice == 1:
                 player.prog = parts[current].path[2]
        else:
            pass

    def choicehandler(choice):
        adjust = int(choice) -1
        optnum = len(parts[current].opt)

        if player.prog == 2:
            player.inv = 'aja'

        if player.prog == 3:
            player.inv = 'rush'

        if player.prog == 4:
            player.inv = 'lamb'

        if int(choice) <= optnum and player.prog not in anomalies:
            # if player.prog == 15 and 'aja' in player.inv and cmd == parts[current].opt[adjust][0]:
            #     player.prog = 18
            # elif player.prog == 15 and 'rush' in player.inv and cmd == parts[current].opt[adjust][0]:
            #     player.prog = 19
            # elif player.prog == 15 and 'lamb' in player.inv and cmd == parts[current].opt[adjust][0]:
            #     player.prog = 20
            # elif player.prog == 16 and 'aja' in player.inv and cmd == parts[current].opt[adjust][0]:
            #     player.prog = 18
            # elif player.prog == 16 and 'rush' in player.inv and cmd == parts[current].opt[adjust][0]:
            #     player.prog = 19
            # elif player.prog == 16 and 'lamb' in player.inv and cmd == parts[current].opt[adjust][0]:
            #     player.prog = 20
            # elif player.prog == 17 and 'aja' in player.inv and cmd == parts[current].opt[adjust][0]:
            #     player.prog = 18
            # elif player.prog == 17 and 'rush' in player.inv and cmd == parts[current].opt[adjust][0]:
            #     player.prog = 19
            # elif player.prog == 17 and 'lamb' in player.inv and cmd == parts[current].opt[adjust][0]:
            #     player.prog = 20
            if cmd == parts[current].opt[adjust][0]:
                player.prog = parts[current].path[adjust]
        else: 
            print(f'Please choose from the available selections.')

    if cmd == "q" or cmd == "Q":
        break

    anomalyhandler(cmd)
    choicehandler(cmd)

    # def choicehandler(choice):
    #     adjust = int(choice) -1
    #     if cmd == parts[current].opt[adjust][0]:
    #         player.prog = parts[current].path[adjust]
    #     else: 
    #         print('I didn\'t understand that.')

