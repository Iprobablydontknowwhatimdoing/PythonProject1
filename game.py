from typing import List

def show_options(option_list: List[str]):
    for string in option_list:
        print(f" - {string}")
def decide(decisions: List[str], show_by_default: bool):
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

class SmugglersHideout:
    def __init__(self):
        self.self = self
    def describe_main_room(self):
        print("Your elbows are resting on the grimy surface of an old table, who\'s last date of cleaning could accurately \n"
              "be estimated in \"years\" rather than \"days\" ago. A mug of sharp ale sits in your hand of which you have \n"
              "had to refill at least twice, though to be honest, you can't remember exactly how many times ago. This is \n"
              "the hideout that you and your fellow smugglers call home, base of operations, hideout, and sometimes viler \n"
              "things if they've had a few drinks. They tended to be vile people after a few drinks. But you're drinking \n"
              "despite that, because today one of your buddies was caught. They were only smuggling money and magic, not \n"
              "anything the Tyrant would be interested in, it seemed unfair he would be hanged for just moving bags around. \n"
              "Yeah, unfair. This life is unfair. 'I will get him out of the noose', you think to yourself. 'snot right, \n"
              "a man hanging for an offence like that.\n\n"
              "A map of the city decorates the far wall, with a few markings on it. There is a group of smugglers bringing \n"
              "in bags full of unknown goods, chatting while they do so. They shuffle through the front of an abandoned \n"
              "bar, into the back where the goods are kept")
        match (decide(["inspect map", 'approach smugglers', 'enter back','leave hideout'], True)):
            case 0:
                SmugglersHideout.inspect_map()
            case 1:
                SmugglersHideout.talk_to_smugglers()
            case 2:
                SmugglersHideout.describe_back()
            case 3:
                Graysoul.describe_outside_safehouse()
    def inspect_map(self):
        print("The map is worn on the edges, and has quite a few stains, but is still readable. It shows the city in excruciatingly \n"
              "little detail, but on it are marked a plethora of red loops, and the annotations on the map describe them \n"
              "as routs for police and guards. The three routs are as follows: one rout around ")
class Graysouls:
    # def describe_outside_safehouse(self):