import data


class Works:
    '''
    {
        'works': list[data.Work],                  #文件的名称，一个文件代表一个员工
        'history': list[data.History],            #一个文件里可能有很多个Sheet
        'success': list[str],            #一个文件里可能有很多个Sheet
        'failure': list[str],            #一个文件里可能有很多个Sheet
        'repeat': list[str],            #一个文件里可能有很多个Sheet
        
    }
    '''

    def __init__(self) -> None:
        self.works: list[data.Work] = []
