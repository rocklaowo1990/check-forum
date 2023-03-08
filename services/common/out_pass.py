import services.data as data
import services.util.consol as consol


def out_pass(
    w_i: int,
    works: data.Works,
    work: data.Work,
    sheet: data.Sheet,
    s_i: int,
    is_url: bool,
    log_path: str,
    type: int = 1,
):
    log_content = '任务[%d/%d] > %s > %s[%d/%d] ==> %s: %s' % (
        w_i + 1,
        len(works.works),
        work.name,
        sheet.name,
        s_i + 1,
        len(work.sheets),
        '论坛的审核' if type == 1 else '任务的结果',
        '通过' if is_url else '不通过',
    )
    if is_url:
        consol.succful(log_content, log_path)
    else:
        consol.error(log_content, log_path)