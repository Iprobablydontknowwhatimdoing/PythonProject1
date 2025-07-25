from typing import List, Optional
# You walk where no man has walked before. This path hasn't been implemented yet

def show_options(option_list: List[str]):
    i = 0
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
    else:
        print('Sorry, I didn\'t catch that, please try again')
        return decide(decisions, False)


discoveredOptions: dict[str, bool] = {'guard change': False, 'club': False, 'dagger': False, 'lock picks': False,
                                      'key wax': False, 'cards': False}
def failure_condition():
    print("You walk where no man has walked before. This path hasn't been implemented yet")
    print("Regardless, you lost, so this is where your story ends. Better luck next time.")
    decision = decide(['retry','quit'],True)
    match decision:
        case 0:
            discoveredOptions['guard change'] = False
            discoveredOptions['club'] = False
            discoveredOptions['dagger'] = False
            discoveredOptions['lock picks'] = False
            discoveredOptions['key wax'] = False
            discoveredOptions['cards'] = False
            print("\nThis is your second life! don't waste it.\n\n")
            SmugglersHideout.describe_main_room()
        case 1:
            print("\nO.K. Goodbye. Hope you had fun!")
def victory_condition():
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
            print("\nHave fun on your second run!\n\n")
            SmugglersHideout.describe_main_room()
        case 1:
            print("Hope you had fun, and congratulations again!")
class Graysoul:
    @staticmethod
    def describe_outside_safehouse():
        print("You find yourself on an old grimy ally, which you follow to the main road leading into the city. You know that\n"
              "if you continue along this path you'll eventually get to the nick where Gurathen is being held. Are you ready to\n"
              "try to get him out?")
        if discoveredOptions['guard change']:
            decision = decide(['follow path', 'wait until shift change','go back'],False)
            match decision:
                case 0:
                    print("You continue along the path, paved with cobblestones. You can feel the beating of your heart as \n"
                          "people pass by you, but noone seems to think anything is out of the ordinary. It's been a while \n"
                          "since you walked these streets, and the cobblestones feel rough and hard against your worn-down shoes\n"
                          "compared to the dirt you normally walk on. You reach the bridge, and as you walk over it the water rushes \n"
                          "beneath you, nearly but not quite covering the clattering of the planks of wood that make up the \n"
                          "bridge. The spray brings welcome releaf from both the stuffy summer night and the rancid oder that \n"
                          "seems to fill nearly all cities.")
                    Graysoul.describe_nick(False)
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
                            Graysoul.describe_nick(True)
                        case 1:
                            print("You decide to sit and watch the river. The bubbling of the river brings back memories of \n"
                                  "playing on the farm where you grew up. As you swing your legs over the edge to hopefully catch \n"
                                  "some cool spray, you think of how you spent your life and of your childhood. You long to \n"
                                  "be a kid again, or at least to have a choice in what you are. it isn't long before the guard \n"
                                  "is about to change, and you get up from the bridge as guards shuffle with their lantern held \n"
                                  "out to ward against the dark, and follow them.")
                            Graysoul.describe_nick(True)
                        case 2:
                            print("You walk where no man has walked before. This path hasn't been implemented yet")
                            print("It's time for you to make your friend escape.")
                            Graysoul.describe_nick(True)
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
                    Graysoul.describe_nick(False)
                case 1:
                    print("You return to the smugglers' den.")
                    SmugglersHideout.describe_main_room()

    @staticmethod
    def describe_nick(waited_shift: bool):
        print("The nick is surprisingly small; it doesn't even have a second floor. It doesn't have to, you suppose, \n"
              "when execution is the punishment for every, even minor, infraction. It also makes your job harder.")
        if waited_shift:
            print("As you approach the guardhouse,")



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
            case 2:
                SmugglersHideout.describe_back_hall()
            case 3:
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
                "as routs for police and guards. One in particular catches your eye: a guard change over the nick where Gurathen\n"
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
              "a storm. The room is mostly cached in dust, with the path between the entrance and corner more recently kicked up.\n"
              "Out of the corner of your eye, you see a rat scuttle across the room and through a hole in the corner. It is \n"
              "more silent here than most other places in the city, and one can, on the quieter nights, if they close their eyes,\n"
              " almost imagine themselves in a forest. Spider webs cross ceiling. They had allotted the larger room for goods \n"
              "in hope for more business that never came. There's nothing in here for you.")
        SmugglersHideout.describe_back_hall()

    @staticmethod
    def describe_bunk_room():
        print("Three sets of bunk beds line the room, upon which yellowed mattresses are lain. Ratty quilts cover these, \n"
              "but only two of them have pillows. In the middle of the room, on a short table, an old deck of cards sits, \n"
              "which they play most nights. An oil lamp flickers on the table, but you quickly put it out; It's not good to \n"
              "waste oil with the prices they're charging these days. You will have to figure out who left it on once you free \n"
              "Gurathen")
        decision = decide(['go to bed', 'take cards', 'go back'],False)
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
                SmugglersHideout.describe_back_hall()
if __name__ == "__main__":
    SmugglersHideout.describe_main_room()
