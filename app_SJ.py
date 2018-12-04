from flask import Flask, jsonify, render_template, jsonify,request
from sklearn.externals import joblib
import requests
import pandas as pd
import numpy as np
import pymongo
import json
import pickle

from pymongo import MongoClient
#from flask_pymongo import Pymongo

model = joblib.load('models/danceability_model.pkl')


app = Flask(__name__, static_url_path='/static', template_folder='template')

url = 'mongodb://admin:yaybootcamp2018@ds231228.mlab.com:31228/songs_ml'
client = MongoClient(url)
db = client['songs_ml']

@app.route("/", methods=['GET', 'POST'])
def index():
	'''
	data = requests.form.get('sendData')
	X = pd.Dataframe(data) #
	predictions = model.predict(X)
	'''
	return render_template("index.html")

@app.route('/test', methods = ['POST'])
def test():
    
    
    
    return flask.jsonify({'msg': 'success'})
'''
@app.route("/test", methods=['GET','POST'])
def test():
    clicked=None
    if request.method == "POST":
        clicked=request.json['data']
    return render_template("test.html")
'''


@app.route("/data")
def data():
	json_data = []
	collection = db.songs
	songs_data = collection.find()
	l = list(songs_data)
	for i in l:
	  v = list(i.values())[1]
	  json_data.append(
	 	{
		 "track" : v[2],
		 "acousticness" : v[1],
		 "danceability" : v[0],
		 "duration_ms" : v[3], 
		 "energy" : v[4], 
		 "instrumentalness" : v[5],
		 "key" : v[6],
		 "liveness": v[7],
		 "loudness": v[8],
		 "mode" : v[9], 
		 "speechiness" : v[10],
		 "tempo" : v[11], 
		 "time_signature" : v[13], 
		 "track" : v[14],
		 "track_href" : v[15],
		 "valence": v[16]
		})
	#print(json_data)
	return jsonify(json_data)
# #load model
# model = pickle.load(open('decision_tree_model.pkl', 'r'))

# #define route with post request
# @app.route('/', methods=["POST"])
# def index():
# 	# get array of features from post requests
# 	# features = request.get_json()

# 	# #creating a response object
#  #    #storing the model's prediction in the object
# 	# response = {}
# 	# response['predictions'] = model.predict([features]).tolist()

# 	# return jsonify(response)

if __name__ == '__main__':
	app.run(debug=True)