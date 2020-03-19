from flask import Flask,render_template, make_response,jsonify
import pandas as pd 
from flask_cors import CORS, cross_origin
from dataParsing import DataParser
from utils import dict_response

app = Flask(__name__)
#Our Cors Policy
CORS(app,supports_credentials=True,expose_headers='Authorization')
app.config['CORS_HEADERS'] = 'Content-Type'
#Creating the master data class MD
md=DataParser()

@app.route('/data/country-data',methods=['POST','GET'])
def get_country_data():
    return dict_response(md.Country_Data)



app.run(debug=True)