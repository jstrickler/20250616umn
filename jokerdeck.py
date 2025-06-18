from card import Card
from carddeck import CardDeck

class JokerDeck(CardDeck):
    def _make_deck(self):
        super()._make_deck()
        for joker_number in 1, 2:
            joker = Card(f"JOKER{joker_number}", "**JOKER**")
            self._cards.append(joker)

j = JokerDeck()
j.shuffle()
print(j)
print(f"{j.cards = }")
