from services.remote_web_driver_factory import RemoteWebDriverFactory
from selenium.webdriver.common.by import By
from scrappers.scrapper import Scrapper
from typing import List
from scrappers.model import Call, Link

class FunbioScrapper(Scrapper):
    def __init__(self, source, source_name):
        self.source = source
        self.source_name = source_name

    def extract_calls(self) -> List[Call]:
        source = self.source
        
        driver = RemoteWebDriverFactory.get_driver()

        driver.get(source)
        main_content_containers = driver.find_elements(By.XPATH, '//*[@id="selecoes"]/div[2]/div[2]/div/div/div[1]')

        calls: List[Call] = []

        for container in main_content_containers:
            try:
                title = container.find_element(By.XPATH, './/a/h4').text
                description = container.find_element(By.XPATH, './/h6[3]').text
            except:
                continue
            
            inscription = container.find_element(By.XPATH, './/h6[4]/strong').text
            initial_funding = container.find_element(By.XPATH, './/h6[5]/strong').text

            driver.get(container.find_element(By.XPATH, './/a[3]').get_attribute('href'))

            links_container = driver.find_elements(By.XPATH, '//*[@id="__next"]/div[1]/div[2]/div[1]/a')
            links: List[Link] = []

            for link in links_container:
                try:
                    links.append({
                        'title': link.text,
                        'link': link.get_attribute('href')
                    })
                except:
                    continue

            calls.append(Call(
                title=title,
                source=self.source_name,
                description=description,
                inscription=inscription,
                initial_funding=initial_funding,
                links=links
            ))

        driver.quit()
        return calls
