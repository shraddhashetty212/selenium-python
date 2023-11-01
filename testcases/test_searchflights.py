

#LINK : https://www.selenium.dev/documentation/webdriver/waits/
#LINK : https://www.selenium.dev/documentation/webdriver/support_features/expected_conditions/

import time

import pytest
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from pages.flight_launch_page import LaunchPage
from pages.search_flights_results_page import SearchFlights
from utilities.utils import Utils


@pytest.mark.usefixtures("setup")
class TestFlightBooking():
    def test_flight_booking(self):
        lp = LaunchPage(self.driver)
        #lp.departfrom("New Delhi")
        lp.enterDepartFromLocation("New Delhi")
        #lp.goingto("Nelson")
        lp.enterGoingToLocation("New York")
        lp.clickSearch()

        #to handle scroll
        lp.page_scroll()

        #to filter using 1 stop filter
        sf = SearchFlights(self.driver)
        sf.filter_stop()


        #allstops1 = lp.wait_for_presence_of_all_elements(By.XPATH, "")



        #to search through the serach result and print and assert the 1 stop
        # ut = Utils()
        # ut.assertListItemText(allstops1, "1 Stop")



        #explicit wait
        #wait = WebDriverWait(driver, 10)

        #fluent wait
        self.wait = WebDriverWait(self.driver, 10, 2, ignored_exceptions=[TypeError])

        #search_results = driver.find_element(By.XPATH, "//span[@class='poi-result__codePost'][normalize-space()='PHF']").click()
        #print(search_results)
        #wait.until(EC.visibility_of_element_located(By.XPATH, "//span[@class='poi-result__codePost'][normalize-space()='PHF']"))
        # for results in search_results:
        #     print(results.text)
        #     if "Norfolk International Airport" in results.text:
        #         results.click()
        #         break



