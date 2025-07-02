from typing import Type
from scrappers.scrapper import Scrapper
from utils import file

class CallGenerator:
    @staticmethod
    def generate(scrapper_class: Type[Scrapper], source: str, source_name: str):
        scrapper = scrapper_class(source, source_name)
        calls = scrapper.extract_calls()

        json_file_name = source_name + '_calls'

        file.save_json(json_file_name, calls)
