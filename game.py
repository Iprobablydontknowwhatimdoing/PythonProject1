from typing import List, Optional
# You walk where no man has walked before. This path hasn't been implemented yet

def show_options(option_list: List[str]):
    i = 1
    for string in option_list:
        print(f' {i}. {string}')
        i += 1


def decide(decisions: List[str], show_by_default: Optional[bool]):
    if show_by_default:
        show_options(decisions)
    answer = input('What do you want to do? (you can always say \'hint\') > ')
    if answer.lower().strip() == "hint":
        show_options(decisions)
        return decide(decisions, False)
    elif answer.lower().strip() in decisions:
        return decisions.index(answer.lower().strip())
    elif ord(answer.lower().strip()[0]) == ord('1') or ord(answer.lower().strip()[0]) == ord('2') or ord(answer.lower().strip()[0]) == ord('3') or ord(answer.lower().strip()[0]) == ord('4') or ord(answer.lower().strip()[0]) == ord('5') or ord(answer.lower().strip()[0]) == ord('6') or ord(answer.lower().strip()[0]) == ord('7') or ord(answer.lower().strip()[0]) == ord('8') or ord(answer.lower().strip()[0]) == ord('9'):
        return int(answer.lower().strip()[0]) - 1
    else:
        print('Sorry, I didn\'t catch that, please try again')
        return decide(decisions, False)


discoveredOptions: dict[str, bool] = {'guard change': False, 'club': False, 'dagger': False, 'lock picks': False,
                                      'key wax': False, 'cards': False, 'lamp': False}
def failure_condition():
    print("Regardless of how you did it, you lost, so this is where your story ends. Better luck next time.")
    decision = decide(['retry','quit'],True)
    match decision:
        case 0:
            discoveredOptions['guard change'] = False
            discoveredOptions['club'] = False
            discoveredOptions['dagger'] = False
            discoveredOptions['lock picks'] = False
            discoveredOptions['key wax'] = False
            discoveredOptions['cards'] = False
            discoveredOptions['lamp'] = False
            print("\nThis is your second life! don't waste it.\n\n")
            SmugglersHideout.describe_main_room()
        case 1:
            print("\nO.K. Goodbye. Hope you had fun!")
def victory_condition(): #TODO: turn off lamp option
    print("You walk where no man has walked before. This path hasn't been implemented yet")
    print("Even though I haven't fleshed out this part, Congratulations! You beat the game! How does it feel?")
    print("Do you want to try again?")
    decision = decide(['play again','quit'],True)
    match decision:
        case 0:
            discoveredOptions['guard change'] = False
            discoveredOptions['club'] = False
            discoveredOptions['dagger'] = False
            discoveredOptions['lock picks'] = False
            discoveredOptions['key wax'] = False
            discoveredOptions['cards'] = False
            discoveredOptions['lamp'] = False
            print("\nHave fun on your second run!\n\n")
            SmugglersHideout.describe_main_room()
        case 1:
            print("Hope you had fun, and congratulations again!")
