from flask import Flask, Response
import requests
import os


app = Flask(__name__)

API_KEY = "HDEV-0e4e1574-46f9-4bef-b3fa-cef596d2e1a9"
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
        print("Respuesta:", data)  

        rango = data['data']['current_data']['currenttierpatched']
        puntos = data['data']['current_data']['ranking_in_tier']
        mmr = data['data']['mmr_change_to_last_game']

        respuesta = f"{rango} con {puntos} puntos, mi última partida []"
    except Exception as e:
        print("Error:", e)
        respuesta = "Rango no disponible"
    return Response(respuesta, mimetype='text/plain')

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
