from flask import Flask, render_template, url_for, redirect

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')
@app.route('/Market')
def market_place():
    exnotes = [
    {'id':'1', 'name':'idk'},
    {'id':'2', 'name':'234'}
    ]
    return render_template('market.html', exnotes=exnotes)

if __name__ == '__main__':
    app.run(debug=True, port=8000)
