#COPYRIGHT 2016
#BY NATHAN MORRISSEY

print "//===\\\  ===//  //\\\   ||\\\  //||   //\\\  ||     //   //===\\\ "
print "||   ||    //  //==\\\  ||  v// ||  //==\\\ ||//        \\\____"
print "\\\___//   //__//    \\\ ||      || //    \\\||\\\         _____||"
print " "
print "      //=====\\\  ||     ||  ||====  //=====\\\  ========"
print "      ||     ||  ||     ||  ||      \\\_____       ||"
print "      ||   \\\||  ||     ||  ||====         \\\     ||"
print "      \\\____\\\   \\\_____//  ||____   ______//     ||"
print " "
print "Centuries ago, the land of Amarin thrived under the rule of King Ozamak, \na wise and powerful ruler who placed the comfort of his kingdom above his own. \nEventually, however, Ozamak's power and riches began to corrupt his once-benevolent spirit. \nBy the end of the king's life, wars, famine, and disease had desomated his kingdom while he \nhid away in his castle's dungeons, admiring his wealth. Fearing death, Ozamak cast a spell \nupon himself, binding his consciousness to his body indefinitely. Ozamak the Lich guards the \ndungeon's treasure to this day. It is your duty to slay Ozamak and restore Amarin's glory!"
print " "
print 'What is your name, noble adventurer?'
name = raw_input('>')
print "Welcome, " + name + "! You can control your character by typing 'attack' to attack and enemy,\n'flee' to escape from an enemy, 'walk' to advance, 'inv' to display your inventory, 'heal' to use a healing potion."
print " "

defense = 1
damage = 10
crit_chance = .33
max_hp = 10000
hp = max_hp
healing_potions = 1
has_light = True
room = 0
sb_unlocked = False
game_over = False
flame_sword_unlocked = False
armor_unlocked = False
health_sheild_unlocked = False
moat_frozen = False


hp_regen = ['Health Regen', True]
freeze = ['Freeze', True]
confuse = ['Confuse', True]
fortify = ['Fortify', True]
sharpen = ['Sharpen', True]
light = ['Light', True]
weaken = ['Weaken', True]

player = [
    name, #..................0
    hp, #....................1
    max_hp, #................2
    damage, #................3
    crit_chance, #...........4
    healing_potions, #.......5
    freeze, #................6      spell
    hp_regen, #..............7      ''
    confuse, #...............8      ''
    fortify, #...............9      ''
    sharpen, #...............10     ''
    light, #.................11     ''
    weaken, #................12     ''
    has_light, #.............13
    sb_unlocked, #...........14
    flame_sword_unlocked, #..15
    armor_unlocked, #........16
    health_sheild_unlocked, #17
    moat_frozen, #...........18
    defense #................19
    ]

skeleton = ['skeleton', 1, 5]
spider = ['spider', 1, 10]
zombie = ['zombie', 30, 7]
witch_doctor = ['Witch Doctor', 100, 15]
posessed_armor = ['Posessed Armor', 200, 20]
ozamak = ['Ozamak the Lich', 1000, 40]

def reset(creature):
    if creature == skeleton:
        return ['skeleton', 1, 5]
    elif creature == spider:
        return ['spider', 1, 10]
    elif creature == zombie:
        return ['zombie', 1, 7]
    elif creature == witch_doctor:
        return ['Witch Doctor', 1, 15]
    elif creature == posessed_armor:
        return ['Posessed Armor', 2, 20]
    else:
        return ['Ozamak the Lich', 1000, 40]

def battle(p, e):
    #while both player hp and enemy hp are over 0
    while p[1] > 0:
        print " "
        print "your HP:" + str(p[1])
        print " "
        print e[0] + " HP:" + str(e[1])
        while 1:
            print " "
            userIn = raw_input('>')
            print " "
            if userIn.lower() == "attack" or userIn.lower() == 'a':
                print "you attacked and did " + str(p[3]) + " damage!"
                e[1] -= p[3]
                break
            elif userIn.lower() == 'heal':
                p = heal(p)
            elif (userIn.lower() == 'spellbook' or userIn.lower() == 's') and p[14]:
                p = spellbook(p, 0)
            else:
                print 'Cannot perform that command'
        if e[1] <= 0:
            print "You defeated the " + e[0] + "!"
            break

        #subtract enemy damage from player hp
        print e[0] + " attacked and did " + str(e[2]/p[19]) + " damage!"
        p[1] -= e[2]/p[19]
        if p[1] <= 0:
            break
    p[19] = 1.0
    return p

