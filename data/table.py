class Td:

    def __init__(self) -> None:
        self.data: list[str] = []
        pass


class Table:

    def __init__(self) -> None:
        self.head: Td = Td()
        self.body: list[Td] = []
        pass