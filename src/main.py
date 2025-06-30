from flask import Flask
from flask_cors import CORS
from typing import Type
from scrappers.scrapper import Scrapper
from scrappers.fundacao_araucaria.scrapper import FundacaoAraucariaScrapper 
from utils import file

app = Flask(__name__)

cors = CORS(app)

app.config['CORS_HEADERS'] = 'Content-Type'
def generate(scrapper_class: Type[Scrapper], source: str, source_name: str):
    scrapper = scrapper_class(source)
    calls = scrapper.extract_calls()

    json_file_name = source_name + '_editais'

    file.save_json(json_file_name, calls)

@app.route('/calls', methods=['GET'])
def get():
    pass

if __name__ == '__main__':
    generate(
        FundacaoAraucariaScrapper,
        'https://www.fappr.pr.gov.br/Programas-Abertos',
        'fundacao_araucaria'
    )
    
    app.run(debug=True)
