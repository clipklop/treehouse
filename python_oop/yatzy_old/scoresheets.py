#


from hands import YatzyHand
from dice import D6


class YatzyScoresheet:
    def score_ones(self, hand):
        return sum(hand.ones)

    def score_twos(self, hand):
        return sum(hand.twos)

    def _score_set(self, hand, set_size):
        scores = [0]
        for worth, count in hand._sets.items():
            if count == set_size:
                scores.append(worth * set_size)
        return max(scores)

    def score_one_pair(self, hand):
        return self._score_set(hand, 2)


hand = YatzyHand()
three = D6(value=3)
four = D6(value=4)
one = D6(value=1)
hand[:] = [one, three, three, four, four]

print(YatzyScoresheet().score_one_pair(hand))