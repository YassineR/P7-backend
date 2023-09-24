from flask import Flask
import pickle

app = Flask(__name__)

@app.route('/')
def index():
    return 'Add id client in route to have his data'


@app.route('/<id_client>')
def get_id_client(id_client):
    return "The id is " + str(id_client)

with open('lgbm_client_scoring.pkl', 'rb') as model_file:
    model = model_file.read()

@app.route('/get-model', methods=['GET'])
def get_model():	
    return model

