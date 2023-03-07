import services.util as util


def error(message: str, log_path: str = ''):
    '''
    - 系统输出信息: 错误信息
    - 日志会单独用一个文本记录
    '''
    print('\033[0;35;40m==\033[0;35;40m>\033[0;%d;40m %s\033[0m' %
          (31, message))

    # 写入日志文件
    # 没有处理的就不写入日志里
    # 处理总数量大于0为判定条件
    if not log_path == '':
        util.path.write(log_path, message)


def log(message: str, log_path: str = ''):
    '''
    - 系统输出信息: 普通输出日志
    - 日志会单独用一个文本记录

    '''
    print('\033[0;35;40m==\033[0;35;40m>\033[0;%d;40m %s\033[0m' %
          (33, message))

    # 写入日志文件
    # 没有处理的就不写入日志里
    # 处理总数量大于0为判定条件
    if not log_path == '':
        util.path.write(log_path, message)


def succful(message: str, log_path: str = ''):
    '''
    - 系统输出信息: 成功信息的输出
    - 日志会单独用一个文本记录
    '''
    print('\033[0;35;40m==\033[0;35;40m>\033[0;%d;40m %s\033[0m' %
          (32, message))

    # 写入日志文件
    # 没有处理的就不写入日志里
    # 处理总数量大于0为判定条件
    if not log_path == '':
        util.path.write(log_path, message)
