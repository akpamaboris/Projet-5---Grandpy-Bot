from flask import Flask, render_template, jsonify


app=Flask(__name__)
app.static_folder='static'

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/processing')
def processing():
	return jsonify({"key":"hey"})


if __name__== '__main__':
	app.run(debug=True)