import os
import pandas as pd
import common
import data
import service


def get_data(path: str, log_path: str = ''):
    work_data = data.Work()

    log_content = '%s ==> 正在准备读取数据' % (path)
    service.c_log(log_content, log_path)

    isXls = '.xls'.upper() in str(os.path.splitext(path)).upper()
    isXlsx = '.xlsx'.upper() in str(os.path.splitext(path)).upper()
    isCsv = '.csv'.upper() in str(os.path.splitext(path)).upper()

    if not isXls and not isXlsx and not isCsv:
        log_content = '%s ==> 文件格式不正确' % (path)
        service.c_err(log_content, log_path)

    else:
        # 文件名
        n = os.path.split(path)[-1]  # 先去的文件名字+后缀
        work_data.name = os.path.splitext(n)[0]  # 取得不含后缀的名字
        work_data.history.name = os.path.splitext(n)[0]  # 取得不含后缀的名字

        log_content = '%s ==> 文件名: %s' % (path, work_data.name)
        service.c_err(log_content, log_path)

        # 开始读取表格信息
        # 读取的是单个表格文件的所有 sheet
        df = pd.read_excel(path, sheet_name=None)
        log_content = '%s ==> 数据读取成功 \n\n%s\n' % (path, df)
        service.c_log(log_content, log_path)

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
                service.c_log(log_content, log_path)

                log_content = '%s ==> %s %s' % (
                    path,
                    sheet_name,
                    row_data,
                )
                service.c_log(log_content, log_path)

                # 每一行也有数据的, 我们需要解析出来
                data_row = data.Row()

                # 把每一行的信息转成数组
                row_list = list(row_data.values())

                data_row.url_1 = common.clear_nan(row_list[0]).strip()
                data_row.url_2 = common.clear_nan(row_list[1]).strip()
                data_row.url_3 = common.clear_nan(row_list[2]).strip()
                data_row.title = common.clear_nan(row_list[3]).strip()
                data_row.nick_name = common.clear_nan(row_list[4]).strip()

                log_content = '%s ==> %s 数据解析完成' % (path, sheet_name)
                service.c_log(log_content, log_path)

                log_content = '%s ==> %s url_1: %s' % (
                    path,
                    sheet_name,
                    data_row.url_1,
                )
                service.c_log(log_content, log_path)
                log_content = '%s ==> %s url_2: %s' % (
                    path,
                    sheet_name,
                    data_row.url_2,
                )
                service.c_log(log_content, log_path)
                log_content = '%s ==> %s url_3: %s' % (
                    path,
                    sheet_name,
                    data_row.url_3,
                )
                service.c_log(log_content, log_path)
                log_content = '%s ==> %s title: %s' % (
                    path,
                    sheet_name,
                    data_row.title,
                )
                service.c_log(log_content, log_path)
                log_content = '%s ==> %s nick_name: %s\n' % (
                    path,
                    sheet_name,
                    data_row.nick_name,
                )
                service.c_log(log_content, log_path)

                data_sheet.data.append(data_row)

            work_data.data.append(data_sheet)

            log_content = '%s ==> 数据读取完成\n\n' % (path)
            service.c_log(log_content, log_path)

    return work_data
