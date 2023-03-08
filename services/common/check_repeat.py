import services.data as data


def check_repeat(works: data.Works, work_name: str, forum_name: str):
    repeat_str: list[str] = []

    pass_w = False

    for w in works.works:
        if w.name == work_name:
            continue

        pass_s = False
        if pass_w:
            continue

        for s in w.sheets:

            if pass_s:
                break

            for r in s.rows:

                in_url_1 = forum_name in r.url_1
                in_url_2 = forum_name in r.url_2
                in_url_3 = forum_name in r.url_3

                if in_url_1 or in_url_2 or in_url_3:
                    repeat_str.append(w.name)
                    pass_s = True
                    pass_w = True
                    break

    return repeat_str