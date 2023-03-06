import service
import pandas as pd
import common


def get_srf(path: str, log_path: str = ''):
    # 定义数据
    urls: list[str] = []

    # 如果文件存在则读取
    if service.f_ishave(path):
        # 开始读取表格信息
        # 读取的是单个表格文件的所有 sheet
        df = pd.read_excel(path, sheet_name=None)

        log_content = '%s ==> 数据读取成功\n%s\n' % (path, df)
        service.c_log(log_content, log_path)

        # 开始分析表格数据
        # 主要是看这个表格有多少页
        # 每一页都需要解析出来
        for sheet_name, sheet_data in df.items():
            # 格式化表格文件
            sheet_rows = sheet_data.to_dict(orient='records')
            row_index = 0

            # 读取每一行的信息
            for row_data in sheet_rows:
                row_index += 1

                log_content = '%s ==> %s 正在解析第 %d 行数据\n%s' % (
                    path,
                    sheet_name,
                    row_index,
                    row_data,
                )
                service.c_log(log_content, log_path)

                # 把每一行的信息转成数组
                row_list = list(row_data.values())

                # 读取表格的第一列数据
                url = common.clear_nan(row_list[0]).strip()
                urls.append(url)

        log_content = '\n'
        service.c_log(log_content, log_path)

    return urls