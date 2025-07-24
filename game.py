from pydoc import describe
from random import choice
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

discoveredOptions: dict[str, bool] = {'guard change': False}

class SmugglersHideout:
    def describe_main_room(returning: Optional[bool]):
        if not returning:
            print("Your elbows are resting on the grimy surface of an old table, who\'s last date of cleaning could accurately \n"
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
        match (decide(["inspect map", 'approach smugglers', 'enter back','leave hideout'], True)):
            case 0:
                SmugglersHideout.inspect_map()
            case 1:
                SmugglersHideout.talk_to_smugglers()
            case 2:
                SmugglersHideout.describe_back_hall(None)
            case 3:
                Graysoul.describe_outside_safehouse()
    def talk_to_smugglers():
        print("You are going where noone has gone before. This path has not been implimented yet.")
        SmugglersHideout.describe_main_room(True)
    def inspect_map():
        if discoveredOptions['guard change']:
            print("You already did this!")
        else:
            print("The map is worn on the edges, and has quite a few stains, but is still readable. It shows the city in excruciatingly \n"
            "little detail, but on it are marked a plethora of red loops, and the annotations on the map describe them \n"
            "as routs for police and guards. One in particular catches your eye: a guard change over the nick where Gurathen\n"
            "is being kept. The guards will change at 11pm, maybe then would be a good time to sneak in.")
            discoveredOptions['guard change'] = True
            SmugglersHideout.describe_main_room(True)
    def describe_back_hall(returning: Optional[bool]):
        if returning:
            print("You are now in the hall")
        else:
            print(
                "You walk into the hallway that leads to the three main back rooms. The hall is yellowed and moldy, and a \n"
                "distinct smell permeates the entire premise, of alcohol, must, and smoke. The right hall leads to the storage \n"
                "area, where they store the goods they shuttle through the river Habat, and into the cities further south. \n"
                "The left hall leads to the weapons and gear storage, where they store the tools of there trade. Most are rusted\n"
                "as they rarely have to use any of them. The final room is the bunks, where you sleep.")
        decision = decide(["go to weapons", 'go to storage', 'go to bunks', 'go to main room'],True)
        match decision:
            case 0:
                SmugglersHideout.describe_weapons_room()
            case 1:
                SmugglersHideout.describe_storage_room()
            case 2:
                SmugglersHideout.describe_bunk_room()
            case 3:
                SmugglersHideout.describe_main_room(True)
    def describe_weapons_room():
        print("A small storage closet here is crammed full of useful tools, but on the top shelf of the closet, a few weapons gleam.")
        decision = decide(['inspect weapons', 'inspect tools', 'return to hall'], False)
        match decision:
            case 0:
                SmugglersHideout.inspect_weapons_in_storage()
            case 1:
                SmugglersHideout.

    def inspect_weapons_in_storage():
        print("You are going where noone has gone before. This path has not been implimented yet.")
        SmugglersHideout.describe_back_hall(True)
    def describe_storage_room():
        print("You are going where noone has gone before. This path has not been implimented yet.")
        SmugglersHideout.describe_back_hall(True)
    def describe_bunk_room():
        print("You are going where noone has gone before. This path has not been implimented yet.")
        SmugglersHideout.describe_back_hall(True)
class Graysouls:
    def describe_outside_safehouse():
        print("You are going where noone has gone before. This path has not been implimented yet.")
        SmugglersHideout.describe_main_room(True)
if __name__ == "__main__":
    SmugglersHideout.describe_main_room(None)