import common
import data


def check_repeat(works: data.Works, work_name: str, forum_name: str):
    repeat_str: list[str] = []

    pass_w = False

    for w in works.works:
        if w.name == work_name:
            continue

        pass_s = False
        if pass_w:
            continue

        for s in w.data:

            if pass_s:
                break

            for r in s.data:

                in_url_1 = forum_name in r.url_1
                in_url_2 = forum_name in r.url_2
                in_url_3 = forum_name in r.url_3

                if in_url_1 or in_url_2 or in_url_3:
                    repeat_str.append(w.name)
                    pass_s = True
                    pass_w = True
                    break

    return repeat_str


def check_black(history: data.History, url: str):
    is_pass = True
    name = ''
    number = 0

    for key in data.const.blacklist:
        if key in url:
            repeat = 0
            number = data.const.blacklist[key]
            name = key

            for r in history.successful:

                in_url_1 = key in r.resault_1.url
                in_url_2 = key in r.resault_2.url
                in_url_3 = key in r.resault_3.url

                if in_url_1 or in_url_2 or in_url_3:
                    repeat += 1

            if repeat >= data.const.blacklist[key]:
                is_pass = False

    return is_pass, name, number