class Graysoul:
    @staticmethod
    def describe_outside_safehouse():
        print("You find yourself in an old grimy alley, which you follow to the main road leading into the city. You know that\n"#TODO: search for this path hasnt been implemented
              "if you continue along this path you'll eventually get to the jailhouse where Gurathen is being held. Are you ready to\n"
              "try to get him out?")
        if discoveredOptions['guard change']:#TODO: remove debug
            decision = decide(['follow path', 'wait until shift change','go back'],False)
            match decision:
                case 0:
                    print("You continue along the path, paved with cobblestones. You can feel the beating of your heart as \n"
                          "people pass by you, but noone seems to think anything is out of the ordinary. It's been a while \n"
                          "since you walked these streets, and the cobblestones feel rough and hard against your worn-down shoes\n"
                          "compared to the dirt you normalley walk on. You reach the bridge, and as you walk over it the water rushes \n"
                          "beneath you, nearly but not quite covering the clattering of the planks of wood that make up the \n"
                          "bridge. The spray brings welcome releaf from both the stuffy summer night and the rancid oder that \n"
                          "seems to fill nearly all cities.")
                    Graysoul.describe_jailhouse(False)
                case 1:
                    print("You decide to wait until the guard changes shift. How do you want to do that?")
                    time_decision = decide(['walk in the park','watch the river','buy some food'], True)
                    match time_decision:
                        case 0:
                            print("You decide to walk for a while in the park, which is one of the few parks in a city in \n"
                                  "the entire empire, which was part of the reason you decided to move here (not that you \n"
                                  "make much use of it now). Calling it a park would be a bit generous, it was more the size of a \n"
                                  "large community garden and a small clearing, and contained about as much vegetation. But \n"
                                  "despite this, it offered a respite from the city that you much appreciate, and offers \n"
                                  "city-dwellers a place to think where they could pretend to be somewhere else. The time \n"
                                  "passes quickly, and before you know it, the guard is about to change.")
                            Graysoul.describe_jailhouse(True)
                        case 1:
                            print("You decide to sit and watch the river. The bubbling of the river brings back memories of \n"
                                  "playing on the farm where you grew up. As you swing your legs over the edge to hopefully catch \n"
                                  "some cool spray, you think of how you spent your life and of your childhood. You long to \n"
                                  "be a kid again, or at least to have a choice in what you are. it isn't long before the guard \n"
                                  "is about to change, and you get up from the bridge as guards shuffle with their lantern held \n"
                                  "out to ward against the dark, and follow them.")
                            Graysoul.describe_jailhouse(True)
                        case 2:
                            print("You walk where no man has walked before. This path hasn't been implemented yet")
                            print("It's time for you to make your friend escape.")
                            Graysoul.describe_jailhouse(True)
                case 2:
                    print("You return to the smugglers' den.")
                    SmugglersHideout.describe_main_room()
        else:
            decision = decide(['follow path', 'go back'], False)
            match decision:
                case 0:
                    print(
                        "You continue along the path, paved with cobblestones. You can feel the beating of your heart as \n"
                        "people pass by you, but noone seems to think anything is out of the ordinary. It's been a while \n"
                        "since you walked these streets, and the cobblestones feel rough and hard against your worn-down shoes\n"
                        "compared to the dirt you normally walk on. You reach the bridge, and as you walk over it the water rushes \n"
                        "beneath you, nearly but not quite covering the clattering of the planks of wood that make up the \n"
                        "bridge. The spray brings welcome releaf from both the stuffy summer night and the rancid oder that \n"
                        "seems to fill nearly all cities.")
                    Graysoul.describe_jailhouse(False)
                case 1:
                    print("You return to the smugglers' den.")
                    SmugglersHideout.describe_main_room()

    @staticmethod
    def describe_jailhouse(waited_shift: bool):
        print("The jailhouse is surprisingly small; it doesn't even have a second floor. It doesn't have to, you suppose, \n"
              "when execution is the punishment for every, even minor, infraction. It also makes your job harder.")
        if waited_shift:
            print("As you approach the guardhouse, sneaking just ahead of the shift change guards, you see the \n"
                  "flickering lights of the jailhouse, coming from a group inside who huddle around a table playing a game \n"
                  "of cards. They don't have a straight view of the holding cells, and you think if you hadn't waited until the \n"
                  "shift, they might patrol the cells and catch you. You see a back door that you could sneak through, and avoid \n"
                  "the guards at the front door. You'll have to be quick though; If you don't hurry, then the guards in the \n"
                  "next shift will catch you. So you hurry to the back. You approach the door, under which a feint warm light \n"
                  "streams out. When you try to turn the handle, though, it doesn't budge; the door is locked.")
            if discoveredOptions['key wax'] or discoveredOptions['lock picks']:
                if discoveredOptions['key wax'] and discoveredOptions['lock picks']:
                    print("You have two ways of opening this lock. You know the key imprint device will work, but if you use that, then \n"
                          "it may take too long. You are good with lock picks, but if you can't get the lock open, it will definitely\n"
                          "take too long. You think you recognize the lock though, and it's one you have good experience with.")
                    decision = decide(['use key imprint device', 'use lock picks'], False)
                    match decision:
                        case 0:
                            print("You bring the key imprint device to the lock, and mold it to the inside of the lock. \n"
                                  "After five minutes of waiting, you can turn the key and successfully turn the door.\n")
                            Graysoul.describe_inside_jailhouse()
                            print("You kneel to unlock the cell door. You already used your key imprint device on the back door, so here \n"
                                  "you get out your lock picks. With a little time and difficulty, you manage to unlock the door. But just as \n"
                                  "you start to usher Gurathen out (with a finger on your lips for silence), three of the shift change guards \n"
                                  "burst from the door and capture you, pushing you to the ground, and bind you. Gurathen is shoved back in \n"
                                  "his cell, and you are put in a cell opposite his. He cries out, but is quickly silenced by the guards, and \n"
                                  "both of you are gagged with a gruff 'Can't have you talking to each other' from one of the guards.")
                            failure_condition()
                        case 1:
                            print("You get out your lock picks, and smoothly pick the lock. You have enough experience practicing on this model \n"
                                  "it barely takes any time at all, and you slide the door open to enter the jailhouse.")
                            Graysoul.describe_inside_jailhouse()
                            print("After you tell Gurathen to be quite with a finger to your lips, you kneel down to unlock his cell. You don't \n"
                                  "have as much experience with this lock,  so it would take longer than the key imprint device, but mercifully, this \n"
                                  "lock is relatively rustless. You think you could pretty easily open it, as though you haven't practiced particularly \n"
                                  "on this model, it is a much lest robust lock, as it seems the guards were relying on themselves being there to catch \n"
                                  "intruders.")
                            decision = decide(['use key imprint device','use lock picks','bust door open'], False)
                            match decision:
                                case 0:
                                    print("You get the key imprint device and set it into the lock and let it set. But as you turn it, \n"
                                          "the guards open the door and see you. You took too long letting the key set, and they see you \n"
                                          "at the cell door. They rush to surround you, and put you inside a cell opposite Gurathen's. \n"
                                          "They bind you with ropes, take everything you have on you, and lock the door.")
                                    failure_condition()
                                case 1:
                                    print("Your lock picks slide into place, and click the cell door opens. You gesture for Gurathen to \n"
                                          "leave the cell, and hurry to the back door. After you leave, though, you see a guard coming \n"
                                          "around the building, presumably on a normal circuit. As he rounds the building, he sees you.")
                                    if discoveredOptions['dagger'] or discoveredOptions['club']:
                                        if discoveredOptions['dagger'] and discoveredOptions['club']:
                                            print("but before he attacks you, you have a split second to act. You could attack him with your dagger or your \n"
                                                  "club, or you could just run and hope he isn't fast enough to catch you.")
                                            decision = decide(['attack with club', 'attack with dagger', 'run'], False)
                                            match decision:
                                                case 0:
                                                    print("You club him in the back of the head, and he falls to the ground. You knocked him out, but you didn't kill him \n"
                                                          "You should move quickly before his fellow guards notice that he hasn't come back. You rush down the path the way you \n"
                                                          "came, and manage to get out of the city before the guard catches you!")
                                                    victory_condition()
                                                case 1:
                                                    print("You attack him with the dagger, aiming for the throat (hoping to silence him). But because of \n"
                                                          "your ineptitude with the dagger, you slip and only hit him in the chest. He hits you with his baton \n"
                                                          "in your second of shock, and knocks you out.")
                                                    failure_condition()
                                                case 2:
                                                    print("You decide to run away, and grab Gurathen, hauling him after you. You successfully make it to the safe house,\n"
                                                          "but what you don't know is that you were being tracked. Just as you settle down at the table in the main room,\n"
                                                          "a dozen guards and policemen shove through the door and arrest you and the rest of the smugglers, taking the goods \n"
                                                          "and bringing you all to the jailhouse. In the rush, you are separated from Gurathen and can't tell if he escaped.")
                                                    failure_condition()
                                        if discoveredOptions['dagger']:
                                            decision =  decide(['attack','run'],False)
                                            match decision:
                                                case 0:
                                                    print(
                                                        "You attack him with the dagger, aiming for the throat (hoping to silence him). But because of \n"
                                                        "your ineptitude with the dagger, you slip and only hit him in the chest. He hits you with his baton \n"
                                                        "in your second of shock, and knocks you out.")
                                                    failure_condition()
                                                case 1:
                                                    print(
                                                        "You decide to run away, and grab Gurathen, hauling him after you. You successfully make it to the safe house,\n"
                                                        "but what you don't know is that you were being tracked. Just as you settle down at the table in the main room,\n"
                                                        "a dozen guards and policemen shove through the door and arrest you and the rest of the smugglers, taking the goods \n"
                                                        "and bringing you all to the jailhouse. In the rush, you are separated from Gurathen and can't tell if he escaped.")
                                                    failure_condition()
                                        if discoveredOptions['club']:
                                            decision = decide(['attack', 'run'], False)
                                            match decision:
                                                case 0:
                                                    print(
                                                        "You club him in the back of the head, and he falls to the ground. You knocked him out, but you didn't kill him \n"
                                                        "You should move quickly before his fellow guards notice that he hasn't come back. You rush down the path the way you \n"
                                                        "came, and manage to get out of the city before the guard catches you!")
                                                    victory_condition()
                                                case 1:
                                                    print(
                                                        "You decide to run away, and grab Gurathen, hauling him after you. You successfully make it to the safe house,\n"
                                                        "but what you don't know is that you were being tracked. Just as you settle down at the table in the main room,\n"
                                                        "a dozen guards and policemen shove through the door and arrest you and the rest of the smugglers, taking the goods \n"
                                                        "and bringing you all to the jailhouse. In the rush, you are separated from Gurathen and can't tell if he escaped.")
                                                    failure_condition()
                                        else:
                                            print(
                                                "You try to run away, and grab Gurathen, hauling him after you. You successfully make it to the safe house,\n"
                                                "but what you don't know is that you were being tracked. Just as you settle down at the table in the main room,\n"
                                                "a dozen guards and policemen shove through the door and arrest you and the rest of the smugglers, taking the goods \n"
                                                "and bringing you all to the jailhouse. In the rush, you are separated from Gurathen and can't tell if he escaped.")
                                            failure_condition()
                if discoveredOptions['lock picks']:
                    print(
                        "You get out your lock picks, and smoothly pick the lock. You have enough experience practicing on this model \n"
                        "it barely takes any time at all, and you slide the door open to enter the jailhouse.")
                    Graysoul.describe_inside_jailhouse()
                    print(
                        "After you tell Gurathen to be quite with a finger to your lips, you kneel down to unlock his cell. You don't \n"
                        "have as much experience with this lock,  so it would take longer than the key imprint device, but mercifully, this \n"
                        "lock is relatively rustless. You think you could pretty easily open it, as though you haven't practiced particularly \n"
                        "on this model, it is a much lest robust lock, as it seems the guards were relying on themselves being there to catch \n"
                        "intruders.")
                    print(
                        "Your lock picks slide into place, and click the cell door opens. You gesture for Gurathen to \n"
                        "leave the cell, and hurry to the back door. After you leave, though, you see a guard coming \n"
                        "around the building, presumably on a normal circuit. As he rounds the building, he sees you.")
                    if discoveredOptions['dagger'] or discoveredOptions['club']:
                        if discoveredOptions['dagger'] and discoveredOptions['club']:
                            print(
                                "but before he attacks you, you have a split second to act. You could attack him with your dagger or your \n"
                                "club, or you could just run and hope he isn't fast enough to catch you.")
                            decision = decide(['attack with club', 'attack with dagger', 'run'], False)
                            match decision:
                                case 0:
                                    print(
                                        "You club him in the back of the head, and he falls to the ground. You knocked him out, but you didn't kill him \n"
                                        "You should move quickly before his fellow guards notice that he hasn't come back. You rush down the path the way you \n"
                                        "came, and manage to get out of the city before the guard catches you!")
                                    victory_condition()
                                case 1:
                                    print(
                                        "You attack him with the dagger, aiming for the throat (hoping to silence him). But because of \n"
                                        "your ineptitude with the dagger, you slip and only hit him in the chest. He hits you with his baton \n"
                                        "in your second of shock, and knocks you out.")
                                    failure_condition()
                                case 2:
                                    print(
                                        "You decide to run away, and grab Gurathen, hauling him after you. You successfully make it to the safe house,\n"
                                        "but what you don't know is that you were being tracked. Just as you settle down at the table in the main room,\n"
                                        "a dozen guards and policemen shove through the door and arrest you and the rest of the smugglers, taking the goods \n"
                                        "and bringing you all to the jailhouse. In the rush, you are separated from Gurathen and can't tell if he escaped.")
                                    failure_condition()
                        if discoveredOptions['dagger']:
                            decision = decide(['attack', 'run'], False)
                            match decision:
                                case 0:
                                    print(
                                        "You attack him with the dagger, aiming for the throat (hoping to silence him). But because of \n"
                                        "your ineptitude with the dagger, you slip and only hit him in the chest. He hits you with his baton \n"
                                        "in your second of shock, and knocks you out.")
                                    failure_condition()
                                case 1:
                                    print(
                                        "You decide to run away, and grab Gurathen, hauling him after you. You successfully make it to the safe house,\n"
                                        "but what you don't know is that you were being tracked. Just as you settle down at the table in the main room,\n"
                                        "a dozen guards and policemen shove through the door and arrest you and the rest of the smugglers, taking the goods \n"
                                        "and bringing you all to the jailhouse. In the rush, you are separated from Gurathen and can't tell if he escaped.")
                                    failure_condition()
                        if discoveredOptions['club']:
                            decision = decide(['attack', 'run'], False)
                            match decision:
                                case 0:
                                    print(
                                        "You club him in the back of the head, and he falls to the ground. You knocked him out, but you didn't kill him \n"
                                        "You should move quickly before his fellow guards notice that he hasn't come back. You rush down the path the way you \n"
                                        "came, and manage to get out of the city before the guard catches you!")
                                    victory_condition()
                                case 1:
                                    print(
                                        "You decide to run away, and grab Gurathen, hauling him after you. You successfully make it to the safe house,\n"
                                        "but what you don't know is that you were being tracked. Just as you settle down at the table in the main room,\n"
                                        "a dozen guards and policemen shove through the door and arrest you and the rest of the smugglers, taking the goods \n"
                                        "and bringing you all to the jailhouse. In the rush, you are separated from Gurathen and can't tell if he escaped.")
                                    failure_condition()
                        else:
                            print(
                                "You try to run away, and grab Gurathen, hauling him after you. You successfully make it to the safe house,\n"
                                "but what you don't know is that you were being tracked. Just as you settle down at the table in the main room,\n"
                                "a dozen guards and policemen shove through the door and arrest you and the rest of the smugglers, taking the goods \n"
                                "and bringing you all to the jailhouse. In the rush, you are separated from Gurathen and can't tell if he escaped.")
                            failure_condition()
        else:
            print("As you approach the guardhouse you see the flickering lights of the jailhouse, coming from a group inside \n"
                  "who huddle around a table playing a game of cards. They don't have a straight view of the holding cells. \n"
                  "You see a back door that you could sneak through, and avoid the guards at the front door. You'll have \n"
                  "to be quick though; If you don't hurry, then the guards will throw you in too, so you hurry to the back. \n"
                  "You approach the door, under which a feint warm light streams out. When you try to turn the handle, though, \n"
                  "it doesn't budge; the door is locked. And just as you're doing that, a guard circles around the building. \n"
                  "He calls out that someone is trying to get into the jailhouse, and more guards come rushing towards you. You manage \n"
                  "to run away, but the guards are on high alert the rest of the night, and you don't get another opportunity to \n"
                  "free Gurathen. The next morning he is executed in the park. You can see the pain in your friend's eyes as \n"
                  "he struggles for breath as he is hanged")
            failure_condition()

    @staticmethod
    def describe_inside_jailhouse():
        print("The inside of the jailhouse has grime and dust caching nearly every surface, making it hard to breath. The \n"
              "odor of unwashed bodies wafts into your nostrils, though there are only two people in here at the moment \n"
              "There are two hallways, each with ten cells (five on each side). From the rust on most of the locks, it \n"
              "looks like they rarely get visitors. The laughter of the guardsmen drifts in from the cracked door of the \n"
              "guard room. The guard change will be here soon and take up their attention for a while longer, but it's\n"
              "good to get a move on now. You pass the unused cells, each with a wooden bucket and a bed frame, though no \n"
              "mattresses adorn them. Eventualley you reach the cell Gurathen is being kept in; No less dirty, but at \n"
              "least the locks were kept less rusty due to more frequent use. Less carries a lot of weight in that sentence. \n")


