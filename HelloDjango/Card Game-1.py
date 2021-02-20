import random

# масти
SPADE = 1
HEARTS = 2
CLOVER = 3
DIAMOND = 4
# наименование карты
# A,K,Q,J,T,E,N,NEIGH,EIGHT,SEVEN,SIX
# количество игроков

# количество карт на руках
player_deck = 6


class Card(object):
    suit = ["SPADE", "HEARTS", "CLOVER", "DIAMOND"]
    value = ["A", "K", "Q", "J", "10", "9", "8", "7", "6"]

    def __init__(self, suit, value):
        self.suit = suit
        suit = ["SPADE", "HEARTS", "CLOVER", "DIAMOND"]
        self.value = value
        value = ["A", "K", "Q", "J", "10", "9", "8", "7", "6"]

    def __str__(self):
        self.card = str(self.suit) + " " + str(self.value)

    # text = "%s's contains:\n" % self.name
    # for card in self.cards:
    # text += str(card) + " "
    # text += "\nHand value: " + str(self.get_value())
    # return text
    def name_to_value(self):
        self.name_to_value = {n: i for i, n in enumerate(self.value)}  # поиск индекса подостоинству

    def __repr__(self):
        return f"Player{self.card}"

    def __lt__(self, other):
        return self.suit + self.value > other

    def __eq__(self, other):
        return self.suit + self.value == other


class CardDeck(object):

    def __init__(self, cards=None):

        if cards is None:

            self._cards = self.get_full_deck()

        else:

            self._cards = cards

    def __str__(self):
        return 'Deck{}'.format(self.cards)     #self._cards = [Card(suit,value) for suit,value in product ['6','7','8','9','10','J','Q','K','T',['SPADE','HEARTS','CLOVER','DIAMOND']] #print(Card)

    def shuffle(self):                                                               #(self, gen: random.Random = None):
        random.shuffle(self.cards)                                                          #self.gen = gen or random.Random()  # случайное генерирование
                                                                                         #self._cards = list(self._cards)  # копируем колоду # self.gen.shuffle(self._cards) # мешаем карты #return

    def pick_first(self, suit, value, pick_first):
        self.pick_first = []
        for i in range(suit):
            for j in range(value):
                pick_first.append(self._cards(i, j))
        print(self.pick_first)

    def get_full_deck(self, suit, value):
        self.cards = [Card(i) for i in range(36)]   #self._get_full_deck = [] #for self._cards in range (0, 35)
        self.shuffle()

        self.full_deck = []
        for i in range(suit):
            for j in range(value):
                return CardDeck

    def player_deck(self, card_deck, Player):
        self.deck = list(card_deck)  # копируем колоду
        self.player = [Player(i, []).take_cards_from_deck(self.deck)   # создаем игроков и раздаем им по 6 карт
                         for i in range(Player)]

    def print_players(self):
        print(self.players)

    def get_first_player(self, trump, cards, value):#players
        self.trump = input()
        self.trump = self.CardDeck[0][1]  # козырь карта сверху

        if (cards[0][-1] not in CardDeck) or (cards[1][-1] not in CardDeck) or (trump not in CardDeck):
            print("Error")  # если масть 1й карты совпадает с мастью козыря
        elif cards[0][-1] == trump and cards[1][-1] != trump:
            print("First") # если масть 2й карты не совпадает с мастью козыря
        if value.index(CardDeck[0][:-1]) > value.index(CardDeck[1][:-1]):
            print("First")  # если индекс 1й карты больше


class Player(object):
    def __init__(self, index, player_deck):
        self.index = index
        self.player_deck = player_deck

    def __repr__(self):
        return f"Player{self.six_cards_for_hands()!r}"

    def six_cards_for_hands(self, CardDeck):
        self.player_deck = player_deck
        for self.Player in range(CardDeck):
            print(player_deck)

    def take_cards_from_deck(self, deck: list):  #взять не достоющее кол-во карт из колоды
        lack = max(0, player_deck - len(self.cards))
        n = min(len(deck), lack)  # колода уменьшится
        self.add_cards(deck[:n])
        del deck[:n]

        return self

    def sort_hand(self):
        self.cards.sort(key=lambda c: (self.name_to_value[c[0]], c[1]))   # сортировка по достоинству
        return self

    def take_card(self, card):
        self.cards.remove(card)

    def main():

        full_deck = CardDeck()

        num_players = int(input('Enter num players'))

        players = [get_player_deck(full_deck) for i in range(num_players)]

        print_players(player)

        trump = []

        first_player = get_first_player(players, trump)

    if __name__ == '__main__':
        main()

