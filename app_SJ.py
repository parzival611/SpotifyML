from flask import Flask, jsonify, render_template, jsonify
from sklearn.externals import joblib
from flask import request
import pandas as pd
import numpy as np
import pymongo
import json
import pickle
import random
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
		{'acousticness': acousticness},
		{'energy': energy},
		{'instrumentalness': instrumentalness},
		{'liveness': liveness},
		{'loudness': loudness},
		{'tempo':  tempo},
		{'valence': valence}
	]

	#print(data)
	#print(type(data))

	values_list = []
	for features in data:
		for k, v in features.items():
			print('{}: {}'.format(k, v))
			values_list.append(v)

	print(values_list[0])
	print(values_list[1])
	print(values_list[2])
	print(values_list[3])
	print(values_list[4])
	print(values_list[5])
	print(values_list[6])
	#print(type(values_list[0]))
	

	print("----------------------------")

	print(type(values_list[0]))
	print(type(values_list[1]))

	print("----------------------------")
	print("----------------------------")
	print("FLOAT VALUE BELOW")

	all_float_values = []

	if type(values_list[0]) == str:
		float_1 = float(values_list[0])
		print(float_1)
		print(type(float_1))
		all_float_values.append(float_1)

	if type(values_list[1]) == str:
		float_2 = float(values_list[1])
		print(float_2)
		print(type(float_2))
		all_float_values.append(float_2)

	if type(values_list[2]) == str:
		float_3 = float(values_list[2])
		print(float_3)
		print(type(float_3))
		all_float_values.append(float_3)


	if type(values_list[3]) == str:
		float_4 = float(values_list[3])
		print(float_4)
		print(type(float_4))
		all_float_values.append(float_4)

	if type(values_list[4]) == str:
		float_5 = float(values_list[4])
		print(float_5)
		print(type(float_5))
		all_float_values.append(float_5)

	if type(values_list[5]) == str:
		float_6 = float(values_list[5])
		print(float_6)
		print(type(float_6))
		all_float_values.append(float_6)

	if type(values_list[6]) == str:
		float_7 = float(values_list[6])
		print(float_7)
		print(type(float_7))
		all_float_values.append(float_7)

	print("------CONVERTED FLOATS INTO A NEW LIST-------")
	print(all_float_values)
	print("---------------------------------------------")
	print("\n")

	print("------ENUMERATION-------")
	for counter, value in enumerate(all_float_values):
		print(counter, value)
	print("---------------------------------------------")
	print("\n")

	print("-----NUMPY ARRAY CONVERSION-------")

	float_values_np = np.array(all_float_values)

	final_reshaped_np = float_values_np.reshape(1, -1)

	print(final_reshaped_np)
	print(f"TYPE IS {type(final_reshaped_np)}")
	print(f"SHAPE IS {final_reshaped_np.shape}")

	print("\n")

	print("---------------------------------------------")
	print("------------ML MODEL RESULTS-----------------")

	#-------------- MODEL ---------------------

	# X = StandardScaler().fit_transform(X)
	
	if final_reshaped_np.shape == (1, 7):
		predictions = model.predict(final_reshaped_np)
		final_score = round(predictions[0], 3)
		print("Calculating...")
		print(f'Model prediction is {final_score}')


		if final_score >= 0.75:
			print("HIGH DANCEABILITY! :-D ")

		if final_score >= 0.50 and final_score <= 0.75:
			print("PRETTY DANCEABLE! :-)")

		if final_score >= 0.25 and final_score <= 0.50:
			print("Eh, decent danceability :-/")

		if final_score < 0.25:
			print("Awful... Can't dance to this :-(")


	
	# predictions = 3
	
	
	# print(predictions)
	# print(f'Model prediction is {predictions}')
	# print(acousticness, '', energy, '', instrumentalness, '', liveness, '', loudness, '', tempo, '', valence) 
	# return render_template("index.html", tits=predictions)
	return render_template("index.html") #solution=final_score)


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