#!/usr/bin/env python3
"""Generate 1000 unique riddles as JSON for the YumFu RIDDLES section."""
import json, os, random

riddles = []
seen = set()

def add(q, a, h, c):
    key = q.strip().lower()
    if key in seen:
        return
    seen.add(key)
    riddles.append({"q": q.strip(), "a": a.strip(), "hint": h.strip(), "cat": c})

CLASSIC = [
    ("What has keys but can't open locks?", "A piano", "You play it with your fingers.", "objects"),
    ("What has a face and two hands but no arms or legs?", "A clock", "It tells you something all day.", "objects"),
    ("What has to be broken before you can use it?", "An egg", "Breakfast food.", "food"),
    ("What has many teeth but cannot bite?", "A comb", "You use it on your hair.", "objects"),
    ("What has a neck but no head?", "A bottle", "It can hold liquid.", "objects"),
    ("What gets wetter the more it dries?", "A towel", "You use it after a shower.", "objects"),
    ("What has an eye but cannot see?", "A needle", "Used with thread.", "objects"),
    ("What has a thumb and four fingers but is not alive?", "A glove", "Keeps your hands warm.", "objects"),
    ("What can travel around the world while staying in a corner?", "A stamp", "It goes on an envelope.", "objects"),
    ("What runs but never walks, has a bed but never sleeps?", "A river", "Water flows in it.", "nature"),
    ("What has cities but no houses, forests but no trees, and water but no fish?", "A map", "You use it to navigate.", "objects"),
    ("What goes up but never comes down?", "Your age", "It only increases.", "concepts"),
    ("What can you catch but not throw?", "A cold", "You sneeze with it.", "concepts"),
    ("What is full of holes but still holds water?", "A sponge", "Used for cleaning.", "objects"),
    ("What can fill a room but takes up no space?", "Light", "Flip a switch.", "concepts"),
    ("What has words but never speaks?", "A book", "You read it.", "objects"),
    ("What building has the most stories?", "A library", "Full of books.", "places"),
    ("What has a ring but no finger?", "A telephone", "It makes a sound.", "objects"),
    ("The more you take, the more you leave behind. What am I?", "Footsteps", "You make them when walking.", "concepts"),
    ("What is so fragile that saying its name breaks it?", "Silence", "Shhh.", "concepts"),
    ("What has 88 keys but can't open a single door?", "A piano", "It makes music.", "objects"),
    ("What flies without wings?", "Time", "It passes.", "concepts"),
    ("What is always in front of you but can't be seen?", "The future", "It hasn't happened yet.", "concepts"),
    ("What gets bigger the more you take away?", "A hole", "Dig it.", "concepts"),
    ("What has a spine but no bones?", "A book", "Full of pages.", "objects"),
    ("What has ears but cannot hear?", "A cornfield", "Corn on the cob.", "nature"),
    ("What is black when clean and white when dirty?", "A chalkboard", "You write on it.", "objects"),
    ("What has a tongue but cannot talk?", "A shoe", "You wear it.", "objects"),
    ("What has a head and a tail but no body?", "A coin", "Heads or tails.", "objects"),
    ("What word is spelled incorrectly in every dictionary?", "Incorrectly", "Read it literally.", "words"),
    ("What begins with T, ends with T, and has T in it?", "A teapot", "Full of tea.", "objects"),
    ("What five-letter word becomes shorter when you add two letters?", "Short", "Add 'er'.", "words"),
    ("Which month has 28 days?", "All of them", "Every month has at least 28.", "trick"),
    ("If you drop me I'm sure to crack, but smile at me and I'll smile back. What am I?", "A mirror", "You see yourself.", "objects"),
    ("I'm tall when young and short when old. What am I?", "A candle", "It burns down.", "objects"),
    ("What can be cracked, made, told, and played?", "A joke", "Ha ha.", "concepts"),
    ("What is always coming but never arrives?", "Tomorrow", "Always a day away.", "concepts"),
    ("What can you keep after giving it to someone?", "Your word", "A promise.", "concepts"),
    ("What loses its head in the morning and gets it back at night?", "A pillow", "You sleep on it.", "objects"),
    ("What is black, white, and read all over?", "A newspaper", "Daily news.", "objects"),
    ("What kind of room has no doors or windows?", "A mushroom", "It's a fungus.", "food"),
    ("What is light as a feather, yet the strongest person can't hold it for five minutes?", "Breath", "Inhale, exhale.", "body"),
    ("What can you hear but not see, and only comes when you speak?", "An echo", "Shout in a canyon.", "concepts"),
    ("What do you call a fish with no eyes?", "A fsh", "Remove the i's.", "words"),
    ("What has a crown but is not a king?", "A tooth", "In your mouth.", "body"),
    ("What is round on both ends and high in the middle?", "Ohio", "A US state.", "places"),
    ("I am an odd number. Take away one letter and I become even. What am I?", "Seven", "Remove the 's'.", "numbers"),
    ("A farmer has 17 sheep and all but 9 die. How many are left?", "9", "'All but 9' means 9 remain.", "numbers"),
    ("How many times can you subtract 10 from 100?", "Once", "After that it's 90, not 100.", "numbers"),
    ("Two fathers and two sons go fishing. Each catches one fish, but only three fish are caught. How?", "They are grandfather, father, and son", "Count the generations.", "lateral"),
    ("A cowboy rides into town on Friday, stays three days, and leaves on Friday. How?", "His horse is named Friday", "Think about names.", "lateral"),
    ("The person who makes it doesn't want it. The person who buys it doesn't use it. The person who uses it doesn't know it. What is it?", "A coffin", "A somber one.", "lateral"),
    ("What is at the end of a rainbow?", "The letter W", "Spell 'rainbow'.", "words"),
    ("What has feet but no legs?", "A ruler", "Measures 12 inches.", "objects"),
    ("What kind of coat is best put on wet?", "A coat of paint", "For your walls.", "objects"),
    ("What has a bark but no bite?", "A tree", "It has leaves.", "nature"),
    ("What has roots that nobody sees, and is taller than trees?", "A mountain", "It reaches the sky.", "nature"),
    ("What can you break, even if you never pick it up or touch it?", "A promise", "You give your word.", "concepts"),
    ("What has one head, one foot, and four legs?", "A bed", "You sleep in it.", "objects"),
    ("What comes down but never goes up?", "Rain", "It falls from clouds.", "nature"),
    ("What has a heart that doesn't beat?", "An artichoke", "It's a vegetable.", "food"),
    ("What has 13 hearts but no other organs?", "A deck of cards", "Play a game.", "objects"),
    ("What English word has three consecutive double letters?", "Bookkeeper", "Someone who tracks money.", "words"),
    ("What gets sharper the more you use it?", "Your brain", "Keep learning.", "concepts"),
    ("What is easy to get into but hard to get out of?", "Trouble", "Avoid it.", "concepts"),
]
for q, a, h, c in CLASSIC:
    add(q, a, h, c)

words_with = {
    "A":"apple","B":"banana","C":"cat","D":"dog","E":"elephant","F":"fish","G":"goat",
    "H":"horse","I":"igloo","J":"jam","K":"kite","L":"lion","M":"moon","N":"nest",
    "O":"owl","P":"pig","Q":"queen","R":"rain","S":"sun","T":"tree","U":"umbrella",
    "V":"violin","W":"whale","X":"xylophone","Y":"yak","Z":"zebra"
}
for L, w in words_with.items():
    add(f"I'm a letter of the alphabet, and the word '{w}' begins with me. What letter am I?",
        L, f"Start of '{w}'.", "words")

