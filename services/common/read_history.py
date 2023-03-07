import services.data as data
import services.util.consol as consol
import services.util.json as json


def read_history(path: str, log_path: str = ''):
    history: list[data.History] = []

    log_content = '%s ==> 历史记录 ==> 正在读取' % (path)
    consol.log(log_content, log_path)

    json_read = json.read(path)  #读取json文件

    log_content = '%s ==> 历史记录 ==> 读取成功' % (path)
    consol.log(log_content, log_path)

    log_content = '%s ==> %s' % (path, history)
    consol.log(log_content, log_path)

    history_list = list(json_read)
    for h in history_list:
        _h = dict(h)
        _data = data.History().from_dict(_h)
        history.append(_data)

    log_content = '\n\n'
    consol.error(log_content, log_path)

    return history
