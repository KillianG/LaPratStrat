import enum


class Position(enum.IntEnum):
    BT = 1
    SB = 2
    BB = 3
    UTG = 4
    UTG1 = 5
    MP = 6
    MP1 = 7
    HJ = 8
    CT = 9


class Category(enum.IntEnum):
    Cat1 = 1
    Cat2 = 2
    Cat3 = 3
    Cat4 = 4
    Cat5 = 5
    Cat6 = 6
    Cat7 = 7
    Cat8 = 8
    Cat9 = 9


def init_position(phrase):
    player_position = None
    position_names = [p.name for p in Position]
    while player_position not in position_names:
        player_position = input(f"{phrase}({', '.join(position_names)}): ").upper()
    return Position[player_position]


def init_category(phrase):
    hand = input(phrase).upper()
    categories = (
        ("AA", "KK"),
        ("QQ", "AKS", "AKO", "JJ"),
        ("AQS", "AQO", "TT", "99"),
        ("AJS", "KQS", "88", "77"),
        ("AJO", "ATS", "ATO", "KQO", "KJS", "66", "55"),
        ("A9S", "A8S", "A7S", "A6S", "A5S", "A4S", "A3S", "A2S", "KJO", "KTS", "QJS", "JTS", "44", "33", "22"),
        ("A9", "A8", "A7", "A6", "A5", "A4", "A3", "A2", "KTO", "QJO", "QTO", "JTO", "T9S", "98S", "87S", "76S",
         "65S", "54S"),
        ("K9S", "K9O", "K8S", "K8O", "Q9S", "Q8S", "J9S", "T8S", "T9O", "97S", "98O", "86S", "87O", "75S",
         "76O", "64S"),
    )
    for i, category in enumerate(categories):
        if hand in category:
            return Category(i + 1)
    return Category.Cat9


def question(phrase):
    answer = input(phrase + "(Y/N): ").upper()
    return answer == "Y"


def preflop(pos, cat, blind, passed, limpers, relance):
    if passed:
        if pos == Position.SB or pos == Position.BT:
            if blind >= 10 and cat <= 7:
                print("PLAY")
            elif blind < 10 and cat <= 8:
                print("PLAY")
        if pos == Position.CT or pos == Position.HJ:
            if blind >= 10 and cat <= 6:
                print("PLAY")
            elif blind >= 5 and cat <= 7:
                print("PLAY")
            elif blind < 5 and cat <= 8:
                print("PLAY")
        if pos == Position.UTG:
            if blind >= 10 and cat <= 5:
                print("PLAY")
            elif blind >= 5 and cat <= 6:
                print("PLAY")
            elif blind < 5 and cat <= 7:
                print("PLAY")
    elif limpers:
        if blind >= 10 and cat <= 4:
            print("PLAY 1")
        elif blind >= 5 >= cat:
            print("PLAY 2 ")
        elif blind < 5 and cat <= 6:
            print("PLAY 3 ")
    elif relance:
        if blind >= 10 and cat <= 3:
            print("PLAY")
        elif blind >= 5 and cat <= 4:
            print("PLAY")
        elif blind < 5 and cat <= 5:
            print("PLAY")


if __name__ == "__main__":
    pos = init_position("Quelle position ?: ")
    cat = init_category("Quelle main ?: ")
    blinde = int(input("Combien de blinde ?: "))
    passed = question("Tout le monde s'est couché ?: ")
    limpers = question("Des gens ont limp ?: ")
    relance = question("Quelqu'un relance ?: ")
    preflop(pos, cat, blinde, passed, limpers, relance)
