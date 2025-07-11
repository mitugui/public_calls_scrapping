from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from scrappers.scrapper import Scrapper
from typing import List
from scrappers.model import Call, Link

class CNPQScrapper(Scrapper):
    def __init__(self, source):
        self.source = source

    def extract_calls(self):
        source = self.source

        options = FirefoxOptions()
        options.add_argument('--headless')
        options.set_preference('webdriver_accept_untrusted_certs', True)
        options.set_preference('acceptInsecureCerts', True)

        driver = webdriver.Firefox(options=options)
        driver.get(source)

        main_content_containers = driver.find_elements(By.XPATH, '//*[contains(@class, "espaco-conteudo")]/div/div[2]/div/div/ol/li')

        calls: List[Call] = []

        for container in main_content_containers:
            links: List[Link] = []

            try:
                title = container.find_element(By.XPATH, './/div[1]/h4').text
                description = container.find_element(By.XPATH, './/div[1]/p').text
                inscription = container.find_element(By.XPATH, './/div[1]/div/ul/li').text
                link = container.find_element(By.XPATH, './/div[2]/div/div/div/a')

                links.append({
                    'title': 'Chamada',
                    'link': link.get_attribute('href')
                })
            except Exception:
                continue

            calls.append(Call(
                title=title,
                description=description,
                inscription=inscription,
                links=links
            ))

        driver.quit()
        return calls
