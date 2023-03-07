import numpy as np
import pandas as pd

import services.data as data
import services.util as util


def clear_nan(value):
    '''
    ### 解析表格里的数据
    - 转成字符串
    '''
    _value = str(value)

    if _value == '' or _value is np.nan or _value.upper() == 'nan'.upper():
        return ''
    else:
        return _value


def read_data(path: str, log_path: str = ''):
    work_data = data.Work()

    log_content = '%s ==> 正在准备读取数据' % (path)
    util.consol.log(log_content, log_path)

    isXls = '.xls'.upper() in str(util.path.splitext(path)).upper()
    isXlsx = '.xlsx'.upper() in str(util.path.splitext(path)).upper()
    isCsv = '.csv'.upper() in str(util.path.splitext(path)).upper()

    if not isXls and not isXlsx and not isCsv:
        log_content = '%s ==> 文件格式不正确' % (path)
        util.consol.error(log_content, log_path)

    else:
        # 文件名
        n = util.path.split(path)[-1]  # 先去的文件名字+后缀
        work_data.name = util.path.splitext(n)[0]  # 取得不含后缀的名字
        work_data.history.name = util.path.splitext(n)[0]  # 取得不含后缀的名字

        log_content = '%s ==> 文件名: %s' % (path, work_data.name)
        util.consol.error(log_content, log_path)

        # 开始读取表格信息
        # 读取的是单个表格文件的所有 sheet
        df = pd.read_excel(path, sheet_name=None)
        log_content = '%s ==> 数据读取成功 \n\n%s\n' % (path, df)
        util.consol.log(log_content, log_path)

        for sheet_name, sheet_data in df.items():

            # 格式化表格文件
            sheet_rows = sheet_data.to_dict(orient='records')

            # 每一个 sheet 也有一个数据
            # 每个 sheet 是有多行数据组成
            data_sheet = data.Sheet()
            data_sheet.name = sheet_name

            row_index = 0

            # 读取每一行的信息
            for row_data in sheet_rows:
                row_index += 1

                log_content = '%s ==> %s 正在解析第 %d 行数据' % (
                    path,
                    sheet_name,
                    row_index,
                )
                util.consol.log(log_content, log_path)

                log_content = '%s ==> %s %s' % (
                    path,
                    sheet_name,
                    row_data,
                )
                util.consol.log(log_content, log_path)

                # 每一行也有数据的, 我们需要解析出来
                data_row = data.Row()

                # 把每一行的信息转成数组
                row_list = list(row_data.values())

                data_row.url_1 = clear_nan(row_list[0]).strip()
                data_row.url_2 = clear_nan(row_list[1]).strip()
                data_row.url_3 = clear_nan(row_list[2]).strip()
                data_row.title = clear_nan(row_list[3]).strip()
                data_row.nick_name = clear_nan(row_list[4]).strip()

                log_content = '%s ==> %s 数据解析完成' % (path, sheet_name)
                util.consol.log(log_content, log_path)

                log_content = '%s ==> %s url_1: %s' % (
                    path,
                    sheet_name,
                    data_row.url_1,
                )
                util.consol.log(log_content, log_path)
                log_content = '%s ==> %s url_2: %s' % (
                    path,
                    sheet_name,
                    data_row.url_2,
                )
                util.consol.log(log_content, log_path)
                log_content = '%s ==> %s url_3: %s' % (
                    path,
                    sheet_name,
                    data_row.url_3,
                )
                util.consol.log(log_content, log_path)
                log_content = '%s ==> %s title: %s' % (
                    path,
                    sheet_name,
                    data_row.title,
                )
                util.consol.log(log_content, log_path)
                log_content = '%s ==> %s nick_name: %s\n' % (
                    path,
                    sheet_name,
                    data_row.nick_name,
                )
                util.consol.log(log_content, log_path)

                data_sheet.rows.append(data_row)

            work_data.sheets.append(data_sheet)

            log_content = '%s ==> 数据读取完成\n\n' % (path)
            util.consol.log(log_content, log_path)

    return work_data