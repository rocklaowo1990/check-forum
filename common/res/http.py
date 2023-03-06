from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import data


class Http:

    def __init__(self, url: str = '') -> None:
        self.url = url
        self.resault = data.Resault()

    def get(self):
        if not 'http' in self.url:
            return None

        driver = webdriver.Chrome()
        # driver.implicitly_wait(3)

        try:
            driver.get(self.url)
            self.resault.is_get = True

        except:
            return None

        # try:
        #     WebDriverWait(driver, 3).until(
        #         EC.presence_of_element_located((By.TAG_NAME, 'table')))
        #     self.resault.is_have_table = True
        # except:
        #     return None

        return driver

    def get_table(self):
        driver = self.get()

        response = data.Response()
        response.resault = self.resault

        if driver == None:
            return response

        tables_elements = []

        try:
            tables_elements = driver.find_elements(By.TAG_NAME, 'table')
        except:
            pass

        if tables_elements != []:

            for t in tables_elements:
                _table = data.Table()

                try:
                    thead = t.find_element(By.TAG_NAME, 'thead')
                    tr_head = thead.find_element(By.TAG_NAME, 'tr')

                    thlist_head = tr_head.find_elements(By.TAG_NAME, 'th')

                    for th in thlist_head:
                        text = th.text
                        text = text.strip()
                        text = text.replace('\n', ' ')
                        if text != '' and text != ' ':
                            _table.head.data.append(text)
                except:
                    pass

                try:
                    tbody = t.find_element(By.TAG_NAME, 'tbody')
                    tr_body_list = tbody.find_elements(By.TAG_NAME, 'tr')

                    for tr in tr_body_list:
                        td_list = tr.find_elements(By.TAG_NAME, 'td')
                        td_data = data.Td()

                        for td in td_list:
                            text = td.text
                            text = text.strip()
                            text = text.replace('\n', ' ')
                            if text != '' and text != ' ':
                                td_data.data.append(text)

                        if td_data.data != []:
                            _table.body.append(td_data)
                except:
                    pass

                if _table.body != []:
                    response.tables.append(_table)

        

        try:
            tables_elements = driver.find_elements(By.TAG_NAME, 'dl')
        except:
            pass

        if tables_elements != []:

            _table = data.Table()

            for t in tables_elements:
                td_data = data.Td()
                try:
                    dt = t.find_element(By.TAG_NAME, 'dt')
                    text = dt.text
                    text = text.strip()
                    text = text.replace('\n', ' ')
                    if text != '' and text != ' ':
                        td_data.data.append(text)

                    dd_list = t.find_elements(By.TAG_NAME, 'dd')
                    for dd in dd_list:
                        text = dd.text
                        text = text.strip()
                        text = text.replace('\n', ' ')
                        if text != '' and text != ' ':
                            td_data.data.append(text)

                except:
                    pass

                if td_data.data != []:
                    _table.body.append(td_data)

            if _table.body != []:
                response.tables.append(_table)

        

        try:
            tables_elements = driver.find_elements(
                By.CLASS_NAME, 'structItem')
        except:
            pass

        if tables_elements != []:
            _table = data.Table()

            for t in tables_elements:
                td_data = data.Td()

                try:

                    dd_list = t.find_elements(
                        By.CLASS_NAME, 'structItem-cell')

                    for dd in dd_list:
                        text = dd.text
                        text = text.strip()
                        text = text.replace('\n', ' ')
                        if text != '' and text != ' ':
                            td_data.data.append(text)

                except:
                    pass

                if td_data.data != []:
                    _table.body.append(td_data)

            if _table.body != []:

                response.tables.append(_table)

        

        try:
            tables_elements = driver.find_elements(
                By.TAG_NAME, 'li')
        except:
            pass

        if tables_elements != []:
            _table = data.Table()

            for t in tables_elements:
                td_data = data.Td()

                try:

                    dd_list = t.find_elements(
                        By.XPATH, './*')

                    for dd in dd_list:
                        text = dd.text
                        text = text.strip()
                        text = text.replace('\n', ' ')
                        if text != '' and text != ' ':
                            td_data.data.append(text)

                except:
                    pass

                if td_data.data != []:
                    _table.body.append(td_data)

            if _table.body != []:
                response.tables.append(_table)
                
        if response.tables != []:
            self.resault.is_have_table = True

        return response
