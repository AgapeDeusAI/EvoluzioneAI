from flask import Flask, request, jsonify
from flask_cors import CORS
from EvoluzioneAI import EvoluzioneAI

app = Flask(__name__)
CORS(app)

evo = EvoluzioneAI()

@app.route("/", methods=["GET"])
def home():
    return jsonify({"status": "✅ Evoluzione AI attiva"})

@app.route("/tick", methods=["POST"])
def tick():
    try:
        risultato = evo.tick_evolutivo()
        return jsonify({"success": True, "risultato": risultato})
    except Exception as e:
        return jsonify({"success": False, "errore": str(e)})

if __name__ == "__main__":
    app.run(port=3007)