def heal(p):
    if p[5] > 0:
        if p[1] <= (p[2] - 50):
            p[1] += 50
        else:
            p[1] = p[2]
        p[5] -= 1
        print "You have healed! Current HP: " + str(p[1])
        print "You have " + str(p[5]) + " healing potions left."
    else:
        print "No more healing potions!"
    return p

def spellbook(p, room):
    print " "
    print " ___________________________________________----------____________________________________________"
    print " ==============                                                                   ================"
    print " |              ==============              ===========             ==============               |"
    print " |                             =============     |     =============                             |"
    print " |                                               |                                               |"
    print " |                                               |                                               |"
    print " |                                               |                                               |"
    print " |                                               |                                               |"
    print " |                    " + p[6][0] + "                     |                     " + p[10][0] + "                   |"
    print " |                                               |                                               |"
    print " |                                               |                                               |"
    print " |                  " + p[7][0] + "                 |                     " + p[11][0] + "                     |"
    print " |                                               |                                               |"
    print " |                                               |                                               |"
    print " |                   " + p[8][0] + "                     |                     " + p[12][0] + "                    |"
    print " |                                               |                                               |"
    print " |                                               |                                               |"
    print " |                   " + p[9][0] + "                     |                                               |"
    print " |                                               |                                               |"
    print " |                                               |                                               |"
    print " |                                               |                                               |"
    print " |                                               |                                               |"
    print " |                                               |                                               |"
    print " |                                               |                                               |"
    print " |                                               |                                               |"
    print " |                                               |                                               |"
    print " |                                               |                                               |"
    print " =============                                   |                                 =============="
    print "              =================             ===========            ==============="
    print "                               =============           ============"
    print " "
    print " "
    print "From now on, type 'spellbook' to access this menu. Type anything besides a spell's name to exit this menu."
    print "Which spell would you like to use? You may only use each spell once."
    p[14] = True
    userIn = raw_input('>')
    if userIn.lower() == 'light' and p[11][1]:
        print "You used Light. The spellbook glows to light the way."
        p[11][0] = '     '
        p[13] = True
        p[11][1] = False
        return p
    elif userIn.lower() == 'freeze' and p[6][1]:
        print "You used Freeze. Any water nearby is frozen."
        p[6][0] = '      '
        p[18] = True
        p[6][1] = False
        return p
    elif userIn.lower() == 'fortify' and p[9][1]:
        print "You used Fortify. Your defense temporarily increases."
        p[9][0] = '       '
        p[9][1] = False
        p[19] += .5
        return p
    else:
        print "That doesnt seem to do much..."
        return p



