import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from base.base_driver import BaseDriver


class LaunchPage(BaseDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #Locator
    DEPART_FROM_FIELD = "//input[@placeholder='Leaving from']"
    GOING_TO_FIELD = "//input[@placeholder='Going to']"

    def getDepartFromField(self):
        return self.driver.find_element(By.XPATH, self.DEPART_FROM_FIELD)

    def enterDepartFromLocation(self, departlocation):
        self.getDepartFromField().click()
        self.getDepartFromField().send_keys(departlocation)
        time.sleep(2)
        self.getDepartFromField().send_keys(Keys.ENTER)

    def getGoingToField(self):
        return self.driver.find_element(By.XPATH, self.GOING_TO_FIELD)

    def enterGoingToLocation(self, goingtolocation):
        self.getGoingToField().click()
        self.getGoingToField().send_keys(goingtolocation)
        time.sleep(2)
        self.getGoingToField().send_keys(Keys.ENTER)

    """
    def departfrom(self, departlocation):
        # to select directly using full text and clicking on enter
        depart_from = self.driver.find_element(By.XPATH, "//input[@placeholder='Leaving from']")
        depart_from.send_keys("New Delhi")
        time.sleep(2)
        depart_from.send_keys(Keys.ENTER)  # => for any keys in the keyboard
    

    def goingto(self, goingtolocation):
        # selecting from the search result displayed when typing "New"
        arrival_to = self.driver.find_element(By.XPATH, "//input[@placeholder='Going to']")
        arrival_to.click()
        arrival_to.send_keys("New York")
        time.sleep(2)
        arrival_to.send_keys(Keys.ENTER)
    """


    def clickSearch(self):
        self.driver.find_element(By.XPATH, "//span[@class='m-searchForm__searchBtn-search ml-4']").click()
        time.sleep(3)