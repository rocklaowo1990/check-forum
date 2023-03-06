import service


def out_jindu(
    w_i: int,
    len_ws: int,
    w_name: str,
    s_name: str,
    s_i: int,
    len_s: int,
    r_i: int,
    len_r: int,
    log_path: str,
):
    log_content = '任务[%d/%d] > %s > %s[%d/%d] ==> 当前的进度: %d / %d' % (
        w_i + 1,
        len_ws,
        w_name,
        s_name,
        s_i + 1,
        len_s,
        r_i + 1,
        len_r,
    )
    service.c_log(log_content, log_path)