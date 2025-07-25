from typing import List, Optional


def show_options(option_list: List[str]):
    for string in option_list:
        print(f" - {string}")


def decide(decisions: List[str], show_by_default: Optional[bool]):
    if show_by_default:
        show_options(decisions)
    answer = input("What do you want to do? (you can always say 'hint') > ")
    if answer.lower().strip() == "hint":
        show_options(decisions)
        return decide(decisions, False)
    elif answer.lower().strip() in decisions:
        return decisions.index(answer.lower().strip())
    else:
        print('Sorry, I didn\'t catch that, please try again')
        return decide(decisions, False)


discoveredOptions: dict[str, bool] = {'guard change': False, 'club': False, 'dagger': False, 'lock picks': False,
                                      'key wax': False}


class Graysoul:
    @staticmethod
    def describe_outside_safehouse():
        print("You are going where noone has gone before. This path has not been implemented yet.")
        SmugglersHideout.describe_main_room()


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
        match (decide(["inspect map", 'approach smugglers', 'enter back', 'leave hideout'], True)):
            case 0:
                SmugglersHideout.inspect_map()
            case 1:
                SmugglersHideout.talk_to_smugglers()
            case 2:
                SmugglersHideout.describe_back_hall()
            case 3:
                Graysoul.describe_outside_safehouse()

    @staticmethod
    def talk_to_smugglers():
        print("You are going where noone has gone before. This path has not been implemented yet.")
        SmugglersHideout.describe_main_room()

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
            "The left hall leads to the weapons and gear storage, where they store the tools of there trade. Most are rusted\n"
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
                'While the club fits nicely in your hand, you could switch it out with the dagger if you wanted, or drop the \n'
                'club back here. After all, you\'ve never needed a weapon before.')
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
                'While you already have a dagger, you know how to use the club better, and it can prove more useful in \n'
                'covert operations. Maybe it would be a better pick for you. You could switch the dagger out for the club,\n'
                'or you could leave the club back here. After all, you\'ve never needed a weapon before.')
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
                "A dozen or so weapons hang on a wooden rack that seems to have been jerry rigged from scraps of rotting wood. \n"
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
                'lock picks here. If you don\'t need them, they will just get in the way.')
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
            print(
                "The key wax is pretty slow, it might be useful to take the lock picks. Or you could just drop it off here \n"
                "so as not to get in the way"
                )
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
        print("You are going where noone has gone before. This path has not been implemented yet.")
        SmugglersHideout.describe_back_hall()

    @staticmethod
    def describe_bunk_room():
        print("You are going where noone has gone before. This path has not been implemented yet.")
        SmugglersHideout.describe_back_hall()


if __name__ == "__main__":
    SmugglersHideout.describe_main_room()
