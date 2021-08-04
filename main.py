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

def initPosition():
    position = input("What place ? (BT, SB, BB, UTG, UTG+1, MP, MP+1, HJ, CT): ")
    if position == "BT": return Position.BT
    if position == "SB": return Position.SB
    if position == "BB": return Position.BB
    if position == "UTG": return Position.UTG
    if position == "UTH+1": return Position.UTG1
    if position == "MP": return Position.MP
    if position == "MP+1": return Position.MP
    if position == "HJ": return Position.HJ
    if position == "CT": return Position.CT


def initCategory():
    hand = input("What hand: ").upper()
    Cat1_Hand = ["AA", "KK"]
    Cat2_Hand = ["QQ", "AKS", "AKO", "JJ"]
    Cat3_Hand = ["AQS", "AQO", "TT", "99"]
    Cat4_Hand = ["AJS", "KQS", "88", "77"]
    Cat5_Hand = ["AJO", "ATS", "ATO", "KQO", "KJS", "66", "55"]
    Cat6_Hand = ["A9S", "A8S", "A7S", "A6S", "A5S", "A4S", "A3S", "A2S", "KJO", "KTS", "QJS", "JTS", "44", "33", "22"]
    Cat7_Hand = ["A9", "A8", "A7", "A6", "A5", "A4", "A3", "A2", "KTO", "QJO", "QTO", "JTO", "T9S", "98S", "87S", "76S",
                 "65S", "54S"]
    Cat8_Hand = ["K9S", "K9O", "K8S", "K8O", "Q9S", "Q8S", "J9S", "T8S", "T9O", "97S", "98O", "86S", "87O", "75S",
                 "76O", "64S"]
    if hand in Cat1_Hand: return Category.Cat1
    if hand in Cat2_Hand: return Category.Cat2
    if hand in Cat3_Hand: return Category.Cat3
    if hand in Cat4_Hand: return Category.Cat4
    if hand in Cat5_Hand: return Category.Cat5
    if hand in Cat6_Hand: return Category.Cat6
    if hand in Cat7_Hand: return Category.Cat7
    if hand in Cat8_Hand: return Category.Cat8
    return Category.Cat9


def question(phrase):
    res = input(phrase + "(Y/N)").upper()
    if res == "Y": return True
    return False


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
        elif blind >= 5 and cat <= 5:
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
    pos = initPosition()
    cat = initCategory()
    blinde = int(input("Combien de blinde: "))
    passed = question("Tout le monde s'est couché ? ")
    limpers = question("Des gens ont limp ? ")
    relance = question("Quelqu'un relance ? ")
    preflop(pos, cat, blinde, passed, limpers, relance)
