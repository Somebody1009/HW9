from rational import Rational

class RationalList:
    def __init__(self, items=None):
        if items is None:
            self.items = []
        else:
            self.items = [self._check_item(item) for item in items]

    def _check_item(self, item):
        if isinstance(item, Rational):
            return item
        elif isinstance(item, int):
            return Rational(item)
        else:
            raise TypeError("Element must be Rational or int.")

    def __getitem__(self, index):
        return self.items[index]

    def __setitem__(self, index, value):
        self.items[index] = self._check_item(value)

    def __len__(self):
        return len(self.items)

    def __add__(self, other):
        if isinstance(other, RationalList):
            return RationalList(self.items + other.items)
        else:
            return RationalList(self.items + [self._check_item(other)])

    def __iadd__(self, other):
        if isinstance(other, RationalList):
            self.items += other.items
        else:
            self.items.append(self._check_item(other))
        return self

    def sum(self):
        result = Rational(0)
        for item in self.items:
            result += item
        return result
