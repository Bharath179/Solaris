import logging
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Permission_page:
    navigation_bar_xpath = "//div[@class='group relative flex flex-col justify-between px-2 pb-4 h-screen']"
    settings_bar_xpath = "//p[text()='Settings']"
    permissions_xpath = "//p[text()='Permissions']"
    permission_newBtn_xpath = "//button[text()='New Permission']"
    permission_txt_field_xpath = "//input[@id='name']"
    check_boxes_xpath = "//input[@type='checkbox']"
    reports_checkboxes_xpath = "(//div[@class='grid grid-cols-2 h-14 content-center px-3'])[7]/descendant::input"
    create_btn_xpath = "//button[text()='Create']"
    records_xpath = "//td[text()='No Records Found.']"

    def __init__(self, driver):
        self.driver = driver

    def get_navigation_bar(self):
        navigation = self.driver.find_element(By.XPATH, self.navigation_bar_xpath)
        action = ActionChains(self.driver)
        time.sleep(2)
        action.move_to_element(navigation).perform()
        return self.driver.find_element(By.XPATH, self.navigation_bar_xpath)

    def click_settings_tab(self):
        self.driver.find_element(By.XPATH, self.settings_bar_xpath).click()

    def click_on_permission_tab(self):
        self.driver.find_element(By.XPATH, self.permissions_xpath).click()

    def click_on_permission_newBtn(self):
        self.driver.find_element(By.XPATH, self.permission_newBtn_xpath).click()

    def enter_permission_name(self, name):
        self.driver.find_element(By.XPATH, self.permission_txt_field_xpath).send_keys(name)

    def select_checkboxes(self):
        checkboxes = self.driver.find_elements(By.XPATH, self.check_boxes_xpath)
        for i in range(min(5, len(checkboxes))):
            checkboxes[i].click()

    def scroll_to_reports(self):
        checkboxes = self.driver.find_elements(By.XPATH, self.reports_checkboxes_xpath)
        for checkbox in checkboxes:
            action = ActionChains(self.driver)
            action.move_to_element(checkbox).pause(1).click().perform()
            time.sleep(1)

    def click_on_createBtn(self):
        try:
            # Wait for the create button to be clickable, with a timeout of 10 seconds
            create_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, self.create_btn_xpath))
            )
            create_button.click()
        except Exception as exception:
            raise RuntimeError("Error occurred while clicking on the Create button: %s" % exception)

    def check_user_created_or_not(self):
        records = self.driver.find_elements(By.XPATH, self.records_xpath)
        if records and any(record.is_displayed() for record in records):
            raise RuntimeError("No records found, user not created.")
        else:
            logging.info("Records are available.")
