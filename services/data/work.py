import services.data as data


class Works:
    '''
    - 包含很多个 Work 对象
    '''

    def __init__(self) -> None:
        self.works: list[Work] = []  #包含很多个 Work 对象


class Work:
    '''
    - 一个Work对象代表一个文件, 这里是文件名
    - 一个 Work文件包含很多个 Sheet 对象
    - 和这个人的历史记录的对象
    '''

    def __init__(self) -> None:
        self.name: str = ''  #一个Work对象代表一个文件，这里是文件名
        self.sheets: list[Sheet] = []  #一个 Work文件包含很多个 Sheet 对象
        self.history: data.History = data.History()  #历史记录


class Sheet:
    '''
    - 一个sheet里面可能有很多行, 这里的row是行
    - 每个sheet都有自己的表格名字
    '''

    def __init__(self) -> None:
        self.name: str = ''
        self.rows: list[Row] = []


class Row:
    '''
    {
        'url_1': str,                #第一页地址
        'url_2': str,                #第二页地址
        'url_3': str,                #第三页地址
        'title': str,                #论坛标题
        'nick_name': str             #昵称
        'forum_name: str             #论坛的名字
    }
    '''

    def __init__(self) -> None:
        self.url_1: str = ''
        self.url_2: str = ''
        self.url_3: str = ''
        self.title: str = ''
        self.nick_name: str = ''
        # self.forum_name: str = ''
