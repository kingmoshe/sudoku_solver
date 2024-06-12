from typing import List


class BoardVal:
    def __init__(self, sizes_of_groups: List[int]):
        self.counter = {i: 0 for i in range(1, 10)}
        for g in sizes_of_groups:
            self.counter[g] += 1

    def __lt__(self, other):
        for i in range(1, 10):
            if self.counter[i] != other.counter[i]:
                return self.counter[i] > other.counter[i]
        return False

    def __repr__(self):
        return '(' + ', '.join(map(str, [value for key, value in self.counter.items()])) + ')'
