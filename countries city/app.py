from flask import *
import requests


def cities(country):
    url = 'https://raw.githubusercontent.com/samayo/country-json/master/src/country-by-cities.json'
    res = requests.get(url).json()
    for i in range(len(res)):
        if res[i]['country'] == country:
            return res[i]['cities']
    
app = Flask(__name__)

@app.route("/")
def index():
    url = 'https://raw.githubusercontent.com/samayo/country-json/master/src/country-by-cities.json'
    countrieslist = requests.get(url).json()
    return render_template("index.html",countries=countrieslist)

@app.route('/cities/<country>')
def citiesList(country):
    citieslist = cities(country)
    if citieslist:
        return jsonify(city=citieslist)
    else:
        return jsonify(error='not found!')

if __name__ == '__main__':
    app.run(debug=True)