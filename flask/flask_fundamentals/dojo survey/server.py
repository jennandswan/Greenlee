from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/users', methods=['POST'])
def create_user():
    nameInput = request.form['name']
    locationInput = request.form['location']
    languageInput = request.form['language']
    commentsInput = request.form['comments']
    return render_template('results.html', name=nameInput, location=locationInput, language=languageInput, comments=commentsInput)

if __name__ == '__main__':
    app.run(debug=True)