import data
import service


def out_put_data(works: data.Works, log_path: str = ''):
    for w in works.works:

        for s in w.data:
            log_content = '%s ==> 正在输出需要执行的数据 ==> %s\n' % (w.name, s.name)
            service.c_err(log_content, log_path)

            for r in s.data:
                log_content = '%s ==> %s title: %s' % (w.name, s.name, r.title)
                service.c_log(log_content, log_path)

                log_content = '%s ==> %s nicke_name: %s' % (
                    w.name,
                    s.name,
                    r.nick_name,
                )
                service.c_log(log_content, log_path)

                log_content = '%s ==> %s url_1: %s' % (w.name, s.name, r.url_1)
                service.c_log(log_content, log_path)

                log_content = '%s ==> %s url_2: %s' % (w.name, s.name, r.url_2)
                service.c_log(log_content, log_path)

                log_content = '%s ==> %s url_3: %s\n' % (w.name, s.name,
                                                         r.url_3)
                service.c_log(log_content, log_path)
    log_content = '\n'
    service.c_log(log_content, log_path)
