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

@app.route("/")
def index():
	acousticness = request.args.get('acousticness')
	energy = request.args.get('energy')
	instrumentalness = request.args.get('instrumentalness')
	liveness = request.args.get('liveness')
	loudness = request.args.get('loudness')
	tempo = request.args.get('tempo')
	valence = request.args.get('valence')

	# do something to the get request variables convert into same values as your 230, 13
	data = [		
		#{'acousticness': acousticness},
		{'energy': energy},
		# {'instrumentalness': instrumentalness},
		# {'liveness': liveness},
		# {'loudness': loudness},
		# {'tempo':  tempo},
		# {'valence': valence}
	]

	# print(data)
	# print(type(data))


	values_list = []


	acoustic_string = data[0]['acousticness']
	acoustic_float = float(acoustic_string)
	print(acoustic_float)
	print(type(acoustic_float))
	values_list.append(acoustic_float)

	energy_string = data[1]['energy']
	energy_float = float(energy_string)
	print(energy_float)
	print(type(energy_float))
	values_list.append(energy_float)

	# instrumentalness_string = data[2]['instrumentalness']
	# instrumentalness_float = float(instrumentalness_string)
	# print(instrumentalness_float)
	# print(type(instrumentalness_float))
	# values_list.append(instrumentalness_float)

	# liveness_string = data[3]['liveness']
	# liveness_float = float(liveness_string)
	# print(liveness_float)
	# print(type(liveness_float))
	# values_list.append(liveness_float)

	# loudness_string = data[4]['loudness']
	# loudness_float = float(loudness_string)
	# print(loudness_float)
	# print(type(loudness_float))
	# values_list.append(loudness_float)

	# tempo_string = data[5]['tempo']
	# tempo_float = float(tempo_string)
	# print(tempo_float)
	# print(type(tempo_float))
	# values_list.append(tempo_float)

	# valence_string = data[0]['valence']
	# valence_float = float(valence_string)
	# print(valence_float)
	# print(type(valence_float))
	# values_list.append(valence_float)

	print(values_list)

	# X = np.array(data)
	# X = StandardScaler().fit_transform(X)
	# predictions = model.predict(X)
	# predictions = 3
	# data_list = data.values()

	# d_list = []
	# d_list.append(data['acousticness'])
	# print(X)
	# print(data)
	# print(type(X))

	
	# print(predictions)
	# print(f'Model prediction is {predictions}')
	# print(acousticness, '', energy, '', instrumentalness, '', liveness, '', loudness, '', tempo, '', valence) 
	# return render_template("index.html", tits=predictions)
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

	# set condtionals
	# def acousctiness(score):
	# 	if score == 'All Acoustic':
	# 		acousticness = '0.80'
	# 	elif score == 'Mostly Acoustic':
	# 		acousticness = '0.60'
	# 	elif score == "Mostly Digital"
	# 		acousticness = '0.40'
	# 	else score == "Pure Digital"

	# return score

	# def energy(score_2):
	# 	# if score == 'Relaxed':
	# 	# 	energy = 'boobs'

	# 	return score_2

	# if tempo == 'Relaxed':
 #        tempo = <= 80 and >=60
 #    elif tempo == 'Moderate':
 #    	tempo = <= 100 and >= 80

if __name__ == '__main__':
	app.run(debug=True)