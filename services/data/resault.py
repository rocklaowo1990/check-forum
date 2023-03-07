class ResaultRow:
    '''
    - 这个数据代表的是每一行的结果
    - 一般来说一行都有三个地址
    '''

    def __init__(self) -> None:
        self.title: str = ''
        self.nick_name: str = ''
        self.resault_1: Resault = Resault()
        self.resault_2: Resault = Resault()
        self.resault_3: Resault = Resault()
        self.sheet_name: str = ''
        self.r_i: int = 0
        self.is_pass = False

    def from_dict(self, json: dict):
        keys = json.keys()

        if 'title' in keys and json['title'] != None:
            self.title = json['title']

        if 'nick_name' in keys and json['nick_name'] != None:
            self.nick_name = json['nick_name']

        if 'resault_1' in keys and json['resault_1'] != None:
            self.resault_1 = Resault().from_dict(json['resault_1'])

        if 'resault_2' in keys and json['resault_2'] != None:
            self.resault_2 = Resault().from_dict(json['resault_2'])

        if 'resault_3' in keys and json['resault_3'] != None:
            self.resault_3 = Resault().from_dict(json['resault_3'])

        if 'sheet_name' in keys and json['sheet_name'] != None:
            self.sheet_name = json['sheet_name']

        if 'r_i' in keys and json['r_i'] != None:
            self.r_i = json['r_i']

        if 'is_pass' in keys and json['is_pass'] != None:
            self.is_pass = json['is_pass']

        return self

    def to_json(self):
        json = {}
        json['title'] = self.title
        json['nick_name'] = self.nick_name
        json['resault_1'] = self.resault_1.to_json()
        json['resault_2'] = self.resault_2.to_json()
        json['resault_3'] = self.resault_3.to_json()
        json['sheet_name'] = self.sheet_name
        json['r_i'] = self.r_i
        json['is_pass'] = self.is_pass
        return json


class Resault:
    '''
    - Reasault 对象是单个地址的审核结果
    - is_get: 网站是否能访问
    - is_have_table: 网站中是否包含表格的文件
    - is_have_title: 网站中的表格是否包含标题
    - is_have_nick: 网站中的表格是否包含昵称
    - time: 帖子的发帖日期是否是今天
    - read: 帖子是否有超过20个人查看
    - url_p: 网站的日访问量是否达标了
    '''

    def __init__(self) -> None:
        self.url: int = ''
        self.name: str = ''
        self.repeated: list[str] = []
        self.is_processed: bool = False
        self.is_get: bool = False
        self.is_have_table: bool = False
        self.is_have_title: bool = False
        self.is_have_nick: bool = False
        self.is_today: bool = False
        self.read: int = 0
        self.is_pass: bool = False
        pass

    def from_dict(self, json: dict):
        keys = json.keys()

        if 'url' in keys and json['url'] != None:
            self.url = json['url']

        if 'name' in keys and json['name'] != None:
            self.name = json['name']

        if 'repeated' in keys and json['repeated'] != None:
            self.repeated = json['repeated']

        if 'is_processed' in keys and json['is_processed'] != None:
            self.is_processed = json['is_processed']

        if 'is_get' in keys and json['is_get'] != None:
            self.is_get = json['is_get']

        if 'is_have_table' in keys and json['is_have_table'] != None:
            self.is_have_table = json['is_have_table']

        if 'is_have_title' in keys and json['is_have_title'] != None:
            self.is_have_title = json['is_have_title']

        if 'is_have_nick' in keys and json['is_have_nick'] != None:
            self.is_have_nick = json['is_have_nick']

        if 'is_today' in keys and json['is_today'] != None:
            self.is_today = json['is_today']

        if 'read' in keys and json['read'] != None:
            self.read = json['read']

        if 'is_pass' in keys and json['is_pass'] != None:
            self.is_pass = json['is_pass']

        return self

    def to_json(self):
        json = {}
        json['url'] = self.url
        json['name'] = self.name
        json['repeated'] = self.repeated
        json['is_processed'] = self.is_processed
        json['is_get'] = self.is_get
        json['is_have_table'] = self.is_have_table
        json['is_have_title'] = self.is_have_title
        json['is_have_nick'] = self.is_have_nick
        json['is_today'] = self.is_today
        json['read'] = self.read
        json['is_pass'] = self.is_pass
        return json