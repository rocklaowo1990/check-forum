import services.data as data


def check_black(history: data.History, url: str):
    is_pass = True
    name = ''
    number = 0

    for key in data.const.BLACK_LIST:
        if key in url:
            repeat = 0
            number = data.const.BLACK_LIST[key]
            name = key

            for r in history.successful:

                in_url_1 = key in r.resault_1.url
                in_url_2 = key in r.resault_2.url
                in_url_3 = key in r.resault_3.url

                if in_url_1 or in_url_2 or in_url_3:
                    repeat += 1

            if repeat >= data.const.BLACK_LIST[key]:
                is_pass = False

    return is_pass, name, number