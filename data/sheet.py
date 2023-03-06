import data


class Sheet:
    '''
    {
        'name': str,                  #Sheet的名称
        'data': list[Row],            #表格里有很多行
    }
    '''

    def __init__(self) -> None:
        self.name: str = ''
        self.data: list[data.Row] = []
