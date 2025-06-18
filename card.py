class Card:  # inherit from 'object'
    def __init__(self, rank, suit):
        self._rank = rank
        self._suit = suit

    @property
    def rank(self):  # getter property
        return self._rank
    #  rank = property(rank)

    @property
    def suit(self):
        return self._suit
    
    @suit.setter
    def suit(self, value):
        if isinstance(value, str):
            self._suit = value
        else:
            raise TypeError("Suit must be a string")

    # human (programmer) friendly
    def __str__(self):  # str(...)
        return f"{self.rank}-{self.suit}"

    # how to recreate the object
    def __repr__(self):
        return f"Card('{self.rank}', '{self.suit}')"

c1 = Card('A', 'Spades')
print(c1)
print(f"{c1 = }")  # uses repr()
c2 = Card('8', 'Diamonds')
print(f"{c1.rank = }")
print(f"{c1.suit = }")
c1.suit = "Hearts"
print(c2)