def rooms(room, p, sk, sp, zb, pa, wd):
    if room == 1:
        print "Your torch lights up the corridor, revealing a long hallway lined with various\nworn-out tapestries and rusty suits of armor."

        p = user_input(p, room)

        print "Despite doing your best to stay quiet, an army of skeletons crawl from every doorway,\nconverging on your location!"
        p = battle(p, sk)
        sk = reset(sk)
        print "Another skeleton attacks!"
        p = battle(p, sk)
        sk = reset(sk)
        print "Another skeleton attacks!"
        p = battle(p, sk)
        sk = reset(sk)
        if p[1] <= 0:
            print "You were killed."
            return p

        print "After slaying the first three skeletons and picking up a health potion (+50 hp),\nyou find an escape route through a crack in the rock wall."
        p[5] += 1
        print "Do you want to take the escape route or fight your way past the skeletons? (escape, fight)"
        escaped = False
        userIn = ''
        while 1:
            userIn = raw_input('>')
            if userIn.lower() == 'escape':
                p = rooms(4, p, sk, sp, zb, pa, wd)
                escaped = True
                break
            elif userIn.lower() == 'fight':
                break
            elif userIn.lower() == 'heal':
                p = heal(p)
            else:
                print "That is not a valid option."

        if p[1] <= 0:
            return p

        if escaped == False:
            print "You continue fighting the skeletons..."
            print "Another skeleton attacks!"
            p = battle(p, sk)
            sk = reset(sk)
            print "Another skeleton attacks!"
            p = battle(p, sk)
            sk = reset(sk)
            if p[1] <= 0:
                return p
            print "Finally you slash your way past the last corpse and find yourself in a candle-lit chamber."
        else:
            print "Through the door, you climb a stone spiral staircase and arrive in a candle-lit chamber."

        p = user_input(p, room)
        print "Advancing, you come to an allyway with a tile floor. You step on one of the tiles but it falls\naway underfoot! You realize that this must be a puzzle. On the wall you read this inscription:"
        print " "
        print " "
        print "        I am a well-known sequence, you see,"
        print "           Most often solved recursively!"
        print " "
        print " "
        print "you look ahead and notice that the tiles are numbered like so:"
        print " "
        print " "
        print "                               FINISH"
        print "  =================================================================="
        print "  |            |            |            |            |            |"
        print "  |      1     |      2     |      3     |      4     |      5     |"
        print "  |            |            |            |            |            |"
        print "  |            |            |            |            |            |"
        print "  =================================================================="
        print "  |            |            |            |            |            |"
        print "  |      1     |      2     |      3     |      4     |      5     |"
        print "  |            |            |            |            |            |"
        print "  |            |            |            |            |            |"
        print "  =================================================================="
        print "  |            |            |            |            |            |"
        print "  |      1     |      2     |      3     |      4     |      5     |"
        print "  |            |            |            |            |            |"
        print "  |            |            |            |            |            |"
        print "  =================================================================="
        print "  |            |            |            |            |            |"
        print "  |      1     |      2     |      3     |      4     |      5     |"
        print "  |            |            |            |            |            |"
        print "  |            |            |            |            |            |"
        print "  =================================================================="
        print "  |            |            |            |            |############|"
        print "  |      1     |      2     |      3     |      4     |############|"
        print "  |            |            |            |            |############|"
        print "  |            |            |            |            |############|"
        print "  =================================================================="
        print "                               START"
        print " "
        print "Starting from the bottom, taking one step per row, enter the numbers of the steps you wish to take\nseparated by spaces. ie:2 4 1 3 5"

        userIn = raw_input('>')
        if userIn == '1 1 2 3 5' or userIn == '11235':
            print "That was the right path! You make it accross safely."
        elif userIn == '1':
            print "You step on the first platform and you hear a slow rumble...and then nothing.\n You have taken the correct first step."
            userIn = raw_input('>')
            if userIn == '1':
                print "You step on to the next platform. You have chosen wisely."
                userIn = raw_input('>')
                if userIn == '2':
                    print "You step on to the next platform. You have chosen wisely."
                    userIn = raw_input('>')
                    if userIn == '3':
                        print "You step on to the next platform. You have chosen wisely."
                        userIn = raw_input('>')
                        if userIn == '5':
                            print "You step on to the next platform. You have chosen wisely."
                        else:
                            print "You take a wrong step and plummet to your death."
                            p[1] = 0
                            return p
                    else:
                        print "You take a wrong step and plummet to your death."
                        p[1] = 0
                        return p
                else:
                    print "You take a wrong step and plummet to your death."
                    p[1] = 0
                    return p
            else:
                print "You take a wrong step and plummet to your death."
                p[1] = 0
                return p
        else:
            print "You take a wrong step and plummet to your death."
            p[1] = 0
            return p

        print "On the other side of the trap you stop to catch your breath and hear a faint moaning coming from up ahead."
        p = user_input(p, room)
        print "It appears like just another zombie but something seems different. You can just barely make out a metalic\nnoise each time the creature steps cloaser. Now you can see your light glinting off of a fiery\nbroadsword and suit of armor. You can only guess at hat grotesque, rotting corpse lies beneath.\nYou draw your sword and prepart to battle the beast."
        p = battle(p, pa)
        if p[1] <= 0:
            return p

        print "After a long and grueling battle, your sword finds its way through the armor and strikes the creature's heart.\nYou grasp the sword from its dead fingers, claiming it as your own. (+10 base damage)"
        p[3] += 10
        p[15] = True
        print "There seems to be an exit... You take it and it leads you back to the main room with the four doors."
        return p

    elif room == 2:
        print "filler 2"
        return p
    elif room == 3:
        print "filler 3"
        return p
    elif room == 4:
        print "You escaped the skeletons but now find yourself in a dusty library full of tomes and spellbooks.\nUnfortunately, you dropped your torch as you were making your escape. Now your only source of light\nis that of the torch through the crack you climbed through."
        p = user_input(p, room)
        print "You walk a bit further into the labyrinth of books but don't have enought light to proceed.\nYou decide to look through some spellbooks for something to help you navigate the maze. One ancient,\nleather-bound tome with a ruby-studded spine stands out in particular. You open it and find this:"
        p[13] = False
        while 1:
            print "You can't find your way throught this maze in the dark. You need some sort of light source."
            p = spellbook(p, room)
            if p[13] == True:
                break
        print "That spell seems to have proveded you with a portable light source!"
        p = user_input(p, room)
        print "The area is illuminated just in time to reveal a nest of spiders.\nYou still have time to flee but in doing so you could miss out on some loot. (escape, fight)"

        while 1:
            userIn = raw_input('>')
            if userIn.lower() == 'escape':
                break
            elif userIn.lower() == 'fight':
                print "You have a spider in your sights!"
                p = battle(p, sp)
                sp = reset(sp)
                print "Another spider attacks!"
                p = battle(p, sp)
                sp = reset(sp)
                print "Another spider attacks!"
                p = battle(p, sp)
                sp = reset(sp)
                if p[1] > 0:
                    break
                else:
                    return p
            else:
                print "Not a valid command."

        print "You defeated the nest and claim a healing potion (+50 hp)"
        p[5] += 1

        print "As you continue to walk, the rows of book cases grow farther apart and you eventually\nreach a deep moat filled with man-eating leaches. The exit seems to be just on the other side!"
        while 1:
            print "You must find a way to cross the moat."
            p = user_input(p, room)
            if p[18] == True:
                break

        print "The spell you used froze the water in front of you! You may now cross the frozen moat."
        p = user_input(p, room)
        print "You arrive at the exit"
        return p


