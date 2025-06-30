from selenium import webdriver
from selenium.webdriver.common.by import By
from typing import List
from scrappers.fundacao_araucaria.model import Link, Call
from scrappers.scrapper import Scrapper

class FundacaoAraucariaScrapper(Scrapper):
    def __init__(self, source):
        self.source = source

    def extract_calls(self) -> List[Call]:
        source = self.source

        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        web_driver = webdriver.Chrome(options=options)
        web_driver.get(source)

        main_content_containers = web_driver.find_elements(By.XPATH, '//*[@id="content"]/div/div[1]/div')

        calls: List[Call] = []

        for container in main_content_containers:
            try:
                titulo = container.find_element(By.XPATH, './/div[1]/h3').text
                descricao = container.find_element(By.XPATH, './/div[1]/p').text
            except:
                continue

            spans = container.find_elements(By.XPATH, './/div[2]//span')

            inscricao = None
            responsavel = None
            dotacao = None

            for span in spans:
                text = span.text.strip()
                if text.startswith("Inscrição:"):
                    inscricao = text.replace("Inscrição:", "").strip()
                elif text.startswith("Dotação Inicial:"):
                    dotacao = text.replace("Dotação Inicial:", "").strip()

            links_container = container.find_elements(By.XPATH, './/div[1]/ul/li')
            links: List[Link] = []

            for link in links_container:
                try:
                    a_tag = link.find_element(By.XPATH, './/span/a')
                    links.append({
                        "title": a_tag.text,
                        "link": a_tag.get_attribute('href')
                    })
                except:
                    continue

            calls.append(Call(
                title=titulo,
                description=descricao,
                inscription=inscricao,
                initial_funding=dotacao,
                links=links
            ))

        web_driver.quit()
        return calls
