from flask import Flask, request
from flask_cors import CORS
from scrappers.fundacao_araucaria.scrapper import FundacaoAraucariaScrapper
from scrappers.cnpq.scrapper import CNPQScrapper
from services.call_generator import CallGenerator
import json

app = Flask(__name__)

cors = CORS(app)

app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/calls', methods=['GET'])
def get():    
    path = './fundacao_araucaria_calls.json'

    with open(path, 'r') as file:
        data = json.load(file)

    path = './cnpq_calls.json'

    with open(path, 'r') as file:
        data += json.load(file)
    
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)

    start = (page - 1) * per_page
    end = start + per_page

    paginated_data = data[start:end]

    return {
        'page': page,
        'per_page': per_page,
        'data': paginated_data,
        'total': len(data),
    }, 200

if __name__ == '__main__':
    CallGenerator.generate(
        FundacaoAraucariaScrapper,
        'https://www.fappr.pr.gov.br/Programas-Abertos',
        'fundacao_araucaria'
    )

    CallGenerator.generate(
        CNPQScrapper,
        'http://memoria2.cnpq.br/web/guest/chamadas-publicas',
        'cnpq'
    )

    app.run(host='0.0.0.0')
