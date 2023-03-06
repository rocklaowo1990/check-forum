class FileChildren:

    def __init__(self, path: str = '', children: list[str] = []) -> None:
        self.path: str = path,
        self.children: list[str] = children