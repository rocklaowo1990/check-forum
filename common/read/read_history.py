import service
import data
import common


def get_history(path: str, log_path: str = ''):
    history: list[data.History] = []
    read_json = common.get_json(path, log_path)

    log_content = '%s ==> 历史记录 ==> 数据的类型为 %s' % (path, type(read_json))
    service.c_log(log_content, log_path)

    if type(read_json).__name__ == 'list':
        _read_json = list(read_json)
        for r in _read_json:
            _r = dict(r)
            _data = data.History().from_json(_r)
            history.append(_data)

    else:
        log_content = '%s ==> 历史记录 ==> 数据类型不正确\n\n' % (path, type(_read_json))
        service.c_err(log_content, log_path)

    log_content = '\n\n'
    service.c_err(log_content, log_path)

    return history
