import services.data as data
import services.util.path as path


def write_resault(target_path: str, w: data.Work):
    w_path = path.join(target_path, '%s的结果.txt' % (w.name))
    len_f = len(w.history.failure)
    len_s = len(w.history.successful)
    len_a = len_f + len_s
    content = '==================== %s的结果 ====================\n\n' % (w.name)

    content += '任务总数: %d (成功: %d  /  失败: %d)\n\n' % (len_a, len_s, len_f)

    if w.history.successful != []:
        content += '成功明细:\n'
        content += '------------------------------------------------------------------------------\n'

    s_i = 0
    for s in w.history.successful:
        s_i += 1
        content += '第 %d 个论坛在表格里的位置: 表格[%s] > 第 %d 行\n' % (s_i, s.sheet_name,
                                                           s.r_i + 1)
        content += '帖子的标题: %s\n' % (s.title)
        content += '发帖人昵称: %s\n' % (s.nick_name)
        if s.resault_1.url != '':
            content += '第一页地址: %s\n' % (s.resault_1.url)
            content += '论坛的名称: %s\n' % (s.resault_1.name)
        if s.resault_2.url != '':
            content += '第二页地址: %s\n' % (s.resault_2.url)
            content += '论坛的名称: %s\n' % (s.resault_2.name)
        if s.resault_3.url != '':
            content += '第三页地址: %s\n' % (s.resault_3.url)
            content += '论坛的名称: %s\n' % (s.resault_3.name)

        content += '------------------------------------------------------------------------------\n'

    if w.history.failure != []:
        content += '\n失败明细:\n'
        content += '------------------------------------------------------------------------------\n'

    s_i = 0
    for s in w.history.failure:
        s_i += 1
        content += '第 %d 个论坛在表格里的位置: 表格[%s] > 第 %d 行\n' % (s_i, s.sheet_name,
                                                           s.r_i + 1)
        content += '帖子第标题: %s\n' % (s.title)
        content += '发帖人昵称: %s\n' % (s.nick_name)
        content += '下面是这个论坛失败的原因,请仔细核对,对结果有任何疑问请找上级申述\n'
        if s.resault_1.url != '':
            content += '第一页地址: %s\n' % (s.resault_1.url)
            content += '论坛的名称: %s\n' % (s.resault_1.name)
            if s.resault_1.repeated != []:
                content += '论坛有重复: %s\n' % (s.resault_1.repeated)
            elif not s.resault_1.is_get:
                content += '论坛的重复: 无\n'
                content += '论坛的访问: 失败\n'
            elif not s.resault_1.is_have_title:
                content += '论坛的重复: 无\n'
                content += '论坛的访问: 成功\n'
                content += '论坛的标题: 没有找到\n'
            elif not s.resault_1.is_have_nick:
                content += '论坛的重复: 无\n'
                content += '论坛的访问: 成功\n'
                content += '论坛的标题: 已找到\n'
                content += '论坛的昵称: 没有找到\n'
            else:
                content += '论坛的重复: 无\n'
                content += '论坛的访问: 成功\n'
                content += '论坛的表格: 已找到\n'
                content += '论坛的标题: 已找到\n'
                content += '论坛的昵称: 已找到\n'

        if s.resault_2.url != '':
            content += '第二页地址: %s\n' % (s.resault_2.url)
            content += '论坛的名称: %s\n' % (s.resault_2.name)
            if s.resault_2.repeated != []:
                content += '论坛有重复: %s\n' % (s.resault_2.repeated)
            elif not s.resault_2.is_get:
                content += '论坛的重复: 无\n'
                content += '论坛的访问: 失败\n'
            elif not s.resault_2.is_have_title:
                content += '论坛的重复: 无\n'
                content += '论坛的访问: 成功\n'
                content += '论坛的标题: 没有找到\n'
            elif not s.resault_2.is_have_nick:
                content += '论坛的重复: 无\n'
                content += '论坛的访问: 成功\n'
                content += '论坛的标题: 已找到\n'
                content += '论坛的昵称: 没有找到\n'
            else:
                content += '论坛的重复: 无\n'
                content += '论坛的访问: 成功\n'
                content += '论坛的表格: 已找到\n'
                content += '论坛的标题: 已找到\n'
                content += '论坛的昵称: 已找到\n'

        if s.resault_3.url != '':
            content += '第三页地址: %s\n' % (s.resault_3.url)
            content += '论坛的名称: %s\n' % (s.resault_3.name)
            if s.resault_3.repeated != []:
                content += '论坛有重复: %s\n' % (s.resault_3.repeated)
            elif not s.resault_3.is_get:
                content += '论坛的重复: 无\n'
                content += '论坛的访问: 失败\n'
            elif not s.resault_3.is_have_title:
                content += '论坛的重复: 无\n'
                content += '论坛的访问: 成功\n'
                content += '论坛的标题: 没有找到\n'
            elif not s.resault_3.is_have_nick:
                content += '论坛的重复: 无\n'
                content += '论坛的访问: 成功\n'
                content += '论坛的标题: 已找到\n'
                content += '论坛的昵称: 没有找到\n'
            else:
                content += '论坛的重复: 无\n'
                content += '论坛的访问: 成功\n'
                content += '论坛的表格: 已找到\n'
                content += '论坛的标题: 已找到\n'
                content += '论坛的昵称: 已找到\n'

        content += '------------------------------------------------------------------------------\n'

    with open(w_path, 'w+', newline='\n', encoding='utf-8') as f:
        f.write('%s\n' % (content))
    f.close()
