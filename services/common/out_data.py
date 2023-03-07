import services.data as data
import services.util.consol as consol


def out_data(works: data.Works, log_path: str = ''):
    for w in works.works:

        for s in w.sheets:
            log_content = '%s ==> 正在输出需要执行的数据 ==> %s\n' % (w.name, s.name)
            consol.error(log_content, log_path)

            for r in s.rows:
                log_content = '%s ==> %s title: %s' % (w.name, s.name, r.title)
                consol.log(log_content, log_path)

                log_content = '%s ==> %s nicke_name: %s' % (
                    w.name,
                    s.name,
                    r.nick_name,
                )
                consol.log(log_content, log_path)

                if r.url_1 != '':
                    log_content = '%s ==> %s url_1: %s' % (w.name, s.name,
                                                           r.url_1)
                    consol.log(log_content, log_path)

                if r.url_2 != '':
                    log_content = '%s ==> %s url_2: %s' % (w.name, s.name,
                                                           r.url_2)

                    consol.log(log_content, log_path)
                if r.url_3 != '':
                    log_content = '%s ==> %s url_3: %s\n' % (w.name, s.name,
                                                             r.url_3)
                    consol.log(log_content, log_path)
                log_content = '\n'
                consol.log(log_content, log_path)
