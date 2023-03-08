import services.data as data


def check_proce(history: list[data.ResaultRow], url_name: str):

    is_proce = False
    for s in history:

        list_url = [s.resault_1.name, s.resault_2.name, s.resault_3.name]
        is_proce = url_name != '' and url_name in list_url

        if is_proce:
            break

    return is_proce