OBJECTS = [
    ("umbrella","I open when it rains and keep you dry, folded up small when the sky is high."),
    ("clock","My hands go round and round all day, I tell you time but cannot play."),
    ("mirror","Look at me and you'll see you, everything you do I do too."),
    ("candle","I give you light and slowly die, the longer I burn the shorter I lie."),
    ("shadow","I follow you in the light of day, but in the dark I fade away."),
    ("book","Turn my pages one by one, and worlds appear till you are done."),
    ("key","Small and metal, I fit a hole, unlocking doors is my whole role."),
    ("ladder","Step by step you climb on me, to reach the heights you wish to see."),
    ("balloon","Fill me with air and I will grow, prick me once and off I go."),
    ("kite","On windy days I love to fly, a string keeps me from the sky."),
    ("map","I show you cities, roads, and seas, yet I fold up with the greatest ease."),
    ("pillow","Rest your head on me at night, and I'll hold your dreams till morning light."),
    ("bridge","I stretch across the river wide, so you can walk from side to side."),
    ("lantern","In the dark I glow so bright, a little flame gives you sight."),
    ("compass","I always point you to the north, to guide your travels back and forth."),
    ("hourglass","Sand runs through me grain by grain, when I'm empty, turn me again."),
    ("telescope","Look through me toward the night, and distant stars come into sight."),
    ("anchor","Heavy and iron, I sink below, to keep the ship from drifting slow."),
    ("whistle","Blow through me and I will sing, a sharp clear note is what I bring."),
    ("drum","Beat on me and I will boom, filling up the empty room."),
    ("bell","Give me a swing and I will chime, ringing out to mark the time."),
    ("net","Full of holes yet I still catch, whatever swims into my patch."),
    ("scarecrow","I stand in fields both night and day, to keep the hungry crows away."),
    ("windmill","My arms turn round in country breeze, grinding grain with graceful ease."),
    ("fountain","Water leaps from me up high, then falls back down and never dry."),
    ("telephone","Speak to me and I will send, your voice across to a distant friend."),
    ("scissors","Two sharp blades that cross and part, I cut the paper for your art."),
    ("magnet","I pull the iron toward my side, a hidden force I cannot hide."),
    ("wheel","Round and round forever I spin, to make the journey we begin."),
    ("crayon","I come in colors bold and bright, I fill your pages with delight."),
    ("suitcase","Pack me full and off we go, to places near or far, you know."),
    ("thermometer","I rise and fall to show the heat, telling if you're feverish or sweet."),
    ("padlock","Turn the key or spin the dial, I guard your secrets all the while."),
    ("violin","Draw the bow across my strings, and sweet and sorrowed music sings."),
    ("chessboard","Black and white in tidy rows, where kings and queens and knights oppose."),
    ("hammer","I pound the nail with one hard smack, to build the house or fix the shack."),
    ("broom","With bristles wide I sweep the floor, and chase the dust right out the door."),
    ("kettle","Fill me up and heat me high, and steam will whistle from me by-and-by."),
    ("clock_tower","High above the town I stand, my chiming heard across the land."),
    ("bicycle","Two round wheels and pedals too, I carry you the whole way through."),
]
for name, verse in OBJECTS:
    label = name.replace("_", " ").title()
    add(verse + " What am I?", label, f"An object starting with '{name[0].upper()}'.", "objects")

ANIMALS = [
    ("owl","I fly at night and hoot so wise, with big round golden glowing eyes."),
    ("bee","I buzz from flower to flower all day, and make sweet honey along the way."),
    ("spider","Eight legs I have to spin my thread, catching flies within my web."),
    ("frog","I hop from lily pad to log, and croak all night from in the bog."),
    ("snail","I carry my house upon my back, and leave a slimy shiny track."),
    ("bat","I sleep by day, hang upside down, and fly at night around the town."),
    ("penguin","In a tuxedo I always dress, on icy shores I love it best."),
    ("kangaroo","I hop on two strong springy feet, and keep my baby snug and neat."),
    ("chameleon","I change my color as I please, to hide among the leaves and trees."),
    ("octopus","Eight long arms I use to swim, in ocean deep and dark and dim."),
    ("peacock","I fan my tail of shining blue, with eye-like spots that stare at you."),
    ("camel","Across the desert sand I plod, a hump of fat is quite my mod."),
    ("dolphin","I leap from waves with joyful grace, a friendly smile upon my face."),
    ("firefly","I blink my light on summer nights, a tiny lantern taking flight."),
    ("hedgehog","I curl into a spiky ball, when danger comes I fear no fall."),
    ("woodpecker","I tap the tree trunk all day long, rat-a-tat is my only song."),
    ("seahorse","I'm named for a land animal, but swim upright and very small."),
    ("beaver","I build my dam of sticks and mud, to hold back the flowing flood."),
    ("cricket","On summer eves I chirp my tune, beneath the glowing silver moon."),
    ("elephant","The largest beast upon the land, with a trunk and tusks so grand."),
    ("giraffe","My neck is long, I'm very tall, I reach the leaves above you all."),
    ("turtle","Slow and steady on I creep, my shell's the fortress that I keep."),
    ("cheetah","The fastest runner on the plain, I catch my prey with speed insane."),
    ("swan","White and graceful on the lake, a curving neck for beauty's sake."),
    ("wolf","I howl beneath the moon so bright, and hunt in packs throughout the night."),
    ("fox","Red and clever, sly and quick, escaping traps is my best trick."),
    ("crab","Sideways on the sand I walk, with pincer claws instead of talk."),
    ("parrot","I mimic every word you say, in feathers green and bright and gay."),
    ("squirrel","I gather nuts and climb the tree, my bushy tail flicks after me."),
    ("ladybug","Red with spots of blackest dot, a tiny beetle in the plot."),
    ("koala","In eucalyptus trees I doze, munching leaves in sleepy pose."),
    ("panda","Black and white and round and slow, on bamboo shoots I love to grow."),
    ("otter","I float on my back in the stream, and crack a shell — a happy dream."),
    ("mole","Beneath the ground I dig my hall, I rarely see the sun at all."),
    ("bull","With mighty horns and thunderous snort, I charge the red cape as my sport."),
]
for name, verse in ANIMALS:
    add(verse + " What am I?", name.title(), f"An animal starting with '{name[0].upper()}'.", "animals")

