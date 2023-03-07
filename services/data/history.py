import services.data as data


class History:
    '''
    {
        'name': str,                  #文件的名称, 一个文件代表一个员工
        'failure': list[str],         #成功的论坛列表
        'successful': list[str],      #成功的论坛列表
        'repeated': list[str],        #成功的论坛列表
    }
    '''

    def __init__(self) -> None:
        self.name: str = ''
        self.failure: list[data.ResaultRow] = []
        self.successful: list[data.ResaultRow] = []

    def from_dict(self, json: dict):
        keys = json.keys()

        if 'name' in keys and json['name'] != None:
            self.name = json['name']

        if 'failure' in keys and json['failure'] != None:
            if type(json['failure']).__name__ == 'list':
                _list = list(json['failure'])
                for item in _list:
                    self.failure.append(data.ResaultRow().from_dict(item))

        if 'successful' in keys and json['successful'] != None:
            if type(json['successful']).__name__ == 'list':
                _list = list(json['successful'])
                for item in _list:
                    self.successful.append(data.ResaultRow().from_dict(item))

        return self

    def to_json(self):
        json = {}
        json['name'] = self.name
        json['failure'] = []
        json['successful'] = []
        for f in self.failure:
            json['failure'].append(f.to_json())
        for s in self.successful:
            json['successful'].append(s.to_json())
        return json
