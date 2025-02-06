import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class Dashboard:
    navigation_bar_xpath="//div[@class='group relative flex flex-col justify-between px-2 pb-4 h-screen']"
    select_on_option_dropdown_xpath="//button[@type='button']//span[text()='Select an Option']"
    slect_first_option_from_dropdown_xpath="//div[text()='SECI600P1']"
    select_date_xpath="//*[@class='rs-input-group-addon']"
    all_dates_xpath="//*[@title= '29 Jan 2025']"
    station_details_xpath="//*[@class='bg-[#F3F4F6] flex flex-col md:flex-row']"

    def __init__(self,driver):
        self.driver=driver

    def get_navigation_bar(self):
        navigation=self.driver.find_element(By.XPATH,self.navigation_bar_xpath)
        action = ActionChains(self.driver)
        time.sleep(2)
        action.move_to_element(navigation).perform()
        return self.driver.find_element(By.XPATH, self.navigation_bar_xpath)

    def click_on_dropdown(self):
        self.driver.find_element(By.XPATH,self.select_on_option_dropdown_xpath).click()

    def get_select_first_option(self):
        self.driver.find_element(By.XPATH,self.slect_first_option_from_dropdown_xpath).click()

    def get_date(self):
        self.driver.find_element(By.XPATH,self.select_date_xpath).click()

    def get_paricular_date(self):
        date=self.driver.find_element(By.XPATH,self.all_dates_xpath)
        date.click()
        time.sleep(2)
        return date


    def get_station_details(self):
        station_element=self.driver.find_element(By.XPATH,self.station_details_xpath)
        return station_element.text