FOODS = [
    ("banana","I'm yellow and I have a peel, a monkey's favorite tasty meal."),
    ("watermelon","Green outside and red within, with black seeds beneath my skin."),
    ("popcorn","I start as tiny yellow seeds, then pop to white for movie needs."),
    ("pineapple","Spiky crown and golden hide, sweet and juicy fruit inside."),
    ("cheese","From milk I'm made and often yellow, mice adore me, hungry fellow."),
    ("honey","Golden, sticky, sweet, and thick, the bees all make me — take a lick."),
    ("carrot","Long and orange, crunchy too, rabbits love to nibble through."),
    ("tomato","Red and round, some call me fruit, in salads I am quite the beaut."),
    ("bread","From flour and water I am kneaded, baked in ovens, warm and needed."),
    ("lemon","Yellow, sour, full of zest, in lemonade I taste the best."),
    ("strawberry","Red and sweet with seeds outside, a summer treat none can hide."),
    ("coconut","Hard and brown and hairy shell, sweet white milk inside as well."),
    ("grape","Small and round in bunches grown, to raisins I am sometimes thrown."),
    ("pumpkin","Orange and round in autumn air, carve my face for a Halloween scare."),
    ("noodle","Long and thin I twist and slide, in steaming soup I love to hide."),
    ("chili","Small and red but full of fire, one bite raises your temper higher."),
    ("apple","Red or green upon a tree, keep the doctor away from thee."),
    ("orange","Round and bright, I share my name, with a color just the same."),
    ("potato","Beneath the soil I grow in dirt, mashed or fried, I'll never hurt."),
    ("ice_cream","Cold and sweet on summer days, I melt beneath the sunny rays."),
    ("pancake","Flat and round upon your plate, with syrup poured, I taste so great."),
    ("pretzel","Twisted, salty, baked with care, a knotted snack beyond compare."),
    ("mango","Golden, juicy, tropical treat, no fruit I know is quite so sweet."),
    ("cabbage","Round and leafy, layered tight, a green ball wrapped up nice and light."),
    ("garlic","In cloves I come with pungent smell, I flavor soups and stews so well."),
    ("donut","Round with a hole right in my center, sugar-glazed for those who enter."),
    ("waffle","Square with pockets, crisp and light, I hold the syrup just right."),
    ("cherry","Small and red on slender stem, in pairs I hang, a shining gem."),
    ("peach","Soft and fuzzy, sweet and round, the juiciest fruit that can be found."),
    ("onion","Peel my layers and you may cry, I add my flavor to the fry."),
]
for name, verse in FOODS:
    label = name.replace("_", " ").title()
    add(verse + " What am I?", label, f"A food starting with '{name[0].upper()}'.", "food")

NATURE = [
    ("rainbow","After rain I arch the sky, seven colors way up high."),
    ("snowflake","No two of me are quite the same, I fall in winter, cold's my game."),
    ("cloud","I float above you soft and white, then turn to grey and rain at night."),
    ("volcano","I sleep for years then wake to roar, spilling fire from my core."),
    ("river","I wind and flow from hill to sea, and never stop, just watch and see."),
    ("wind","You cannot see me, yet I'm strong, I push the sails and clouds along."),
    ("thunder","I follow lightning with a boom, that shakes and rattles every room."),
    ("lightning","A jagged flash across the sky, I strike the ground from way up high."),
    ("moon","I glow at night, I wax and wane, and pull the tides across the main."),
    ("sun","I rise each morning in the east, and give my warmth to man and beast."),
    ("star","A tiny light in blackest night, I twinkle far, a distant sight."),
    ("mountain","I rise above the clouds so proud, my peak is often veiled in shroud."),
    ("waterfall","I tumble down from ledge to pool, my misty spray is fresh and cool."),
    ("desert","Endless sand and blazing heat, few plants grow beneath my feet."),
    ("glacier","A river made of ancient ice, I move so slow, I'm cold as vice."),
    ("forest","Full of trees both tall and green, the deepest, greenest, leafy scene."),
    ("cave","A hollow deep within the stone, where bats and darkness make their home."),
    ("island","Surrounded all around by sea, a piece of land where palms grow free."),
    ("tornado","A spinning funnel dark and wide, I tear the land on every side."),
    ("dewdrop","At dawn I sparkle on the grass, a tiny bead of morning glass."),
    ("frost","On cold clear nights I paint the pane, with feathered ice, a crystal chain."),
    ("comet","With a blazing tail I streak the night, a wanderer of ancient light."),
    ("earthquake","The ground will tremble, shake, and crack, when I awake there's no way back."),
    ("aurora","In polar skies I dance and glow, green and purple, soft and slow."),
    ("meadow","A field of grass and flowers gay, where butterflies and bees all play."),
]
for name, verse in NATURE:
    add(verse + " What am I?", name.title(), f"A part of nature starting with '{name[0].upper()}'.", "nature")

# Number sum riddles
random.seed(42)
pairs = set()
while len(pairs) < 60:
    x = random.randint(11, 89); y = random.randint(11, 89)
    if x + y != 100:
        pairs.add((x, y))
for x, y in list(pairs):
    add(f"I am the number you get when you add {x} and {y}. What number am I?",
        str(x + y), "Add the tens, then the ones.", "numbers")

# Multiplication riddles
prods = set()
while len(prods) < 45:
    x = random.randint(3, 12); y = random.randint(3, 12)
    prods.add((x, y))
for x, y in list(prods):
    add(f"Multiply {x} by {y}. What number do you get?", str(x * y),
        f"Think of the {x} times table.", "numbers")

# Sequence riddles
SEQS = [
    ("2, 4, 6, 8, ...", "10", "Even numbers."),
    ("1, 3, 5, 7, ...", "9", "Odd numbers."),
    ("1, 4, 9, 16, ...", "25", "Perfect squares."),
    ("1, 1, 2, 3, 5, 8, ...", "13", "Fibonacci - add the last two."),
    ("2, 6, 12, 20, ...", "30", "n times (n+1)."),
    ("1, 2, 4, 8, 16, ...", "32", "Doubling each time."),
    ("3, 6, 9, 12, ...", "15", "Multiples of three."),
    ("5, 10, 15, 20, ...", "25", "Counting by fives."),
    ("100, 90, 80, 70, ...", "60", "Counting down by tens."),
    ("1, 8, 27, 64, ...", "125", "Perfect cubes."),
    ("2, 3, 5, 7, 11, ...", "13", "Prime numbers."),
    ("1, 2, 6, 24, 120, ...", "720", "Factorials."),
    ("81, 27, 9, 3, ...", "1", "Divide by three each time."),
    ("10, 20, 40, 80, ...", "160", "Doubling from ten."),
    ("50, 45, 40, 35, ...", "30", "Down by five."),
]
for s, ans, h in SEQS:
    add(f"What number comes next in the sequence: {s}?", ans, h, "numbers")

# Days / months / time riddles
TIME_RIDDLES = [
    ("What comes once in a minute, twice in a moment, but never in a thousand years?", "The letter M", "Look at the spelling.", "words"),
    ("What has 365 pages but is not a book?", "A calendar", "One page per day.", "objects"),
    ("What day comes three days after the day which comes two days after the day which comes immediately after the day before Monday?", "Saturday", "Work it out step by step.", "trick"),
    ("If yesterday was tomorrow, today would be Sunday. What day is it really?", "Friday", "Solve the puzzle backward.", "trick"),
    ("What season are you in when the leaves fall?", "Autumn", "Also called fall.", "nature"),
    ("How many seconds are in a minute?", "60", "A full sweep of the clock.", "numbers"),
    ("How many days are in a leap year?", "366", "One extra day in February.", "numbers"),
    ("What is the only day that is an anagram of nothing common but ends in -day like all the rest, coming right before Monday?", "Sunday", "The first day of the week.", "trick"),
]
for q, a, h, c in TIME_RIDDLES:
    add(q, a, h, c)

