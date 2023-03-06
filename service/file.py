import os
import service
import data

# os 拆分路径
# 要拆分路径时，也不要直接去拆字符串，而要通过os.path.split()函数
# 这样可以把一个路径拆分为两部分，后一部分总是最后级别的目录或文件名
# os.path.split('/Users/michael/testdir/file.txt')
# >>> ('/Users/michael/testdir', 'file.txt')

# os.path.splitext() 可以直接让你得到文件扩展名
# os.path.splitext('/path/to/file.txt')
# >>> ('/path/to/file', '.txt')


# 判断文件夹是否存在
def is_have(path: str, isMake: bool = False, log_path: str = ''):
    '''
    - is_have 方法是判断这个目录是不是存在，
    - 可以携带一个参数：isMake（不存在的话是否创建一个）
    '''
    log_content = '检查文件是否存在 ==> %s' % (path)
    service.c_log(log_content, log_path)

    _is_have = os.path.exists(path)

    if _is_have:
        log_content = '文件存在检查结果 ==> 存在'
    else:
        log_content = '文件存在检查结果 ==> 不存在'

    if not _is_have and isMake:
        service.c_log(log_content, log_path)
        log_content = '正在创建一个文件 ==> %s' % (path)
        service.c_log(log_content, log_path)

        os.makedirs(path)

        _is_have = True
    else:
        service.c_log(log_content, log_path)

    return _is_have


def write(path: str, content: str, type: str = 'a+'):
    '''
    ## 文件的写入方法
    ### type:
    + 'a' 在文件的末尾追加写入
    + 'r' 读取模式（默认值）
    + 'w' 写入模式
    + 'x' 独占写入模式
    + 'a' 附加模式
    + 'b' 二进制模式（与其他模式结合使用）
    + 't' 文本模式（默认值，与其他模式结合使用）
    + '+' 读写模式（与其他模式结合使用）
    '''
    with open(path, type, newline='\n', encoding='utf-8') as f:
        f.write('%s\n' % (content))
    f.close()


def rename(path: str):
    '''
    - 给文件重新命名
    - 如果包含一些不合法的符号就会纠正
    '''
    new = ''

    for v in path:

        isalnum = v.isalnum()  #是否是数字
        ishans = '\u4e00' <= v <= '\u9fa5'  #是否是汉字
        isfu = v == '_' or v == '.'  #是否是允许的特殊符号

        if isalnum or ishans or isfu:  #合法的字符保持不变
            new += v

        elif v == ' ':  #空格会改成_，其他不合法的不添加
            new += '_'

    return new


def check(path: str, log_path: str = ''):
    '''
    - 检查一个路径的文件是否合法
    - 如果包含一些不合法的符号就会纠正
    '''

    log_content = '%s ==> 正在检查文件名称是否合法' % (path)
    service.c_log(log_content, log_path)

    file_check = data.FileChildren()

    path_list = os.path.split(path)
    
    _path = rename(path_list[-1])
    _path = os.path.join(path_list[0], _path)

    if _path != path:
        log_content = '%s ==> 文件名称不合法,更改为 %s' % (path, _path)
        service.c_err(log_content, log_path)
        os.rename(path, _path)
    else:
        log_content = '%s ==> 文件名称合法' % (path)
        service.c_suc(log_content, log_path)

    file_check.path = _path

    if os.path.isdir(_path):
        log_content = '%s ==> 这是一个文件夹,继续对文件夹里的文件进行检查' % (_path)
        service.c_log(log_content, log_path)

        old_children = os.listdir(_path)
        log_content = '%s ==> 文件夹包含的文件 %s' % (_path, old_children)
        service.c_log(log_content, log_path)

        for child in old_children:
            log_content = '%s ==> %s ==> 正在检查文件名称是否合法' % (_path, child)
            service.c_log(log_content, log_path)

            new_child = rename(child)
            old_child_path = os.path.join(_path, child)
            new_child_path = os.path.join(_path, new_child)

            if new_child != child:
                log_content = '%s ==> %s ==> 文件名称不合法,更改为 %s' % (
                    _path,
                    child,
                    new_child,
                )
                service.c_log(log_content, log_path)
                os.rename(old_child_path, new_child_path)
            else:
                log_content = '%s ==> %s ==> 文件名称合法' % (_path, child)
                service.c_suc(log_content, log_path)

            file_check.children.append(new_child_path)
    else:
        log_content = '%s ==> 这是一个非文件夹' % (path, _path)
        service.c_log(log_content, log_path)

    log_content = '%s ==> 检查完成 %s' % (file_check.path, file_check.children)
    service.c_log(log_content, log_path)
    return file_check
