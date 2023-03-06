import data


def find_history(history: list[data.History], work_name: str):
    _h: data.History = data.History()

    for h in history:
        if h.name == work_name:
            _h = h
            break
    return _h