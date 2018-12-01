from flask import Flask, jsonify, render_template, jsonify
import requests
import pandas as pd
import numpy as np
import pymongo
import json
import pickle
from pymongo import MongoClient
#from flask_pymongo import Pymongo



app = Flask(__name__, static_url_path='/static', template_folder='templates')

url = 'mongodb://admin:USCbootcamp2018@ds123444.mlab.com:23444/songs_ml'
client = MongoClient(url)
db = client['songs_ml']

#app.config['MONGO_URI'] = "mongodb://admin:USCbootcamp2018@ds141633.mlab.com:41633/songs_ml"
#mongo = PyMongo(app)

@app.route("/")
def index():
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
			 "track" : v[0],
			 "acousticness" : v[1],
			 "danceability" : v[2],
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
			}
		   )
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