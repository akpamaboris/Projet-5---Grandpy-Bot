from flask import Flask, render_template, jsonify, request
import wikipedia
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import googlemaps
from flask_googlemaps import GoogleMaps,Map

#faire test google maps
#faire test des mocks

app=Flask(__name__)
app.static_folder='static'
app.config['GOOGLEMAPS_KEY'] = "AIzaSyCFRB_ipsZztDSGoRwKOsnhXiWOKzi2YyU"
GoogleMaps(app)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/processing', methods=["POST"])
def processing():
	message = request.form['message']
	if message:
		message= message + " je suis passé par Flask"
		return jsonify({'message':str(message)})

	return jsonify({'error': 'désolé il y a eu une erreur'})

@app.route('/processingtest', methods=["POST"])
def processingtest():
	message = request.form['message']
	if message:
		# Je recupère le résultat de recherche du browser
		search_from_browser = request.form['message']

		# je tokenize la phrase, c'est à dire que je sépare une phrase
		# en de plus petits éléments
		wordTokens = word_tokenize(search_from_browser)

		# je crée une liste vide pour pouvoir stocker la phrase une fois que les stop words
		# auront étés enlevés de celle ci
		phrase_avec_filtre = []

		#Je specifie que les stopwords sont en français
		stopWords= set(stopwords.words("french"))

		# Je crée une boucle avec la variable w pour repérer les éléments qu'il y  a dans
		# ma requête tokénisée qui ne sont pas dans les stop words en français
		# ce procédé permet de filtrer tous les stop words afin de recueuillir une requête
		# filtrée sous forme de liste

		for w in wordTokens:
			if w not in stopWords:
				phrase_avec_filtre.append(w)

		# je convertis cette liste alors tous juste créée en un élément string
		full_str = " ".join([str(elem) for elem in phrase_avec_filtre])

		return jsonify({"suggestion_search": 'i tried', "input_user": search_from_browser})
	return jsonify({'error': 'désolé il y a eu une erreur'})


'''
		#Je specifie que les stopwords sont en français
		stopWords= set(stopwords.words("french"))

		#je tokenize la phrase, c'est à dire que je sépare une phrase
		#en de plus petits éléments
		wordTokens = word_tokenize(search_from_browser)

		#je crée une liste vide pour pouvoir stocker la phrase une fois que les stop words
		#auront étés enlevés de celle ci
		phrase_avec_filtre=[]

		#Je crée une boucle avec la variable w pour repérer les éléments qu'il y  a dans
		#ma requête tokénisée qui ne sont pas dans les stop words en français
		#ce procédé permet de filtrer tous les stop words afin de recueuillir une requête
		#filtrée sous forme de liste

		for w in wordTokens:
			if w not in stopwords:
				phrase_avec_filtre.append(w)

		#je convertis cette liste alors tous juste créée en un élément string
		full_str= " ".join([str(elem) for elem in phrase_avec_filtre])

		#je commence à préparer mon opération de cherchage
		searchRequest = str(full_str)
		return jsonify({"suggestion_search": 'i tried', "input_user": search_from_browser})

	return jsonify({'error': 'désolé il y a eu une erreur'})'''


@app.route('/finalprocessing', methods=["POST"])
def final_processing():

	#Je recupère le résultat de recherche du browser
	search_from_browser= request.form['message']

	#je vérifie si le résultat de recherche du browser existe
	# je vais retourner au browser 3 json objects si jamais l'utilisateur a rentré une recherche
	# dans son input text , ces 3 json objects sont :
	# 1 - L'input de l'utilisateur, que je vais nommer : input_user
	# 2 - Le résultat des recherches que je vais nommer : result_search
	# 3 - des suggestions de recherche que je vais nommer : suggestion_search


	if search_from_browser:

		#Je specifie que les stopwords sont en français
		stopWords= set(stopwords.words("french"))

		#je tokenize la phrase, c'est à dire que je sépare une phrase
		#en de plus petits éléments
		wordTokens = word_tokenize(search_from_browser)

		#je crée une liste vide pour pouvoir stocker la phrase une fois que les stop words
		#auront étés enlevés de celle ci
		phrase_avec_filtre=[]

		#Je crée une boucle avec la variable w pour repérer les éléments qu'il y  a dans
		#ma requête tokénisée qui ne sont pas dans les stop words en français
		#ce procédé permet de filtrer tous les stop words afin de recueuillir une requête
		#filtrée sous forme de liste

		for w in wordTokens:
			if w not in stopWords:
				phrase_avec_filtre.append(w)

		#je convertis cette liste alors tous juste créée en un élément string
		full_str= " ".join([str(elem) for elem in phrase_avec_filtre])

		#je commence à préparer mon opération de cherchage
		searchRequest = str(full_str)

		#j'initialise la librairie wikipedia pour des recherches en français
		wikipedia.set_lang("fr")

		#Je rentre ma clé d'API google maps dans la constante API_KEY
		#ne pas afficher de clé sur github


		API_KEY = 'AIzaSyCFRB_ipsZztDSGoRwKOsnhXiWOKzi2YyU'

		#J'initialise mon objet map_client

		map_client = googlemaps.Client(API_KEY)


		response = map_client.find_place([searchRequest], input_type='textquery',
										 fields=['formatted_address', 'photos', 'name', \
												 'place_id', 'geometry/location/lng', 'geometry/location/lat'])

		response_formatted_address = response['candidates'][0]['formatted_address']
		response_latitude = response['candidates'][0]['geometry']['location']['lat']
		response_longitude = response['candidates'][0]['geometry']['location']['lng']
		response_html_attributions = response['candidates'][0]['photos'][0]['html_attributions'][0]

		#quoi qu'il se passe, que ça soit pour le try ou le except, je vais retourner un jsonify object
		#avec les 3 fameuses variables


		try:
			#1- je m'occupe de la variable 1 => input_user
			input_user = search_from_browser

			#2 - je m'occupe de la variable 2 => result_search
			result_search = str(wikipedia.summary(searchRequest, sentences=5 , auto_suggest=True))

			#3 je m'occupe de la variable 3 => suggestion_search
			suggestion_search = wikipedia.search(str(searchRequest), results=10, suggestion=True)

			return jsonify({"input_user":input_user, "result_search": result_search, "suggestion_search": suggestion_search,"latitude":response_latitude, "longitude": response_longitude, "datacarte" :str(response_html_attributions)})
		except:
			#je ne retourne un objet qu'avec seulement 2 variables dans le cas de l'except

			#1- Je m'occupe de la variable 1 => input_user
			input_user = search_from_browser

			#2 - je m'occupe de la variable 3=> suggestion search
			suggestion_search = wikipedia.search(str(searchRequest),results=10,suggestion=True)
			return jsonify({"suggestion_search": suggestion_search,"input_user":input_user })


	#si le résultat du browser n'existe pas alors je retourne ce json object
	#qui permet au browser d'afficher une erreur
	return jsonify({'error':'désolé il y a eu une erreur'})


if __name__== '__main__':

	app.run(debug=True)