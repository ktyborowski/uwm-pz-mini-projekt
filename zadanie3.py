class Vector2D:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def _add(self, value):
        if isinstance(value, Vector2D):
            return Vector2D(self.x + value.x, self.y + value.y)
        elif isinstance(value, tuple):
            if len(value) != 2:
                raise ValueError(
                    f"Incorrect tuple length. Expected 2. Got {len(value)}."
                )
            return Vector2D(self.x + value[0], self.y + value[1])
        else:
            raise TypeError(
                f"Can only add Vector2D or tuple (not '{type(value)}') to Vector2D"
            )

    def __add__(self, value):
        return self._add(value)

    def __radd__(self, value):
        return self._add(value)

    def __str__(self):
        return f"({self.x}, {self.y})"


if __name__ == "__main__":
    vec = Vector2D(2, 1)

    vec1 = Vector2D(-2, 2)

    vec2 = (5, 3)

    print(vec + vec1)
    print(vec1 + vec)

    print(vec1 + vec2)

    result = vec1 + vec2

    print(result + vec2)