class SmugglersHideout:
    @staticmethod
    def describe_main_room():
        print(
            "Your elbows are resting on the grimy surface of an old table, who\'s last date of cleaning could accurately \n"
            "be estimated in \"years\" rather than \"days\" ago. A mug of sharp ale sits in your hand of which you have \n"
            "had to refill at least twice, though to be honest, you can't remember exactly how many times ago. This is \n"
            "the hideout that you and your fellow smugglers call home, base of operations, hideout, and sometimes viler \n"
            "things if they've had a few drinks. They tended to be vile people after a few drinks. But you're drinking \n"
            "despite that, because today one of your buddies was caught. They were only smuggling money and magic, not \n"
            "anything the Tyrant would be interested in, it seemed unfair he would be hanged for just moving bags around. \n"
            "Yeah, unfair. This life is unfair. 'I will get him out of the noose', you think to your. 'snot right, \n"
            "a him hanging for an offence like that.\n\n"
            "A map of the city decorates the far wall, with a few markings on it. There is a group of smugglers bringing \n"
            "in bags full of unknown goods, chatting while they do so. They shuffle through the front of an abandoned \n"
            "bar, into the back where the goods are kept")
        match (decide(["inspect map", 'enter back', 'leave hideout'], True)):
            case 0:
                SmugglersHideout.inspect_map()
            case 1:
                SmugglersHideout.describe_back_hall()
            case 2:
                Graysoul.describe_outside_safehouse()

    @staticmethod
    def inspect_map():
        if discoveredOptions['guard change']:
            print("You already did this!")
            SmugglersHideout.describe_main_room()
        else:
            print(
                "The map is worn on the edges, and has quite a few stains, but is still readable. It shows the city in excruciatingly \n"
                "little detail, but on it are marked a plethora of red loops, and the annotations on the map describe them \n"
                "as routs for police and guards. One in particular catches your eye: a guard change over the jailhouse where Gurathen\n"
                "is being kept. The guards will change at 11pm, maybe then would be a good time to sneak in.")
            discoveredOptions['guard change'] = True
            SmugglersHideout.describe_main_room()

    @staticmethod
    def describe_back_hall():
        print(
            "You walk into the hallway that leads to the three main back rooms. The hall is yellowed and moldy, and a \n"
            "distinct smell permeates the entire premise, of alcohol, must, and smoke. The right hall leads to the storage \n"
            "area, where they store the goods they shuttle through the river Habat, and into the cities further south. \n"
            "The left hall leads to the weapons and gear storage, where they store the tools of their trade. Most are rusted\n"
            "as they rarely have to use any of them. The final room is the bunks, where you sleep.")
        decision = decide(["go to weapons", 'go to storage', 'go to bunks', 'go to main room'], True)
        match decision:
            case 0:
                SmugglersHideout.describe_weapons_room()
            case 1:
                SmugglersHideout.describe_storage_room()
            case 2:
                SmugglersHideout.describe_bunk_room()
            case 3:
                SmugglersHideout.describe_main_room()

    @staticmethod
    def describe_weapons_room():
        print(
            "A small storage closet here is crammed full of useful tools, but on the top shelf of the closet, a few weapons gleam.\n"
            "Another shelf, lower down, holds a few tools, a couple of which you know how to use")
        decision = decide(['inspect weapons', 'inspect tools', 'go back'], False)
        match decision:
            case 0:
                SmugglersHideout.inspect_weapons_in_storage()
            case 1:
                SmugglersHideout.inspect_tools_in_storage()
            case 2:
                SmugglersHideout.describe_back_hall()

    @staticmethod
    def inspect_weapons_in_storage():
        print(f"\nDEBUG: {discoveredOptions}\n")
        if discoveredOptions['club']:
            print(
                "While the club fits nicely in your hand, you could switch it out with the dagger if you wanted, or drop the \n"
                "club back here. After all, you\'ve never needed a weapon before.")
            decision = decide(['switch with dagger', 'leave club', 'go back'], False)
            match decision:
                case 0:
                    print(
                        "The dagger falls into your hand heavily, though you are reluctant to leave the club here, you \n"
                        "know you'll need at least one hand.")
                    discoveredOptions['dagger'] = True
                    discoveredOptions['club'] = False
                    SmugglersHideout.inspect_weapons_in_storage()
                case 1:
                    print(
                        "You've never needed a weapon before, so why should you need one now? You leave the club on the shelf.")
                    discoveredOptions['club'] = False
                    SmugglersHideout.inspect_weapons_in_storage()
                case 2:
                    SmugglersHideout.describe_weapons_room()
        elif discoveredOptions['dagger']:
            print(
                "While you already have a dagger, you know how to use the club better, and it can prove more useful in \n"
                "covert operations. Maybe it would be a better pick for you. You could switch the dagger out for the club,\n"
                "or you could leave the club back here. After all, you\'ve never needed a weapon before.")
            decision = decide(['switch with club', 'leave dagger', 'go back'], False)
            match decision:
                case 0:
                    print(
                        "The club falls into your hand heavily, though you are reluctant to leave the dagger here, you \n"
                        "know you'll need at least one hand.")
                    discoveredOptions['dagger'] = False
                    discoveredOptions['club'] = True
                    SmugglersHideout.inspect_weapons_in_storage()
                case 1:
                    print(
                        "You've never needed a weapon before, so why should you need one now? You leave the dagger on the shelf.")
                    discoveredOptions['dagger'] = False
                    SmugglersHideout.inspect_weapons_in_storage()
                case 2:
                    SmugglersHideout.describe_weapons_room()
        else:
            print(
                "A dozen or so weapons hang on a wooden rack that seems to have been jerry-built from scraps of rotting wood. \n"
                "Most you don't know how to use, and they are all in disrepair, with spots of rust on some, and on others it \n"
                "is difficult to tell the rust from the weapon itself. While you don't know how to use a bladed weapon, one \n"
                "implement in particular catches your eye. A small club in the bottom right of the could offer you something \n"
                "in a fight. There's also a dagger hanging off of a particularly precarious hook that has less rust than the \n"
                "rest, and has an edge.")  # TODO: add option to choose if have both.
            decision = decide(['take club', 'take dagger', 'go back'], False)
            match decision:
                case 0:
                    print(
                        "The club falls heavily into your hand, and offers a reassuring presence, though you hope you won't need it.")
                    discoveredOptions['club'] = True
                    SmugglersHideout.inspect_weapons_in_storage()
                case 1:
                    print(
                        "The dagger feels heavy in your hand, though you aren't sure, if push came to shove, you would be able to use it.")
                    discoveredOptions['dagger'] = True
                    SmugglersHideout.inspect_weapons_in_storage()
                case 2:
                    SmugglersHideout.describe_weapons_room()

    @staticmethod
    def inspect_tools_in_storage():
        print(f"\nDEBUG: {discoveredOptions}\n")
        if discoveredOptions['lock picks']:
            print(
                'While the lock picks will work  on a simple lock, you could also take the key imprint device, or drop the \n'
                "lock picks here. If you don\'t need them, they will just get in the way.")
            decision = decide(['take key imprint device', 'leave lock picks', 'go back'], False)
            match decision:
                case 0:
                    if discoveredOptions['key wax']:
                        print("You already have this")
                        SmugglersHideout.inspect_tools_in_storage()
                    else:
                        print(
                            "You slip the key wax into your pocket, it's better to be safe than sorry.")
                        discoveredOptions['key wax'] = True
                        SmugglersHideout.inspect_tools_in_storage()
                case 1:
                    print("You may as well drop it off here if you don't need it so it doesn't get in the way")
                    discoveredOptions['lock picks'] = False
                    SmugglersHideout.inspect_tools_in_storage()
                case 2:
                    SmugglersHideout.describe_weapons_room()
        elif discoveredOptions['key wax']:
            print("The key wax is pretty slow, it might be useful to take the lock picks. Or you could just drop it off here \n"
                "so as not to get in the way")
            decision = decide(['take lock picks', 'leave key wax', 'go back'], False)
            match decision:
                case 0:
                    if discoveredOptions['lock picks']:
                        print("You already have this")
                        SmugglersHideout.inspect_tools_in_storage()
                    else:
                        print("You slip the lock picks into your pocket, it's better to be safe than sorry.")
                        discoveredOptions['lock picks'] = True
                        SmugglersHideout.inspect_tools_in_storage()
                case 1:
                    print("You may as well drop it off here if you don't need it so it doesn't get in the way")
                    discoveredOptions['key wax'] = False
                    SmugglersHideout.inspect_tools_in_storage()
                case 2:
                    SmugglersHideout.describe_weapons_room()
        else:
            print(
                "A couple tools sit on the shelf, though you haven't bothered to learn most of them. \n"
                "The two you are confident you can use are the lock picking set and the key imprint device. \n"
                "The lock picking set is quicker, but the key imprint device (key wax) will work on any key. \n"
                "Both are small enough to fit in your pocket")
            decision = decide(['take lock picking set', 'take key imprint device', 'go back'], False)
            match decision:
                case 0:
                    print(
                        "You take the lock picking set. Are you planning anything uh... Illegal?")
                    discoveredOptions['lock picks'] = True
                    SmugglersHideout.inspect_tools_in_storage()
                case 1:
                    print("You take the key imprint device, which feels oddly squishy.")
                    discoveredOptions['key wax'] = True
                    SmugglersHideout.inspect_tools_in_storage()
                case 2:
                    SmugglersHideout.describe_weapons_room()

    @staticmethod
    def describe_storage_room():
        print("A few sacks have been dropped into the relatively large room, clumped together as if they are huddling from \n"
              "a storm. The room is mostly caked in dust, with the path between the entrance and corner more recently kicked up.\n"
              "Out of the corner of your eye, you see a rat scuttle across the room and through a hole in the corner. It is \n"
              "more silent here than most other places in the city, and one can, on the quieter nights, if they close their eyes,\n"
              " almost imagine themselves in a forest. Spider webs cross ceiling. They had allotted the larger room for goods \n"
              "in hope for more business that never came. There's nothing in here for you.")
        SmugglersHideout.describe_back_hall()

    @staticmethod
    def describe_bunk_room():
        if discoveredOptions['lamp'] and discoveredOptions['cards']:
            print(
                "Thought the room is quite dark, you can still make out the outline of three sets of bunks lining the room.\n"
                "In the middle of the room, on a short table, where your box of cards used to be. A dark oil lamp sits on\n"
                "the table; it's not good to waste oil with the prices they're charging these days. Other than that,\n"
                "the room is pretty barren\n")
            decision = decide(['go to bed', 'leave cards', 'turn on lamp' 'go back'], False)
            match decision:
                case 0:
                    print(
                        "You reach your bunk, but aren't tired. You try to get to sleep anyway; the meager light coming under\n"
                        "the door keeps you up. You are unable to go to sleep, despite your best efforts. It's been nearly an hour.")
                    SmugglersHideout.describe_bunk_room()
                case 1:
                    print(
                        "You slip the cards back on the table; you don't want the others to find out")
                    discoveredOptions['cards'] = False
                    SmugglersHideout.describe_bunk_room()
                case 2:
                    print("The oil lamp flickers to life, but you feel weird leaving it on and wasting oil when you aren't using it\n")
                    discoveredOptions['lamp'] = False
                    SmugglersHideout.describe_bunk_room()
                case 3:
                    SmugglersHideout.describe_back_hall()
        elif discoveredOptions['lamp'] and not discoveredOptions['cards']:
            print(
                "Thought the room is quite dark, you can still make out the outline of three sets of bunks lining the room."
                "In the middle of the room, on a short table, is a small box, which as your eyes adjust to the darkness, resolves \n"
                "into the deck of cards which you play most nights. A dark oil lamp sits on the table; it's not good to \n"
                "waste oil with the prices they're charging these days.  Other than that, the room is pretty barren\n")
            decision = decide(['go to bed', 'take cards', 'turn off lamp' 'go back'], False)
            match decision:
                case 0:
                    print(
                        "You reach your bunk, but aren't tired. You try to get to sleep anyway; the meager light coming under\n"
                        "the door keeps you up. You are unable to go to sleep, despite your best efforts. It's been nearly an hour.")
                    SmugglersHideout.describe_bunk_room()
                case 1:
                    if discoveredOptions['cards']:
                        print(
                            "You've already taken the cards; they are no longer on the table. You only *have* one pair of cards.")
                    else:
                        print(
                            "You slip the cards into your pocket; it's always good to have a deck of cards. Just hope the others \n"
                            "don't find out")
                        discoveredOptions['cards'] = True
                    SmugglersHideout.describe_bunk_room()
                case 2:
                    print("The oil lamp flickers to life, but you feel weird leaving it on and wasting oil when you aren't using it\n")
                    discoveredOptions['lamp'] = False
                    SmugglersHideout.describe_bunk_room()
                case 3:
                    SmugglersHideout.describe_back_hall()
        elif discoveredOptions['cards'] and not discoveredOptions['lamp']:
            print("Three sets of bunk beds line the room, upon which yellowed mattresses are lain. Ratty quilts cover these, \n"
                  "but only two of them have pillows. In the middle of the room there is a short table where a deck of cards used \n"
                  "to be which you play most nights. An oil lamp flickers on the table, giving off light, but you should turn it off; \n"
                  "it's not a good idea to waste oil with the prices they're charging these days. You will have to figure out who \n"
                  "left it on once you free Gurathen")
            decision = decide(['go to bed', 'leave cards', 'turn off lamp' 'go back'], False)
            match decision:
                case 0:
                    print(
                        "You reach your bunk, but aren't tired. You try to get to sleep anyway; the meager light coming under\n"
                        "the door keeps you up. You are unable to go to sleep, despite your best efforts. It's been nearly an hour.")
                    SmugglersHideout.describe_bunk_room()
                case 1:
                    if discoveredOptions['cards']:
                        print(
                            "You've already taken the cards; they are no longer on the table. You only *have* one pair of cards.")
                    else:
                        print(
                            "You slip the cards back on the table; you don't want the others to find out")
                        discoveredOptions['cards'] = False
                    SmugglersHideout.describe_bunk_room()
                case 2:
                    print(
                        "You turn off the old lamp, and the room is now a lot darker, but at least you aren't wasting oil.\n"
                        "You can still see a little by the light coming from the hall")
                    discoveredOptions['lamp'] = True
                    SmugglersHideout.describe_bunk_room()
                case 3:
                    SmugglersHideout.describe_back_hall()
        elif not discoveredOptions['cards'] and not discoveredOptions['lamp']:
            print(
                "Three sets of bunk beds line the room, upon which yellowed mattresses are lain. Ratty quilts cover these, \n"
                "but only two of them have pillows. In the middle of the room, on a short table, an old deck of cards sits, \n"
                "which they play most nights. An oil lamp flickers on the table, giving off light, but you should turn it off; \n"
                "it's not a good idea to waste oil with the prices they're charging these days. You will have to figure out who \n"
                "left it on once you free Gurathen")
            decision = decide(['go to bed', 'take cards', 'turn off lamp' 'go back'],False)
            match decision:
                case 0:
                    print("You reach your bunk, but aren't tired. You try to get to sleep anyway; the meager light coming under\n"
                          "the door keeps you up. You are unable to go to sleep, despite your best efforts. It's been nearly an hour.")
                    SmugglersHideout.describe_bunk_room()
                case 1:
                    if discoveredOptions['cards']:
                        print("You've already taken the cards; they are no longer on the table. You only *have* one pair of cards.")
                    else:
                        print("You slip the cards into your pocket; it's always good to have a deck of cards. Just hope the others \n"
                          "don't find out")
                        discoveredOptions['cards'] = True
                    SmugglersHideout.describe_bunk_room()
                case 2:
                    print("You turn off the old lamp, and the room is now a lot darker, but at least you aren't wasting oil.\n"
                          "You can still see a little by the light coming from the hall")
                    discoveredOptions['lamp'] = True
                    SmugglersHideout.describe_bunk_room()
                case 3:
                    SmugglersHideout.describe_back_hall()
if __name__ == "__main__":
    SmugglersHideout.describe_main_room()
