import data


class Work:
    '''
    {
        'name': str,                  #文件的名称，一个文件代表一个员工
        'data': list[Row],            #一个文件里可能有很多个Sheet
    }
    '''

    def __init__(self) -> None:
        self.name: str = ''
        self.data: list[data.Sheet] = []
        self.history: data.History = data.History()
