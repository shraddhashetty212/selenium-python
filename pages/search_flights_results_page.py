from selenium.webdriver.common.by import By

from base.base_driver import BaseDriver


class SearchFlights(BaseDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def filter_stop(self):
        one_stop_checkbox = self.driver.find_element(By.XPATH, "//body[1]/div[1]/div[2]/div[7]/div[1]/div[1]/dl[1]/div[1]/dd[2]/dl[1]/dd[1]/dl[1]/dd[2]/div[1]/label[1]/span[1]/i[1]")
        one_stop_checkbox.click()
