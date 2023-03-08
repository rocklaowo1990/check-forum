import services.data as data
import services.common as common
import services.util.consol as consol
import services.util.web as web
from selenium.webdriver.common.by import By


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


def check_url(
    works: data.Works,
    w_i: int,
    s_i: int,
    r_i: int,
    u_i: int,
    log_path: str = '',
):
    work = works.works[w_i]
    sheet = work.sheets[s_i]
    url = sheet.rows[r_i].url_1
    history = work.history
    resault = data.Resault()

    page = '第一页地址'
    if u_i == 2:
        url = sheet.rows[r_i].url_2
        page = '第二页地址'
    elif u_i == 3:
        page = '第三页地址'
        url = sheet.rows[r_i].url_3

    forum_name = get_forum_name(url)
    resault.name = forum_name
    resault.url = url

    log_content = '任务[%d/%d] > %s > %s[%d/%d] ==> %s: %s' % (
        w_i + 1,
        len(works.works),
        work.name,
        sheet.name,
        s_i + 1,
        len(work.sheets),
        page,
        url,
    )
    consol.log(log_content, log_path)

    log_content = '任务[%d/%d] > %s > %s[%d/%d] ==> 论坛的名字: %s' % (
        w_i + 1,
        len(works.works),
        work.name,
        sheet.name,
        s_i + 1,
        len(work.sheets),
        forum_name,
    )
    consol.log(log_content, log_path)

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
            len(work.sheets),
            forum_name,
        )
        consol.error(log_content, log_path)
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
            len(work.sheets),
            forum_name,
            resault.repeated,
        )
        consol.log(log_content, log_path)
        return resault

    check_black = common.check_black(work.history, url)

    if not check_black[0]:
        log_content = '任务[%d/%d] > %s > %s[%d/%d] ==> %s: 主站 %s 重复的次数太多: 已超过 %s 次' % (
            w_i + 1,
            len(works.works),
            work.name,
            sheet.name,
            s_i + 1,
            len(work.sheets),
            forum_name,
            check_black[1],
            check_black[2],
        )
        consol.log(log_content, log_path)

        resault.repeated.extend([
            '论坛 %s 已经超过最大使用次数 %s 次，禁止再次使用' % (check_black[1], check_black[2])
        ])

        return resault

    try:
        response = web.get(url)
        body_text = response.find_element(By.TAG_NAME, 'body').text
        resault.is_get = True
        log_content = '任务[%d/%d] > %s > %s[%d/%d] ==> 论坛的访问: 成功' % (
            w_i + 1,
            len(works.works),
            work.name,
            sheet.name,
            s_i + 1,
            len(work.sheets),
        )
        consol.succful(log_content, log_path)
    except:
        log_content = '任务[%d/%d] > %s > %s[%d/%d] ==> 论坛的访问: 失败' % (
            w_i + 1,
            len(works.works),
            work.name,
            sheet.name,
            s_i + 1,
            len(work.sheets),
        )
        consol.succful(log_content, log_path)
        return resault

    title_key = sheet.rows[r_i].title.strip().upper()
    nick_key = sheet.rows[r_i].nick_name.strip().upper()

    if title_key in body_text.upper():
        resault.is_have_title = True
        log_content = '任务[%d/%d] > %s > %s[%d/%d] ==> 论坛的标题: 已找到' % (
            w_i + 1,
            len(works.works),
            work.name,
            sheet.name,
            s_i + 1,
            len(work.sheets),
        )
        consol.succful(log_content, log_path)

    else:
        log_content = '任务[%d/%d] > %s > %s[%d/%d] ==> 论坛的标题: 无' % (
            w_i + 1,
            len(works.works),
            work.name,
            sheet.name,
            s_i + 1,
            len(work.sheets),
        )
        consol.error(log_content, log_path)
        return resault

    if nick_key in body_text.upper():
        resault.is_have_nick = True
        log_content = '任务[%d/%d] > %s > %s[%d/%d] ==> 论坛的昵称: 已找到' % (
            w_i + 1,
            len(works.works),
            work.name,
            sheet.name,
            s_i + 1,
            len(work.sheets),
        )
        consol.succful(log_content, log_path)
    else:
        log_content = '任务[%d/%d] > %s > %s[%d/%d] ==> 论坛的昵称: 无' % (
            w_i + 1,
            len(works.works),
            work.name,
            sheet.name,
            s_i + 1,
            len(work.sheets),
        )
        consol.error(log_content, log_path)
        return resault

    resault.is_pass = True

    return resault