# Spelling / word-play riddles (programmatic rhyme-answer pairs)
RHYMES = [
    ("I rhyme with 'cat' and you wear me on your head. What am I?", "A hat", "Keeps the sun off.", "words"),
    ("I rhyme with 'star' and I drive on the road. What am I?", "A car", "Has four wheels.", "words"),
    ("I rhyme with 'house' and I'm a tiny squeaky animal. What am I?", "A mouse", "Cats chase me.", "words"),
    ("I rhyme with 'bee' and I grow tall with leaves. What am I?", "A tree", "Green in summer.", "words"),
    ("I rhyme with 'night' and I help you see in the dark. What am I?", "A light", "Flip the switch.", "words"),
    ("I rhyme with 'cake' and I'm a big body of water. What am I?", "A lake", "Ducks swim on me.", "words"),
    ("I rhyme with 'ring' and a bird uses me to fly. What am I?", "A wing", "Birds have two.", "words"),
    ("I rhyme with 'moon' and you eat soup with me. What am I?", "A spoon", "Found in the kitchen.", "words"),
    ("I rhyme with 'bell' and a snail lives inside me. What am I?", "A shell", "Found on the beach.", "words"),
    ("I rhyme with 'chair' and it grows on your head. What am I?", "Hair", "You brush me.", "words"),
    ("I rhyme with 'four' and you walk through me to enter. What am I?", "A door", "It opens and closes.", "words"),
    ("I rhyme with 'goat' and it floats on water. What am I?", "A boat", "It sails.", "words"),
    ("I rhyme with 'snow' and it curves in the sky after rain. What am I?", "A bow (rainbow)", "Seven colors.", "words"),
    ("I rhyme with 'red' and you sleep in me. What am I?", "A bed", "Soft and cozy.", "words"),
    ("I rhyme with 'fun' and it shines in the sky. What am I?", "The sun", "Bright and hot.", "words"),
    ("I rhyme with 'ball' and I'm very high, not short. What am I?", "Tall", "Opposite of short.", "words"),
    ("I rhyme with 'fox' and I'm a container with a lid. What am I?", "A box", "You pack things in me.", "words"),
    ("I rhyme with 'king' and it flies with feathers. What am I?", "A wing", "Birds use two.", "words"),
    ("I rhyme with 'blue' and you wear me on your foot. What am I?", "A shoe", "Comes in a pair.", "words"),
    ("I rhyme with 'clock' and it's on the seashore. What am I?", "A rock", "Hard and heavy.", "words"),
]
for q, a, h, c in RHYMES:
    add(q, a, h, c)

# Lateral / brain teasers
LATERAL = [
    ("A man is found dead in a locked room with a puddle of water and broken glass. How did he die?", "He was standing on a block of ice that melted; hanged himself.", "The water was once solid.", "lateral"),
    ("What can run but never walks, has a mouth but never talks, has a head but never weeps, has a bed but never sleeps?", "A river", "It flows to the sea.", "lateral"),
    ("I am not alive, but I can grow; I don't have lungs, but I need air; I don't have a mouth, but water kills me. What am I?", "Fire", "It flickers and burns.", "lateral"),
    ("The more of this there is, the less you see. What is it?", "Darkness", "Turn off the lights.", "lateral"),
    ("What can point in every direction but can't reach the destination by itself?", "Your finger", "Or a signpost.", "lateral"),
    ("A girl fell off a 20-foot ladder but wasn't hurt. How?", "She fell off the bottom rung.", "How high was she really?", "lateral"),
    ("What gets broken without being held?", "A promise", "Or a record.", "lateral"),
    ("If a rooster lays an egg on the peak of a roof, which way does it roll?", "Roosters don't lay eggs.", "Think about biology.", "trick"),
    ("Before Mount Everest was discovered, what was the tallest mountain on Earth?", "Mount Everest - it was still tallest.", "It existed already.", "trick"),
    ("A doctor and a boy were fishing. The boy was the doctor's son, but the doctor was not the boy's father. Who was the doctor?", "His mother.", "Challenge your assumptions.", "lateral"),
    ("What has to be given before you can keep it?", "Your word", "A promise.", "lateral"),
    ("How far can a dog run into the woods?", "Halfway - after that it's running out.", "Think geometry.", "trick"),
    ("What can you put in a bucket to make it weigh less?", "A hole", "It lets water out.", "lateral"),
    ("What word becomes a palindrome when you view it in a mirror... no, what 7-letter word has hundreds of letters in it?", "Mailbox", "Think of what it holds.", "lateral"),
    ("A plane crashes on the border of two countries. Where do you bury the survivors?", "You don't bury survivors.", "Read carefully.", "trick"),
]
for q, a, h, c in LATERAL:
    add(q, a, h, c)

# Country capitals
CAPITALS = {
    "France":"Paris","Japan":"Tokyo","Italy":"Rome","Spain":"Madrid","Germany":"Berlin",
    "England":"London","Russia":"Moscow","China":"Beijing","Egypt":"Cairo","Greece":"Athens",
    "Canada":"Ottawa","Australia":"Canberra","Brazil":"Brasilia","India":"New Delhi","Mexico":"Mexico City",
    "Portugal":"Lisbon","Norway":"Oslo","Sweden":"Stockholm","Ireland":"Dublin","Austria":"Vienna",
    "Turkey":"Ankara","Thailand":"Bangkok","Peru":"Lima","Cuba":"Havana","Kenya":"Nairobi",
    "Poland":"Warsaw","Finland":"Helsinki","Denmark":"Copenhagen","Iceland":"Reykjavik","Hungary":"Budapest",
    "Argentina":"Buenos Aires","Chile":"Santiago","Vietnam":"Hanoi","Morocco":"Rabat","Netherlands":"Amsterdam",
}
for country, cap in CAPITALS.items():
    add(f"I am the capital city of {country}. What city am I?", cap, f"It's the main city of {country}.", "geography")

# Color riddles
COLORS = [
    ("I am the color of the sky on a clear day and of the deep ocean. What color am I?", "Blue", "Think of the sea.", "colors"),
    ("I am the color of grass and leaves in spring. What color am I?", "Green", "Nature's shade.", "colors"),
    ("I am the color of a ripe tomato and a fire truck. What color am I?", "Red", "Stop signs use me.", "colors"),
    ("I am the color of the sun and a banana. What color am I?", "Yellow", "Bright and cheery.", "colors"),
    ("I am the color of snow and clouds. What color am I?", "White", "Pure and clean.", "colors"),
    ("I am the color of the night sky and coal. What color am I?", "Black", "Darkest of all.", "colors"),
    ("I am the color you get by mixing red and blue. What color am I?", "Purple", "Royal shade.", "colors"),
    ("I am the color of a carrot and a sunset. What color am I?", "Orange", "Shares a name with a fruit.", "colors"),
    ("I am the color of chocolate and tree bark. What color am I?", "Brown", "Earthy tone.", "colors"),
    ("I am the color of a flamingo and cotton candy. What color am I?", "Pink", "Soft and sweet.", "colors"),
    ("I am the color of storm clouds and elephants. What color am I?", "Grey", "Between black and white.", "colors"),
    ("I am the color of gold and treasure. What color am I?", "Gold", "Pirates seek me.", "colors"),
]
for q, a, h, c in COLORS:
    add(q, a, h, c)

# Body part riddles
BODY = [
    ("I let you smell flowers and food. What part of the body am I?", "The nose", "In the middle of your face.", "body"),
    ("You have two of me to hear with. What am I?", "Ears", "On the sides of your head.", "body"),
    ("You use me to chew your food, and I come in a set of many. What am I?", "Teeth", "Brush me twice a day.", "body"),
    ("I pump blood all around your body. What am I?", "The heart", "I beat all day.", "body"),
    ("You use me to see the world. I come in a pair. What am I?", "Eyes", "Blink me sometimes.", "body"),
    ("I help you grab and hold things, with five fingers each. What am I?", "Hands", "You clap with me.", "body"),
    ("I carry you around all day and end in ten toes. What am I?", "Feet", "You wear shoes on me.", "body"),
    ("I think and remember and live inside your skull. What am I?", "The brain", "You use me to solve riddles.", "body"),
    ("I help you breathe, filling with air. There are two of me. What am I?", "Lungs", "Inside your chest.", "body"),
    ("I am the longest bone in your body, in your upper leg. What am I?", "The femur", "The thigh bone.", "body"),
]
for q, a, h, c in BODY:
    add(q, a, h, c)

