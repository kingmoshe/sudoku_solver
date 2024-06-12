class Position:
    def __init__(self, i: int, j: int):
        self.i = i
        self.j = j

    def __eq__(self, other) -> bool:
        if not isinstance(other, Position):
            print("problem")
            raise NotImplemented("in position", other)
        return self.i == other.i and self.j == other.j

    def __lt__(self, other):
        if self.i != other.i:
            return self.i < other.i
        return self.j < other.j

    def __repr__(self) -> str:
        return f'{self.i}-{self.j}'
