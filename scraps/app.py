from flask import Flask, jsonify
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
import numpy as np

app = Flask(__name__)

engine = create_engine("sqlite:///db/spotifydb.sqlite")
Base = automap_base()
Base.prepare(engine, reflect=True)
Playlist = Base.classes.playlist
session = Session(engine)

@app.route("/")
def welcome():

	return (
		f'Welcome<br/>'
		f'/playlist</br>'
		f'/playlist_2</br>'
	)

# Return a list of data
@app.route("/playlist")
def playlist():
	# query all tracks
	songs = session.query(Playlist.track, Playlist.id).all()
	
	#Create a dictionary from returned list
	results = dict(songs)
	
	#print(songs)
	return jsonify(songs)

@app.route("/playlist_2")
def all_columns():
	
	songs = session.query(Playlist.track, Playlist.id).all()

	all_songs = []
	for song in songs:
		song_dict = {}
		song_dict['Track'] = Playlist.track
		song_dict['id'] = Playlist.id
		all_songs.append(song_dict)
	    
	#print(all_songs)
	return jsonify(all_songs)

if __name__ == '__main__':
	app.run(debug=True)