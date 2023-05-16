from flask import Flask,render_template

app=Flask(__name__, static_url_path='/static')

@app.route("/")
@app.route("/home")
def home():
	return render_template("index.html")

@app.route("/bmicalc")
def bmicalc():
	return render_template("bmiCacl.html")

@app.route("/login")
def login():
	return render_template("login.html")

if __name__ == '__main__':
	app.run(debug = True,port=5001)