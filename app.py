from flask import Flask, Response
import requests
import os

app = Flask(__name__) 

API_KEY = os.environ.get("API_KEY")
NOMBRE = "Nayecute Twitch"
TAG = "965"
REGION = "na"

@app.route('/')
def index():
    return "API Valorant funcionando"

@app.route('/rango')
def rango():
    url = f"https://api.henrikdev.xyz/valorant/v2/mmr/{REGION}/{NOMBRE.replace(' ', '%20')}/{TAG}?api_key={API_KEY}"
    try:
        res = requests.get(url)
        data = res.json()

        current_data = data.get('data', {}).get('current_data', None)
        if not current_data:
            return Response("No hay datos actuales disponibles.", mimetype='text/plain')

        rango = current_data.get('currenttierpatched', 'Desconocido')
        puntos = current_data.get('ranking_in_tier', 'Desconocido')
        mmr_change = current_data.get('mmr_change_to_last_game', 'Desconocido')

        respuesta = f"{rango}, con {puntos} puntos, Mi última partida: [{mmr_change}]"
    except Exception as e:
        print("Error:", e)
        respuesta = "Rango no disponible"
    return Response(respuesta, mimetype='text/plain')

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

