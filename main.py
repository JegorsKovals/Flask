from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
	return "Hi!"

@app.route('/home')
def home():
	return render_template('home.html')

@app.route('/about')
def about():
	return render_template('about.html')

@app.route('/contacts')
def contact():
  return render_template('contacts.html', phone = "20319482")


if __name__ == '__main__':
	app.run(threaded=True, port=5020, debug=True)