# 'I start and end' spelling riddles for common words
SPELL = [
    ("cat","a small furry pet that says meow"),
    ("dog","a loyal pet that says woof"),
    ("hat","something you wear on your head"),
    ("sun","the bright star that lights our day"),
    ("bee","an insect that makes honey"),
    ("cup","you drink your tea from me"),
    ("box","a square container for storage"),
    ("pen","you write with ink using me"),
    ("bed","you sleep on me at night"),
    ("egg","a hen lays me for breakfast"),
    ("fan","I spin to make cool air"),
    ("jar","a glass container with a lid"),
    ("key","I unlock doors"),
    ("map","I show you where to go"),
    ("net","I catch fish and butterflies"),
    ("owl","a wise bird of the night"),
    ("pig","a pink farm animal that oinks"),
    ("rug","a soft mat on the floor"),
    ("web","a spider spins me"),
    ("zip","I fasten your jacket"),
]
for w, clue in SPELL:
    add(f"I am {clue}. My name has {len(w)} letters and starts with '{w[0].upper()}'. What am I?",
        w.capitalize(), f"It rhymes and is a common {len(w)}-letter word.", "words")

# Sports riddles
SPORTS = [
    ("In this sport you kick a round ball into a net; the rest of the world calls it football. What is it?", "Soccer", "World's most popular sport.", "sports"),
    ("You shoot a ball through a hoop high off the ground in this sport. What is it?", "Basketball", "Tall players excel.", "sports"),
    ("You hit a small ball with a racket over a net, scoring love, 15, 30, 40. What sport is it?", "Tennis", "Played at Wimbledon.", "sports"),
    ("You swing a bat, run around bases, and try to reach home. What sport is it?", "Baseball", "Home run!", "sports"),
    ("You hit a small white ball into 18 holes using clubs. What sport is it?", "Golf", "Yell 'fore!'.", "sports"),
    ("You ride waves standing on a board. What sport is it?", "Surfing", "Done in the ocean.", "sports"),
    ("You glide on ice wearing blades on your feet. What sport is it?", "Ice skating", "Cold and graceful.", "sports"),
    ("You throw a ball to knock down ten pins. What sport is it?", "Bowling", "Aim for a strike.", "sports"),
    ("You punch an opponent wearing gloves inside a ring. What sport is it?", "Boxing", "Ding ding, round one.", "sports"),
    ("You race on two wheels using pedals and handlebars. What sport is it?", "Cycling", "The Tour de France.", "sports"),
]
for q, a, h, c in SPORTS:
    add(q, a, h, c)

# Instrument riddles
INSTRUMENTS = [
    ("I have 88 black and white keys and make music when pressed. What am I?", "Piano", "A large keyboard instrument.", "music"),
    ("I have six strings and you strum me around a campfire. What am I?", "Guitar", "Rock stars love me.", "music"),
    ("I am small, have four strings, and come from Hawaii. What am I?", "Ukulele", "A tiny guitar.", "music"),
    ("You blow into me and press keys; I'm long, silver, and shrill. What am I?", "Flute", "Held sideways.", "music"),
    ("I am big, brass, and you blow into me for a deep booming sound. What am I?", "Tuba", "The biggest brass.", "music"),
    ("You hit me with sticks to keep the beat. What am I?", "Drums", "Boom boom bang.", "music"),
    ("I have black and white keys but you carry me and squeeze me. What am I?", "Accordion", "Squeeze box.", "music"),
    ("You draw a bow across my four strings, resting me under your chin. What am I?", "Violin", "A small fiddle.", "music"),
    ("I am like a violin but much bigger; you play me standing up. What am I?", "Cello", "Deep and warm.", "music"),
    ("You blow into me and I'm curly brass; heard often in jazz. What am I?", "Trumpet", "Loud and bright.", "music"),
]
for q, a, h, c in INSTRUMENTS:
    add(q, a, h, c)

# Occupation riddles
JOBS = [
    ("I put out fires and rescue cats from trees. Who am I?", "A firefighter", "I ride a red truck.", "people"),
    ("I care for sick people and help doctors in the hospital. Who am I?", "A nurse", "I wear scrubs.", "people"),
    ("I teach children lessons in a classroom. Who am I?", "A teacher", "I write on the board.", "people"),
    ("I fly airplanes across the sky. Who am I?", "A pilot", "I sit in the cockpit.", "people"),
    ("I bake bread and cakes early each morning. Who am I?", "A baker", "I work in a bakery.", "people"),
    ("I catch criminals and keep people safe. Who am I?", "A police officer", "I wear a badge.", "people"),
    ("I fix teeth and tell you to floss. Who am I?", "A dentist", "Open wide!", "people"),
    ("I grow crops and raise animals on the land. Who am I?", "A farmer", "I drive a tractor.", "people"),
    ("I deliver letters and packages to your door. Who am I?", "A mail carrier", "I carry a big bag.", "people"),
    ("I cook delicious meals in a restaurant kitchen. Who am I?", "A chef", "I wear a tall white hat.", "people"),
    ("I study the stars and planets through a telescope. Who am I?", "An astronomer", "I work at night.", "people"),
    ("I paint pictures and create art. Who am I?", "An artist", "I use a brush.", "people"),
]
for q, a, h, c in JOBS:
    add(q, a, h, c)

# ---- Pad to exactly 1000 with more arithmetic + doubling riddles ----
def count():
    return len(riddles)

def num_count():
    return sum(1 for r in riddles if r["cat"] == "numbers")

NUM_CAP = 150
# subtraction riddles (capped)
subs = set()
while num_count() < NUM_CAP and len(subs) < 200:
    x = random.randint(20, 99); y = random.randint(1, x-1)
    if (x, y) in subs: continue
    subs.add((x, y))
    add(f"Start with {x} and take away {y}. What number is left?", str(x - y),
        "Subtract step by step.", "numbers")

# doubling riddles (capped)
dbl = set()
while num_count() < NUM_CAP and len(dbl) < 150:
    n = random.randint(6, 250)
    if n in dbl: continue
    dbl.add(n)
    add(f"What is double the number {n}?", str(n*2), "Add the number to itself.", "numbers")

