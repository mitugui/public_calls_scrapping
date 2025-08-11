from services.remote_web_driver_factory import RemoteWebDriverFactory
from selenium.webdriver.common.by import By
from scrappers.scrapper import Scrapper
from typing import List
from scrappers.model import Call, Link

class FundacaoAraucariaScrapper(Scrapper):
    def __init__(self, source, source_name):
        self.source = source
        self.source_name = source_name

    def extract_calls(self) -> List[Call]:
        source = self.source
        
        driver = RemoteWebDriverFactory.get_driver()

        driver.get(source)

        main_content_containers = driver.find_elements(By.XPATH, '//*[@id="content"]/div/div[1]/div')

        calls: List[Call] = []

        for container in main_content_containers:
            try:
                title = container.find_element(By.XPATH, './/div[1]/h3').text
                description = container.find_element(By.XPATH, './/div[1]/p').text
            except:
                continue

            spans = container.find_elements(By.XPATH, './/div[2]//span')

            inscription = None
            initial_funding = None

            for span in spans:
                text = span.text.strip()
                if text.startswith('Inscrição'):
                    inscription = text.replace('Inscrição:', '').strip()
                elif text.startswith('Dotação Inicial:'):
                    initial_funding = text.replace('Dotação Inicial:', '').strip()

            links_container = container.find_elements(By.XPATH, './/div[1]/ul/li')
            links: List[Link] = []

            for link in links_container:
                try:
                    a_tag = link.find_element(By.XPATH, './/span/a')
                    links.append({
                        'title': a_tag.text,
                        'link': a_tag.get_attribute('href')
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
