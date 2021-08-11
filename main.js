(function main() {
  'use strict';

  // Data {{{
  const data = new Map([
    [
      0,
      {
        description: `<p>You are in your favorite record store. It's a basement-level space, but somehow still has a ton of deeply sun-faded promo posters (which they refuse to sell you, no matter how many times you ask). There's  a "book section" with a bunch of old issues of Rolling Stone and Maximum Rocknroll, some fat little 20th-century-summarizing record review books, a couple Elvis biographies, and a weird amount of 90s porno mags. A box of Grateful Dead bootleg tapes (both audience and soundboard) sits near the counter. The $1 CD wall promises scuffed-up copies of BMG Music Club one-hit-wonder flotsam, and always more than a few Ani DiFranco selections (why?). There are also, naturally, a ton of used vinyl records for sale.</p>`,
        choices: [
          {
            description: 'Dig in some crates',
            moveTo: 1,
          },
        ],
      },
    ],
    [
      1,
      {
        description: `<p>There's a "Beatles" section that only ever has solo George and Ringo albums, and cover compilations like the 'All This and World War II' soundtrack. If you wanted to get down on your knees and crawl, a bunch of forgettable 78s wait for you under the main bins (never any rock n' roll, and definitely never any "race records"). The few times you've flipped through their decaying paper sleeves, you've worried about potential asbestos content. There is a wall of cassettes but that's a 50-50 shot at buying something that's melted into a warbly hell in somebody's backseat.nnDespite all this, the store usually has a few gems. You've narrowed it down to three titles.</p><p><em>WARNING:</em> Your decision will greatly determine your fate!</p>`,
        choices: [
          {
            description: 'Aja by Steely Dan',
            item: 'aja',
            getPoints: true,
            moveTo: 2,
          },
          {
            description: 'Moving Pictures by Rush',
            item: 'rush',
            getPoints: true,
            moveTo: 3,
          },
          {
            description: 'The Lamb Lies Down on Broadway by Genesis',
            item: 'lamb',
            getPoints: true,
            moveTo: 4,
          },
        ],
      },
    ],
    [
      2,
      {
        description: '<p>Nice, a classic. What pressing is it?</p>',
        choices: [
          {
            description: `Let's check!`,
            moveTo: 5,
          },
        ],
      },
    ],
    [
      3,
      {
        description: '<p>Nice, a classic. What pressing is it?</p>',
        choices: [
          {
            description: `Let's check!`,
            moveTo: 6,
          },
        ],
      },
    ],
    [
      4,
      {
        description: '<p>Nice, a classic. What pressing is it?</p>',
        choices: [
          {
            description: `Let's check!`,
            moveTo: 7,
          },
        ],
      },
    ],
    [
      5,
      {
        description: `<p>There's a thread on the Steve Hoffman forums with over 650 posts in it, but you're not about to traipse through all that bullshit in full, on your smartphone, here at the store. People seem pretty over the moon about an original pressing with <em>AB-1006033</em> carved into the deadwax.</p>`,
        choices: [
          {
            description: 'Check the deadwax',
            moveTo: 8,
          },
        ],
      },
    ],
    [
      6,
      {
        description: `<p>'The Rush Vinyl Pressing Thread' on the Steve Hoffman forums says to check the deadwax to see if both sides have an <em>'RL'</em> (for <em>Robert Ludwig</em>). A lot of people are arguing for various CD masterings too but you're not about the digital life anymore, not since dropping well over $600 on a turntable cartridge alone.</p>`,
        choices: [
          {
            description: 'Check the deadwax',
            moveTo: 9,
          },
        ],
      },
    ],
    [
      7,
      {
        description: `<p>You discreetly (you think) pull out your phone and see what people are saying about it on the Steve Hoffman forums. They all seem to be fawning over the <em>200g Classic Records reissue</em> from 2001. Weird time for vinyl, you almost never see stuff from that era second-hand.</p><p>Could this be…?</p>`,
        choices: [
          {
            description: 'Could it?',
            moveTo: 10,
          },
        ],
      },
    ],
    [
      8,
      {
        description: `<p>Hell yeah, there it is! <em>AB-1006</em>!</p>`,
        choices: [
          {
            description: 'Inspect the rest of the disc.',
            moveTo: 11,
          },
        ],
      },
    ],
    [
      9,
      {
        description: `<p>Clear as day on both sides, <em>'RL'</em>! Dutch pressing, apparently.</p>`,
        choices: [
          {
            description: 'Inspect the rest of the disc.',
            moveTo: 11,
          },
        ],
      },
    ],
    [
      10,
      {
        description: `<p>It could! <em>'Manufactured and Distributed under exclusive license to Classic Records'</em> is there on both the center labels and the back cover, otherwise it looks like an Atco original.</p><p>Hell yeah!</p>`,
        choices: [
          {
            description: 'Inspect the discs.',
            moveTo: 12,
          },
        ],
      },
    ],
    [
      11,
      {
        description: `<p>Looks real clean! Aged for sure, but no big scuffs or scratches that you can see.</p>`,
        choices: [
          {
            description: 'Take this bad boy up to the counter!',
            moveTo: 13,
          },
        ],
      },
    ],
    [
      12,
      {
        description: `<p>They look good! The Near Mint grading on the price sticker isn't far off.</p>`,
        choices: [
          {
            description: '<p>Take this bad boy up to the counter!</p>',
            moveTo: 13,
          },
        ],
      },
    ],
    [
      13,
      {
        description: `<p>You walk up to the counter with some excitement but also considerable dread that the clerk is going to want to talk to you, a lot.</p>`,
        choices: [
          {
            description: `Who's working?`,
            moveTo: 14,
          },
        ],
      },
    ],
    [
      14,
      {
        description: `<p><em>Phil</em> is working the register today. An old hand for sure, a hi-fi wizard with waist-length grey hair tied back in an intricate braid. He's friendly enough, but does not value anyone's time particularly highly.</p>`,
        choices: [
          {
            description: `"Hey man! How's it going?"`,
            getPoints: true,
            moveTo: 15,
          },
          {
            description: `Approach in silence.`,
            moveTo: 16,
          },
          {
            description: `Mutter to yourself angrily in the hopes he'll be too scared to engage.`,
            moveTo: 17,
          },
        ],
      },
    ],
    [
      15,
      {
        description: `<p>"Hey, brotherman. How's it hangin'. Balmy day out there, man. Balmy. Have people been using that word a lot more lately? I feel like I'm hearing that shit all day everyday man. We don't have THAT many balmy days, but I gotta give it to 'em today, it's a balmy one.</p><p>Whatcha got there?"</p>`,
        choices: [
          {
            description: 'Put your purchase on the counter.',
            moveTo: {
              aja: 18,
              rush: 19,
              lamb: 20,
            },
          },
        ],
      },
    ],
    [
      16,
      {
        description: `<p>"Hello! What did ya find today?"</p>`,
        choices: [
          {
            description: 'Put your purchase on the counter.',
            moveTo: {
              aja: 18,
              rush: 19,
              lamb: 20,
            },
          },
        ],
      },
    ],
    [
      17,
      {
        description: `<p>"I can take who's next."</p>`,
        choices: [
          {
            description: 'Put your purchase on the counter.',
            moveTo: {
              aja: 18,
              rush: 19,
              lamb: 20,
            },
          },
        ],
      },
    ],
    [
      18,
      {
        description: `<p>"Aja. Nice, man. Classic. Did you know they didn't want Purdie to do a shuffle on 'Home At Last' but he managed to sneak it in anyway?? That guy was a trip, man. He'd set up little signs next to his kit that said shit like "YOU DID IT, YOU HIRED THE HITMAKER." I love that shit man. Have you read 'Reeling in the Years'? 'Major Dudes' is okay but it's mostly old Rolling Stone reviews and shit. 'Eminent Hipsters' is fun if you dig Fagen rambling on about jazz and being a crabby old bastard. That 33 1/3 book is fine too but I'd skip it and just watch the 'Classic Albums' documentary. It's on YouTube with Japanese subtitles for some reason, hasn't been copyright flagged yet."</p>`,
        choices: [
          {
            description: `"Oh really? Nice. That's cool man."`,
            getPoints: true,
            moveTo: 21,
          },
          {
            description: `"Yes. I know all this."`,
            moveTo: 22,
          },
          {
            description: `Silence. Stonewall him until he runs out of gas.`,
            moveTo: 23,
          },
        ],
      },
    ],
    [
      19,
      {
        description: `<p>"Moving Pictures, unimpeachable man, truly unimpeachable. How do you get two songs like Tom Sawyer and Limelight on the same record? It's almost unfair. I got so into this band and then I'm reading along with the lyrics on 2112 and they thank Ayn Rand…? The GENIUS of Ayn Rand…!?!? Broke my heart, man. How can ya be so progressive musically and so back-asswards in the political realm."</p>`,
        choices: [
          {
            description: `"I dunno, man. That's rough."`,
            getPoints: true,
            moveTo: 21,
          },
          {
            description: `"Yeah."`,
            moveTo: 22,
          },
          {
            description: `Silence. Stonewall him until he runs out of gas.`,
            moveTo: 23,
          },
        ],
      },
    ],
    [
      20,
      {
        description: `<p>"And the Laaaaaaaamb… Lies Dowwwwwwwn… on Broo-OO-ooadway!! Hell yeah man. Gabriel's last stand. Carpet Crawlers is a stone classic, man. You ever see the live show they did where he tells that trippy story before going into Supper's Ready? Is that on here (*looks at sleeve*) ah shit, that's right it's on Foxtrot. Another heavy one. Did you know Eno worked on this one? Makes sense if you look at the hair they were both sporting at the time."</p>`,
        choices: [
          {
            description: `"Oh really? Nice. That's cool man."`,
            getPoints: true,
            moveTo: 21,
          },
          {
            description: `"Yes. I know all this."`,
            moveTo: 22,
          },
          {
            description: `Silence. Stonewall him until he runs out of gas.`,
            moveTo: 25,
          },
        ],
      },
    ],
    [
      21,
      {
        description: `<p>He holds up the sleeve and calls to <em>Jeffery</em>, the teen-aged stock boy. "JEFF! You heard this one yet? Stone classic."</p><p>Jeff gives a thumbs-up; he's either familiar with it or knows well enough to let sleeping tigers lie.</p><p>"Kids today, man. The internet! I had to know somebody hip to get into any halfway decent records when I was that young. Pat Boone, Sing Along with Mitch type shit in my parents' hi-fi all the time, man. Who needs it.</p><p>"That'll be <em>$34.98</em>."</p>`,
        choices: [
          {
            description: 'Pay the man.',
            cost: -34.98,
            moveTo: 29,
          },
        ],
      },
    ],
    [
      22,
      {
        description: `<p>Phil looks a bit stung; clearly he thought your acquaintance was on its way to proper friendship. He was maybe even going to invite you to the barbecue this weekend, held in the parking lot behind the store (you've always thought that seemed like a cool, scofflaw kind of event).</p><p>"Your total is <em>$34.98</em>."</p>`,
        choices: [
          {
            description: 'Pay the man.',
            cost: -34.98,
            moveTo: 29,
          },
        ],
      },
    ],
    [
      23,
      {
        description: `<p>"Not a weak track on there, man. Can you imagine how many people are getting into the Dan just from hip hop samples? De La Soul using 'Peg', Peter Gunz and Lord Tariq using 'Black Cow'… not to mention Kanye using 'Kid Charlemagne' but we're out in the weeds now, talking about <em>the Royal Scam</em>. Underrated disc, if you ask me. 'Everyone's Gone to the Movies' is such a sleeper creeper of a song!"</p>`,
        choices: [
          {
            description: '…',
            moveTo: 26,
          },
        ],
      },
    ],
    [
      24,
      {
        description: `<p>"People like to rag on the Rush boys, but I never quite got that—they're as legitimate as anybody, progressive or moderate. Whatever your stance is on weird time signatures and fretless double-necked guitars, they were layin' down some heavy, ponderous shit! For my dollar anyway. Well they're Canadian, so I guess my seventy-three cents."</p>`,
        choices: [
          {
            description: '…',
            moveTo: 27,
          },
        ],
      },
    ],
    [
      25,
      {
        description: `<p>"Oh the purists like to jump ship around <em>Trick of the Tail</em>, but I followed these guys clear through to <em>Invisible Touch</em>. Is the production style really dated? Of course! Is the video for Land of Confusion terrifying? Absolutely! But I'll be damned if it isn't still top notch quality tuneage."</p>`,
        choices: [
          {
            description: '…',
            moveTo: 28,
          },
        ],
      },
    ],
    [
      26,
      {
        description: `<p>(to the tune of 'Rikki Don't Lose That Number')</p><p>"<em>$34.98</em>—ah!</p><p>You can leave the money on the thing.</p><p>Get your change in a minute, da-daah-dinnnng."</p>`,
        choices: [
          {
            description: 'Pay the man.',
            cost: -34.98,
            moveTo: 29,
          },
        ],
      },
    ],
    [
      27,
      {
        description: `<p>(to the tune of 'Limelight')</p><p>"<em>$34.98</em>, is how much you must pay, for this re-cord-to-play! Hm hm, daaaa, da daahda dum, ga THMP THMP da daah daaaaaahhhh."</p>`,
        choices: [
          {
            description: 'Pay the man.',
            cost: -34.98,
            moveTo: 29,
          },
        ],
      },
    ],
    [
      28,
      {
        description: `<p>(to the tune of 'Invisible Touch')</p><p>"That'll be, <em>$34.98</em>—ah! Put the cash, right-down-here-on-the-thing!"</p>`,
        choices: [
          {
            description: 'Pay the man.',
            cost: -34.98,
            moveTo: 29,
          },
        ],
      },
    ],
    [
      29,
      {
        description: `<p>"Enjoy that thing, man! It'll sound boss on your setup, I just know it."</p>`,
        choices: [
          {
            description: 'Leave the shop.',
            moveTo: 30,
          },
        ],
      },
    ],
    [
      30,
      {
        description: `<p>You climb into your '98 Tercel, taking extra care to set your new purchase down on the passenger seat, all but buckling it in. As you coast down Main St., you get a small frisson of hope about your afternoon to come. A great find! Reference quality! You can just imagine what the guys will say when you have them over for a demonstration. The low end always scares <em>Jaco</em>, your faithful calico tomcat, but you know enough by now to gently usher him into the other room.</p><p>Oh shit! Jaco!</p><p>His food was low when you checked.</p>`,
        choices: [
          {
            description: 'Hang a left on Elm and head to the pet store.',
            moveTo: {
              aja: 31,
              rush: 32,
              lamb: 33,
            },
          },
        ],
      },
    ],
    [
      31,
      {
        description: `<p>You navigate to the pet shop and get his cat food (sensitive stomach, senior blend, goddamn $18).</p><p>You have <em>'Limelight'</em> stuck in your head though—you probably should have bought Moving Pictures instead.</p>`,
        choices: [
          {
            description: 'Goddamnit.',
            cost: -17.98,
            moveTo: 34,
          },
        ],
      },
    ],
    [
      32,
      {
        description: `<p>You navigate to the pet shop and get his cat food (sensitive stomach, senior blend, goddamn $18).</p><p>You have <em>'Carpet Crawlers'</em> stuck in your head though-- you probably should have bought The Lamb Lies Down on Broadway instead.</p>`,
        choices: [
          {
            description: 'Goddamnit.',
            cost: -17.98,
            moveTo: 34,
          },
        ],
      },
    ],
    [
      33,
      {
        description: `<p>You navigate to the pet shop and get his cat food (sensitive stomach, senior blend, goddamn $18).</p><p>You have <em>'Peg'</em> stuck in your head though-- you probably should have bought Aja instead.</p>`,
        choices: [
          {
            description: 'Goddamnit.',
            cost: -17.98,
            moveTo: 34,
          },
        ],
      },
    ],
    [
      34,
      {
        description: `<p>You head home, damn near broke at this point (good thing you didn't need gas!). It'll be worth it though; how often do you actually find a decent record, used, in this good of shape? Phil was right, it's going to sound boss as hell.</p>`,
        choices: [
          {
            description: 'Pull into your parking spot.',
            moveTo: 35,
          },
        ],
      },
    ],
    [
      35,
      {
        description: `<p>You're almost home free, but your neighbor <em>Chip</em> accosts you as you're about to put the key in the lock.</p>`,
        choices: [
          {
            description: `"Hey, man! What's the haps?"`,
            getPoints: true,
            moveTo: 36,
          },
          {
            description: `Nod, mumble something vague and go inside.`,
            moveTo: 37,
          },
          {
            description: `"Kind of in a hurry right now, Chip."`,
            moveTo: 38,
          },
          {
            description: `"Fuck off, Chip"`,
            moveTo: 39,
          },
        ],
      },
    ],
    [
      36,
      {
        description: `<p>"Can't complain! Can-not-complain, my man."</p>`,
        choices: [
          {
            description: 'Ask about his kids',
            moveTo: 40,
          },
          {
            description: 'Ask about his wife',
            moveTo: 41,
          },
          {
            description: 'Wrap things up and go inside.',
            moveTo: 42,
          },
        ],
      },
    ],
    [
      37,
      {
        description: `<p>"Next time! Man, sometime we gotta hit the pub and—"</p>`,
        choices: [
          {
            description: 'Close the door and lock it.',
            moveTo: 42,
          },
        ],
      },
    ],
    [
      38,
      {
        description: `<p>He seems a bit dejected, but generally unshakeable when in a good mood.</p><p>"Fast times at Ridgewood Apartments, I get it. Keep your stick on the ice, man!"</p>`,
        choices: [
          {
            description: 'Close the door and lock it.',
            moveTo: 42,
          },
        ],
      },
    ],
    [
      39,
      {
        description: `<p>"What did you just say to me you piece of shit? Nobody LIKES you here. Did you know that? I'm glad I slept with your wife last year. Go the fuck inside and listen to your jazz fusion whatever-the-fuck. If I hear that shit through the walls again I'm gonna knock down this door and break your goddamn legs. FUCK you"</p>`,
        choices: [
          {
            description: 'Go inside.',
            moveTo: 42,
          },
        ],
      },
    ],
    [
      40,
      {
        description: `<p>"They're incredible! God, they're just the best.</p><p><em>Dean</em> just started middle school, the little spaz. Always going on about some new bullshit I gotta buy him so he can fit in. Buncha weird shit. Made in China. I don't know man.</p><p><em>Erica</em>, god bless her, she's still in diapers and I'm in no hurry to see that change. I'm gonna fucking murder the first boy who kisses her."</p>`,
        choices: [
          {
            description: `"Ah. Nice, that's just great. I gotta head in man, great seeing ya."`,
            moveTo: 42,
          },
        ],
      },
    ],
    [
      41,
      {
        description: `<p>"<em>Debbie</em>? Hot as ever, man. You know; we all know. It's ok, I know all the guys around here like to look. I don't mind a quick glance but you better keep it zipped up pal!! I'm a generous enough guy but let's just say we can't share EVERYthing with our neighbors! Hahahaha. Tight knit community here at Ridgewood but get outta here, I don't think so nosiree."</p>`,
        choices: [
          {
            description: `"Ah. Nice, that's just great. I gotta head in man, great seeing ya."`,
            moveTo: 42,
          },
        ],
      },
    ],
    [
      42,
      {
        description: `<p>You go inside.</p><p>Your apartment is a modest one. The main door opens into your living room, where there is a very weathered couch, glass coffee table, and small television with VCR. You used to have a Laserdisc player too (the only choice for anyone who cares about sound even a little), but you lost that in the divorce. Your apartment is technically a two bedroom, but one of those became the listening room as soon as you moved in.</p>`,
        choices: [
          {
            description: 'Feed Jaco.',
            moveTo: 43,
          },
        ],
      },
    ],
    [
      43,
      {
        description: `<p>Jaco is very glad to have a fresh bowl of food. Even with the sensitive-stomach blend, it'll still be an 80/20 chance of him vomiting in the next day or two. You love him anyway though, perhaps even more than the smooth fretless bass tones of his namesake.</p>`,
        choices: [
          {
            description: 'Move to the listening room.',
            moveTo: 45,
          },
          {
            description: 'Have a nice snack first.',
            getPoints: true,
            moveTo: 44,
          },
        ],
      },
    ],
    [
      44,
      {
        description: `<p>You go to the kitchen to prepare your go-to snack: a slice of Muenster cheese melted on some 12-grain bread, paired with a tall glass of 2% milk. You don't remember when you started making this, but you're very glad nobody but your cat is here to see you eating it.</p>`,
        choices: [
          {
            description: `Now you're ready to listen, to appreciate.`,
            moveTo: 45,
          },
        ],
      },
    ],
    [
      45,
      {
        description: `<p>You enter the listening room.</p><p>This is your sanctum santorum. In here you cannot hear the troubles of the outside world, figuratively or literally.</p><p>The speakers are nice, tall <em>Bang & Olufsen Beolab Penta 2</em> that you got second-hand from your pal <em>Dave</em> when he upgraded to the Penta 3's. Your receiver is a <em>McIntosh MAC1700</em> that you have proudly (but very nervously) serviced yourself over the years. The turntable that'll spin your new purchase is a handsome wood-finish <em>Linn LP12</em> with a <em>Lyra Delos</em> cartridge, per the recommendations of a complete stranger on the internet. An empty wood shelf sits on the wall a bit above your hi-fi stack, reserved for the day you finally pull the trigger on a reel-to-reel tape deck.</p><p>You also have a mediocre SACD player that you have not used in three years.</p>`,
        choices: [
          {
            description:
              'Turn everything on and let it warm up for a good half hour. Lot of tubes in there, lot of voltage that needs stabilizing.',
            moveTo: 46,
          },
        ],
      },
    ],
    [
      46,
      {
        description:
          '<p>Your system makes a series of satisfyingly bold clicks and pops as you turn the components on.</p>',
        choices: [
          {
            description: 'Sit in silence.',
            moveTo: 47,
          },
        ],
      },
    ],
    [
      47,
      {
        description: `<p>You sit in the room's lone chair and think about things for a half hour.</p>`,
        choices: [
          {
            description: 'Think about your hi-fi setup.',
            moveTo: 48,
          },
          {
            description: 'Think about your ex-wife.',
            moveTo: 49,
          },
          {
            description: `Check tomorrow's weather.`,
            moveTo: 50,
          },
        ],
      },
    ],
    [
      48,
      {
        description: `<p>You wonder sometimes about switching up your phono cartridge, but on your salary you can't exactly afford to have a whole fleet of them to pick from. You try to get in the occasional demo session at the hi-fi shop two towns over, but you're careful to not stop by TOO often and be seen as some kind of freeloader. No matter how deep into a niche hobby you dig yourself, your pre-existing anxieties will always be in there with you unless you decide to actually work on yourself in earnest. Maybe talk to someone, read one of the books the marriage counselor gave you when it was just a trial separation and not a full and legal divorce.</p>`,
        choices: [
          {
            description: 'Well, everything should be warmed up by now.',
            moveTo: 56,
          },
        ],
      },
    ],
    [
      49,
      {
        description: `<p><em>Sheila</em>…</p><p>What is she doing right now, you wonder. Did she throw herself back into her painting after the split? You always felt like you kept her from her creative pursuits on some level. Maybe you critiqued works in progress one too many times, you're not sure, but eventually the canvas and easel just stopped coming out altogether.</p>`,
        choices: [
          {
            description: 'How did you two meet again?',
            moveTo: 51,
          },
        ],
      },
    ],
    [
      50,
      {
        description:
          '<p>You check your smartphone before remembering it might be adding unwanted electrical interference to your otherwise sealed-off listening room. (The weather will be fine tomorrow.)</p>',
        choices: [
          {
            description: 'Put your phone in the other room.',
            moveTo: 54,
          },
        ],
      },
    ],
    [
      51,
      {
        description: `<p>You met Sheila through some mutual friends. <em>Fred</em> was the one hosting the party, you think. It's so long ago now. It was awkward at first, feeling such an electric and mutual attraction to someone you just met, and trying hard to not show it too soon. You looked for openings all night, and at some point felt so bold as to claim an empty seat on the ottoman next to her when its occupant flitted over to a different conversation circle in the kitchen. You managed to get past the clunkiness of the first few small-talk questions, finding shared interest in Fred's shelf of artist monographs (more specifically a shared distaste for Jackson Pollock and his CIA ties). You walked her home that night; you still don't know where you found the nerve to propose that. Or make that first phone call two afternoons later.</p>`,
        choices: [
          {
            description: 'Remember last summer at Cape Cod?',
            moveTo: 52,
          },
        ],
      },
    ],
    [
      52,
      {
        description: `<p>God, the Cape Cod trip. A second honeymoon of sorts, an unexpected oasis in the middle of weeks of fighting. It was as if a change of scenery somehow put an unspoken truce into effect. You overshot the tacit "tolerate one another" promise of most tired-marriage vacations, and ended up back in some kind of pleasantly naïve teenage place, emotionally speaking. You brought wine but ended up drinking none of it, intoxication would have felt redundant.</p>`,
        choices: [
          {
            description: 'Where did it all go wrong?',
            moveTo: 53,
          },
        ],
      },
    ],
    [
      53,
      {
        description:
          '<p>You stopped listening, mostly. Stopped showing up, being present. Dove full force into your hobbies, and became a kind of shadow of yourself. None of it was her fault and you hate that she thinks it was.</p>',
        choices: [
          {
            description: `Tubes are probably warmed up by now. Let's hear this new disc.`,
            moveTo: 56,
          },
        ],
      },
    ],
    [
      54,
      {
        description: `<p>You go back into the living room and put your phone face-down on the coffee table, after putting it into Airplane Mode for additional security against unwanted vibrations. Jaco looks up from a nap he's drifting in and out of.</p>`,
        choices: [
          {
            description: 'Pet Jaco.',
            moveTo: 55,
          },
        ],
      },
    ],
    [
      55,
      {
        description: `<p>You give Jaco some behind-the-ear skritches. He'll always be here for you.</p>`,
        choices: [
          {
            description: 'Head back in and listen to your new record!',
            moveTo: 56,
          },
        ],
      },
    ],
    [
      56,
      {
        description: `<p>Over the years, you've developed a delicate technique for unsleeving a record and only touching the edges and the label. You all but lunge at anyone who tries to put something on at your parties, fearing they'll get their grubby fingerprints all in the grooves. You haven't held a party in six years.</p>`,
        choices: [
          {
            description: `Let's get this cleaned up.`,
            moveTo: 57,
          },
        ],
      },
    ],
    [
      57,
      {
        description: `<p>Even the cleanest-looking of records can still be filthy, so you turn to your trusted <em>RECORD DOCTOR V</em>, a vacuum-based machine. After applying the right amount of cleaning solution to Side 1, you place it face-down over its brush-lined vacuum slit. There's a hockey puck shaped handle thing you put on top of the label that has little grips so you can turn the disc manually (you can't yet afford a full-auto disc washer, and this has irked you for years). The machine whines like a full-size canister vacuum cleaner, and you let it do its thing for three slow revolutions of the LP. This is the part where Jaco usually hides under the couch.</p><p>Your disc now shines magnificently.</p>`,
        choices: [
          {
            description: 'Pop it on the turntable!',
            moveTo: 58,
          },
        ],
      },
    ],
    [
      58,
      {
        description:
          '<p>You place it on your turntable with the utmost care.</p>',
        choices: [
          {
            description: 'Throw a nice heavy weight on the center label.',
            moveTo: 59,
          },
        ],
      },
    ],
    [
      59,
      {
        description:
          '<p>You secure a big brass doorknob looking thing on top of the disc. No chance it will drift or wobble now.</p>',
        choices: [
          {
            description: 'What about static though?',
            moveTo: 60,
          },
        ],
      },
    ],
    [
      60,
      {
        description:
          '<p>The disc looks totally free of dust, but static is the invisible menace! You take your carbon fiber brush and let the LP spin three times underneath its light touch.</p>',
        choices: [
          {
            description: 'But is the needle itself clean?',
            moveTo: 61,
          },
        ],
      },
    ],
    [
      61,
      {
        description: `<p>Just to be safe, you do the melamine trick you learned about, taking a 'Magic Eraser' pad and delicately lowering the needle onto it a few times. (Strictly vertically! Horizontal motion could fuck the needle up but good, you're told.) It's a small blessing that your turntable has a cue lever for this.</p>`,
        choices: [
          {
            description: 'Sit in your listening chair.',
            moveTo: 62,
          },
        ],
      },
    ],
    [
      62,
      {
        description: `<p>You ease into your favorite listening chair, a mid-range IKEA job called <em>EKERÖ</em> that you picked up because it reminded you of the old Maxell commercials.</p><p>Wait, what in the hell is that buzz?</p>`,
        choices: [
          {
            description: 'Check the speaker wires',
            moveTo: 63,
          },
          {
            description: 'Check the turntable ground wire',
            getPoints: true,
            moveTo: 64,
          },
          {
            description: `Turn off all the lights in your apartment in case they're interfering somehow.`,
            moveTo: 65,
          },
        ],
      },
    ],
    [
      63,
      {
        description: `<p>The speaker wires look ok! Nothing is loose, no spindly little shits poking out from your top-notch wire twisting job a few years back.</p>`,
        choices: [
          {
            description: 'Check the turntable ground wire.',
            getPoints: true,
            moveTo: 64,
          },
          {
            description: `Turn off all the lights in your apartment in case they're interfering somehow.`,
            moveTo: 67,
          },
        ],
      },
    ],
    [
      64,
      {
        description: `<p>That's it! The ground wire on the turntable somehow came loose.</p>`,
        choices: [
          {
            description: 'Reattach that guy!',
            moveTo: 68,
          },
        ],
      },
    ],
    [
      65,
      {
        description:
          '<p>You turn off all the kitchen and living room lights, but when you return to the listening room the buzz is still there.</p>',
        choices: [
          {
            description: 'Check the speaker wires.',
            moveTo: 66,
          },
          {
            description: 'Check the turntable ground wire.',
            getPoints: true,
            moveTo: 64,
          },
        ],
      },
    ],
    [
      66,
      {
        description:
          '<p>The speaker wires look ok! Nothing is loose, no spindly little shits poking out from your top-notch wire twisting job a few years back.</p>',
        choices: [
          {
            description: 'Check the turntable ground wire.',
            getPoints: true,
            moveTo: 64,
          },
        ],
      },
    ],
    [
      67,
      {
        description:
          '<p>You turn off all the kitchen and living room lights, but when you return to the listening room the buzz is still there.</p>',
        choices: [
          {
            description: 'Check the turntable ground wire.',
            getPoints: true,
            moveTo: 64,
          },
        ],
      },
    ],
    [
      68,
      {
        description: `<p>The buzz is gone!</p><p>It's time at last to spin this record.</p>`,
        choices: [
          {
            description: 'Drop the needle!',
            moveTo: {
              aja: 69,
              rush: 70,
              lamb: 71,
            },
          },
        ],
      },
    ],
    [
      69,
      {
        description: `<p>Hell yeah. Side 1, Track 1 of AJA…</p><p><em>'Black Cow'</em></p>`,
        choices: [
          {
            description: 'Take the needle off the record.',
            moveTo: 72,
          },
        ],
      },
    ],
    [
      70,
      {
        description: `<p>Hell yeah. Side 1, Track 1 of MOVING PICTURES…</p><p><em>'Tom Sawyer'</em>`,
        choices: [
          {
            description: 'Take the needle off the record.',
            moveTo: 72,
          },
        ],
      },
    ],
    [
      71,
      {
        description: `<p>Hell yeah. Side 1, Track 1 of THE LAMB LIES DOWN ON BROADWAY…</p><p><em>'The Lamb Lies Down on Broadway'</em></p>`,
        choices: [
          {
            description: 'Take the needle off the record.',
            moveTo: 72,
          },
        ],
      },
    ],
    [
      72,
      {
        description:
          '<p>What the fuck. "Near Mint"!? And the first fucking SONG has a skip? You could kill Phil. What kinda mickey mouse goddamn moron operation is he running down there</p>',
        choices: [
          {
            description: 'Re-sleeve the LP.',
            moveTo: 73,
          },
          {
            description: 'Eat your feelings.',
            moveTo: 74,
          },
          {
            description: 'Go for a walk to try and calm down.',
            moveTo: 75,
          },
        ],
      },
    ],
    [
      73,
      {
        description:
          '<p>You try to steady your hands to put the record away. Goddamnit, even a VG+ graded record should have played with no skips what the HELL.</p>',
        choices: [
          {
            description: 'Take the record back to the store.',
            moveTo: {
              aja: 76,
              rush: 77,
              lamb: 78,
            },
          },
        ],
      },
    ],
    [
      74,
      {
        description:
          '<p>You power through half a Sara Lee pound cake you have in the fridge.</p><p>You feel a bit sick, which proves to be a welcome distraction.</p>',
        choices: [
          {
            description: 'Take the record back to the store.',
            moveTo: {
              aja: 76,
              rush: 77,
              lamb: 78,
            },
          },
        ],
      },
    ],
    [
      75,
      {
        description: `<p>You decide to go for a walk around the apartment complex. There's a pool in the center courtyard area but nobody has used it in a while. A few leaves float near the edge, and you wonder how many times Chip's son has peed in there. Thank Christ you don't happen upon that guy or his shitty kid on your walk.</p><p>You're a little out of breath now, but not feeling any better about things.</p>`,
        choices: [
          {
            description: 'Take the record back to the store.',
            moveTo: {
              aja: 76,
              rush: 77,
              lamb: 78,
            },
          },
        ],
      },
    ],
    [
      76,
      {
        description:
          '<p>You get into your car, and as you turn the engine over you catch the end of Black Cow on the radio, as if to specifically mock you.</p>',
        choices: [
          {
            description: 'Change the station.',
            moveTo: 79,
          },
        ],
      },
    ],
    [
      77,
      {
        description:
          '<p>You get into your car, and as you turn the engine over you catch the end of Tom Sawyer on the radio, as if to specifically mock you.</p>',
        choices: [
          {
            description: 'Change the station',
            moveTo: 79,
          },
        ],
      },
    ],
    [
      78,
      {
        description:
          '<p>You get into your car, and as you turn the engine over you catch the end of The Lamb Lies Down on Broadway on the radio, as if to specifcally mock you.</p>',
        choices: [
          {
            description: 'Change the station.',
            moveTo: 79,
          },
        ],
      },
    ],
    [
      79,
      {
        description: `<p>You scan around for a while, but everything scares you. You wish you hadn't left your <em>Pono</em> at home.</p>`,
        choices: [
          {
            description: 'Drive in silence',
            moveTo: 80,
          },
        ],
      },
    ],
    [
      80,
      {
        description: `<p>There's a noticeable whining sound. Your fan belt probably needs to be replaced.</p>`,
        choices: [
          {
            description: 'Pull into the record store parking lot.',
            moveTo: 81,
          },
          {
            description: 'Pass the store and go to your mechanic.',
            moveTo: 82,
          },
        ],
      },
    ],
    [
      81,
      {
        description: `<p>You pull into the parking lot of the record store, and take a few breaths to steady yourself before going in and confronting Phil about his slip-up, about his goddamn blind-ass useless moron eyes not noticing that this record was going to skip like all HELL.</p>`,
        choices: [
          {
            description: 'Take a few more breaths.',
            moveTo: 83,
          },
        ],
      },
    ],
    [
      82,
      {
        description: `<p>You keep on driving. You can't tell if the whining noise is getting worse or if it's just your imagination, but it's probably a good idea to get it checked out sooner than later.</p><p>You pull into John's Garage.</p>`,
        choices: [
          {
            description: 'Go see if John has some time today to look at it.',
            moveTo: 84,
          },
        ],
      },
    ],
    [
      83,
      {
        description: `<p>You take some deep breaths, "square breaths" as the counselor had called them.</p><p>Breathe in for four seconds, hold it four seconds, let it out for four seconds, hold that for four more seconds.</p><p>Repeat.</p><p>It's never worked particularly well for you, but you don't need an assault charge on your record today so you're trying real hard.</p>`,
        choices: [
          {
            description: 'Go inside.',
            moveTo: 94,
          },
        ],
      },
    ],
    [
      84,
      {
        description: `<p>"Hey! What brings you here? Nope, stop right there, I'll tell ya what brings you here: fan belt. I could hear ya from the toilet when you pulled in. I can pop a new one on there once I'm done this guy I got up on the lift here, if you can wait about half an hour."</p>`,
        choices: [
          {
            description: 'Plop down in one of the waiting room chairs.',
            moveTo: 85,
          },
        ],
      },
    ],
    [
      85,
      {
        description: `<p>It smells like grease and gasoline, with an air freshener not pulling quite enough weight. It's a comforting smell; you used to like waiting for the old Monte Carlo to get tuned-up when you were a child. You would read whatever book you had on you, and if you were lucky your dad would give you a quarter for the M&M machine.</p><p>Does this garage have one of those, you wonder?</p>`,
        choices: [
          {
            description: 'It does!',
            cost: -0.25,
            moveTo: 86,
          },
        ],
      },
    ],
    [
      86,
      {
        description: `<p>Oh hell yes.</p><p>The handle produces a strangely satisfying grinding noise as you turn it, and the way-past-expired candies fall down their chute and hit the metal retainer flap. You pop some of them in your mouth and wonder what the deal is with expired ones, why do the shells crack over time? You feel like you should be able to suss out the science of it, but you come up blank. There's probably a youtube video about this.</p><p>The specific taste and texture of the stale M&M's has completed the transformation: you are a kid again for these few minutes.</p>`,
        choices: [
          {
            description: `Remember the tan-colored M&M's?`,
            getPoints: true,
            moveTo: 87,
          },
        ],
      },
    ],
    [
      87,
      {
        description: `<p>Yeah! They used to have brown AND tan…? What boring shit is that. Remember when they did the contest to decide on the new color. You had to call some 1-800 number or something. What were the colors…it was blue, pink, and.... purple?</p><p>Was that it?</p>`,
        choices: [
          {
            description: 'Was it?',
            moveTo: 88,
          },
        ],
      },
    ],
    [
      88,
      {
        description: `<p>You think so, yeah. It's all kinda redundant now, huh. You can go to those specialty candy stores, or god forbid the huge M&M store in Times Square, and just get whatever colors you want.</p>`,
        choices: [
          {
            description:
              'Do you think they have to swap out the blue ones for special-ordered tan ones in period movies?',
            moveTo: 89,
          },
        ],
      },
    ],
    [
      89,
      {
        description: `<p>They must! Well, any prop department worth a damn probably does, anyway.</p>`,
        choices: [
          {
            description: `There's probably a youtube video about it.`,
            moveTo: 90,
          },
        ],
      },
    ],
    [
      90,
      {
        description: `<p>"Yo! Your car's all set."</p><p>John is waving his hand in front of your face.</p>`,
        choices: [
          {
            description: '"Thanks, man! What do I owe ya?"',
            moveTo: 91,
          },
        ],
      },
    ],
    [
      91,
      {
        description: `<p>"$110."</p><p>Shit. You don't have nearly enough cash on you.</p>`,
        choices: [
          {
            description: '"You guys take cards?"',
            moveTo: 92,
          },
        ],
      },
    ],
    [
      92,
      {
        description: `<p>"Sure, sure. Give 'er here."</p><p>He runs your Discover card through one of those old carbon-copy machines that makes almost as satisfying a noise as the vending machine crank did.</p>`,
        choices: [
          {
            description: `Let's go return this record.`,
            cost: -110,
            moveTo: 93,
          },
        ],
      },
    ],
    [
      93,
      {
        description: `<p>You're back on the road and everything's sounding normal under the hood. John always does a pretty stellar job with your Tercel.</p>`,
        choices: [
          {
            description: 'Park in front of the record shop.',
            moveTo: 104,
          },
        ],
      },
    ],
    [
      94,
      {
        description: `<p>You calmly (you think) walk into the shop, but Phil is nowhere to be found. You see that teen-aged stockboy Jeff though, and wave him over. He tells you that Phil stepped out.</p>`,
        choices: [
          {
            description: `"Well do you know when he'll be back?"`,
            moveTo: 95,
          },
        ],
      },
    ],
    [
      95,
      {
        description: `<p>"He went home to grab something or other. He lives across the river so it'll be a while. You can hang out here till he gets back if you want."</p><p>Thanks, cool, great.</p>`,
        choices: [
          {
            description: 'Wait for him.',
            moveTo: 96,
          },
          {
            description: 'Go get your car looked at.',
            moveTo: 97,
          },
        ],
      },
    ],
    [
      96,
      {
        description: `<p>You hang out for a while awkwardly, and look through some old 12" promotional flats. You try to make conversation with Jeff at one point but it's unsustainably awkward and you both do your best to just not look each other in the eye after that.</p>`,
        choices: [
          {
            description: 'Just look through some more merchandise, then.',
            moveTo: 98,
          },
        ],
      },
    ],
    [
      97,
      {
        description: `<p>You go outside and try your best, but now the car won't start at all.</p>`,
        choices: [
          {
            description: `Fuckin' awesome. Cool. Go back inside.`,
            moveTo: 98,
          },
        ],
      },
    ],
    [
      98,
      {
        description: `<p>You try your best to center yourself but you're in a dark-ass place now. Except whoa shit wait, when did they get a laserdisc section…!? You didn't even see that before.</p>`,
        choices: [
          {
            description: `Makes sense, they're identical to LPs basically (especially when shelved).`,
            moveTo: 99,
          },
        ],
      },
    ],
    [
      99,
      {
        description: `<p>There's even some CEDs!</p>`,
        choices: [
          {
            description: 'Look through those.',
            moveTo: 100,
          },
          {
            description: '2) What is a CED?',
            moveTo: 101,
          },
        ],
      },
    ],
    [
      100,
      {
        description:
          '<p>Oh damn they have <em>Let It Be</em>! In all its overhyped, very mild awkwardness. This is basically unaffordable in any other home video format.</p>',
        choices: [
          {
            description: 'I should grab it.',
            moveTo: 102,
          },
        ],
      },
    ],
    [
      101,
      {
        description: `<p>Oh man dude, CEDs are interesting as hell, they're like this worse-quality-than-VHS disc that's basically a vinyl record, but for video. It lives in this big square plastic housing but once it's in the machine there's a stylus that goes into a groove on the disc, and it can even skip like a record (and these used ones almost always do), it's a whole thing.</p>`,
        choices: [
          {
            description: 'Well are there any good titles?',
            moveTo: 100,
          },
        ],
      },
    ],
    [
      102,
      {
        description: `<p>You don't even have a machine to play it on!</p><p>Also there's no time for that—Phil just got back.</p>`,
        choices: [
          {
            description: 'Go confront him.',
            moveTo: 103,
          },
        ],
      },
    ],
    [
      103,
      {
        description: '"Heya buddy! Back so soon?"',
        choices: [
          {
            description: '"Hey man, got a little problem here."',
            getPoints: true,
            moveTo: 105,
          },
          {
            description:
              '"Shut the hell up. Just shut up. What the fuck is the idea!?"',
            moveTo: 106,
          },
          {
            description: '3) Take a swing at Phil.',
            moveTo: 107,
          },
        ],
      },
    ],
    [
      104,
      {
        description:
          '<p>You park your car toward the middle of the lot (thinking this is some kind of sly exercise if you do it often enough) and head inside. Phil is there, setting down a sweaty styrofoam food container.</p>',
        choices: [
          {
            description: 'Go confront him.',
            moveTo: 103,
          },
        ],
      },
    ],
    [
      105,
      {
        description: `<p>"What's the issue, friend?"</p>`,
        choices: [
          {
            description:
              'Explain what happened, including every step of your cleaning ritual.',
            moveTo: 111,
          },
        ],
      },
    ],
    [
      106,
      {
        description: `<p>He looks legitimately scared of you; this is not a person who seeks out or relishes conflict in the first place, and your raised voice has the whole store's attention.</p><p>"…W-What's the matter?"</p>`,
        choices: [
          {
            description:
              'Explain what happened, including every step of your cleaning ritual.',
            moveTo: 109,
          },
        ],
      },
    ],
    [
      107,
      {
        description: `<p>You attempt to suckerpunch Phil but he's fast, too fast. He dodges it, and with improbable speed Jeffery gets you into a half nelson from behind. Before you know it he has pulled some kind of Brazilian Jiu-Jitsu move on you and the last thing you hear before losing consciousness is Phil remarking that ya know, before they were Sparks, they were called Halfnelson.</p>`,
        choices: [
          {
            description: 'Wake up in the hospital.',
            moveTo: 108,
          },
        ],
      },
    ],
    [
      108,
      {
        description: `<p>You wake up in some kind of low-urgency part of the city hospital, whatever the opposite of an ICU is.</p><p>Your bill is exorbitant and you still have a scratched record.</p><p><em>BAD ENDING</em></p>`,
        choices: [
          {
            description: 'Restart the game.',
            moveTo: 0,
          },
        ],
      },
    ],
    [
      109,
      {
        description: `"Okay man, well you can return it for store credit if you see something you like. I'm usually pretty diligent about grading the merchandise, I'm sorry you had to come all the way back here."</p><p>He's such a goddamn nice and patient guy. You feel terrible.</p>`,
        choices: [
          {
            description: `"Uh. Thanks, I'll take a look around."`,
            moveTo: 110,
          },
        ],
      },
    ],
    [
      110,
      {
        description: `<p>You look around for a while and end up buying your fifth copy of <em>The Nightfly</em> by Donald Fagen, and a couple old Motown cassettes.</p><p><em>MEDIOCRE ENDING</em></p>`,
        choices: [
          {
            description: 'Restart the game.',
            moveTo: 0,
          },
        ],
      },
    ],
    [
      111,
      {
        description: `<p>"Damn, I'm really sorry to hear that! We usually only do store credit, but you're in here all the time, so let's just go ahead and get you your cash back.</p>`,
        choices: [
          {
            description: '"Aw man, really? Thanks!"',
            cost: 34.98,
            moveTo: 112,
          },
        ],
      },
    ],
    [
      112,
      {
        description: `<p>You no longer possess a scratched record!</p><p>You decide to look around a bit more, and end up finding a copy of <em>Sync<em>hroni<em>city</em> by The Police that has the rare bronze/silver/gold cover variant! You can flip this on eBay even if the disc ends up being scratched, but you're pretty sure you'll just keep it since you almost never see these.</p>`,
        choices: [
          {
            description: `Whoa, and it's only priced at $20…?`,
            cost: -32.50,
            moveTo: 113,
          },
        ],
      },
    ],
    [
      113,
      {
        description: `<p>This is a pretty excellent find! You decide to buy this as well as your fifth copy of <em>The Nightfly</em> by Donald Fagen and call it a day.</p><p><em>GOOD ENDING</em></p>`,
        choices: [
          {
            description: 'Restart the game.',
            moveTo: 0,
          },
        ],
      },
    ],
  ]);
  // }}}

  /**
   * Layer over get and set operations for the Player's state.
   * @namespace
   * @property {string} name - Get or set the player's name.
   * @property {number} points - Get the player's point total.
   * @property {string} inventory - Get or set which album the player chose.
   * @property {number} money - Get or set the player's money total.
   * @property {function} incrementPoints - Increase the player's points by one.
   */
  const Player = { // {{{
    get name() {
      return window.localStorage.getItem('name');
    },
    set name(name) {
      window.localStorage.setItem(
        'name',
        name.charAt(0).toUpperCase() + name.slice(1, name.length)
      );
    },
    get points() {
      if (!window.localStorage.getItem('points')) return 0;
      return parseInt(window.localStorage.getItem('points'), 10);
    },
    incrementPoints() {
      window.localStorage.setItem('points', this.points + 1);
      document.getElementById('points').textContent = this.points;
      return this.points;
    },
    get inventory() {
      return window.localStorage.getItem('inventory');
    },
    set inventory(inventory) {
      if (inventory) {
        window.localStorage.setItem('inventory', inventory);
      }
    },
    get money() {
      if (!window.localStorage.getItem('money')) window.localStorage.setItem('money', '60');
      return JSON.parse(window.localStorage.getItem('money'));
    },
    set money(cost) {
      if (cost) {
        const newAmount = Intl.NumberFormat(
          'en-US', { maximumFractionDigits: 2 }
        ).format(Number.parseFloat(this.money + cost));
        window.localStorage.setItem('money', newAmount);
        document.getElementById('money').textContent = newAmount;
      }
    },
  };
  // }}}

  /**
   * Add scene content to the DOM.
   * @param {number} index - Scene index to render.
   * @return {void}
   */
  function renderScene(index) { // {{{
    // Append the scene text to the DOM.
    const wrapper = document.createElement('div');
    const contents = data.get(index);
    wrapper.innerHTML = contents.description;
    stageElement.appendChild(wrapper);
    // Replace the previous player choices with the new ones.
    choicesElement.innerHTML = contents.choices.reduce((acc, choice) => {
      return acc + `<button
          data-move-to='${JSON.stringify(choice.moveTo)}'
          data-item="${choice.item ? choice.item : ''}"
          data-get-points="${choice.getPoints ? 'true' : 'false'}"
          data-cost="${choice.cost ? choice.cost : ''}"
        >
          ${choice.description}
        </button>`;
    }, '');
  }
  // }}}

  const choicesElement = document.getElementById('choices');

  /**
   * Listen for game choices from the player.
   * @param {object} event - The pointerup event.
   * @return {void}
   */
  choicesElement.addEventListener('pointerup', event => { // {{{
    const choice = event.target.closest('button');
    if (JSON.parse(choice.dataset.getPoints)) Player.incrementPoints();
    Player.inventory = choice.dataset.item;
    Player.money = choice.dataset.cost ? JSON.parse(choice.dataset.cost) : null;
    const moveTo = JSON.parse(choice.dataset.moveTo);
    if (typeof moveTo === 'object')  renderScene(moveTo[Player.inventory]);
    else renderScene(moveTo);
    // Store the previous scene index. This allows us to re-create game-state
    // on a browser refresh.
    const playedScenes = JSON.parse(window.localStorage.getItem('playedScenes'));
    playedScenes.push(moveTo);
    window.localStorage.setItem('playedScenes', JSON.stringify(playedScenes));
  }, {passive: true});
  // }}}

  const stageElement = document.getElementById('stage');

  const playButtonElement = document.getElementById('play');
  // Ask the player for their name if one isn't saved.
  if (!Player.name) {
    playButtonElement.addEventListener('pointerup', function playEvent() {
      Player.name = window.prompt('Please enter your name');
      playButtonElement.hidden = true;
      playButtonElement.removeEventListener('pointerup', playEvent);
      stageElement.innerHTML = `<div><strong>Welcome, ${Player.name}!</strong></div>`;
      renderScene(0);
    });
  }
  // If we have the player's name, render scenes.
  else {
    playButtonElement.hidden = true;
    stageElement.innerHTML = `<div><strong>Welcome, ${Player.name}!</strong></div>`;
    const playedScenes = JSON.parse(window.localStorage.getItem('playedScenes'));
    if (playedScenes.length) playedScenes.forEach(index => renderScene(index));
    else renderScene(0);
  }

  // Initialize storage for which scenes the player has experienced.
  if (!window.localStorage.getItem('playedScenes')) {
    window.localStorage.setItem('playedScenes', JSON.stringify([0]));
  }

})();
// vim: foldmethod=marker