# ---- Themed padding to reach 1000 (variety over arithmetic) ----
MORE_OBJECTS = [
    ("backpack","Sling me on your shoulders two, I carry all the books for you."),
    ("flashlight","Click my switch in the dark of night, and out will beam a helpful light."),
    ("envelope","Slip a letter deep inside, then seal my flap and off you ride."),
    ("clockwork","Wind me tight and let me go, ticking fast then winding slow."),
    ("raincoat","When the clouds begin to pour, wear me and you'll stay dry for sure."),
    ("toothbrush","Twice a day you pick me up, to scrub your teeth then rinse your cup."),
    ("snowman","Three white balls stacked in the cold, a carrot nose and a hat so bold."),
    ("lighthouse","On rocky shore I stand up tall, my beam of light guides ships and all."),
    ("parachute","Jump from high and pull my cord, I bloom above and slow your fall toward the sward."),
    ("trampoline","Bounce on me and you will fly, springing up toward the sky."),
    ("microscope","Look through me at things so small, and tiny worlds appear for all."),
    ("binoculars","Two round lenses side by side, bring far-off birds up close to spied."),
    ("wheelbarrow","One wheel front and handles back, I haul the dirt along the track."),
    ("typewriter","Press my keys and letters clack, black on paper, front to back."),
    ("chandelier","From the ceiling I hang bright, with crystal arms and glowing light."),
    ("periscope","From a sub beneath the sea, I let the sailors up-top see."),
    ("seesaw","Up and down we go in play, one goes high while one down-weighs."),
    ("kaleidoscope","Turn me toward the light and peep, at colored shapes in patterns deep."),
    ("sundial","By my shadow on the ground, the hour of day is truly found."),
    ("weathervane","On the rooftop high I turn, which way the wind blows you can learn."),
]
for name, verse in MORE_OBJECTS:
    if count() >= 1000: break
    label = name.replace("_", " ").title()
    add(verse + " What am I?", label, f"An object starting with '{name[0].upper()}'.", "objects")

MORE_ANIMALS = [
    ("lion","The king of beasts with golden mane, I roar across the grassy plain."),
    ("tiger","Orange with stripes of blackest ink, a mighty cat, more fierce than you'd think."),
    ("zebra","Black and white in stripes I wear, a horse-like beast beyond compare."),
    ("monkey","I swing from branches, love to play, and eat bananas every day."),
    ("rabbit","Long ears and a fluffy tail, I hop through fields down every trail."),
    ("hippo","Huge and grey, I love the mud, and wallow in the river's flood."),
    ("rhino","A horn upon my nose I bear, thick grey skin and heavy stare."),
    ("flamingo","On one pink leg I like to stand, the pinkest bird in all the land."),
    ("seal","I bark and clap and swim with grace, on icy rocks I find my place."),
    ("walrus","Two long tusks and whiskers wide, on Arctic ice I like to slide."),
    ("eagle","With mighty wings I rule the sky, and sharp-eyed catch my prey from high."),
    ("peafowl","My tail's a fan of shining eyes, I strut about to win a prize."),
    ("toucan","A giant colorful beak have I, in rainforest trees I love to fly."),
    ("jaguar","Spotted coat and jungle prowl, the strongest cat with a silent growl."),
    ("gorilla","The largest ape, so strong and wise, I thump my chest to show my size."),
    ("llama","Fuzzy and tall in the mountain air, I hum and spit if you don't take care."),
    ("raccoon","A masked bandit of the night, I raid the trash with sneaky might."),
    ("platypus","A duck-like bill, I lay an egg, yet I'm a mammal with webbed leg."),
    ("starfish","Five arms have I upon the floor, of the ocean by the shore."),
    ("jellyfish","Soft and clear I drift and sting, a floating, boneless, wobbly thing."),
]
for name, verse in MORE_ANIMALS:
    if count() >= 1000: break
    add(verse + " What am I?", name.title(), f"An animal starting with '{name[0].upper()}'.", "animals")

MORE_RHYMES = [
    ("cake","a sweet dessert for birthdays"),("train","runs on rails, choo-choo"),
    ("snake","a long legless reptile that hisses"),("crown","a king wears me on his head"),
    ("drum","you beat me to make rhythm"),("nose","you smell with me"),
    ("clock","I tell the time on the wall"),("frog","a green hopper that croaks"),
    ("whale","the largest animal in the sea"),("chair","you sit on me at the table"),
    ("cloud","I float white in the sky"),("broom","a witch flies on me"),
    ("knight","a warrior in shining armor"),("queen","a royal woman who rules"),
    ("pearl","a shiny gem from an oyster"),("torch","a flame to light the dark"),
    ("anchor","I hold the ship in place"),("feather","light and soft from a bird"),
    ("candle","a wax stick with a flame"),("ladder","you climb my rungs to go up"),
]
for w, clue in MORE_RHYMES:
    if count() >= 1000: break
    add(f"I am {clue}. What am I?", w.capitalize(), f"Starts with '{w[0].upper()}'.", "objects")

MORE_GEO = {
    "Switzerland":"Bern","Belgium":"Brussels","Scotland":"Edinburgh","Kenya":"Nairobi",
    "South Korea":"Seoul","Indonesia":"Jakarta","Philippines":"Manila","New Zealand":"Wellington",
    "Nigeria":"Abuja","Colombia":"Bogota","Ukraine":"Kyiv","Czechia":"Prague",
    "Croatia":"Zagreb","Romania":"Bucharest","Cambodia":"Phnom Penh","Nepal":"Kathmandu",
    "Iceland":"Reykjavik","Jordan":"Amman","Lebanon":"Beirut","Malaysia":"Kuala Lumpur",
}
for country, cap in MORE_GEO.items():
    if count() >= 1000: break
    add(f"I am the capital city of {country}. What city am I?", cap, f"Main city of {country}.", "geography")

# ---- Large themed batch to reduce arithmetic dominance ----
MYTH = [
    ("A one-eyed giant of Greek myth who trapped Odysseus in a cave.", "A Cyclops", "One giant eye.", "myth"),
    ("A horse with a single spiraling horn on its forehead.", "A unicorn", "A magical creature.", "myth"),
    ("A fire-breathing beast with scales, wings, and a hoard of gold.", "A dragon", "Knights fight me.", "myth"),
    ("Half man, half horse, galloping through legends.", "A centaur", "An archer of myth.", "myth"),
    ("A bird that bursts into flame and is reborn from its ashes.", "A phoenix", "Reborn from fire.", "myth"),
    ("A woman with snakes for hair whose gaze turns you to stone.", "Medusa", "Do not look directly.", "myth"),
    ("A giant sea monster of the deep with many long tentacles.", "The Kraken", "It sinks ships.", "myth"),
    ("A creature that is part lion, part goat, and part serpent.", "A chimera", "A mix of three beasts.", "myth"),
    ("A hairy man-beast said to roam the northwest forests.", "Bigfoot", "Also called Sasquatch.", "myth"),
    ("A small mischievous creature that hides gold at the rainbow end.", "A leprechaun", "Irish luck.", "myth"),
    ("A person who transforms into a wolf under the full moon.", "A werewolf", "Beware the full moon.", "myth"),
    ("A three-headed dog that guards the gates of the underworld.", "Cerberus", "Three heads, one job.", "myth"),
    ("A tiny winged being that sprinkles magic dust.", "A fairy", "Think Tinker Bell.", "myth"),
    ("A beautiful sea maiden, half woman and half fish.", "A mermaid", "She sings by the shore.", "myth"),
    ("A genie of legend who grants three wishes from a lamp.", "A genie", "Rub the lamp.", "myth"),
]
for q, a, h, c in MYTH:
    if count() >= 1000: break
    add("Riddle me this: " + q + " Who or what am I?", a, h, c)

