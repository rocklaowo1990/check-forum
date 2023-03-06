import json
import service


def get_json(path: str, log_path: str = ''):
    history = {}

    log_content = '%s ==> 历史记录 ==> 正在读取' % (path)
    service.c_log(log_content, log_path)

    with open(path) as file:
        history = json.loads(file.read().strip())
    file.close()

    log_content = '%s ==> 历史记录 ==> 读取成功' % (path)
    service.c_log(log_content, log_path)

    log_content = '%s ==> %s' % (path, history)
    service.c_log(log_content, log_path)

    return history