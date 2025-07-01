from flask import Flask
from flask_cors import CORS
from scrappers.fundacao_araucaria.scrapper import FundacaoAraucariaScrapper
from services.call_generator import CallGenerator

app = Flask(__name__)

cors = CORS(app)

app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/calls', methods=['GET'])
def get():
    pass

if __name__ == '__main__':
    CallGenerator.generate(
        FundacaoAraucariaScrapper,
        'https://www.fappr.pr.gov.br/Programas-Abertos',
        'fundacao_araucaria'
    )

    app.run(debug=True)
