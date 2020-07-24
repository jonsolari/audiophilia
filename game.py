import time
import platform
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame

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

# to clear terminal screen on windows and mac osx

def clear():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

# basic word wrap algorithm

def linebreaks(string):

    newstring = ''
    counter = 0
    charcounter = 0

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

# progression attribute will change depending on choices player makes, and this will dictate what's shown for a description and next set of choices

class Section: 
    def __init__(self, desc, opt, path):
        self.desc = desc
        self.opt = opt
        self.path = path

# script of the game itself

parts = {
    0: Section('You are in your favorite record store. It\'s a basement-level space, but somehow still has a ton of deeply sun-faded promo posters (which they refuse to sell you, no matter how many times you ask). There\'s  a \"book section\" with a bunch of old issues of Rolling Stone and Maximum Rocknroll, some fat little 20th-century-summarizing record review books, a couple Elvis biographies, and a weird amount of 90s porno mags. A box of Grateful Dead bootleg tapes (both audience and soundboard) sits near the counter. The $1 CD wall promises scuffed-up copies of BMG Music Club one-hit-wonder flotsam, and always more than a few Ani DiFranco selections (why?). There are also, naturally, a ton of used vinyl records for sale.', ['1) Dig in some crates'], [1]),
    1: Section('There\'s a \"Beatles\" section that only ever has solo George and Ringo albums, and cover compilations like the \'All This and World War II\' soundtrack. If you wanted to get down on your knees and crawl, a bunch of forgettable 78s wait for you under the main bins (never any rock n\' roll, and definitely never any "race records"). The few times you\'ve flipped through their decaying paper sleeves, you\'ve worried about potential asbestos content. There is a wall of cassettes but that\'s a 50-50 shot at buying something that\'s melted into a warbly hell in somebody\'s backseat.\n\nDespite all this, the store usually has a few gems. You\'ve narrowed it down to three titles.\n\n\033[33mWARNING:\033[0m Your decision will greatly determine your fate!', ['1) ' + '\033[31m' + 'Aja by Steely Dan'+'\033[0m', '2) ' + '\033[32m'+'Moving Pictures by Rush' + '\033[0m', '3) ' + '\033[34m'+'The Lamb Lies Down on Broadway by Genesis'+'\033[0m',], [2, 3, 4]),
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
    18: Section('"Aja. Nice, man. Classic. Did you know they didn\'t want Purdie to do a shuffle on \'Home At Last\' but he managed to sneak it in anyway?? That guy was a trip, man. He\'d set up little signs next to his kit that said shit like "YOU DID IT, YOU HIRED THE HITMAKER." I love that shit man. Have you read \'Reeling in the Years\'? \'Major Dudes\' is okay but it\'s mostly old Rolling Stone reviews and shit. \'Eminent Hipsters\' is fun if you dig Fagen rambling on about jazz and being a crabby old bastard. That 33 1/3 book is fine too but I\'d skip it and just watch the \'Classic Albums\' documentary. It\'s on YouTube with Japanese subtitles for some reason, hasn\'t been copyright flagged yet."', ['1) "Oh really? Nice. That\'s cool man."', '2) "Yes. I know all this."', '3) Silence. Stonewall him until he runs out of gas.'], [21, 22, 23]),
    19: Section('"Moving Pictures, unimpeachable man, truly unimpeachable. How do you get two songs like Tom Sawyer and Limelight on the same record? It\'s almost unfair. I got so into this band and then I\'m reading along with the lyrics on 2112 and they thank Ayn Rand...? The GENIUS of Ayn Rand....!?!? Broke my heart, man. How can ya be so progressive musically and so back-asswards in the political realm."', ['1) "I dunno, man. That\'s rough."', '2) "Yeah."', '3) Silence. Stonewall him until he runs out of gas.'], [21, 22, 24]),
    20: Section('"And the Laaaaaaaamb.... Lies Dowwwwwwwn.... on Broo-OO-ooadway!! Hell yeah man. Gabriel\'s last stand. Carpet Crawlers is a stone classic, man. You ever see the live show they did where he tells that trippy story before going into Supper\'s Ready? Is that on here (*looks at sleeve*) ah shit, that\'s right it\'s on Foxtrot. Another heavy one. Did you know Eno worked on this one? Makes sense if you look at the hair they were both sporting at the time."', ['1) "Oh really? Nice. That\'s cool man."', '2) "Yes. I know all this."', '3) Silence. Stonewall him until he runs out of gas.'], [21, 22, 25]),
    21: Section('He holds up the sleeve and calls to \033[31mJeffery\033[0m, the teen-aged stock boy. "JEFF! You heard this one yet? Stone classic."\n\nJeff gives a thumbs-up; he\'s either familiar with it or knows well enough to let sleeping tigers lie.\n\n"Kids today, man. The internet! I had to know somebody hip to get into any halfway decent records when I was that young. Pat Boone, Sing Along with Mitch type shit in my parents\' hi-fi all the time, man. Who needs it.\n\n"That\'ll be \033[32m$34.98\033[0m."', ['1) Pay the man.'], [29]),
    22: Section('Phil looks a bit stung; clearly he thought your acquaintance was on its way to proper friendship. He was maybe even going to invite you to the barbecue this weekend, held in the parking lot behind the store (you\'ve always thought that seemed like a cool, scofflaw kind of event). \n\n"Your total is \033[32m$34.98\033[0m."', ['1) Pay the man.'], [29]),
    23: Section('"Not a weak track on there, man. Can you imagine how many people are getting into the Dan just from hip hop samples? De La Soul using \'Peg\', Peter Gunz and Lord Tariq using \'Black Cow\'... not to mention Kanye using \'Kid Charlemagne\' but we\'re out in the weeds now, talking about \u001b[36mthe Royal Scam\033[0m. Underrated disc, if you ask me. \'Everyone\'s Gone to the Movies\' is such a sleeper creeper of a song!"', ['1) ...'], [26]),
    24: Section('"People like to rag on the Rush boys, but I never quite got that-- they\'re as legitimate as anybody, progressive or moderate. Whatever your stance is on weird time signatures and fretless double-necked guitars, they were layin\' down some heavy, ponderous shit! For my dollar anyway. Well they\'re Canadian, so I guess my seventy-three cents."', ['1) ...'], [27]),
    25: Section('"Oh the purists like to jump ship around \u001b[36mTrick of the Tail\033[0m, but I followed these guys clear through to \033[35mInvisible Touch\033[0m. Is the production style really dated? Of course! Is the video for Land of Confusion terrifying? Absolutely! But I\'ll be damned if it isn\'t still top notch quality tuneage."', ['1) ...'], [28]),
    26: Section('(to the tune of \'Rikki Don\'t Lose That Number\')\n\n"\033[32m$34.98\033[0m- ah! \u266b\nYou can leave the money on the thing, \u266b\nGet your change in a minute, da-daah-dinnnng \u266b"', ['1) Pay the man.'], [29]),
    27: Section('(to the tune of \'Limelight\')\n\n"\033[32m$34.98\033[0m, \u266b\nis how much you must pay, \u266b\nfor this re-cord-to-play! \u266b\nHm hm, daaaa, da daahda dum, ga THMP THMP da daah daaaaaahhhh \u266b"', ['1) Pay the man.'], [29]),
    28: Section('(to the tune of \'Invisible Touch\')\n\n"That\'ll be, \033[32m$34.98\033[0m- ah! \u266b\nPut the cash, \u266b\nright- down- here-on-the-thing! \u266b"', ['1) Pay the man.'], [29]),
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
    39: Section('"What did you just say to me you piece of shit? Nobody LIKES you here. Did you know that? I\'m glad I slept with your wife last year. Go the fuck inside and listen to your jazz fusion whatever-the-fuck. If I hear that shit through the walls again I\'m gonna knock down this door and break your goddamn legs. FUCK you"', ['1) Go inside.'], [42]),
    40: Section('"They\'re incredible! God, they\'re just the best.\n\n\033[31mDean\033[0m just started middle school, the little spaz. Always going on about some new bullshit I gotta buy him so he can fit in. Buncha weird shit. Made in China. I don\'t know man.\n\n\033[31mErica\033[0m, god bless her, she\'s still in diapers and I\'m in no hurry to see that change. I\'m gonna fucking murder the first boy who kisses her."', ['1) "Ah. Nice, that\'s just great. I gotta head in man, great seeing ya."'], [42]),
    41: Section('"\033[31mDebbie\033[0m? Hot as ever, man. You know; we all know. It\'s ok, I know all the guys around here like to look. I don\'t mind a quick glance but you better keep it zipped up pal!! I\'m a generous enough guy but let\'s just say we can\'t share EVERYthing with our neighbors! Hahahaha. Tight knit community here at Ridgewood but get outta here, I don\'t think so nosiree."', ['1) "Ah. Nice, that\'s just great. I gotta head in man, great seeing ya."'], [42]),
    42: Section('You go inside.\n\nYour apartment is a modest one. The main door opens into your living room, where there is a very weathered couch, glass coffee table, and small television with VCR. You used to have a Laserdisc player too (the only choice for anyone who cares about sound even a little), but you lost that in the divorce. Your apartment is technically a two bedroom, but one of those became the listening room as soon as you moved in.', ['1) Feed Jaco.'], [43]),
    43: Section('Jaco is very glad to have a fresh bowl of food. Even with the sensitive-stomach blend, it\'ll still be an 80/20 chance of him vomiting in the next day or two. You love him anyway though, perhaps even more than the smooth fretless bass tones of his namesake.', ['1) Move to the listening room.', '2) Have a nice snack first.'], [45, 44]),
    44: Section('You go to the kitchen to prepare your go-to snack: a slice of Muenster cheese melted on some 12-grain bread, paired with a tall glass of 2% milk. You don\'t remember when you started making this, but you\'re very glad nobody but your cat is here to see you eating it.', ['1) Now you\'re ready to listen, to appreciate.'], [45]),
    45: Section('You enter the listening room.\n\nThis is your sanctum santorum. In here you cannot hear the troubles of the outside world, figuratively or literally.\n\nThe speakers are nice, tall \033[34mBang & Olufsen Beolab Penta 2\033[0ms that you got second-hand from your pal \033[33mDave\033[0m when he upgraded to the Penta 3\'s. Your receiver is a \033[32mMcIntosh MAC1700\033[0m that you have proudly (but very nervously) serviced yourself over the years. The turntable that\'ll spin your new purchase is a handsome wood-finish \033[31mLinn LP12\33[0m with a \033[35mLyra Delos\033[0m cartridge, per the recommendations of a complete stranger on the internet. An empty wood shelf sits on the wall a bit above your hi-fi stack, reserved for the day you finally pull the trigger on a reel-to-reel tape deck.\n\nYou also have a mediocre SACD player that you have not used in three years.', ['1) Turn everything on and let it warm up for a good half hour.\nLot of tubes in there, lot of voltage that needs stabilizing.'], [46]),
    46: Section('Your system makes a series of satisfyingly bold clicks and pops as you turn the components on.', ['1) Sit in silence.'], [47]),
    47: Section('You sit in the room\'s lone chair and think about things for a half hour.', ['1) Think about your hi-fi setup.', '2) Think about your ex-wife.', '3) Check tomorrow\'s weather.'], [48, 49, 50]),
    48: Section('You wonder sometimes about switching up your phono cartridge, but on your salary you can\'t exactly afford to have a whole fleet of them to pick from. You try to get in the occasional demo session at the hi-fi shop two towns over, but you\'re careful to not stop by TOO often and be seen as some kind of freeloader. No matter how deep into a niche hobby you dig yourself, your pre-existing anxieties will always be in there with you unless you decide to actually work on yourself in earnest. Maybe talk to someone, read one of the books the marriage counselor gave you when it was just a trial separation and not a full and legal divorce.', ['1) Well, everything should be warmed up by now.'], [56]),
    49: Section('\033[35mSheila\033[0m...\n\nWhat is she doing right now, you wonder. Did she throw herself back into her painting after the split? You always felt like you kept her from her creative pursuits on some level. Maybe you critiqued works in progress one too many times, you\'re not sure, but eventually the canvas and easel just stopped coming out altogether.', ['1) How did you two meet again?'], [51]),
    50: Section('You check your smartphone before remembering it might be adding unwanted electrical interference to your otherwise sealed-off listening room. (The weather will be fine tomorrow.)', ['1) Put your phone in the other room.'], [54]),
    51: Section('You met Sheila through some mutual friends. \03333mFred\033[0m was the one hosting the party, you think. It\'s so long ago now. It was awkward at first, feeling such an electric and mutual attraction to someone you just met, and trying hard to not show it too soon. You looked for openings all night, and at some point felt so bold as to claim an empty seat on the ottoman next to her when its occupant flitted over to a different conversation circle in the kitchen. You managed to get past the clunkiness of the first few small-talk questions, finding shared interest in Fred\'s shelf of artist monographs (more specifically a shared distaste for Jackson Pollack and his CIA ties). You walked her home that night; you still don\'t know where you found the nerve to propose that. Or make that first phone call two afternoons later.', ['1) Remember last summer at Cape Cod?'], [52]),
    52: Section('God, the Cape Cod trip. A second honeymoon of sorts, an unexpected oasis in the middle of weeks of fighting. It was as if a change of scenery somehow put an unspoken truce into effect. You overshot the tacit "tolerate one another" promise of most tired-marriage vacations, and ended up back in some kind of pleasantly naïve teenage place, emotionally speaking. You brought wine but ended up drinking none of it, intoxication would have felt redundant.', ['1) Where did it all go wrong?'], [53]),
    53: Section('You stopped listening, mostly. Stopped showing up, being present. Dove full force into your hobbies, and became a kind of shadow of yourself. None of it was her fault and you hate that she thinks it was.', ['1) Tubes are probably warmed up by now. Let\'s hear this new disc.'], [56]),
    54: Section('You go back into the living room and put your phone face-down on the coffee table, after putting it into Airplane Mode for additional security against unwanted vibrations. Jaco looks up from a nap he\'s drifting in and out of.', ['1) Pet Jaco.'], [55]),
    55: Section('You give Jaco some behind-the-ear skritches. He\'ll always be here for you.', ['1) Head back in and listen to your new record!'], [56]),
    56: Section('Over the years, you\'ve developed a delicate technique for unsleeving a record and only touching the edges and the label. You all but lunge at anyone who tries to put something on at your parties, fearing they\'ll get their grubby fingerprints all in the grooves. You haven\'t held a party in six years', ['1) Let\'s get this cleaned up.'], [57]),
    57: Section('Even the cleanest-looking of records can still be filthy, so you turn to your trusted \033[32mRECORD DOCTOR V\033[0m, a vacuum-based machine. After applying the right amount of cleaning solution to Side 1, you place it face-down over its brush-lined vacuum slit. There\'s a hockey puck shaped handle thing you put on top of the label that has little grips so you can turn the disc manually (you can\'t yet afford a full-auto disc washer, and this has irked you for years). The machine whines like a full-size canister vacuum cleaner, and you let it do its thing for three slow revolutions of the LP. This is the part where Jaco usually hides under the couch.\n\nYour disc now shines magnificently.', ['1) Pop it on the turntable!'], [58]),
    58: Section('You place it on your turntable with the utmost care.', ['1) Throw a nice heavy weight on the center label.'], [59]),
    59: Section('You secure a big brass doorknob looking thing on top of the disc. No chance it will drift or wobble now.', ['1) What about static though?'], [60]),
    60: Section('The disc looks totally free of dust, but static is the invisible menace! You take your carbon fiber brush and let the LP spin three times underneath its light touch.', ['1) But is the needle itself clean?'], [61]),
    61: Section('Just to be safe, you do the melamine trick you learned about, taking a \'Magic Eraser\' pad and delicately lowering the needle onto it a few times. (Strictly vertically! Horizontal motion could fuck the needle up but good, you\'re told.) It\'s a small blessing that your turntable has a cue lever for this.', ['1) Sit in your listening chair.'], [62]),
    62: Section('You ease into your favorite listening chair, a mid-range IKEA job called \033[33mEKERÖ\033[0m that you picked up because it reminded you of the old Maxell commercials.\n\nWait, what in the hell is that buzz?', ['1) Check the speaker wires', '2) Check the turntable ground wire', '3) Turn off all the lights in your apartment in case they\'re interfering somehow.'], [63, 64, 65]),
    63: Section('The speaker wires look ok! Nothing is loose, no spindly little shits poking out from your top-notch wire twisting job a few years back.', ['1) Check the turntable ground wire.', '2) Turn off all the lights in your apartment in case they\'re interfering somehow.'], [64, 67]),
    64: Section('That\'s it! The ground wire on the turntable somehow came loose.', ['1) Reattach that guy!'], [68]),
    65: Section('You turn off all the kitchen and living room lights, but when you return to the listening room the buzz is still there.', ['1) Check the speaker wires.', '2) Check the turntable ground wire.'], [66, 64]),
    66: Section('The speaker wires look ok! Nothing is loose, no spindly little shits poking out from your top-notch wire twisting job a few years back.', ['1) '], [64]),
    67: Section('You turn off all the kitchen and living room lights, but when you return to the listening room the buzz is still there.', ['1) Check the turntable ground wire.'], [64]),
    68: Section('The buzz is gone!\n\nIt\'s time at last to spin this record.', ['1) Drop the needle!'], [69, 70, 71]),
    69: Section('Hell yeah. Side 1, Track 1 of AJA.... \n\n\033[31m\'Black Cow\'\033[0m', ['1) Take the needle off the record.'], [72]),
    70: Section('Hell yeah. Side 1, Track 1 of MOVING PICTURES.... \n\n\033[32m\'Tom Sawyer\'\033[0m', ['1) Take the needle off the record.'], [72]),
    71: Section('Hell yeah. Side 1, Track 1 of THE LAMB LIES DOWN ON BROADWAY.... \n\n\033[34m\'The Lamb Lies Down on Broadway\'\033[0m', ['1) Take the needle off the record.'], [72]),
    72: Section('What the fuck. "Near Mint"!? And the first fucking SONG has a skip? You could kill Phil. What kinda mickey mouse goddamn moron operation is he running down there', ['1) Re-sleeve the LP.', '2) Eat your feelings.', '3) Go for a walk to try and calm down.'], [73, 74, 75]),
    73: Section('You try to steady your hands to put the record away. Goddamnit, even a VG+ graded record should have played with no skips what the HELL.', ['1) Take the record back to the store.'], [76, 77, 78]),
    74: Section('You power through half a Sara Lee pound cake you have in the fridge.\n\nYou feel a bit sick, which proves to be a welcome distraction.', ['1) Take the record back to the store.'], [76, 77, 78]),
    75: Section('You decide to go for a walk around the apartment complex. There\'s a pool in the center courtyard area but nobody has used it in a while. A few leaves float near the edge, and you wonder how many times Chip\'s son has peed in there. Thank Christ you don\'t happen upon that guy or his shitty kid on your walk.\n\nYou\'re a little out of breath now, but not feeling any better about things.', ['1) Take the record back to the store.'], [76, 77, 78]),
    76: Section('You get into your car, and as you turn the engine over you catch the end of Black Cow on the radio, as if to specifically mock you.', ['1) Change the station.'], [79]),
    77: Section('You get into your car, and as you turn the engine over you catch the end of Tom Sawyer on the radio, as if to specifically mock you.', ['1) Change the station.'], [79]),
    78: Section('You get into your car, and as you turn the engine over you catch the end of The Lamb Lies Down on Broadway on the radio, as if to specifcally mock you.', ['1) Change the station.'], [79]),
    79: Section('You scan around for a while, but everything scares you. You wish you hadn\'t left your \033[33mPono\033[0m at home.', ['1) Drive in silence.'], [80]),
    80: Section('There\'s a noticeable whining sound. Your fan belt probably needs to be replaced.', ['1) Pull into the record store parking lot.', '2) Pass the store and go to your mechanic.'], [81, 82]),
    81: Section('You pull into the parking lot of the record store, and take a few breaths to steady yourself before going in and confronting Phil about his slip-up, about his goddamn blind-ass useless moron eyes not noticing that this record was going to skip like all HELL', ['1) Take a few more breaths.'], [83]),
    82: Section('You keep on driving. You can\'t tell if the whining noise is getting worse of if it\'s just your imagination, but it\'s probably a good idea to get it checked out sooner than later. \n\nYou pull into John\'s Garage.', ['1) Go see if John has some time today to look at it.'], [84]),
    83: Section('You take some deep breaths, "square breaths" as the counselor had called them.\n\nBreathe in for four seconds,\n hold it four seconds,\n let it out for four seconds,\n hold that for four more seconds.\n\nRepeat.\n\nIt\'s never worked particularly well for you, but you don\'t need an assault charge on your record today so you\'re trying real hard.', ['1) Go inside.'], [94]),
    84: Section('"Hey! What brings you here? Nope, stop right there, I\'ll tell ya what brings you here: fan belt. I could hear ya from the toilet when you pulled in. I can pop a new one on there once I\'m done this guy I got up on the lift here, if you can wait about half an hour."', ['1) Plop down in one of the waiting room chairs.'], [85]),
    85: Section('It smells like grease and gasoline, with an air freshener not pulling quite enough weight. It\'s a comforting smell; you used to like waiting for the old Monte Carlo to get tuned-up when you were a child. You would read whatever book you had on you, and if you were lucky your dad would give you a quarter for the M&M machine.\n\nDoes this garage have one of those, you wonder?', ['1) It does!'], [86]),
    86: Section('Oh hell yes.\n\nThe handle produces a strangely satisfying grinding noise as you turn it, and the way-past-expired candies fall down their chute and hit the metal retainer flap. You pop some of them in your mouth and wonder what the deal is with expired ones, why do the shells crack over time? You feel like you should be able to suss out the science of it, but you come up blank. There\'s probably a youtube video about this.\n\nThe specific taste and texture of the stale M&M\'s has completed the transformation: you are a kid again for these few minutes.', ['1) Remember the tan-colored M&M\'s?'], [87]),
    87: Section('Yeah! They used to have brown AND tan...? What boring shit is that. Remember when they did the contest to decide on the new color. You had to call some 1-800 number or something. What were the colors...it was Blue, Pink, and.... Purple?\n\nWas that it?', ['1) Was it?'], [88]),
    88: Section('You think so, yeah. It\'s all kinda redundant now, huh. You can go to those specialty candy stores, or god forbid the huge M&M store in Times Square, and just get whatever colors you want.', ['1) Do you think they have to swap out the blue ones for\nspecial-ordered tan ones in period movies?'], [89]),
    89: Section('They must! Well, any prop department worth a damn probably does, anyway.', ['1) There\'s probably a youtube video about it.'], [90]),
    90: Section('"Yo! Your car\'s all set."\n\nJohn is waving his hand in front of your face.', ['1) "Thanks, man! What do I owe ya?"'], [91]),
    91: Section('"$110."\n\nShit. You don\'t have nearly enough cash on you."', ['1) "You guys take cards?"'], [92]),
    92: Section('"Sure, sure. Give \'er here."\n\nHe runs your Discover card through one of those old carbon-copy machines that makes almost as satisfying a noise as the vending machine crank did.', ['1) Let\'s go return this record.'], [93]),
    93: Section('You\'re back on the road and everything\'s sounding normal under the hood. John always does a pretty stellar job with your Tercel.', ['1) Park in front of the record shop.'], [104]),
    94: Section('You calmly (you think) walk into the shop, but Phil is nowhere to be found. You see that teen-aged stockboy Jeff though, and wave him over. He tells you that Phil stepped out.', ['1) "Well do you know when he\'ll be back?"'], [95]),
    95: Section('"He went home to grab something or other. He lives across the river so it\'ll be a while. You can hang out here till he gets back if you want."\n\nThanks, cool, great.', ['1) Wait for him.', '2) Go get your car looked at.'], [96, 97]),
    96: Section('You hang out for a while awkwardly, and look through some old 12" promotional flats. You try to make conversation with Jeff at one point but it\'s unsustainably awkward and you both do your best to just not look each other in the eye after that.', ['1) Just look through some more merchandise, then.'], [98]),
    97: Section('You go outside and try your best, but now the car won\'t start at all.', ['1) Fuckin\' awesome. Cool. Go back inside.'], [98]),
    98: Section('You try your best to center yourself but you\'re in a dark-ass place now. Except whoa shit wait, when did they get a laserdisc section..!? You didn\'t even see that before.', ['1) Makes sense, they\'re identical to LPs basically (especially when shelved).'], [99]),
    99: Section('There\'s even some CEDs!', ['1) Look through those.', '2) What is a CED?'], [100, 101]),
    100: Section('Oh damn they have \033[96mLet It Be\033[0m! In all its overhyped, very mild awkwardness. This is basically unaffordable in any other home video format. ', ['1) I should grab it.'], [102]),
    101: Section('Oh man dude, CEDs are interesting as hell, they\'re like this worse-quality-than-VHS disc that\'s basically a vinyl record, but for video. It lives in this big square plastic housing but once it\'s in the machine there\'s a stylus that goes into a groove on the disc, and it can even skip like a record (and these used ones almost always do), it\'s a whole thing.', ['1) Well are there any good titles?'], [100]),
    102: Section('You don\'t even have a machine to play it on!\n\nAlso there\'s no time for that-- Phil just got back.', ['1) Go confront him.'], [103]),
    103: Section('"Heya buddy! Back so soon?"', ['1) "Hey man, got a little problem here."', '2) "Shut the hell up. Just shut up. What the fuck is the idea!?"', '3) Take a swing at Phil.'], [105, 106, 107]),
    104: Section('You park your car toward the middle of the lot (thinking this is some kind of sly exercise if you do it often enough) and head inside. Phil is there, setting down a sweaty styrofoam food container.', ['1) Go confront him.'], [103]),
    105: Section('"What\'s the issue, friend?"', ['1) Explain what happened, including every step of your cleaning ritual.'], [111]),
    106: Section('He looks legitimately scared of you; this is not a person who seeks out or relishes conflict in the first place, and your raised voice has the whole store\'s attention.\n\n"... W-What\'s the matter?"', ['1) Explain what happened, including every step of your cleaning ritual.'], [109]),
    107: Section('You attempt to suckerpunch Phil but he\'s fast, too fast. He dodges it, and with improbable speed Jeffery gets you into a halfnelson from behind. Before you know it he has pulled some kind of Brazilian Jiu-Jitsu move on you and the last thing you hear before losing consciousness is Phil remarking that ya know, before they were Sparks, they were called Halfnelson.', ['1) Wake up in the hospital.'], [108]),
    108: Section('You wake up in some kind of low-urgency part of the city hospital, whatever the opposite of an ICU is.\n\nYour bill is exorbitant and you still have a scratched record.\n\n\033[31mBAD ENDING\033[0m', ['Press \'Q\' to exit the game.'], []),
    109: Section('"Okay man, well you can return it for store credit if you see something you like. I\'m usually pretty diligent about grading the merchandise, I\'m sorry you had to come all the way back here."\n\nHe\'s such a goddamn nice and patient guy. You feel terrible.', ['1) "Uh. Thanks, I\'ll take a look around."'], [110]),
    110: Section('You look around for a while and end up buying your fifth copy of \033[94mThe Nightfly\033[0m by Donald Fagen, and a couple old Motown cassettes.\n\n\033[33mMEDIOCRE ENDING\033[0m', ['Press \'Q\' to exit the game.'], []),
    111: Section('"Damn, I\'m really sorry to hear that! We usually only do store credit, but you\'re in here all the time, so let\'s just go ahead and get you your cash back.', ['1) "Aw man, really? Thanks!"'], [112]),
    112: Section('You no longer possess a scratched record!\n\nYou decide to look around a bit more, and end up finding a copy of \033[34mSync\033[31mhroni\033[33mcity\033[0m by The Police that has the rare bronze/silver/gold cover variant! You can flip this on eBay even if the disc ends up being scratched, but you\'re pretty sure you\'ll just keep it since you almost never see these.', ['1) Whoa, and it\'s only priced at $20..?'], [113]),
    113: Section('This is a pretty excellent find! You decide to buy this as well as your fifth copy of \033[94mThe Nightfly\033[0m by Donald Fagen and call it a day.\n\n\033[32mGOOD ENDING\033[0m', ['Press \'Q\' to exit the game.'], []),
}

