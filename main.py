import os
import data
import service
import common

# 打包
# pip3 install pyinstaller
# pip install pyinstaller
# pyinstaller -F forum.py --clean
# pyinstaller -F -i 图标的地址.ico forum.py --clean
# pyinstaller -F -i c:\Users\rockl\Documents\python_forum\bitbug_favicon.ico main.py --clean
# pyinstaller -F main.py --clean

# 第一步：先输入目标文件夹
# 如果不存在，或者输入空值的话会一直要求输入，知道输入 exit 结束
target_input = common.input_target()

# 检查文件名字的合法性，并且获得文件夹里的所有文件
# 如果不是文件夹就会返回空数组【】

target = service.f_check(os.path.split(target_input)[-1])

# 日志文件的目录
# 这里做了一个防护措施
# 如果目标输入的不是一个文件夹则会报错
log_path = os.path.join(target.path, '日志.log')

#数据对象
task = data.Works()
history: list[data.History] = []

# 开始读取数据
# 这里可以读取到表格的数据和历史记录
for f in target.children:
    isXls = '.xls'.upper() == str(os.path.splitext(f)[-1]).upper()
    isXlsx = '.xlsx'.upper() == str(os.path.splitext(f)[-1]).upper()
    isCsv = '.csv'.upper() == str(os.path.splitext(f)[-1]).upper()
    isHistory = 'history.json'.upper() == str(os.path.split(f)[-1]).upper()

    # 这里是读取数据（要执行的数据）
    if isXls or isXlsx or isCsv:
        _data = common.get_data(f, log_path)
        task_work = data.Work()
        task_work.data.append(_data)
        task.works.append(_data)

    # 这里是读取历史记录
    elif isHistory:
        history.extend(common.get_history(f, log_path))

# 输出数据到日志
common.out_data(task, log_path)
common.out_history(history, log_path)

# 开始处理审核程序
check = common.Check(task, history, log_path, target.path)
new_works = check.run()