WEATHER = [
    ("I fall in soft white flakes and blanket the ground in winter.", "Snow", "Cold and white.", "nature"),
    ("I am the loud sound after a lightning flash.", "Thunder", "It rumbles.", "nature"),
    ("I am thick and grey and make it hard to see in the morning.", "Fog", "A low cloud.", "nature"),
    ("I am frozen rain that bounces when it hits the ground.", "Hail", "Ice from the sky.", "nature"),
    ("I am a violent storm that spins over the ocean with strong winds.", "A hurricane", "Also a typhoon.", "nature"),
    ("I am the gentle movement of air you feel on your face.", "A breeze", "A soft wind.", "nature"),
    ("I sparkle on the grass in the cool of early morning.", "Dew", "Morning droplets.", "nature"),
    ("I am ice that forms feathery patterns on cold windows.", "Frost", "Winter artwork.", "nature"),
    ("I am a spinning column of wind that touches down on land.", "A tornado", "A twister.", "nature"),
    ("I am tiny ice pellets falling, between rain and snow.", "Sleet", "Half-frozen rain.", "nature"),
]
for q, a, h, c in WEATHER:
    if count() >= 1000: break
    add(q + " What am I?", a, h, c)

VEHICLES = [
    ("I have two wheels and a motor; wear a helmet to ride me fast.", "A motorcycle", "Vroom.", "vehicles"),
    ("I fly with wings and jet engines carrying many people.", "An airplane", "Takes off from a runway.", "vehicles"),
    ("I sail across the ocean carrying cargo or passengers.", "A ship", "It floats on water.", "vehicles"),
    ("I run on rails and pull many cars, going choo-choo.", "A train", "Engine and cars.", "vehicles"),
    ("I dive beneath the waves and travel underwater.", "A submarine", "Under the sea.", "vehicles"),
    ("I have a spinning rotor on top and can hover in the air.", "A helicopter", "Lifts straight up.", "vehicles"),
    ("I carry astronauts far beyond the sky into space.", "A rocket", "Blast off!", "vehicles"),
    ("I am a long vehicle that carries passengers around the city.", "A bus", "You pay a fare.", "vehicles"),
    ("I float in the sky held up by hot air.", "A hot air balloon", "Rises with heat.", "vehicles"),
    ("I put out fires and race with sirens and a ladder.", "A fire truck", "Bright red.", "vehicles"),
    ("I carry the sick quickly to the hospital with flashing lights.", "An ambulance", "Emergency vehicle.", "vehicles"),
    ("I have big tires and a bucket to dig and move dirt.", "An excavator", "A construction machine.", "vehicles"),
]
for q, a, h, c in VEHICLES:
    if count() >= 1000: break
    add(q + " What am I?", a, h, c)

PLANETS = [
    ("I am the closest planet to the Sun and the smallest.", "Mercury", "A fast messenger.", "space"),
    ("I am the hottest planet, named for a goddess of love.", "Venus", "Earth twin in size.", "space"),
    ("I am the blue planet where you live.", "Earth", "Home sweet home.", "space"),
    ("I am the red planet, named after the god of war.", "Mars", "Two tiny moons.", "space"),
    ("I am the largest planet, a gas giant with a great red spot.", "Jupiter", "The biggest of all.", "space"),
    ("I am famous for my rings of ice and rock.", "Saturn", "Look for my rings.", "space"),
    ("I am a tilted ice giant that spins on my side.", "Uranus", "The sideways planet.", "space"),
    ("I am the farthest planet, deep blue and very windy.", "Neptune", "Named for the sea god.", "space"),
    ("I am the star at the center of our solar system.", "The Sun", "Gives light and heat.", "space"),
    ("I orbit the Earth and glow at night, going through phases.", "The Moon", "It waxes and wanes.", "space"),
    ("I am a rocky world beyond Neptune, once the ninth planet.", "Pluto", "Now a dwarf planet.", "space"),
    ("I streak across the sky as a shooting star.", "A meteor", "Make a wish.", "space"),
]
for q, a, h, c in PLANETS:
    if count() >= 1000: break
    add(q + " What am I?", a, h, c)

CLOTHES = [
    ("You wear me on your feet and lace me up before a walk.", "Shoes", "A pair.", "objects"),
    ("You pull me over your head; I keep your top half warm.", "A sweater", "Cozy in winter.", "objects"),
    ("I wrap around your neck to keep out the cold wind.", "A scarf", "Long and warm.", "objects"),
    ("You slip me on your hands with a place for each finger.", "Gloves", "Warm hands.", "objects"),
    ("I cover your legs, one tube for each, and have pockets.", "Pants", "Wear a belt with me.", "objects"),
    ("You wear me over everything when it is cold outside.", "A coat", "The outer layer.", "objects"),
    ("I hold up your pants and buckle around your waist.", "A belt", "It has a buckle.", "objects"),
    ("You wear me over your eyes to block the bright sun.", "Sunglasses", "Cool and shady.", "objects"),
    ("You tie me at your throat with a fancy shirt.", "A necktie", "Worn to formal events.", "objects"),
    ("I keep your feet warm inside your shoes.", "Socks", "Come in pairs.", "objects"),
]
for q, a, h, c in CLOTHES:
    if count() >= 1000: break
    add(q + " What am I?", a, h, c)

SCHOOL = [
    ("I am full of words and meanings, arranged from A to Z.", "A dictionary", "Look up a word.", "objects"),
    ("You write on me with chalk and wipe me clean.", "A blackboard", "In the classroom.", "objects"),
    ("I am where you borrow books for free and stay quiet.", "A library", "Full of shelves.", "places"),
    ("You erase your pencil mistakes with me.", "An eraser", "Rubs out pencil.", "objects"),
    ("I hold your papers together with a metal pinch.", "A stapler", "Click!", "objects"),
    ("You measure straight lines and length with me.", "A ruler", "Marked in inches.", "objects"),
    ("I am a bag you wear to carry books to school.", "A backpack", "Worn on the back.", "objects"),
    ("You sharpen your pencil by twisting it inside me.", "A pencil sharpener", "Makes a point.", "objects"),
    ("I am a round model of the Earth you can spin.", "A globe", "Find countries on me.", "objects"),
    ("You use me to add and subtract numbers quickly.", "A calculator", "Press the buttons.", "objects"),
]
for q, a, h, c in SCHOOL:
    if count() >= 1000: break
    add(q + " What am I?", a, h, c)

OPPOSITES = [
    ("hot","cold"),("up","down"),("big","small"),("fast","slow"),("day","night"),
    ("happy","sad"),("open","closed"),("light","dark"),("wet","dry"),("full","empty"),
    ("hard","soft"),("loud","quiet"),("high","low"),("young","old"),("rich","poor"),
    ("near","far"),("clean","dirty"),("first","last"),("push","pull"),("win","lose"),
    ("above","below"),("begin","end"),("brave","afraid"),("buy","sell"),("give","take"),
    ("left","right"),("true","false"),("thick","thin"),("smooth","rough"),("early","late"),
]
for a_word, b_word in OPPOSITES:
    if count() >= 1000: break
    add("I am the opposite of '" + a_word + "'. What word am I?", b_word.capitalize(), "The reverse of '" + a_word + "'.", "words")


