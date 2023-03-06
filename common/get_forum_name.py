def get_forum_name(url: str):
    '''
        ### 解析论坛
        - 得到论坛的主域名
        '''
    domain = url
    domain = domain.replace('www.', '')
    domain = domain.replace('//forum.', '')
    domain = domain.replace('//forums.', '')
    domain = domain.replace('//news.', '')
    domain = domain.replace('//new.', '')
    domain = domain.replace('//foro.', '')
    domain = domain.replace('//foros.', '')
    domain = domain.replace('//', '')
    domain = domain.split(':')[-1]
    domain = domain.split('.')[0]
    return domain
