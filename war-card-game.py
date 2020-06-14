from random import shuffle
import time
SUITE = 'H D S C'.split()
RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()


class Deck:
    def __init__(self):
        self.deck = []
        for x in SUITE:
            for y in RANKS:
                card = (x, y)
                self.deck.append(card)

    def split(self):
        shuffle(self.deck)

    def oneHalf(self):
        return self.deck[:len(self.deck)//2]

    def twoHalf(self):
        return self.deck[len(self.deck)//2:]


class Hand:
    def __init__(self, cards):
        self.cards = cards

    def addCard(self, card):
        self.cards.extend(card)

    def removeCard(self):
        return self.cards.pop(0)

    def empty(self):
        return len(self.cards) == 0

    def amount(self):
        return len(self.cards)

    def shuffleHand(self):
        shuffle(self.cards)


class Game:
    def __init__(self):
        self.deck = Deck()
        self.deck.split()
        self.player1 = Hand(self.deck.oneHalf())
        self.player2 = Hand(self.deck.twoHalf())
        self.play()

    def play(self):
        print("\nWelcome to War!\n")
        i = input('Press any key to begin. Q to quit.')
        while True:
            if i is not None and i.lower() != 'q':
                self.deal()
                self.player1.shuffleHand()
                self.player2.shuffleHand()
                print()
                if self.player1.amount() <= 1:
                    print('You LOST.')
                    return
                if self.player2.amount() <= 1:
                    print('You WON!')
                    return
                i = input('Press any key. Q to quit.')
            else:
                break

    def deal(self):
        c1 = self.player1.removeCard()
        c2 = self.player2.removeCard()
        v1 = self.val(c1[1])
        v2 = self.val(c2[1])
        res = ""
        if v1 == v2:
            print(
                "Your card:       {}    \nComputer's Card: {}   ".format(c1, c2))
            print('WAR!\n')
            time.sleep(3)
            self.war(c1, c2)
        else:
            if v1 > v2:
                self.player1.addCard([c1, c2])
                res = 'You get the cards!'
            elif v2 > v1:
                self.player2.addCard([c1, c2])
                res = 'Computer gets the cards.'
            print(
                "Your card:       {}   You have {} cards left! \nComputer's Card: {}   Computer has {} cards left!".format(c1, self.player1.amount(),  c2,  self.player2.amount()))
            print(res)

    def war(self, card1, card2):
        p1_cards = []
        p2_cards = []
        res = ""
        for i in range(3):
            p1_cards.append(self.player1.removeCard())
            p2_cards.append(self.player2.removeCard())
        c1 = self.player1.removeCard()
        c2 = self.player2.removeCard()
        v1 = self.val(c1[1])
        v2 = self.val(c2[1])
        if v1 > v2:
            self.player1.addCard(p1_cards)
            self.player1.addCard(p2_cards)
            self.player1.addCard([c1, c2, card1, card2])
            res = 'You won the WAR! You get all the cards!'
        elif v2 > v1:
            self.player2.addCard(p1_cards)
            self.player2.addCard(p2_cards)
            self.player2.addCard([c1, c2, card1, card2])
            res = 'You lost the WAR :(. Computer gets all the cards.'
        else:
            self.player1.addCard(p1_cards)
            self.player1.addCard([c1, card1])
            self.player2.addCard(p2_cards)
            self.player2.addCard([c2, card2])
            res = "It was a tie! All cards returned to its original owners."
        print(
            "Your card:       {}   You have {} cards left! \nComputer's Card: {}   Computer has {} cards left!".format(c1, self.player1.amount(),  c2,  self.player2.amount()))
        print(res)

    def val(self, val):
        res = 0
        if not any(map(str.isdigit, val)):
            if val == 'J':
                res = 11
            elif val == 'Q':
                res = 12
            elif val == 'K':
                res = 13
            elif val == 'A':
                res = 14
        else:
            res = int(val)
        return res


game = Game()
