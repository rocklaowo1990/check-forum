import data


class Response:

    def __init__(self) -> None:
        self.resault: data.Resault = data.Resault()
        self.tables: list[data.Table] = []
