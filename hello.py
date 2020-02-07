from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World"

@app.route('/hello/<name>')
def new_hello(name):
    return "Hello " + name

@app.route('/list')
def list_websites():
    return render_template('index.html')

@app.route('/process_form', methods=['POST'])
def process_form():
    name = request.form['name']
    fav_color = request.form['fav_color']
    return render_template('user_info.html', n = name, color = fav_color)



if __name__=='__main__':
    app.run(debug=True)
