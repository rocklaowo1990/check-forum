import services.util.path as path
import services.util.consol as consol


def input_target_path(log_path: str = ''):

    # 一直要求输入目标文件夹的名称, 直到正确输入
    # 判断条件: 目录是否存在
    while True:
        path_input = input('\033[0;35;40m==> 请输入目录名称 : \033[0m')
        path_input = path_input.replace("'", '')

        # 不等于空就是说输入了一个目录
        # 判断这个目录是否存在
        if path_input != '' and path_input != '/':
            # 载入文件处理的实例
            # 需要传入一个path
            # is_have 方法是判断这个目录是不是存在,
            # 可以携带一个参数: isMake( 不存在的话是否创建一个 )
            if path.is_have(path_input, False, log_path):
                if path.is_dir(path_input):
                    log_content = '文件目录检查成功 ==> %s' % (path_input)
                    consol.succful(log_content, log_path)
                    return path_input
                else:
                    consol.error(
                        '输入的 %s 不是文件夹, 请重新输入' % (path_input),
                        log_path,
                    )
            elif path_input == 'exit':
                exit()  #结束程序
            else:
                consol.error('目录不存在, 请重新输入', log_path)
        else:
            consol.error('不能输入空值 或  "/"', log_path)
