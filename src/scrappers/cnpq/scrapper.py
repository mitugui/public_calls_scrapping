from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from scrappers.scrapper import Scrapper
from typing import List
from scrappers.cnpq.model import Call

class CNPQScrapper(Scrapper):
    def __init__(self, source):
        self.source = source

    def extract_calls(self):
        source = self.source

        options = FirefoxOptions()
        options.add_argument("--headless")
        options.set_preference("webdriver_accept_untrusted_certs", True)
        options.set_preference("acceptInsecureCerts", True)

        driver = webdriver.Firefox(options=options)
        driver.get(source)

        main_content_containers = driver.find_elements(By.XPATH, '//*[contains(@class, "espaco-conteudo")]/div/div[2]/div/div/ol/li')

        calls: List[Call] = []

        for container in main_content_containers:
            try:
                titulo = container.find_element(By.XPATH, './/div[1]/h4').text
                descricao = container.find_element(By.XPATH, './/div[1]/p').text
                inscricao = container.find_element(By.XPATH, './/div[1]/div/ul/li').text
                link = container.find_element(By.XPATH, './/div[2]/div/div/div/a').get_attribute('href')
            except Exception:
                continue

            calls.append(Call(
                title=titulo,
                description=descricao,
                inscription=inscricao,
                link=link
            ))

        driver.quit()
        return calls
