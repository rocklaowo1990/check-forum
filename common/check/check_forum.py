import re
import time
import common
import data
import service


def check_forum(
    works: data.Works,
    w_i: int,
    s_i: int,
    r_i: int,
    u_i: int,
    log_path: str = '',
):

    work = works.works[w_i]
    sheet = work.data[s_i]
    url = sheet.data[r_i].url_1
    history = work.history
    resault = data.Resault()

    page = '第一页地址'
    if u_i == 2:
        url = sheet.data[r_i].url_2
        page = '第二页地址'
    elif u_i == 3:
        page = '第三页地址'
        url = sheet.data[r_i].url_3

    forum_name = common.get_forum_name(url)
    resault.name = forum_name
    resault.url = url

    log_content = '任务[%d/%d] > %s > %s[%d/%d] ==> %s: %s' % (
        w_i + 1,
        len(works.works),
        work.name,
        sheet.name,
        s_i + 1,
        len(work.data),
        page,
        url,
    )
    service.c_log(log_content, log_path)

    log_content = '任务[%d/%d] > %s > %s[%d/%d] ==> 论坛的名字: %s' % (
        w_i + 1,
        len(works.works),
        work.name,
        sheet.name,
        s_i + 1,
        len(work.data),
        forum_name,
    )
    service.c_log(log_content, log_path)

    if url == '':
        return resault

    is_proce = common.check_proce(history.successful, forum_name)
    resault.is_processed = is_proce

    if is_proce:
        log_content = '任务[%d/%d] > %s > %s[%d/%d] ==> %s: 这个论坛已经处理过' % (
            w_i + 1,
            len(works.works),
            work.name,
            sheet.name,
            s_i + 1,
            len(work.data),
            forum_name,
        )
        service.c_err(log_content, log_path)
        resault.is_pass = True
        return resault

    repeated = common.check_repeat(works, work.name, forum_name)
    resault.repeated.extend(repeated)

    if resault.repeated != []:
        log_content = '任务[%d/%d] > %s > %s[%d/%d] ==> %s: 这个论坛和其他人的论坛重复: %s' % (
            w_i + 1,
            len(works.works),
            work.name,
            sheet.name,
            s_i + 1,
            len(work.data),
            forum_name,
            resault.repeated,
        )
        service.c_log(log_content, log_path)
        return resault

    check_black = common.check_black(work.history, url)

    if not check_black[0]:
        log_content = '任务[%d/%d] > %s > %s[%d/%d] ==> %s: 主站 %s 重复的次数太多: 已超过 %s 次' % (
            w_i + 1,
            len(works.works),
            work.name,
            sheet.name,
            s_i + 1,
            len(work.data),
            forum_name,
            check_black[1],
            check_black[2],
        )
        service.c_log(log_content, log_path)

        resault.repeated.extend(
            ['论坛 %s 已经超过最大使用次数 %s 次，禁止再次使用' % (check_black[1], check_black[2])])

        return resault

    http = common.Http(url)
    response = http.get_table()

    resault.is_get = response.resault.is_get
    resault.is_have_table = response.resault.is_have_table

    if not resault.is_get:
        log_content = '任务[%d/%d] > %s > %s[%d/%d] ==> 论坛的访问: 失败' % (
            w_i + 1,
            len(works.works),
            work.name,
            sheet.name,
            s_i + 1,
            len(work.data),
        )
        service.c_err(log_content, log_path)
        return resault
    else:
        log_content = '任务[%d/%d] > %s > %s[%d/%d] ==> 论坛的访问: 成功' % (
            w_i + 1,
            len(works.works),
            work.name,
            sheet.name,
            s_i + 1,
            len(work.data),
        )
        service.c_suc(log_content, log_path)

    if not resault.is_have_table:
        log_content = '任务[%d/%d] > %s > %s[%d/%d] ==> 列表的检查: 没有找到' % (
            w_i + 1,
            len(works.works),
            work.name,
            sheet.name,
            s_i + 1,
            len(work.data),
        )
        service.c_err(log_content, log_path)
        return resault
    else:
        log_content = '任务[%d/%d] > %s > %s[%d/%d] ==> 列表的检查: 查到到 %d 个表格' % (
            w_i + 1,
            len(works.works),
            work.name,
            sheet.name,
            s_i + 1,
            len(work.data),
            len(response.tables),
        )
        service.c_suc(log_content, log_path)

    table_i = 0
    for table in response.tables:
        table_i += 1

        v_i = -1  # 浏览人数的下标
        p_i = -1  # 发布日期的下标

        log_content = '任务[%d/%d] > %s > %s[%d/%d] ==> 第%d/%d个表格: 正在检查 (一共 %d 行)' % (
            w_i + 1,
            len(works.works),
            work.name,
            sheet.name,
            s_i + 1,
            len(work.data),
            table_i,
            len(response.tables),
            len(table.body),
        )
        service.c_log(log_content, log_path)

        log_content = '任务[%d/%d] > %s > %s[%d/%d] ==> 第%d/%d个表格: 标题 %s' % (
            w_i + 1,
            len(works.works),
            work.name,
            sheet.name,
            s_i + 1,
            len(work.data),
            table_i,
            len(response.tables),
            table.head.data,
        )
        service.c_log(log_content, log_path)

        th_i = 0
        for th in table.head.data:
            if bool(re.search(r'VIEWS|VIEW|READ', th.upper())):
                v_i = th_i
                log_content = '任务[%d/%d] > %s > %s[%d/%d] ==> 第%d/%d个表格: 标题里查找到 View 标签，位置 %d 列(%s)' % (
                    w_i + 1,
                    len(works.works),
                    work.name,
                    sheet.name,
                    s_i + 1,
                    len(work.data),
                    table_i,
                    len(response.tables),
                    v_i + 1,
                    th,
                )
                service.c_suc(log_content, log_path)

            if bool(re.search(r'POST|LAST POST', th.upper())):
                p_i = th_i
                log_content = '任务[%d/%d] > %s > %s[%d/%d] ==> 第%d/%d个表格: 标题里查找到 Post 标签，位置 %d 列(%s)' % (
                    w_i + 1,
                    len(works.works),
                    work.name,
                    sheet.name,
                    s_i + 1,
                    len(work.data),
                    table_i,
                    len(response.tables),
                    p_i + 1,
                    th,
                )
                service.c_suc(log_content, log_path)
            th_i += 1

        td_i = 0
        for td in table.body:
            td_i += 1
            log_content = '任务[%d/%d] > %s > %s[%d/%d] ==> 第%d/%d个表格: 第 %d/%d 行 %s' % (
                w_i + 1,
                len(works.works),
                work.name,
                sheet.name,
                s_i + 1,
                len(work.data),
                table_i,
                len(response.tables),
                td_i,
                len(table.body),
                td.data,
            )
            service.c_log(log_content, log_path)

            if len(td.data) > len(table.head.data) and table.head.data != []:
                log_content = '任务[%d/%d] > %s > %s[%d/%d] ==> 第%d/%d个表格: 第 %d/%d 行数据不太正常' % (
                    w_i + 1,
                    len(works.works),
                    work.name,
                    sheet.name,
                    s_i + 1,
                    len(work.data),
                    table_i,
                    len(response.tables),
                    td_i,
                    len(table.body),
                )
                service.c_err(log_content, log_path)
                continue

            _is_have_title = False
            _is_have_nick = False
            _is_read = False
            _is_today = False

            for text in td.data:
                _text = text.strip().upper()
                title_key = sheet.data[r_i].title.strip().upper()
                nick_key = sheet.data[r_i].nick_name.strip().upper()

                if title_key in _text:
                    _is_have_title = True
                    resault.is_have_title = _is_have_title

                if nick_key in _text:
                    _is_have_nick = True
                    resault.is_have_nick = _is_have_nick

                in_hour = bool(
                    re.search(
                        r'SECOND|SECONDS|MINUTE|MINUTES|HOUR|HOURS|TODAY',
                        text.upper(),
                    ))

                day = time.localtime().tm_mday
                month = time.localtime().tm_mon

                month_str = 'Jan'
                month_str_all = 'January'

                if month == 2:
                    month_str = 'Feb'
                    month_str_all = 'January'
                elif month == 3:
                    month_str = 'Mar'
                    month_str_all = 'March'
                elif month == 4:
                    month_str = 'Apr'
                    month_str_all = 'April'
                elif month == 5:
                    month_str = 'May'
                    month_str_all = 'May'
                elif month == 6:
                    month_str = 'June'
                    month_str_all = 'June'
                elif month == 7:
                    month_str = 'July'
                    month_str_all = 'July'
                elif month == 8:
                    month_str = 'Aug'
                    month_str_all = 'August'
                elif month == 9:
                    month_str = 'Sept'
                    month_str_all = 'September'
                elif month == 10:
                    month_str = 'Oct'
                    month_str_all = 'October'
                elif month == 11:
                    month_str = 'Nov'
                    month_str_all = 'November'
                else:
                    month_str = 'Dec'
                    month_str_all = 'December'

                zuhe_1 = '%s %s' % (month_str, day) in text or '%s 0%s' % (
                    month_str, day) in text
                zuhe_2 = '%s %s' % (day, month_str) in text or '0%s %s' % (
                    day, month_str) in text

                zuhe_3 = '%s %s' % (month_str_all, day) in text or '%s 0%s' % (
                    month_str_all, day) in text
                zuhe_4 = '%s %s' % (day, month_str_all) in text or '0%s %s' % (
                    day, month_str_all) in text

                zuhe_5 = '%s.%s' % (day, month) in text or '0%s.%s' % (day, month) in text or '0%s.0%s' % (
                    day, month) in text or '%s.0%s' % (day, month) in text
                zuhe_6 = '%s.%s' % (month, day) in text or '0%s.%s' % (month, day) in text or '0%s.0%s' % (
                    month, day) in text or '%s.0%s' % (month, day) in text

                zuhe_7 = '%s-%s' % (day, month) in text or '0%s-%s' % (day, month) in text or '0%s-0%s' % (
                    day, month) in text or '%s-0%s' % (day, month) in text
                zuhe_8 = '%s-%s' % (month, day) in text or '0%s-%s' % (month, day) in text or '0%s-0%s' % (
                    month, day) in text or '%s-0%s' % (month, day) in text

                zuhe_9 = '%s/%s' % (day, month) in text or '0%s/%s' % (day, month) in text or '0%s/0%s' % (
                    day, month) in text or '%s/0%s' % (day, month) in text
                zuhe_10 = '%s/%s' % (month, day) in text or '0%s/%s' % (
                    month, day) in text or '0%s/0%s' % (month, day) in text or '%s/0%s' % (month, day) in text

                if zuhe_1 or zuhe_2 or zuhe_3 or zuhe_4 or zuhe_5 or zuhe_6 or zuhe_7 or zuhe_8 or zuhe_9 or zuhe_10 or in_hour:
                    _is_today = True

            log_content = '任务[%d/%d] > %s > %s[%d/%d] ==> 第%d/%d个表格: 第 %d/%d 行是否包含标题 %s' % (
                w_i + 1,
                len(works.works),
                work.name,
                sheet.name,
                s_i + 1,
                len(work.data),
                table_i,
                len(response.tables),
                td_i,
                len(table.body),
                '是' if _is_have_title else '否',
            )
            if _is_have_title:
                service.c_suc(log_content, log_path)
            else:
                service.c_err(log_content, log_path)

            log_content = '任务[%d/%d] > %s > %s[%d/%d] ==> 第%d/%d个表格: 第 %d/%d 行是否包含昵称 %s' % (
                w_i + 1,
                len(works.works),
                work.name,
                sheet.name,
                s_i + 1,
                len(work.data),
                table_i,
                len(response.tables),
                td_i,
                len(table.body),
                '是' if _is_have_nick else '否',
            )
            if _is_have_nick:
                service.c_suc(log_content, log_path)
            else:
                service.c_err(log_content, log_path)

            log_content = '任务[%d/%d] > %s > %s[%d/%d] ==> 第%d/%d个表格: 第 %d/%d 行是否今天发布 %s' % (
                w_i + 1,
                len(works.works),
                work.name,
                sheet.name,
                s_i + 1,
                len(work.data),
                table_i,
                len(response.tables),
                td_i,
                len(table.body),
                '是' if _is_today else '否',
            )
            if _is_today:
                service.c_suc(log_content, log_path)
            else:
                service.c_err(log_content, log_path)

            if not _is_have_title or not _is_have_nick or not _is_today:
                continue

            resault.is_today = True

            read = 0

            for text in td.data:

                _read = 0

                try:
                    _read = int(text)

                except:

                    if bool(re.search(r'VIEWS|VIEW|READ', text.upper())):

                        num_list: list[str] = []
                        _reader_str = ''

                        for s in text:

                            if s.isnumeric() and _reader_str != '%' and _reader_str != '.':
                                _reader_str += s
                            else:
                                if _reader_str != '':
                                    num_list.append(_reader_str)
                                    _reader_str = ''

                        for i in num_list:
                            if int(i) > _read:
                                _read = int(i)

                if _read > read and _read < 100:
                    read = _read

            resault.read = read

            if resault.read >= data.const.min_read:
                _is_read = True

            log_content = '任务[%d/%d] > %s > %s[%d/%d] ==> 第%d/%d个表格: 第 %d/%d 行查看人数是否达标 %s / %s' % (
                w_i + 1,
                len(works.works),
                work.name,
                sheet.name,
                s_i + 1,
                len(work.data),
                table_i,
                len(response.tables),
                td_i,
                len(table.body),
                read,
                '是' if _is_read else '否',
            )
            if _is_read:
                service.c_suc(log_content, log_path)
            else:
                service.c_err(log_content, log_path)

            if _is_read:
                resault.is_pass = True
                break

    return resault
