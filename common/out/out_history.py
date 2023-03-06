import service
import data


def output_history(history: list[data.History], log_path: str = ''):
    for h in history:
        log_content = '%s ==> 正在输出历史记录 ==> 失败记录:' % (h.name)
        service.c_log(log_content, log_path)

        for f in h.failure:
            log_content = '%s ==> %s' % (h.name, f)
            service.c_log(log_content, log_path)

        log_content = '%s ==> 正在输出历史记录 ==> 成功记录:' % (h.name)
        service.c_log(log_content, log_path)

        for s in h.successful:
            log_content = '%s ==> %s' % (h.name, s)
            service.c_log(log_content, log_path)

        log_content = '%s ==> 历史记录输出完成\n' % (h.name)
        service.c_log(log_content, log_path)

    log_content = '\n'
    service.c_log(log_content, log_path)
