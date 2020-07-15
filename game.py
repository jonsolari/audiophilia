import time
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame

# STRUCTURE

# Player is an object with a Name, Progression Index, Inventory, Point Tally, Money Tally, and Error flag 

class Player:
    def __init__(self, name, prog, inv, points, money, err):
        self.name = name
        self.prog = prog
        self.inv = inv
        self.points = points
        self.money = money
        self.err = err

    def __str__(self):
        return f'{self.name}, {self.prog}, {self.inv}'

player = Player('', 0, [], 0, 60.00, False)

def linebreaks(string):

    newstring = ''
    counter = 0

    for i in string:
        if i == ' ':
            counter += 1

        if i == '-':
            counter += 1

        if i == '\n':
            counter = 0

        if counter == 11:
            newstring += i + '\n'
            counter = 0
        else:
            newstring += i
    
    return newstring


# Progression attribute will increment as you go on, and this will dictate what's shown as a prompt

class Section: 
    def __init__(self, desc, opt, path):
        self.desc = desc
        self.opt = opt
        self.path = path

parts = {
    0: Section('You are in your favorite record store. It\'s a basement-level space, but somehow still has a ton of deeply sun-faded promo posters (which they refuse to sell you, no matter how many times you ask). There\'s  a \"book section\" with a bunch of old issues of Rolling Stone and Maximum Rocknroll, some fat little 20th-century-summarizing record review books, a couple Elvis biographies, and a weird amount of 90s porno mags. A box of Grateful Dead bootleg tapes (both audience and soundboard) sits near the counter. The $1 CD wall promises scuffed-up copies of BMG Music Club one-hit-wonder flotsam, and always more than a few Ani DiFranco selections (why?). There are also, naturally, a ton of used vinyl records for sale.', ['1) Dig in some crates'], [1]),
    1: Section('There\'s a \"Beatles\" section only ever has solo George and Ringo albums, and cover compilations like the \'All This and World War II\' soundtrack. If you wanted to get down on your knees and crawl, a bunch of forgettable 78s (never any rock n\' roll, and definitely never any "race records") wait for you under the main bins. The few times you\'ve flipped through their decaying paper sleeves, you\'ve worried about potential asbestos content. There is a wall of cassettes but that\'s a 50-50 shot at buying something that\'s melted into a warbly hell in somebody\'s backseat.\n\nDespite all this, the store usually has a few gems. You\'ve narrowed it down to three titles.\n\n\033[33mWARNING:\033[0m Your decision will greatly determine your fate!', ['1) ' + '\033[31m' + 'Aja by Steely Dan'+'\033[0m', '2) ' + '\033[32m'+'Moving Pictures by Rush' + '\033[0m', '3) ' + '\033[34m'+'The Lamb Lies Down on Broadway by Genesis'+'\033[0m',], [2, 3, 4]),
    2: Section('Nice, a classic. What pressing is it?', ['1) Let\'s check!'], [5]),
    3: Section('Nice, a classic. What pressing is it?', ['1) Let\'s check!'], [6]),
    4: Section('Nice, a classic. What pressing is it?', ['1) Let\'s check!'], [7]),
    5: Section('There\'s a thread on the Steve Hoffman forums with over 650 posts in it, but you\'re not about to traipse through all that bullshit in full, on your smartphone, here at the store. People seem pretty over the moon about an original pressing with \033[31mAB-1006\033[0m carved into the deadwax.', ['1) Check the deadwax.'], [8]),
    6: Section('\'The Rush Vinyl Pressing Thread\' on the Steve Hoffman forums says to check the deadwax to see if both sides have an \033[32m\'RL\'\033[0m (for \033[32mRobert Ludwig\033[0m). A lot of people are arguing for various CD masterings too but you\'re not about the digital life anymore, not since dropping well over $600 on a turntable cartridge alone.', ['1) Check the deadwax.'], [9]),
    7: Section('You discreetly (you think) pull out your phone and see what people are saying about it on the Steve Hoffman forums. They all seem to be fawning over the \033[34m200g Classic Records reissue\033[0m from 2001. Weird time for vinyl, you almost never see stuff from that era second-hand. \n\nCould this be..?', ['1) Could it?'], [10]),
    8: Section('Hell yeah, there it is! \033[31mAB-1006\033[0m!', ['1) Inspect the rest of the disc.'], [11]),
    9: Section('Clear as day on both sides, \033[32m\'RL\'\033[0m! Dutch pressing, apparently.', ['1) Inspect the rest of the disc.'], [11]),
    10: Section('It could! \033[34m\'Manufactured and Distributed under exclusive license to Classic Records\'\033[0m is there on both the center labels and the back cover, otherwise it looks like an Atco original. \n\nHell yeah!', ['1) Inspect the discs.'], [12]),
    11: Section('Looks real clean! Aged for sure, but no big scuffs or scratches that you can see.', ['1) Take this bad boy up to the counter!'], [13]),
    12: Section('They look good! The Near Mint grading on the price sticker isn\'t far off.', ['1) Take this bad boy up to the counter!'], [13]),
    13: Section('You walk up to the counter with some excitement but also considerable dread that the clerk is going to want to talk to you, a lot.', ['1) Who\'s working?'], [14]),
    14: Section('\033[31mPhil\033[0m is working the register today. An old hand for sure, a hi-fi wizard with waist-length grey hair tied back in an intricate braid. He\'s friendly enough, but does not value anyone\'s time particularly highly.', ['1) "Hey man! How\'s it going?"', '2) Approach in silence.', '3) Mutter to yourself angrily in the hopes he\'ll be too scared to engage.'], [15, 16, 17]),
    15: Section('"Hey, brotherman. How\'s it hangin\'. Balmy day out there, man. Balmy. Have people been using that word a lot more lately? I feel like I\'m hearing that shit all day everyday man. We don\'t have THAT many balmy days, but I gotta give it to \'em today, it\'s a balmy one. \n\nWhatcha got there?"', ['1) Put your purchase on the counter.'], [18, 19, 20]),
    16: Section('"Hello! What did ya find today?"', ['1) Put your purchase on the counter.'], [18, 19, 20]),
    17: Section('"I can take who\'s next."', ['1) Put your purchase on the counter.'], [18, 19, 20]),
    18: Section('"Aja. Nice, man. Classic. Did you know they didn\'t want Purdie to do a shuffle on \'Home At Last\' but he managed to sneak it in anyway?? That guy was a trip, man. He\'d set up little signs next to his kit that said shit like "YOU DID IT, YOU HIRED THE HITMAKER." I love that shit man. Have you read \'Reeling in the Years\'? \'Major Dudes\' is okay but it\'s mostly old Rolling Stone reviews and shit. \'Eminent Hipsters\' is fun if you dig Fagen rambling on about jazz and being a crabby old bastard. That 33 1/3 book is fine too but I\'d skip it and just watch the \'Classic Albums\' documentary. It\'s on YouTube with Japanese subtitles for some reason, but it hasn\'t been copyright flagged yet."', ['1) "Oh really? Nice. That\'s cool man."', '2) "Yes. I know all this."', '3) Silence. Stonewall him until he runs out of gas.'], [21, 22, 23]),
    19: Section('Moving Pictures, unimpeachable man, truly unimpeachable. How do you get two songs like Tom Sawyer and Limelight on the same record? It\'s almost unfair. I got so into this band and then I\'m reading along with the lyrics on 2112 and they thank Ayn Rand...? The GENIUS of Ayn Rand....!?!? Broke my heart, man. How can ya be so progressive musically and so back-asswards in the political realm.', ['1) "I dunno, man. That\'s rough."', '2) "Yeah."', '3) Silence. Stonewall him until he runs out of gas.'], [21, 22, 24]),
    20: Section('"And the Laaaaaaaamb.... Lies Dowwwwwwwn.... on Broo-OO-ooadway!! Hell yeah man. Gabriel\'s last stand. Carpet Crawlers is a stone classic, man. You ever see the live show they did where he tells that trippy story before going into Supper\'s Ready? Is that on here (*looks at sleeve*) ah shit, that\'s right it\'s on Foxtrot. Another heavy one. Did you know Eno worked on this one? Makes sense if you look at the hair they were both sporting at the time."', ['1) "Oh really? Nice. That\'s cool man."', '2) "Yes. I know all this."', '3) Silence. Stonewall him until he runs out of gas.'], [21, 22, 25]),
    21: Section('He holds up the sleeve and calls to \033[31mJeffery\033[0m, the teen-aged stock boy. "JEFF! You heard this one yet? Stone classic." \n\nJeff gives a thumbs-up; he\'s either familiar with it or knows well enough to let sleeping tigers lie. \n\n"Kids today, man. The internet! I had to know somebody hip to get into any halfway decent records when I was that young. Pat Boone, Sing Along with Mitch type shit in my parents\' hi-fi all the time, man. Who needs it.\n\n"That\'ll be \033[32m$34.98\033[0m."', ['1) Pay the man.'], [29]),
    22: Section('Phil looks a bit stung; clearly he thought your acquaintance was on its way to proper friendship. He was maybe even going to invite you to the barbecue this weekend, held in the parking lot behind the store (you\'ve always thought that seemed like a cool, scofflaw kind of event). \n\n"Your total is \033[32m$34.98\033[0m."', ['1) Pay the man.'], [29]),
    23: Section('"Not a weak track on there, man. Can you imagine how many people are getting into the Dan just from hip hop samples? De La Soul using \'Peg\', Peter Gunz and Lord Tariq using \'Black Cow\'... not to mention Kanye using \'Kid Charlemagne\' but we\'re out in the weeds now, talking about \u001b[36mthe Royal Scam\033[0m. Underrated disc, if you ask me. \'Everyone\'s Gone to the Movies\' is such a sleeper creeper of a song!"', ['1) ...'], [26]),
    24: Section('"People like to rag on the Rush boys, but I never quite got that-- they\'re as legitimate as anybody, progressive or moderate. Whatever your stance is on weird time signatures and fretless double-necked guitars, they were layin\' down some heavy, ponderous shit! For my dollar anyway. Well they\'re Canadian, so I guess my seventy-three cents."', ['1) ...'], [27]),
    25: Section('"Oh the purists like to jump ship around \u001b[36mTrick of the Tail\033[0m, but I followed these guys clear through to \033[35mInvisible Touch\033[0m. Is the production style really dated? Of course! Is the video for Land of Confusion terrifying? Absolutely! But I\'ll be damned if it isn\'t still top notch quality tuneage."', ['1) ...'], [28]),
    26: Section('"TK singing a song \n\nThat\'ll be \033[32m$34.98\033[0m"', ['1) Pay the man.'], [29]),
    27: Section('"TK singing a song \n\nThat\'ll be \033[32m$34.98\033[0m"', ['1) Pay the man.'], [29]),
    28: Section('"That\'ll be, \033[32m$34.98\033[0m- ah! \u266b\nPut the cash, \u266b\nright- down- here-on-the-thing! \u266b"', ['1) Pay the man.'], [29]),
    29: Section('"Enjoy that thing, man! It\'ll sound boss on your setup, I just know it."', ['1) Leave the shop.'], [30]),
    30: Section('You climb into your \'98 Tercel, taking extra care to set your new purchase down on the passenger seat, all but buckling it in. As you coast down Main St., you get a small frisson of hope about your afternoon to come. A great find! Reference quality! You can just imagine what the guys will say when you have them over for a demonstration. The low end always scares \033[31mJaco\033[0m, your faithful calico tomcat, but you know enough by now to gently usher him into the other room.\n\nOh shit! Jaco! \nHis food was low when you checked.', ['1) Hang a left on Elm and head to the pet store.'], [31, 32, 33]),
    31: Section('You navigate to the pet shop and get his cat food (sensitive stomach, senior blend, goddamn $18).\n\nYou have \033[32m\'Limelight\'\033[0m stuck in your head though-- you probably should have bought Moving Pictures instead.',['1) Goddamnit.'],[34]),
    32: Section('You navigate to the pet shop and get his cat food (sensitive stomach, senior blend, goddamn $18).\n\nYou have \033[34m\'Carpet Crawlers\'\033[0m stuck in your head though-- you probably should have bought The Lamb Lies Down on Broadway instead.',['1) Goddamnit.'],[34]),
    33: Section('You navigate to the pet shop and get his cat food (sensitive stomach, senior blend, goddamn $18).\n\nYou have \033[31m\'Peg\'\033[0m stuck in your head though-- you probably should have bought Aja instead.',['1) Goddamnit.'],[34]),
    34: Section('You head home, damn near broke at this point (good thing you didn\'t need gas!). It\'ll be worth it though; how often do you actually find a decent record, used, in this good of shape? Phil was right, it\'s going to sound boss as hell.',['1) Pull into your parking spot.'],[35]),
    35: Section('You\'re almost home free, but your neighbor \033[31mChip\033[0m accosts you as you\'re about to put the key in the lock.', ['1) "Hey, man! What\'s the haps?"', '2) Nod, mumble something vague and go inside.', '3) "Kind of in a hurry right now, Chip."', '4) "Fuck off, Chip"'], [36, 37, 38, 39]),
    36: Section('"Can\'t complain! Can- not- complain, my man."', ['1) Ask about his kids', '2) Ask about his wife', '3) Wrap things up and go inside.'], [40, 41, 42]),
    37: Section('"Next time! Man, sometime we gotta hit the pub and--"', ['1) Close the door and lock it.'], [42]),
    38: Section('He seems a bit dejected, but generally unshakeable when in a good mood.\n\n"Fast times at Ridgewood Apartments, I get it. Keep your stick on the ice, man!"', ['1) Close the door and lock it.'], [42]),
    39: Section('What did you just say to me you piece of shit? Nobody LIKES you here. Did you know that? I\'m glad I slept with your wife last year. Go the fuck inside and listen to your jazz fusion whatever-the-fuck. If I hear that shit through the walls again I\'m gonna knock down this door and break your goddamn legs. FUCK you', ['1) Go inside.'], [42]),
    40: Section('"They\'re incredible! God, they\'re just the best.\n\nDean just started middle school, the little spaz. Always going on about some new bullshit I gotta buy him so he can fit in. Buncha weird shit. Made in China. I don\'t know man.\n\nErica, god bless her, she\'s still in diapers and I\'m in no hurry to see that change. I\'m gonna fucking murder the first boy who kisses her."', ['1) "Ah. Nice, that\'s just great. I gotta head in man, great seeing ya."'], [42]),
    41: Section('"Debbie? Hot as ever, man. You know; we all know. It\'s ok, I know all the guys around here like to look. I don\'t mind a quick glance but you better keep it zipped up pal!! I\'m a generous enough guy but let\'s just say we can\'t share EVERYthing with our neighbors! Hahahaha. Tight knit community here at Ridgewood but get outta here, I don\'t think so nosiree."', ['1) "Ah. Nice, that\'s just great. I gotta head in man, great seeing ya."'], [42]),
    42: Section('You go inside.\n\nYour apartment is a modest one. The main door opens into your living room, where there is a very weathered couch, glass coffee table, and small television with VCR. You used to have a Laserdisc player too (the only choice for anyone who cares about sound even a little), but you lost that in the divorce. Your apartment is technically a two bedroom, but one of those became the listening room as soon as you moved in.', ['1) Feed Jaco.'], [43]),
    43: Section('Jaco is very glad to have a fresh bowl of food. Even with the sensitive-stomach blend, it\'ll still be an 80/20 chance of him vomiting in the next day or two. You love him anyway though, perhaps even more than the smooth fretless bass tones of his namesake.', ['1) Move to the listening room.', '2) Have a nice snack first.'], [45, 44]),
    44: Section('You go to the kitchen to prepare your go-to snack: a slice of Muenster cheese melted on some 12-grain bread, paired with a tall glass of 2% milk. You don\'t remember when you started making this, but you\'re very glad nobody but your cat is here to see you eating it.', ['1) Now you\'re ready to listen, to appreciate.'], [45]),
    45: Section('You enter the listening room.\n\nThis is your sanctum santorum. In here you cannot hear the troubles of the outside world, figuratively or literally.\n\nThe speakers are nice, tall \033[34mBang & Olufsen Beolab Penta 2\033[0ms that you got second-hand from your pal Jeff when he upgraded to the Penta 3\'s. Your receiver is a \033[32mMcIntosh MAC1700\033[0m that you have proudly (but very nervously) serviced yourself over the years. The turntable that\'ll spin your new purchase is a handsome wood-finish \033[31mLinn LP12\33[0m with a \033[35mLyra Delos\033[0m cartridge, per the recommendations of a complete stranger on the internet. An empty wood shelf sits on the wall a bit above your hi-fi stack, reserved for the day you finally pull the trigger on a reel-to-reel tape deck.\n\nYou also have a mediocre SACD player that you have not used in three years.', ['1) Turn everything on and let it warm up for a good half hour.\nLot of tubes in there, lot of voltage that needs stabilizing.'], [46]),
    46: Section('Your system makes a series of satisfyingly bold clicks and pops as you turn the components on.', ['1) Sit in silence.'], [47]),
    47: Section('You sit in the room\'s lone chair and think about things for a half hour.', ['1) Think about your hi-fi setup.', '2) Think about your ex-wife.', '3) Check tomorrow\'s weather.'], [48, 49, 50]),
    48: Section('You wonder sometimes about switching up your phono cartridge, but on your salary you can\'t exactly afford to have a whole fleet of them to pick from. You try to get in the occasional demo session at the hi-fi shop two towns over, but you\'re careful to not stop by TOO often and be seen as some kind of freeloader. No matter how deep into a niche hobby you dig yourself, your pre-existing anxieties will always be in there with you unless you decide to actually work on yourself in earnest. Maybe talk to someone, read one of the books the marriage counselor gave you when it was just a trial separation and not a full and legal divorce.', ['1) Well, everything should be warmed up by now.'], [56]),
    49: Section('Sheila...\n\nWhat is she doing right now, you wonder. Did she throw herself back into her painting after the split? You always felt like you kept her from her creative pursuits on some level. Maybe you critiqued works in progress one too many times, you\'re not sure, but eventually the canvas and easel just stopped coming out altogether.', ['1) How did you two meet again?'], [51]),
    50: Section('You check your smartphone before remembering it might be adding unwanted electrical interference to your otherwise sealed-off listening room. (The weather will be fine tomorrow.)', ['1) Put your phone in the other room.'], [54]),
    51: Section('You met Sheila through some mutual friends. Fred was the one hosting the party, you think. It\'s so long ago now. It was awkward at first, feeling such an electric and mutual attraction to someone you just met, and trying hard to not show it too soon. You looked for openings all night, and at some point felt so bold as to claim an empty seat on the ottoman next to her when its occupant flitted over to different conversation circle in the kitchen. You managed to get past the clunkiness of the first few small-talk questions, finding shared interest in Fred\'s shelf of artist monographs (more specifically a shared distaste for Jackson Pollack and his CIA ties). You walked her home that night; you still don\'t know where you found the nerve to propose that. Or make that first phone call two afternoons later.', ['1) Remember last summer at Cape Cod?'], [52]),
    52: Section('God, the Cape Cod trip. A second honeymoon of sorts, an unexpected oasis in the middle of weeks of fighting. It was as if a change of scenery somehow put an unspoken truce into effect, but you overshot the tacit "tolerate one another" promise of most tired-marriage vacations, and ended up back in some kind of pleasantly naive teenage place, emotionally. You brought wine but drank none of it, intoxication would have felt redundant.', ['1) Where did it all go wrong?'], [53]),
    53: Section('TK where it all went wrong. you stopped listening, dove into your interests too much, became a kind of shadow of yourself', ['1) Tubes are probably warm by now. Let\'s hear this new disc.'], [56]),
    54: Section('You go back into the living room and put your phone face-down on the coffee table, after putting it into Airplane Mode for additional security against unwanted vibrations. Jaco looks up from a nap he\'s drifting in and out of.', ['1) Pet Jaco.'], [55]),
    55: Section('You give Jaco some behind-the-ear skritches. He\'ll always be there for you.', ['1) Head back in and listen to your new record!'], [56]),
    56: Section('Over the years, you\'ve developed a delicate technique for unsleeving a record and only touching the edges and the label. You all but lunge at anyone who tries to put something on at your parties, fearing they\'ll get their grubby fingerprints all in the grooves. You haven\'t held a party in six years', ['1) Let\'s get this cleaned up.'], [57]),
    57: Section('Even the cleanest-looking of records can still be filthy, so you turn to your trusted \033[32mRECORD DOCTOR V\033[0m, a vacuum-based machine. After applying the right amount of cleaning solution to Side 1, you place it face-down over its brush-lined vacuum slit. There\'s a hockey puck shaped handle thing you put on top of the label that has little grips so you can turn the disc manually (you can\'t yet afford a full-auto disc washer, and this has irked you for years). The machine whines like a full-size canister vacuum cleaner, and you let it do its thing for three slow revolutions of the LP. This is the part where Jaco usually hides under the couch.\n\nYour disc now shines magnificently.', ['1) Pop it on the turntable!'], [58]),
    58: Section('You place it on your turntable with the utmost care.', ['1) Throw a nice heavy weight on the center label.'], [59]),
    59: Section('You secure a big brass doorknob looking thing on top of the disc. No chance it will drift or wobble now.', ['1) What about static though?'], [60]),
    60: Section('The disc looks totally free of dust, but static is the invisible menace! You take your carbon fiber brush and let the LP spin three times underneath its light touch.', ['1) But is the needle itself clean?'], [61]),
    61: Section('Just to be safe, you do the melamine trick you learned about, taking a \'Magic Eraser\' pad and delicately lowering the needle onto it a few times. (Strictly vertically! Horizontal motion could fuck the needle up but good, you\'re told.) It\'s a small blessing that your turntable has a cue lever for this.', ['1) Sit in your listening chair.'], [62]),
    62: Section('You ease into your favorite listening chair, a mid-range IKEA job called \033[33mEKERÖ\033[0m that you picked up because it reminded you of the old Maxell commercials.\n\nWait, what in the hell is that buzz?', ['1) Check the speaker wires', '2) Check the turntable ground wire', '3) Turn off all the lights in your apartment in case they\'re interfering somehow.'], [63, 64, 65]),
    63: Section('The speaker wires look ok! Nothing is loose, no spindly little shits poking out from your top-notch wire twisting job a few years back.', ['1) turntable', '2) all the lights'], [64, 67]),
    64: Section('That\'s it! The ground wire on the turntable somehow came loose.', ['1) Reattach that guy!'], [68]),
    65: Section('You turn off all the kitchen and living room lights, but when you return to the listening room the buzz is still there.', ['1) Check the speaker wires.', '2) Check the turntable ground wire.'], [66, 64]),
    66: Section('The speaker wires look ok! Nothing is loose, no spindly little shits poking out from your top-notch wire twisting job a few years back.', ['1) '], [64]),
    67: Section('You turn off all the kitchen and living room lights, but when you return to the listening room the buzz is still there.', ['1) '], [64]),
    68: Section('The buzz is gone!\n\nIt\'s time at last to spin this record.', ['1) Drop the needle!'], [69, 70, 71]),
    69: Section('Hell yeah. Side 1, Track 1 of AJA.... \033[31m\'Black Cow\'\033[0m', ['1) Take the needle off the record.'], [72]),
    70: Section('Hell yeah. Side 1, Track 1 of MOVING PICTURES.... \033[32m\'Tom Sawyer\'\033[0m', ['1) Take the needle off the record.'], [72]),
    71: Section('Hell yeah. Side 1, Track 1 of THE LAMB LIES DOWN ON BROADWAY.... title track \033[34m\'The Lamb Lies Down on Broadway\'\033[0m', ['1) Take the needle off the record.'], [72]),
    72: Section('What the fuck. "Near Mint"!? And the first fucking SONG has a skip? You could kill Phil. What kinda mickey mouse goddamn moron operation is he running down there', ['1) Re-sleeve the LP.', '2) Eat your feelings.', '3) Go for a walk to try and calm down.'], [73, 74, 75]),
    73: Section('You try to steady your hands to put the record away. Goddamnit, even a VG+ graded record should have played with no skips what the HELL', ['1) Take the record back to the store.'], [76, 77, 78]),
    74: Section('You power through four more pieces of cheese-on-toast.\n\nYou feel a bit sick, which proves to be a welcome distraction.', ['1) Take the record back to the store.'], [76, 77, 78]),
    75: Section('TK you walk around the apartment complex. description of where you live / thankfully you do not see chip. you don\'t feel any more calm though', ['1) Take the record back to the store.'], [76, 77, 78]),
    76: Section('TK you get in the car, the end of Black Cow is on the radio as if to mock you.', ['1) Change the station.'], [79]),
    77: Section('TK you get in the car, the end of Tom Sawyer is on the radio as if to mock you.', ['1) Change the station '], [79]),
    78: Section('TK you get in the car, the end of The Lamb Lies Down on Broadway is on the radio as if to mock you.', ['1) Change the station.'], [79]),
    79: Section('TK you scan around a bit, but everything scares you. wishing you hadn\'t left your Pono at home.', ['1) Drive in silence.'], [80]),
    80: Section('There\'s a noticeable whining sound. Your fan belt probably needs to be replaced.', ['1) Pull into the record store parking lot.'], [81]),
    81: Section('TK ', ['1) '], []),

    # 00: Section('TK ', ['1) '], []),
}

