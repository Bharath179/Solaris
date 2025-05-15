import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from pynput.keyboard import Key, Controller


class Ticketing:
    navigation_bar_xpath = "//div[@class='group relative flex flex-col justify-between px-2 pb-4 h-screen']"
    ticketing_xpath = "//p[text()='Ticketing']"
    new_ticket_button = "//*[text()='New Ticket']"
    category_xpath = "//*[@aria-controls='dropdown-button']//span[text()='Select a Category']"
    select_category_issue_xpath = "//div[text()='DC Board Replacement']"
    priority_xpath = "(//button//span[text()='Select an Option'])[2]"
    priority_option_xpath = "//div[text()='High']"
    user_xpath = "//label[text()='User']//following::span[text()='Select an Option']"
    select_user_xpath = "//div[text()='User 1']"
    issue_time_xpath = "//input[@inputmode='text']"
    select_date_xpath = "//div[@class='rs-calendar-body']//ancestor::div[@aria-label='05 Feb 2025']"
    textarea_xpath = "//textarea[@placeholder='Describle the issue in detail']"
    attachment_xpath = "//div[@role='presentation']"
    create_button_xpath = "//button[text()='Create']"

    def __init__(self, driver):
        self.driver = driver

    def get_navigation_bar(self):
        navigation = self.driver.find_element(By.XPATH, self.navigation_bar_xpath)
        action = ActionChains(self.driver)
        time.sleep(2)
        action.move_to_element(navigation).perform()
        return self.driver.find_element(By.XPATH, self.navigation_bar_xpath)

    def click_ticketing_bar(self):
        self.driver.find_element(By.XPATH, self.ticketing_xpath).click()

    def click_ticket_button(self):
        self.driver.find_element(By.XPATH, self.new_ticket_button).click()

    def click_category_dropdown(self):
        self.driver.find_element(By.XPATH, self.category_xpath).click()

    def click_select_category_issue(self):
        self.driver.find_element(By.XPATH, self.select_category_issue_xpath).click()

    def click_priority_dropdown(self):
        self.driver.find_element(By.XPATH, self.priority_xpath).click()

    def select_option_from_priority_dropdown(self):
        self.driver.find_element(By.XPATH, self.priority_option_xpath).click()

    def click_user_dropdown(self):
        self.driver.find_element(By.XPATH, self.user_xpath).click()

    def select_option_from_user_dropdown(self):
        self.driver.find_element(By.XPATH, self.select_user_xpath).click()

    def click_on_issue_time(self):
        self.driver.find_element(By.XPATH, self.issue_time_xpath).click()

    def select_date_from_calender(self):
        self.driver.find_element(By.XPATH, self.select_date_xpath).click()

    def select_textarea_field(self):
        self.driver.find_element(By.XPATH, self.textarea_xpath).send_keys("DC Board replacement")

    def click_on_attachment_field(self):
        action = ActionChains(self.driver)
        element = self.driver.find_element(By.XPATH, self.attachment_xpath)
        action.move_to_element(element).click().perform()
        keyboard = Controller()
        keyboard.type("C:\\Users\\Lenovo\\Desktop\\attachment.txt")
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        return self.driver.find_element(By.XPATH, self.attachment_xpath)

    def click_on_create_button(self):
        self.driver.find_element(By.XPATH, self.create_button_xpath).click()