def user_input(p, room):
    userIn = ''
    while 1:
        userIn = raw_input('>')
        if userIn.lower() == 'walk' or userIn.lower() == 'w':
            break
        elif userIn.lower() == 'heal' or userIn.lower() == 'h':
            p = heal(p)
        elif (userIn.lower() == 'spellbook' or userIn.lower() == 's') and p[14] == True:
            p = spellbook(p, room)
        elif userIn == 'player':
            print p
        else:
            print 'Cannot perform that command'
    return p


def choose_room(p):
    print "You walk over to the first door and see this carving on it:"
    print " "
    print "         (0)"
    print "       (0).(0)"
    print "         |||"
    print "         |||"
    print "         |||"
    print "    //=========\\\ "
    print "   //^^^| | |^^^\\\ "
    print "   V    | | |    V"
    print "        | | | "
    print "        | | | "
    print "        | | | "
    print "        | | | "
    print "        | | | "
    print "        | | | "
    print "        | | | "
    print "        | | | "
    print "        | | | "
    print "        | | | "
    print "        | | | "
    print "        | | | "
    print "        | | | "
    print "        | | | "
    print "        | | | "
    print "        \ | /"
    print "         \ /"
    print "          V"

    p = user_input(p, room)

    print "You walk over to the second door and see this carving on it:"
    print " "
    print "              __  "
    print "        __   /==\    __"
    print "       /==\  |   |  /==\ "
    print "       |   |  \   \ |   |    _"
    print "        \   \  | _ | \   \  /=\ "
    print " ___     | _ | |   |  | _ || _/ "
    print "|===\    |   | |   |  |   |/  |"
    print " \    \  |  . \|  . \|  . / . /"
    print "   \    \|                /  /"
    print "     \  \   |    |   |   /  /"
    print "      |  |  |    |   /  /  |"
    print "      |   \  \    /  | |  |"
    print "      |                   |"
    print "     /  0   0   0   0   0 \ "
    print "     |___ .    .   .   .___|"
    print "         \____________/"


    p = user_input(p, room)

    print "You walk over to the second door and see this carving on it:"
    print " "
    print "    |\_                      _/|"
    print "    |  \___              ___/  |"
    print "    |      \____________/      |"
    print "    |                          |"
    print "    |                          |"
    print "    |           ||||           |"
    print "    |           ||||           |"
    print "     \      ============      /"
    print "      |     ============     |"
    print "       \        ||||        /"
    print "        \_      ||||      _/"
    print "          \___        ___/"
    print "              \______/"
    print " "
    print "The fourth door seems to be locked by a powerful spell."
    print " "

    if p[15] and p[16]:
        choice = '(3)'
    elif p[15] and p[17]:
        choice = '(2)'
    elif p[16] and p[17]:
        choice = '(1)'
    elif p[15]:
        choice = '(2, 3)'
    elif p[16]:
        choice = '(1, 3)'
    elif p[17]:
        choice = '(1, 2)'
    else:
        choice = '(1, 2, 3)'

    print "Which door do you want to enter? " + choice

    userIn = ''
    while 1:
        userIn = raw_input('>')
        if userIn in choice:
            break
        elif userIn.lower() == 'heal':
            p = heal(p)
        else:
            print "That is not a valid door."
    print "You enter door " + userIn
    return int(userIn), p


