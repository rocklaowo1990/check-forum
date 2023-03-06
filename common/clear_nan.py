import numpy as np


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