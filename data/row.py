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
