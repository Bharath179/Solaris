import time

from selenium.webdriver.common.by import By
import logging


class Dash_board:
    dash_board_xpath = "//div[text()='Dashboard']"
    side_bar_xpath = "(//div[@data-sidebar='sidebar'])[1]"
    components_xpath = "//div[@class='p-5']/div[@class='flex flex-col gap-6']"
    station_xpath = "//button[text()='Station']"
    station_card_xpath = "//div[contains(text(),'Station Details')]/ancestor::div[contains(@class,'card')]"
    generation_card_xpath = "//div[contains(text(),'Generation')]/ancestor::div[contains(@class,'card')]"
    whether_card_xpath = "//div[contains(text(),'Weather and Performance')]/ancestor::div[contains(@class,'card')]"
    station_zones_xpath = "//button[text()='Station']"
    zones_text_xpath = "//div[contains(text(),'STATIONS')]/following-sibling::*//span"

    east_zone_xpath = "//button[@type='button']/descendant::span[text()='East']"
    assam_xpath = "//button[@type='button']/descendant::span[text()='Assam']"
    manipur_xpath = "//button[@type='button']/descendant::span[text()='Manipur']"
    assam_stations_xpath = "//span[text()='Assam']/following::div[@class='pl-4 space-y-3 relative']"
    manipur_stations_xpath = "//span[text()='Manipur']/following::div[@class='pl-4 space-y-3 relative']"

    north_zone_xpath = "//button[@type='button']/descendant::span[text()='North']"
    bihar_xpath = "//button[@type='button']/descendant::span[text()='Bihar']"
    rajasthan_xpath = "//button[@type='button']/descendant::span[text()='Rajasthan']"
    bihar_stations_xpath = "//span[text()='Bihar']/following::div[@class='pl-4 space-y-3 relative']"
    rajasthan_stations_xpath = "//span[text()='Rajasthan']/following::div[@class='pl-4 space-y-3 relative']"

    south_zone_xpath = "//button[@type='button']/descendant::span[text()='South']"
    ka_xpath = "//button[@type='button']/descendant::span[text()='Karnataka']"
    ap_xpath = "//button[@type='button']/descendant::span[text()='Andhra Pradesh']"
    ka_stations_xpath = "//span[text()='Karnataka']/following::div[@class='pl-4 space-y-3 relative']"
    ap_stations_xpath = "//span[text()='Andhra Pradesh']/following::div[@class='pl-4 space-y-3 relative']"

    west_zone_xpath = "//button[@type='button']/descendant::span[text()='West']"
    gt_xpath = "//button[@type='button']/descendant::span[text()='Gujarat']"
    mh_xpath = "//button[@type='button']/descendant::span[text()='Maharashtra']"
    gt_stations_xpath = "//span[text()='Gujarat']/following::div[@class='pl-4 space-y-3 relative']"
    mh_stations_xpath = "//span[text()='Maharashtra']/following::div[@class='pl-4 space-y-3 relative']"

    table_xpath = "//table[@class='w-full caption-bottom text-sm text-center']/tbody/tr"

    quick_create_xpath = "//span[text()='Quick Create']"
    quick_create_options_xpath = "//div[@data-side='bottom']"

    def __init__(self, driver):
        self.driver = driver

    def get_dash_board_txt(self):
        self.driver.find_element(By.XPATH, self.dash_board_xpath)

    def get_side_bar(self):
        return self.driver.find_element(By.XPATH, self.side_bar_xpath)

    def get_components(self):
        return self.driver.find_elements(By.XPATH, self.components_xpath)

    def get_station_txt(self):
        return self.driver.find_element(By.XPATH, self.station_xpath).text

    def station_card(self):
        return self.driver.find_element(By.XPATH, self.station_card_xpath)

    def generation_card(self):
        return self.driver.find_element(By.XPATH, self.generation_card_xpath)

    def weather_card(self):
        return self.driver.find_element(By.XPATH, self.whether_card_xpath)

    def get_station_zones(self):
        self.driver.find_element(By.XPATH, self.station_zones_xpath).click()
        elements = self.driver.find_elements(By.XPATH, self.zones_text_xpath)

        if not elements:
            raise RuntimeError("No station zones found after clicking")

        return elements

    def get_zone_details(self, zone_name, states):
        # Click on the zone button based on zone_name
        if zone_name.lower() == "east":
            self.driver.find_element(By.XPATH, self.east_zone_xpath).click()
        elif zone_name.lower() == "north":
            self.driver.find_element(By.XPATH, self.north_zone_xpath).click()
        elif zone_name.lower() == "south":
            self.driver.find_element(By.XPATH, self.south_zone_xpath).click()
        elif zone_name.lower() == "west":
            self.driver.find_element(By.XPATH, self.west_zone_xpath).click()
        else:
            raise ValueError(f"Zone '{zone_name}' not handled in this method")

        time.sleep(2)

        for state in states:
            # Click state
            if state.lower() == "assam":
                self.driver.find_element(By.XPATH, self.assam_xpath).click()
                stations = self.driver.find_elements(By.XPATH, self.assam_stations_xpath)
            elif state.lower() == "manipur":
                self.driver.find_element(By.XPATH, self.manipur_xpath).click()
                stations = self.driver.find_elements(By.XPATH, self.manipur_stations_xpath)
            elif state.lower() == "bihar":
                self.driver.find_element(By.XPATH, self.bihar_xpath).click()
                stations = self.driver.find_elements(By.XPATH, self.bihar_stations_xpath)
            elif state.lower() == "rajasthan":
                self.driver.find_element(By.XPATH, self.rajasthan_xpath).click()
                stations = self.driver.find_elements(By.XPATH, self.rajasthan_stations_xpath)
            elif state.lower() == "karnataka":
                self.driver.find_element(By.XPATH, self.ka_xpath).click()
                stations = self.driver.find_elements(By.XPATH, self.ka_stations_xpath)
            elif state.lower() == "andhra pradesh":
                self.driver.find_element(By.XPATH, self.ap_xpath).click()
                stations = self.driver.find_elements(By.XPATH, self.ap_stations_xpath)
            elif state.lower() == "gujarat":
                self.driver.find_element(By.XPATH, self.gt_xpath).click()
                stations = self.driver.find_elements(By.XPATH, self.gt_stations_xpath)
            elif state.lower() == "maharashtra":
                self.driver.find_element(By.XPATH, self.mh_xpath).click()
                stations = self.driver.find_elements(By.XPATH, self.mh_stations_xpath)
            else:
                raise ValueError(f"State '{state}' not handled in this method")

            print(f"Stations under {zone_name} > {state}:")
            for station in stations:
                print(f"{station.text}")

    def get_table_values(self):
        rows = self.driver.find_elements(By.XPATH, self.table_xpath)

        active_inverters = []
        inactive_inverters = []

        logging.info("Reading Inverter Table:")

        for row in rows:
            cols = row.find_elements(By.TAG_NAME, "td")
            if len(cols) >= 5:
                name = cols[0].text.strip()
                min_val = cols[1].text.strip()
                max_val = cols[2].text.strip()
                energy = cols[3].text.strip()
                status = cols[4].text.strip()

                logging.info(f" - Name: {name}, Min: {min_val}, Max: {max_val},"
                             f" Energy: {energy}, Status: {status}")

                if status.lower() == "active":
                    active_inverters.append(name)
                else:
                    inactive_inverters.append(name)

        logging.info("\nActive Inverters:")
        for inv in active_inverters:
            logging.info(f"- {inv}")

        logging.info("\nIn-Active Inverters:")
        for inv in inactive_inverters:
            logging.info(f"- {inv}")

        return active_inverters, inactive_inverters

    def get_quick_create(self):
        self.driver.find_element(By.XPATH, self.quick_create_xpath).click()
        return self.driver.find_elements(By.XPATH, self.quick_create_options_xpath)
