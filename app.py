import requests
from flask import Flask, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('hello.html')

# Déposez votre code à partir d'ici :


@app.route("/contact")
def MaPremiereAPI():
    return "<h2>Ma page de contact</h2>"

@app.get("/paris")
def api_paris():
    # URL de l'API externe (Open-Meteo)
    url = "https://api.open-meteo.com/v1/forecast?latitude=48.8566&longitude=2.3522&hourly=temperature_2m"
    
    # On envoie la requête à l'API
    response = requests.get(url)
    data = response.json()

    # On extrait les listes de temps et de températures
    times = data.get("hourly", {}).get("time", [])
    temps = data.get("hourly", {}).get("temperature_2m", [])

    n = min(len(times), len(temps))
    result = [
        {"datetime": times[i], "temperature_c": temps[i]}
        for i in range(n)
    ]

    # On renvoie le résultat au format JSON
    return jsonify(result)
@app.route("/rapport")
def mongraphique():
    return render_template("graphique.html")

@app.route("/histogramme")
def mon_histogramme():
    return render_template("histogramme.html")

@app.get("/api/marseille")
def api_marseille():
    # URL pour le vent à Marseille
    url = "https://api.open-meteo.com/v1/forecast?latitude=43.2965&longitude=5.3698&hourly=windspeed_10m"
    response = requests.get(url)
    data = response.json()

    times = data.get("hourly", {}).get("time", [])
    winds = data.get("hourly", {}).get("windspeed_10m", [])

    n = min(len(times), len(winds))
    result = [
        {"datetime": times[i], "wind_speed": winds[i]}
        for i in range(n)
    ]
    return jsonify(result)

@app.route("/atelier")
def mon_atelier():
    return render_template("atelier.html")

# Ne rien mettre après ce commentaire
    
if __name__ == "__main__":
  app.run(host="0.0.0.0", port=5000, debug=True)