anomalies = [15, 16, 17, 30, 68, 74]
payments = [21, 22, 26, 27, 28]
catfood = [31, 32, 33]

welcome = 'Welcome to AUDIOPHILIA, the game of hi-fi perfection.\n\nPlease enter your name.'

os.system('clear')
print()
print(welcome)
print()
intro = input('-->')

while player.name == '':
    # if intro == "LOAD":
    #     print('Feature TK')
    #     print()
    #     print(welcome)
    #     intro = input('-->')
    # else:
    player.name = intro

print()
print(f'Welcome, {player.name}!')

while True:

    current = player.prog
    
    os.system('clear')

    print(f'\033[1;30;47mAUDIOPHILIA   Player: {player.name}   Points: {player.points}   Money: ${player.money:.2f}\033[0m')

    if player.err == True:
        print()
        print('\033[35mPlease choose from the available selections.\033[0m')
        player.err = False

    print()
    print(linebreaks(parts[current].desc))
    
    print()

    if player.prog == 2:
        player.inv = 'aja'
        # THIS WORKS for playing a MIDI in the fucking command line, which, lol
        pygame.mixer.init()
        pygame.mixer.music.load('multimedia/cow.mid')
        
    if player.prog == 3:
        player.inv = 'rush'
        pygame.mixer.init()
        pygame.mixer.music.load('multimedia/tom.mid')
        
    if player.prog == 4:
        player.inv = 'lamb'
        pygame.mixer.init()
        pygame.mixer.music.load('multimedia/lamb.mid')

    if player.prog in payments:
        player.money -= 34.98

    if player.prog in catfood:
        player.money -= 17.98
    
    # FOR MIDI PLAYER + CHOICE DELAY
    if player.prog == 69:
        pygame.mixer.music.play()
        time.sleep(36) 

    if player.prog == 70:
        pygame.mixer.music.play()
        time.sleep(30) #TBD

    if player.prog == 71:
        pygame.mixer.music.play()
        time.sleep(53) 

    if player.prog == 72:
        pygame.mixer.music.stop()

    for i in parts[current].opt:
        print(i)
    
    print()

    # print("inventory: ", player.inv)

    cmd = input("-->")


    def choicehandler(choice):
        adjust = int(choice) -1
        optnum = len(parts[current].opt)



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
            player.err = True

    if cmd == "q" or cmd == "Q":
        break

    
    choicehandler(cmd)
    


