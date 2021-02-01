from flask import Flask, render_template, jsonify, request


app=Flask(__name__)
app.static_folder='static'

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


if __name__== '__main__':
	app.run(debug=True)