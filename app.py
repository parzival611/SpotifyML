from flask import Flask, jsonify, render_template, jsonify
from sklearn.externals import joblib
from flask import request
import pandas as pd
import numpy as np
import pymongo
import json
import pickle
from pymongo import MongoClient


model = joblib.load('models/danceability_model.pkl')


app = Flask(__name__, static_url_path='/static', template_folder='template')

url = 'mongodb://admin:yaybootcamp2018@ds231228.mlab.com:31228/songs_ml'
client = MongoClient(url)
db = client['songs_ml']

@app.route("/", methods=['GET', 'POST'])
def index():
	if request.method == 'POST':

		data = request.form.get('ready')
		# data = requests.get('sendData')
		X = pd.DataFrame(data) 
		predictions = model.predict(X)

		print(X) 
	return render_template("index.html")

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
		 "id" : v[0],
		 "track" : v[1],
		 "acousticness" : v[2],
		 "danceability" : v[3],
		 "duration_ms" : v[4], 
		 "energy" : v[5],
		 "instrumentalness" : v[6],
		 "key" : v[7],
		 "liveness": v[8],
		 "loudness": v[9],
		 "mode" : v[10], 
		 "speechiness" : v[11],
		 "tempo" : v[12], 
		 "valence": v[13]
		})
	#print(json_data)
	return jsonify(json_data)


if __name__ == '__main__':
	app.run(debug=True)