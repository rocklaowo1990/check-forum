import services.data as data
import services.common as common
import services.util.consol as consol


class Check:

    def __init__(
        self,
        works: data.Works,
        history: list[data.History],
        log_path: str = '',
        target_path: str = '',
    ) -> None:
        self.works: data.Works = works
        self.log_path: str = log_path
        self.history: list[data.History] = history
        self.target_path = target_path

    def sheet(self, work: data.Work, w_i: int, sheet: data.Sheet, s_i: int):
        _work = work
        r_i = 0
        for r in sheet.rows:

            resault_row = data.ResaultRow()
            resault_row.title = r.title
            resault_row.nick_name = r.nick_name
            resault_row.r_i = r_i
            resault_row.sheet_name = sheet.name

            # 这里只是打印一下头部信息
            common.out_title(w_i, len(self.works.works), work.name, sheet, s_i,
                             r_i, len(work.sheets), self.log_path)

            # 这里开始是审核
            # 每个论坛的审核都会返回一个结果
            resault_1 = common.check_url(self.works, w_i, s_i, r_i, 1,
                                         self.log_path)
            resault_row.resault_1 = resault_1
            is_processed_1 = resault_1.is_processed
            is_pass_1 = resault_1.is_pass

            common.out_pass(w_i, self.works, work, sheet, s_i,
                            resault_1.is_pass, self.log_path)

            resault_2 = common.check_url(self.works, w_i, s_i, r_i, 2,
                                         self.log_path)
            resault_row.resault_2 = resault_2
            is_processed_2 = resault_2.is_processed
            is_pass_2 = resault_2.is_pass
            common.out_pass(w_i, self.works, work, sheet, s_i,
                            resault_2.is_pass, self.log_path)

            resault_3 = common.check_url(self.works, w_i, s_i, r_i, 3,
                                         self.log_path)
            resault_row.resault_3 = resault_3
            is_processed_3 = resault_1.is_processed
            is_pass_3 = resault_1.is_pass
            common.out_pass(w_i, self.works, work, sheet, s_i,
                            resault_3.is_pass, self.log_path)

            is_processed = is_processed_1 or is_processed_2 or is_processed_3
            is_pass = is_pass_1 or is_pass_2 or is_pass_3
            resault_row.is_pass = is_pass

            common.out_pass(w_i, self.works, work, sheet, s_i, is_pass,
                            self.log_path, 2)
            consol.log('\n', self.log_path)

            is_in_fail = common.check_in(work.history.failure, r)

            if is_pass:
                if not is_processed:
                    _work.history.successful.append(resault_row)
            else:
                if not is_in_fail:
                    _work.history.failure.append(resault_row)

            r_i += 1

        return _work

    def work(self, w: data.Work, w_i: int):
        s_i = 0  #表示正在处理第 几 个人的业务
        _work = w
        for s in w.sheets:
            _work = self.sheet(_work, w_i, s, s_i)
            s_i += 1

        common.write_resault(self.target_path, w)

    # 入口程序
    def run(self):
        w_i = 0  #表示正在处理第 几 个人的业务

        for w in self.works.works:
            self.work(w, w_i)
            w_i += 1