#main game loop
while 1:
    print "                          ===    ====    ====    ====    ====    ====    ==="
    print "                         |   |__|    |__|    |__|    |__|    |__|    |__|   |"
    print "                         |                                                  |"
    print "                         |                                                  |"
    print "                         |                                                  |"
    print "                         |             =====                =====           |"
    print "                         |            /     \              /     \          |"
    print "                         |           |       |            |       |         |"
    print "                         |           |       |            |       |         |"
    print "                         |           |_______|            |_______|         |"
    print "                          \_                                              _/"
    print "                            \_                                          _/"
    print "                              \                                        /"
    print "                               \_                                    _/"
    print "                                |                                    |"
    print "      ====    ====    ====    ==|                                    |==    ====    ====    ===="
    print "     |    |__|    |__|    |__|  |                                    |  |__|    |__|    |__|    |"
    print "     |                          |                                    |                          |"
    print "     |                          |                                    |                          |"
    print "     |          _______         |                                    |         _______          |"
    print "     |         ||_|_|_||        |                                    |        ||_|_|_||         |"
    print "     |         ||_|_|_||        |                                    |        ||_|_|_||         |"
    print "     |         ||_|_|_||        |                                    |        ||_|_|_||         |"
    print "     |                          |               =======              |                          |"
    print "     |                          |              /| | | |\             |                          |"
    print "     |                          |             |_|_|_|_|_|            |                          |"
    print "     |                          |             |_|_|_|_|_|            |                          |"
    print "     |__________________________|_____________|_|_|_|_|_|____________|__________________________|"
    print " "
    print " "
    print "You enter the ancient dungeon, brushing aside thick sheets of cobwebs as you go.\nOn the wall you find a torch and light it, illuminating the dark chamber."

    player = user_input(player, room)

    print "As you turn the corner, a creature ambushes you!"

    player = battle(player, zombie)
    zombie = reset(zombie)
    print player
    if player[1] <= 0:
        print "You were defeated!"
        break
    print " "
    print "Past the creature's bloody carcass you make out the outline of four doors."

    player = user_input(player, room)

    if not player[15] or not player[16] or not player[17]:
        room, player = choose_room(player)

    #go to that room
    player = rooms(room, player, skeleton, spider, zombie, posessed_armor, witch_doctor)


    if player[1] <= 0:
        break

#Game Over
print " //===\\\   //\\\   ||\\\//||  ||===       //===\\\   \\\    //  ||===   ||==\\\ "
print "||  =\\\   //==\\\  || V/ ||  ||===       ||   ||    \\\  //   ||===   ||==//"
print " \\\__||  //    \\\ ||    ||  ||===       \\\___//     \\\//    ||===   ||  \\\ "

