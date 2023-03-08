import services.data as data
import services.util.consol as consol


def out_title(
    w_i: int,
    len_ws: int,
    w_name: str,
    sheet: data.Sheet,
    s_i: int,
    r_i: int,
    len_s: int,
    log_path: str,
):
    log_content = '任务[%d/%d] > %s > %s[%d/%d] ==> 当前的进度: %d / %d' % (
        w_i + 1,
        len_ws,
        w_name,
        sheet.name,
        s_i + 1,
        len_s,
        r_i + 1,
        len(sheet.rows),
    )
    consol.log(log_content, log_path)

    log_content = '任务[%d/%d] > %s > %s[%d/%d] ==> 帖子的标题: %s' % (
        w_i + 1,
        len_ws,
        w_name,
        sheet.name,
        s_i + 1,
        len_s,
        sheet.rows[r_i].title,
    )
    consol.log(log_content, log_path)

    log_content = '任务[%d/%d] > %s > %s[%d/%d] ==> 帖子的昵称: %s' % (
        w_i + 1,
        len_ws,
        w_name,
        sheet.name,
        s_i + 1,
        len_s,
        sheet.rows[r_i].nick_name,
    )
    consol.log(log_content, log_path)
