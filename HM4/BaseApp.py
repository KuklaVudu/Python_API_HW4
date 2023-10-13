from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from loging_config import setup_logging


class BasePage():
    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://test-stand.gb.ru"
        self.logger = setup_logging()

    def find_element(self, locator, time=30):
        try:
            element = WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                             message=f"Элемент {locator} не найден")
            self.logger.exception("GeekBrains")
        except:
            element = None
        return element

    def get_element_property(self, locator, property):
        element = self.find_element(locator)
        if element:
            return element.value_of_css_property(property)
        else:
            self.logger.exception(f'Свойство {property} не найдено с элементом в локаторе {locator}')
            return None

    def go_to_site(self):
        try:
            start_browsing = self.driver.get(self.base_url)
        except:
            self.logger.exception("Исключение при открытом сайте")
            start_browsing = None
        return start_browsing

    def alert(self):
        try:
            alert_obj = self.driver.switch_to.alert
            return alert_obj.text
        except:
            self.logger.exception("Исключение с предупреждением")
            return None