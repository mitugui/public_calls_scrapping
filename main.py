from flask import Flask
from flask_cors import CORS

app = Flask(__name__)

cors = CORS(app)

app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/calls', methods=['GET'])
def get():
    pass

if __name__ == '__main__':
    app.run(debug=True)