# ---- Compound word riddles ----
COMPOUNDS = [
    ("rain","bow","a colorful arc after a storm"),
    ("sun","flower","a tall yellow bloom that follows the sun"),
    ("butter","fly","a colorful winged insect"),
    ("basket","ball","a sport with a hoop"),
    ("foot","ball","a sport you kick or throw"),
    ("snow","man","a figure built from snowballs"),
    ("fire","place","where logs burn in a home"),
    ("tooth","brush","you clean your teeth with it"),
    ("hair","brush","you tidy your hair with it"),
    ("book","shelf","where you store your books"),
    ("water","fall","water tumbling off a cliff"),
    ("moon","light","the glow of night's satellite"),
    ("star","fish","a five-armed sea creature"),
    ("sea","shell","found on the beach, once a home"),
    ("play","ground","where children swing and slide"),
    ("bed","room","where you sleep"),
    ("news","paper","daily printed news"),
    ("pan","cake","a flat breakfast round"),
    ("straw","berry","a red seedy summer fruit"),
    ("black","board","a dark writing surface"),
    ("gold","fish","a small orange pet swimmer"),
    ("rail","road","where trains travel"),
    ("light","house","a tower guiding ships"),
    ("wheel","chair","a seat with wheels"),
    ("earth","quake","the shaking of the ground"),
    ("water","melon","a big green-and-red juicy fruit"),
    ("pop","corn","a fluffy movie snack"),
    ("cup","cake","a small frosted treat"),
    ("hedge","hog","a small spiny animal"),
    ("dragon","fly","a shimmering pond insect"),
    ("grass","hopper","a green jumping insect"),
    ("lady","bug","a red spotted beetle"),
    ("hum","mingbird","a tiny bird that hovers"),
    ("jelly","fish","a soft floating stinger"),
    ("skate","board","a board with four wheels for tricks"),
    ("sand","castle","a beach tower of sand"),
    ("snow","ball","a packed sphere of snow"),
    ("thunder","storm","a storm with lightning and booms"),
    ("under","ground","below the surface of the earth"),
    ("bird","house","a tiny home for birds"),
]
for a_part, b_part, clue in COMPOUNDS:
    if count() >= 1000: break
    add("I am a compound word. Join '" + a_part + "' and '" + b_part + "' to name " + clue + ". What word am I?",
        (a_part + b_part).capitalize(), "Put the two words together.", "words")

# ---- Baby animal name riddles ----
BABIES = [
    ("dog","puppy"),("cat","kitten"),("cow","calf"),("horse","foal"),("sheep","lamb"),
    ("goat","kid"),("pig","piglet"),("chicken","chick"),("duck","duckling"),("frog","tadpole"),
    ("kangaroo","joey"),("bear","cub"),("lion","cub"),("deer","fawn"),("goose","gosling"),
    ("swan","cygnet"),("owl","owlet"),("fox","kit"),("rabbit","kit"),("seal","pup"),
    ("whale","calf"),("elephant","calf"),("eagle","eaglet"),("spider","spiderling"),("butterfly","caterpillar"),
]
seen_baby = set()
for adult, baby in BABIES:
    if count() >= 1000: break
    q = "What do you call a baby " + adult + "?"
    add(q, "A " + baby, "A young " + adult + ".", "animals")

# ---- Animal group / home riddles ----
HOMES = [
    ("bee","hive"),("bird","nest"),("bear","den"),("rabbit","burrow"),("spider","web"),
    ("fox","den"),("horse","stable"),("pig","sty"),("dog","kennel"),("cow","barn"),
    ("bat","cave"),("fish","aquarium"),("ant","colony"),("eagle","eyrie"),("beaver","lodge"),
]
for animal, home in HOMES:
    if count() >= 1000: break
    add("Where does a " + animal + " live? Name its home.", "A " + home, "A " + animal + " home.", "animals")

# ---- Scrambled word riddles ----
SCRAMBLE = [
    ("elppa","apple"),("namoc","",),
]
SCR_WORDS = ["apple","tiger","house","river","cloud","music","light","chair","plant","stone",
             "bread","dance","smile","dream","ocean","piano","grape","robot","candy","brush",
             "eagle","lemon","zebra","spoon","clock","horse","ghost","flame","pearl","storm",
             "brick","chess","olive","otter","panda","queen","toast","vivid","wagon","yacht"]
def scramble(w):
    import random as _r
    _r.seed(sum(ord(ch) for ch in w))
    letters = list(w)
    for _ in range(20):
        _r.shuffle(letters)
        if "".join(letters) != w:
            break
    return "".join(letters)
for w in SCR_WORDS:
    if count() >= 1000: break
    s = scramble(w)
    add("Unscramble these letters to find a common word: '" + s.upper() + "'. What is the word?",
        w.capitalize(), "It has " + str(len(w)) + " letters and starts with '" + w[0].upper() + "'.", "words")

# ---- Fun trivia riddles ----
TRIVIA = [
    ("I am the largest ocean on Earth. What am I?", "The Pacific Ocean", "It's on the west of the Americas.", "geography"),
    ("I am the longest river in the world (by many counts). What am I?", "The Nile", "It flows through Egypt.", "geography"),
    ("I am the tallest mountain on Earth above sea level. What am I?", "Mount Everest", "In the Himalayas.", "geography"),
    ("I am the largest desert on Earth (a cold one). What am I?", "Antarctica", "It's covered in ice.", "geography"),
    ("I am the biggest animal that has ever lived. What am I?", "The blue whale", "Bigger than any dinosaur.", "animals"),
    ("I am the fastest land animal. What am I?", "The cheetah", "Spotted sprinter.", "animals"),
    ("I am the tallest animal in the world. What am I?", "The giraffe", "Long neck.", "animals"),
    ("I am the largest planet in our solar system. What am I?", "Jupiter", "A gas giant.", "space"),
    ("I am the hardest natural substance on Earth. What am I?", "A diamond", "A precious gem.", "concepts"),
    ("I am the only metal that is liquid at room temperature. What am I?", "Mercury", "Found in old thermometers.", "concepts"),
    ("I am the gas that plants breathe in and we breathe out. What am I?", "Carbon dioxide", "CO2.", "concepts"),
    ("I am the gas humans need to breathe to live. What am I?", "Oxygen", "About 21% of the air.", "concepts"),
    ("I am the closest star to Earth. What am I?", "The Sun", "It's daytime because of me.", "space"),
    ("I am the smallest prime number. What am I?", "2", "The only even prime.", "numbers"),
    ("I am the number of sides on a hexagon. What am I?", "6", "Like a honeycomb cell.", "numbers"),
    ("I am the number of colors in a rainbow. What am I?", "7", "Red to violet.", "numbers"),
    ("I am the number of continents on Earth. What am I?", "7", "Count them on a globe.", "geography"),
    ("I am the number of legs a spider has. What am I?", "8", "Arachnid legs.", "animals"),
    ("I am the number of players on a soccer team on the field. What am I?", "11", "Including the goalkeeper.", "sports"),
    ("I am the number of strings on a standard guitar. What am I?", "6", "Strum them all.", "music"),
]
for q, a, h, c in TRIVIA:
    if count() >= 1000: break
    add(q, a, h, c)


# Final arithmetic pad only if still short
half = set()
while count() < 1000:
    n = random.randint(2, 400) * 2
    if n in half: continue
    half.add(n)
    add(f"What is half of {n}?", str(n//2), "Split it into two equal parts.", "numbers")

TARGET = 1000
riddles_final = riddles[:TARGET]
# Assign ids
out = []
for i, r in enumerate(riddles_final, 1):
    out.append({"id": i, "q": r["q"], "a": r["a"], "hint": r["hint"], "cat": r["cat"]})

outpath = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "docs", "riddles", "riddles.json")
os.makedirs(os.path.dirname(outpath), exist_ok=True)
with open(outpath, "w", encoding="utf-8") as f:
    json.dump({"count": len(out), "riddles": out}, f, ensure_ascii=False, indent=0)

from collections import Counter
cats = Counter(r["cat"] for r in out)
print(f"Total riddles: {len(out)}")
print("By category:", dict(cats))
print("Written to:", os.path.normpath(outpath))
