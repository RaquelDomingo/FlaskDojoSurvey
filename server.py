from flask import Flask, render_template, request
app = Flask(__name__)
app.secret_key = "ThisIsSecret"

@app.route('/')
def index():
    option_list = ['Silicon Valley', 'Los Angeles', 'Seattle', 'Los Angeles', 'Dallas', 'Washington DC', 'Chicago']
    language_list = ['HTML', 'CSS', 'JavaScript', 'Python', 'PHP', 'C++', 'iOS']
    return render_template("mainpage.html", option_list=option_list, language_list=language_list )

@app.route('/result', methods=['POST'])
def create_user():

    return render_template ('resultpage.html', name=request.form['name'], location=request.form['location'], language=request.form['language'], comment=request.form['comment'])

app.run(debug=True) 