# places where the record purchased will affect player's outcomes

anomalies = [15, 16, 17, 30, 68, 73, 74, 75]


# places where things cost/gain the player money, and how much

payments = {29: 34.98, 34: 17.98, 86: 0.25, 93: 110.00, 113: 32.50}
windfall = {112: 34.98}

# places the player can gain points

goodcall = [2, 3, 4, 15, 21, 36, 44, 64, 87, 105]


# initial welcome screen & name prompt

welcome = 'Welcome to AUDIOPHILIA, the game of hi-fi perfection!\n\nPlease enter your name.'

clear()

print()
print(welcome)
print()
intro = input('-->')

while player.name == '':
    if intro != '':
        player.name = intro.capitalize()
    else:
        clear()
        print()
        print("Please enter a name.")
        print()
        intro = input('--> ')

print()
print(f'Welcome, {player.name}!')


# main game loop

while True:

    current = player.prog


    # did the player buy something by taking this path?

    for key, value in payments.items():
        if key == player.prog:
            player.money -= value

    for key, value in windfall.items():
        if key == player.prog:
            player.money += value


    # did the player gain a point?

    if player.prog in goodcall:
        player.points += 1
    
    clear()


    # player status ribbon at the top of each screen

    print(f'\033[1;30;47mAUDIOPHILIA   Player: {player.name}   Points: {player.points}   Money: ${player.money:.2f}\033[0m')

    # description of where the player currently is

    print()
    print(linebreaks(parts[current].desc))
    
    print()


    # specific audio playback preparation cases

    if player.prog == 2:
        player.inv = 'aja'
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

    
    # for audio playback and delay of next-choices set in these specific places

    if player.prog == 69:
        pygame.mixer.music.play()
        time.sleep(36) 

    if player.prog == 70:
        pygame.mixer.music.play()
        time.sleep(22) 

    if player.prog == 71:
        pygame.mixer.music.play()
        time.sleep(53) 


    # to stop the music in one specific place

    if player.prog == 72:
        pygame.mixer.music.stop()


    # prompt to choose a valid option, should the player try not to

    if player.err == True:
        print('\033[35mPlease choose from the available selections.\033[0m')
        print()
        player.err = False


    # display of player's choices after each description

    for i in parts[current].opt:
        print('\033[90m'+i+'\033[0m')
    
    print()


    # player input

    cmd = input("-->")

    def choicehandler(choice):
        
        adjust = int(choice) -1
        optnum = len(parts[current].opt)

        # for places in the 'anomalies' list
        if int(choice) <= optnum and player.prog in anomalies:
            if 'aja' in player.inv and int(choice) == 1:
                player.prog = parts[current].path[0]
            elif 'rush' in player.inv and int(choice) == 1:
                player.prog = parts[current].path[1]
            elif 'lamb' in player.inv and int(choice) == 1:
                player.prog = parts[current].path[2]

        #for normal inputs
        elif int(choice) <= optnum and player.prog not in anomalies:
            if cmd == parts[current].opt[adjust][0]:
                player.prog = parts[current].path[adjust]
        
        #for choice outside the number listed
        else:
            player.err = True

    # to quit the game
    if cmd == "q" or cmd == "Q":
        clear()
        break
    
    # list of valid inputs in the game (after name screen)
    valid = ["q", "Q", "1", "2", "3", "4"]

    # in case player hits anything but a choice or the 'Quit' command
    if cmd not in valid:
        player.err = True
    else:
        choicehandler(cmd)
