from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')
	return 'Hello Lauren! I love you!!! Dis our website nao. Llama.com or something. <3 -Jack'

@app.route('/lauren')
def lauren():
	return render_template('lauren.html')
	return 'Clever, sweet, wifey!'

@app.route('/hello')
@app.route('/hello/<name>')
def hello(name="Fren"):
	return render_template('fren.html', name=name)

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')
